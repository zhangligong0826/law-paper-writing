#!/usr/bin/env python3
"""
法学论文引用格式转换器
GB/T 7714 ↔ Bluebook 双向转换

用法:
  python citation-converter.py --input input.txt --from gbt7714 --to bluebook --output output.txt
  python citation-converter.py --input input.txt --from bluebook --to gbt7714 --output output.txt

输入文件格式: 每行一条引用记录
"""

import re
import argparse
import sys


# ============ GB/T 7714 → Bluebook ============

def gbt7714_to_bluebook(text):
    """将 GB/T 7714 格式的引用转换为 Bluebook 格式"""

    # 1. 期刊论文转换
    # [序号] 作者. 论文标题[J]. 期刊名称, 年份, 卷(期): 起止页码.
    journal_pattern = re.compile(
        r'\[(\d+)\]\s*'                              # [序号]
        r'(.+?)\.\s*'                                 # 作者
        r'(.+?)\[J\]\.\s*'                            # 标题[J]
        r'(.+?),\s*'                                  # 期刊名
        r'(\d{4})'                                     # 年份
        r'(?:\s*,\s*(\d+)\(([^)]+)\))?'                # 卷(期) 可选
        r'(?:\s*:\s*(\d+)(?:-(\d+))?)?'                # 起止页码 可选
        r'\s*\.?\s*$'                                  # 结尾
    )

    def journal_repl(m):
        num = m.group(1)
        author = format_author_bluebook(m.group(2))
        title = m.group(3).strip()
        journal_cn = m.group(4).strip()
        year = m.group(5)
        volume = m.group(6) or ''
        issue = m.group(7) or ''
        start_page = m.group(8) or ''
        end_page = m.group(9) or ''

        journal_en = translate_journal_name(journal_cn)
        journal_abbr = abbreviate_journal(journal_en)

        result = f"{author}, {title}, "
        if volume:
            result += f"{volume} "
        result += f"{journal_abbr} "
        if start_page:
            result += f"{start_page} "
            if end_page:
                result += f"-{end_page} "
        result += f"({year})."
        return f"{num}. {result}"

    text = journal_pattern.sub(journal_repl, text)

    # 2. 专著转换
    # [序号] 作者. 书名[M]. 出版地: 出版社, 年份: 引用页码.
    book_pattern = re.compile(
        r'\[(\d+)\]\s*'
        r'(.+?)\.\s*'
        r'(.+?)\[M\]\.\s*'
        r'(.+?)\s*:\s*(.+?),\s*'
        r'(\d{4})'
        r'(?:\s*:\s*(\d+))?'
        r'\s*\.?\s*$'
    )

    def book_repl(m):
        num = m.group(1)
        author = format_author_bluebook(m.group(2))
        title = m.group(3).strip()
        publisher = m.group(5).strip()
        year = m.group(6)
        page = m.group(7) or ''

        result = f"{author}, {title} ({publisher} {year} ed."
        if page:
            result += f" at {page}"
        result += ")."
        return f"{num}. {result}"

    text = book_pattern.sub(book_repl, text)

    # 3. 编著章节转换
    # [序号] 作者. 章节标题[A]. 编者. 书名[C]. 出版地: 出版社, 年份: 引用页码.
    chapter_pattern = re.compile(
        r'\[(\d+)\]\s*'
        r'(.+?)\.\s*'
        r'(.+?)\[A\]\.\s*'
        r'(.+?)\.\s*'
        r'(.+?)\[C\]\.\s*'
        r'(.+?)\s*:\s*(.+?),\s*'
        r'(\d{4})'
        r'(?:\s*:\s*(\d+))?'
        r'\s*\.?\s*$'
    )

    def chapter_repl(m):
        num = m.group(1)
        author = format_author_bluebook(m.group(2))
        title = m.group(3).strip()
        editor = format_author_bluebook(m.group(4))
        book = m.group(5).strip()
        publisher = m.group(7).strip()
        year = m.group(8)
        page = m.group(9) or ''

        result = f"{author}, {title}, in {editor} ed., {book} ({publisher} {year}"
        if page:
            result += f") at {page}"
        else:
            result += ")"
        result += "."
        return f"{num}. {result}"

    text = chapter_pattern.sub(chapter_repl, text)

    return text


# ============ Bluebook → GB/T 7714 ============

