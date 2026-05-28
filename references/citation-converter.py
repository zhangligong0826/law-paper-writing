#!/usr/bin/env python3
"""
法学论文引用格式辅助转换器
GB/T 7714 ↔ Bluebook 草案转换

用法:
  python citation-converter.py --input input.txt --from gbt7714 --to bluebook --output output.txt
  python citation-converter.py --input input.txt --from bluebook --to gbt7714 --output output.txt

说明:
  本脚本用于初稿整理和格式迁移，不替代人工核对。正式投稿前必须按目标期刊、
  学校模板或 Bluebook 原文规则逐条确认作者、题名、卷期、页码和缩写。
"""

import argparse
import re
import sys


# ============ GB/T 7714 → Bluebook ============

def gbt7714_to_bluebook(text):
    """将 GB/T 7714 引用逐行转换为 Bluebook 草案格式。"""
    return _convert_lines(text, _gbt7714_line_to_bluebook)


def _gbt7714_line_to_bluebook(line):
    stripped = line.strip()
    if not stripped:
        return line

    for converter in (
        _gbt7714_journal_to_bluebook,
        _gbt7714_book_to_bluebook,
        _gbt7714_chapter_to_bluebook,
    ):
        converted = converter(stripped)
        if converted is not None:
            return converted

    return line


def _gbt7714_journal_to_bluebook(line):
    # 常见格式:
    # [1] 作者. 论文标题[J]. 期刊, 2014(5): 32-45.
    # [2] 作者. 论文标题[J]. 期刊, 2022, 44(3): 12-30.
    # [3] 作者. 论文标题[J]. 期刊, 2021: 5-18.
    journal_pattern = re.compile(
        r'^\[(?P<num>\d+)\]\s*'
        r'(?P<author>.+?)\.\s*'
        r'(?P<title>.+?)\[J\]\.\s*'
        r'(?P<journal>.+?),\s*'
        r'(?P<year>\d{4})'
        r'(?:\s*,\s*(?P<volume>\d+)(?:\((?P<issue>[^)]+)\))?)?'
        r'(?:\s*\((?P<issue_only>[^)]+)\))?'
        r'(?:\s*:\s*(?P<start_page>\d+)(?:[-–](?P<end_page>\d+))?)?'
        r'\s*\.?$'
    )
    match = journal_pattern.fullmatch(line)
    if not match:
        return None

    author = format_author_bluebook(match.group('author'))
    title = match.group('title').strip()
    journal_cn = match.group('journal').strip()
    year = match.group('year')
    volume = match.group('volume') or ''
    start_page = match.group('start_page') or ''
    end_page = match.group('end_page') or ''

    journal_abbr = abbreviate_journal(translate_journal_name(journal_cn))

    parts = [f"{match.group('num')}. {author}, {title},"]
    if volume:
        parts.append(volume)
    parts.append(journal_abbr)
    if start_page:
        page_text = start_page
        if end_page:
            page_text += f"-{end_page}"
        parts.append(page_text)
    parts.append(f"({year}).")
    return " ".join(parts)


def _gbt7714_book_to_bluebook(line):
    # [序号] 作者. 书名[M]. 出版地: 出版社, 年份: 引用页码.
    book_pattern = re.compile(
        r'^\[(?P<num>\d+)\]\s*'
        r'(?P<author>.+?)\.\s*'
        r'(?P<title>.+?)\[M\]\.\s*'
        r'(?P<place>.+?)\s*:\s*(?P<publisher>.+?),\s*'
        r'(?P<year>\d{4})'
        r'(?:\s*:\s*(?P<page>\d+))?'
        r'\s*\.?$'
    )
    match = book_pattern.fullmatch(line)
    if not match:
        return None

    author = format_author_bluebook(match.group('author'))
    title = match.group('title').strip()
    publisher = match.group('publisher').strip()
    year = match.group('year')
    page = match.group('page') or ''

    result = f"{match.group('num')}. {author}, {title} ({publisher} {year} ed.)"
    if page:
        result += f" at {page}"
    return result + "."


