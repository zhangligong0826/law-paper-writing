import importlib.util
import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "references" / "citation-converter.py"

spec = importlib.util.spec_from_file_location("citation_converter", MODULE_PATH)
citation_converter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(citation_converter)


class CitationConverterTests(unittest.TestCase):
    def test_journal_year_issue_format(self):
        source = "[1] 王利明. 论民法典的时代特征与编纂步骤[J]. 中国法学, 2014(5): 32-45."
        result = citation_converter.gbt7714_to_bluebook(source)
        self.assertEqual(
            result,
            "1. 王利明, 论民法典的时代特征与编纂步骤, China Legal Sci. 32-45 (2014).",
        )

    def test_journal_volume_issue_format(self):
        source = "[2] 张三. 算法透明义务研究[J]. 法学研究, 2022, 44(3): 12-30."
        result = citation_converter.gbt7714_to_bluebook(source)
        self.assertEqual(
            result,
            "2. 张三, 算法透明义务研究, 44 Chin. J. L. 12-30 (2022).",
        )

    def test_journal_year_pages_format(self):
        source = "[3] 李四. 自动化决策的法律边界[J]. 法学, 2021: 5-18."
        result = citation_converter.gbt7714_to_bluebook(source)
        self.assertEqual(
            result,
            "3. 李四, 自动化决策的法律边界, Law Sci. 5-18 (2021).",
        )

    def test_book_conversion(self):
        source = "[4] 王泽鉴. 民法学说与判例研究(第一册)[M]. 北京: 北京大学出版社, 2009: 56."
        result = citation_converter.gbt7714_to_bluebook(source)
        self.assertEqual(
            result,
            "4. 王泽鉴, 民法学说与判例研究(第一册) (北京大学出版社 2009 ed.) at 56.",
        )

    def test_chapter_conversion(self):
        source = "[5] 张新宝. 侵权责任构成要件[A]. 王利明. 民法典侵权责任编研究[C]. 北京: 中国人民大学出版社, 2016: 89."
        result = citation_converter.gbt7714_to_bluebook(source)
        self.assertEqual(
            result,
            "5. 张新宝, 侵权责任构成要件, in 王利明 ed., 民法典侵权责任编研究 (中国人民大学出版社 2016) at 89.",
        )

    def test_unrecognized_format_is_preserved(self):
        source = "这不是一条规范的参考文献。"
        result = citation_converter.gbt7714_to_bluebook(source)
        self.assertEqual(result, source)


if __name__ == "__main__":
    unittest.main()