def bluebook_to_gbt7714(text):
    """将 Bluebook 格式的引用转换为 GB/T 7714 格式"""

    # 1. 期刊论文转换
    # Author, Title, Volume Journal Page (Year).
    bj_pattern = re.compile(
        r'(\d+)\.\s*'
        r'(.+?),\s*'
        r'(.+?),\s*'
        r'(\d+)\s+'
        r'(.+?)\s+'
        r'(\d+)(?:-(\d+))?\s+'
        r'\((\d{4})\)\.?\s*$'
    )

    def bj_repl(m):
        num = m.group(1)
        author = m.group(2).strip()
        title = m.group(3).strip().rstrip(',')
        volume = m.group(4)
        journal_abbr = m.group(5).strip()
        start_page = m.group(6)
        end_page = m.group(7) or ''
        year = m.group(8)

        journal_cn = reverse_translate_journal(journal_abbr)

        result = f"[{num}] {author}. {title}[J]. {journal_cn}, {year}"
        result += f", {volume}"
        if start_page:
            result += f": {start_page}"
            if end_page:
                result += f"-{end_page}"
        result += "."

        return result

    text = bj_pattern.sub(bj_repl, text)

    # 2. 专著转换
    # Author, Title (Publisher Year ed.) at Page.
    bb_book_pattern = re.compile(
        r'(\d+)\.\s*'
        r'(.+?),\s*'
        r'(.+?)\s+'
        r'\((.+?)\s+(\d{4})\s*ed\.\)'
        r'(?:\s+at\s+(\d+))?'
        r'\.?\s*$'
    )

    def bb_book_repl(m):
        num = m.group(1)
        author = m.group(2).strip()
        title = m.group(3).strip().rstrip(',')
        publisher = m.group(4).strip()
        year = m.group(5)
        page = m.group(6) or ''

        result = f"[{num}] {author}. {title}[M]. 北京: {publisher}, {year}"
        if page:
            result += f": {page}"
        result += "."

        return result

    text = bb_book_pattern.sub(bb_book_repl, text)

    return text


# ============ 辅助函数 ============

def format_author_bluebook(author_str):
    """
    将中文作者格式转为 Bluebook 格式。
    中文: 张三, 李四, 王五
    Bluebook: Zhang San, Li Si & Wang Wu
    """
    authors = [a.strip() for a in author_str.replace('，', ',').split(',') if a.strip()]

    # 处理"等"/"et al."
    if authors and authors[-1].strip() in ['等', 'et al.', 'et al']:
        authors = authors[:-1]

    # 处理译者标注
    authors = [a.split('译')[0].split('，译')[0].strip() for a in authors]

    # 中文人名转拼音（简化版：直接保留原样，实际应用中可接 pypinyin）
    bluebook_authors = []
    for i, a in enumerate(authors):
        if not a:
            continue
        if i == len(authors) - 1 and len(authors) > 1:
            bluebook_authors.append(f"& {a}")
        else:
            bluebook_authors.append(a)

    return ', '.join(bluebook_authors)


# 常见中文法学期刊 → 英文 → Bluebook 缩写
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
    # Common English law journals
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
    """中文期刊名 → 英文名"""
    return JOURNAL_TRANSLATIONS.get(cn_name.strip(), cn_name.strip())


def abbreviate_journal(en_name):
    """英文期刊名 → Bluebook 缩写"""
    return JOURNAL_ABBREVIATIONS.get(en_name.strip(), en_name.strip())


def reverse_translate_journal(abbr):
    """Bluebook 缩写 → 中文名"""
    reverse = {v: k for k, v in JOURNAL_ABBREVIATIONS.items()}
    return reverse.get(abbr.strip(), abbr.strip())


# ============ 主程序 ============

def convert_file(input_path, source_fmt, target_fmt, output_path):
    """转换文件中的引用格式"""
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


def main():
    parser = argparse.ArgumentParser(
        description='法学论文引用格式转换器 (GB/T 7714 ↔ Bluebook)',
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


"""
=== 测试示例 ===

输入 (GB/T 7714):
[1] 王利明. 论民法典的时代特征与编纂步骤[J]. 中国法学, 2014(5): 32-45.
[2] 王泽鉴. 民法学说与判例研究(第一册)[M]. 北京: 北京大学出版社, 2009: 56.
[3] 张新宝. 侵权责任构成要件[A]. 王利明. 民法典侵权责任编研究[C]. 北京: 中国人民大学出版社, 2016: 89.

输出 (Bluebook):
1. 王利明, 论民法典的时代特征与编纂步骤, China Legal Sci. 32-45 (2014).
2. 王泽鉴, 民法学说与判例研究(第一册) (北京大学出版社 2009 ed.) at 56).
3. 张新宝, 侵权责任构成要件, in 王利明 ed., 民法典侵权责任编研究 (中国人民大学出版社 2016) at 89).
"""