def _gbt7714_chapter_to_bluebook(line):
    # [序号] 作者. 章节标题[A]. 编者. 书名[C]. 出版地: 出版社, 年份: 引用页码.
    chapter_pattern = re.compile(
        r'^\[(?P<num>\d+)\]\s*'
        r'(?P<author>.+?)\.\s*'
        r'(?P<title>.+?)\[A\]\.\s*'
        r'(?P<editor>.+?)\.\s*'
        r'(?P<book>.+?)\[C\]\.\s*'
        r'(?P<place>.+?)\s*:\s*(?P<publisher>.+?),\s*'
        r'(?P<year>\d{4})'
        r'(?:\s*:\s*(?P<page>\d+))?'
        r'\s*\.?$'
    )
    match = chapter_pattern.fullmatch(line)
    if not match:
        return None

    author = format_author_bluebook(match.group('author'))
    title = match.group('title').strip()
    editor = format_author_bluebook(match.group('editor'))
    book = match.group('book').strip()
    publisher = match.group('publisher').strip()
    year = match.group('year')
    page = match.group('page') or ''

    result = (
        f"{match.group('num')}. {author}, {title}, in {editor} ed., "
        f"{book} ({publisher} {year})"
    )
    if page:
        result += f" at {page}"
    return result + "."


# ============ Bluebook → GB/T 7714 ============

def bluebook_to_gbt7714(text):
    """将 Bluebook 引用逐行转换为 GB/T 7714 草案格式。"""
    return _convert_lines(text, _bluebook_line_to_gbt7714)


def _bluebook_line_to_gbt7714(line):
    stripped = line.strip()
    if not stripped:
        return line

    for converter in (
        _bluebook_journal_to_gbt7714,
        _bluebook_book_to_gbt7714,
    ):
        converted = converter(stripped)
        if converted is not None:
            return converted

    return line


def _bluebook_journal_to_gbt7714(line):
    # 1. Author, Title, 12 Harv. L. Rev. 34-56 (2020).
    bj_pattern = re.compile(
        r'^(?P<num>\d+)\.\s*'
        r'(?P<author>.+?),\s*'
        r'(?P<title>.+?),\s*'
        r'(?P<volume>\d+)\s+'
        r'(?P<journal>.+?)\s+'
        r'(?P<start_page>\d+)(?:-(?P<end_page>\d+))?\s+'
        r'\((?P<year>\d{4})\)\.?\s*$'
    )
    match = bj_pattern.fullmatch(line)
    if not match:
        return None

    journal_cn = reverse_translate_journal(match.group('journal'))
    result = (
        f"[{match.group('num')}] {match.group('author').strip()}. "
        f"{match.group('title').strip()}[J]. {journal_cn}, {match.group('year')}, "
        f"{match.group('volume')}: {match.group('start_page')}"
    )
    if match.group('end_page'):
        result += f"-{match.group('end_page')}"
    return result + "."


def _bluebook_book_to_gbt7714(line):
    # 1. Author, Title (Publisher 2020 ed.) at 12.
    book_pattern = re.compile(
        r'^(?P<num>\d+)\.\s*'
        r'(?P<author>.+?),\s*'
        r'(?P<title>.+?)\s+'
        r'\((?P<publisher>.+?)\s+(?P<year>\d{4})\s*ed\.\)'
        r'(?:\s+at\s+(?P<page>\d+))?'
        r'\.?\s*$'
    )
    match = book_pattern.fullmatch(line)
    if not match:
        return None

    result = (
        f"[{match.group('num')}] {match.group('author').strip()}. "
        f"{match.group('title').strip()}[M]. 出版地待核: "
        f"{match.group('publisher').strip()}, {match.group('year')}"
    )
    if match.group('page'):
        result += f": {match.group('page')}"
    return result + "."


# ============ 辅助函数 ============

def _convert_lines(text, converter):
    converted_lines = []
    for line in text.splitlines(keepends=True):
        newline = ''
        body = line
        if line.endswith('\r\n'):
            body = line[:-2]
            newline = '\r\n'
        elif line.endswith('\n'):
            body = line[:-1]
            newline = '\n'
        converted_lines.append(converter(body) + newline)
    if not converted_lines and text == '':
        return ''
    return ''.join(converted_lines) if converted_lines else converter(text)


def format_author_bluebook(author_str):
    """
    将作者列表转为 Bluebook 草案格式。
    中文作者暂不自动转拼音，避免错误音译；正式投稿前应人工确认。
    """
    authors = [a.strip() for a in author_str.replace('，', ',').split(',') if a.strip()]

    if authors and authors[-1].strip() in ['等', 'et al.', 'et al']:
        authors = authors[:-1]

    authors = [a.split('译')[0].split('，译')[0].strip() for a in authors]

    bluebook_authors = []
    for i, author in enumerate(authors):
        if not author:
            continue
        if i == len(authors) - 1 and len(authors) > 1:
            bluebook_authors.append(f"& {author}")
        else:
            bluebook_authors.append(author)

    return ', '.join(bluebook_authors)


JOURNAL_TRANSLATIONS = {
    '法学研究': 'Chinese Journal of Law',
    '中国法学': 'China Legal Science',
    '法学': 'Law Science',
    '中外法学': 'Peking University Law Journal',
    '政法论坛': 'Tribune of Political Science and Law',
    '法学评论': 'Law Review',
    '法律科学': 'Legal Science',
    '法商研究': 'Studies in Law and Business',
    '现代法学': 'Modern Law Science',
    '清华法学': 'Tsinghua Law Review',
    '政治与法律': 'Journal of Political Science and Law',
    '环球法律评论': 'Global Law Review',
}

JOURNAL_ABBREVIATIONS = {
    'Chinese Journal of Law': 'Chin. J. L.',
    'China Legal Science': 'China Legal Sci.',
    'Law Science': 'Law Sci.',
    'Peking University Law Journal': 'Peking U. L.J.',
    'Tribune of Political Science and Law': 'Trib. Pol. Sci. & L.',
    'Law Review': 'L. Rev.',
    'Legal Science': 'Legal Sci.',
    'Studies in Law and Business': 'Stud. L. & Bus.',
    'Modern Law Science': 'Mod. L. Sci.',
    'Tsinghua Law Review': 'Tsinghua L. Rev.',
    'Journal of Political Science and Law': 'J. Pol. Sci. & L.',
    'Global Law Review': 'Global L. Rev.',
    'Harvard Law Review': 'Harv. L. Rev.',
    'Yale Law Journal': 'Yale L.J.',
    'Columbia Law Review': 'Colum. L. Rev.',
    'University of Chicago Law Review': 'U. Chi. L. Rev.',
    'Stanford Law Review': 'Stan. L. Rev.',
    'Michigan Law Review': 'Mich. L. Rev.',
    'American Journal of International Law': 'Am. J. Int\'l L.',
    'Journal of Legal Studies': 'J. Legal Stud.',
}


def translate_journal_name(cn_name):
    """中文期刊名 → 英文名。未收录时保留原名，交由人工核对。"""
    return JOURNAL_TRANSLATIONS.get(cn_name.strip(), cn_name.strip())


def abbreviate_journal(en_name):
    """英文期刊名 → Bluebook 缩写草案。未收录时保留原名。"""
    return JOURNAL_ABBREVIATIONS.get(en_name.strip(), en_name.strip())


def reverse_translate_journal(abbr):
    """Bluebook 缩写 → 中文期刊名草案。未收录时保留原缩写。"""
    english_by_abbr = {v: k for k, v in JOURNAL_ABBREVIATIONS.items()}
    english_name = english_by_abbr.get(abbr.strip(), abbr.strip())
    chinese_by_english = {v: k for k, v in JOURNAL_TRANSLATIONS.items()}
    return chinese_by_english.get(english_name, english_name)


# ============ 主程序 ============

def convert_file(input_path, source_fmt, target_fmt, output_path):
    """转换文件中的引用格式。"""
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if source_fmt == 'gbt7714' and target_fmt == 'bluebook':
        result = gbt7714_to_bluebook(content)
    elif source_fmt == 'bluebook' and target_fmt == 'gbt7714':
        result = bluebook_to_gbt7714(content)
    else:
        print(f"错误: 不支持的转换方向 {source_fmt} → {target_fmt}")
        print("支持: gbt7714→bluebook, bluebook→gbt7714")
        sys.exit(1)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(result)

    print(f"转换完成: {input_path} ({source_fmt}) → {output_path} ({target_fmt})")
    print("提示: 转换结果仅供初稿整理，投稿前必须逐条人工核对。")


def main():
    parser = argparse.ArgumentParser(
        description='法学论文引用格式辅助转换器 (GB/T 7714 ↔ Bluebook)',
        epilog='示例: python citation-converter.py --input refs.txt --from gbt7714 --to bluebook --output refs_bb.txt'
    )
    parser.add_argument('--input', '-i', required=True, help='输入文件路径')
    parser.add_argument('--from', dest='source', required=True,
                        choices=['gbt7714', 'bluebook'], help='源格式')
    parser.add_argument('--to', dest='target', required=True,
                        choices=['gbt7714', 'bluebook'], help='目标格式')
    parser.add_argument('--output', '-o', required=True, help='输出文件路径')

    args = parser.parse_args()
    convert_file(args.input, args.source, args.target, args.output)


if __name__ == '__main__':
    main()
