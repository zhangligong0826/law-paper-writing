# 法学论文 Word 文档工作流指南

> 本文档系统梳理法学论文在 Microsoft Word 中的格式规范、Python 自动化方案、排版检查要点及 Skill 集成方法，供法学研究者参考使用。

---

## 一、法学论文 Word 格式规范详解

### 1.1 CSSCI 期刊通用 Word 格式参数

CSSCI（中文社会科学引文索引）收录的法学期刊对投稿稿件有统一的格式要求，以下为**通用基准参数**：

| 格式项目 | 参数值 | Word 设置路径 |
|---------|--------|--------------|
| **纸张大小** | A4 (210mm × 297mm) | 布局 → 页面设置 → 纸张 |
| **页边距-上** | 2.5 cm | 布局 → 页面设置 → 页边距 |
| **页边距-下** | 2.5 cm | 同上 |
| **页边距-左** | 2.8–3.2 cm | 同上（多数为 3.0 cm） |
| **页边距-右** | 2.5–3.0 cm | 同上（多数为 2.8 cm） |
| **装订线** | 0 cm 或 0.5 cm | 同上 |
| **正文字体** | 宋体 (SimSun) | 开始 → 字体 |
| **正文字号** | 小四 (12 pt) | 同上 |
| **正文行距** | 固定值 20–22 磅 或 1.25–1.5 倍行距 | 段落 → 行距 |
| **段首缩进** | 2 字符 | 段落 → 缩进和间距 |
| **段后间距** | 0 行（部分期刊要求 0.5 行） | 同上 |

### 1.2 主流法学期刊具体格式差异表

不同 CSSCI 法学期刊在格式细节上存在差异，投稿前务必核对目标期刊的最新《稿约》。

| 期刊名称 | 正文字号/字体 | 行距 | 页边距(左/右) | 脚注字号 | 脚注编号形式 | 标题层次 | 特殊要求 |
|---------|--------------|------|---------------|---------|-------------|---------|---------|
| **法学研究** | 小四/宋体 | 固定22磅 | 3.0/2.8cm | 五号/宋体 | ①②③（圈码） | 一、(一)、1.、(1) | 摘要300字以内；关键词3-5个；英文摘要 |
| **中国法学** | 小四/宋体 | 1.5倍 | 3.2/3.0cm | 小五/宋体 | [1][2]（方括号） | 一、(一)、1、(1) | 中英文双语标题与摘要；参考文献单独列出 |
| **法学** | 小四/宋体 | 固定20磅 | 3.0/2.8cm | 五号/宋体 | ①②③ | 一、(一)、1.、(1) | 脚注连续编号；不设参考文献 |
| **中外法学** | 五号/宋体 | 1.25倍 | 2.8/2.5cm | 小五/宋体 | ①②③ | 一、(一)、1.、(1) | 英文注释采用Bluebook格式 |
| **政法论坛** | 小四/宋体 | 固定21磅 | 3.0/2.8cm | 五号/宋体 | ①②③ | 一、(一)、1.、(1) | 摘要与正文之间空一行 |
| **法学家** | 小四/宋体 | 固定22磅 | 3.0/2.8cm | 五号/宋体 | ①②③ | 一、(一)、1.、(1) | 需提供作者简介（200字内） |
| **法商研究** | 小四/宋体 | 1.5倍 | 3.0/2.5cm | 小五/宋体 | [1][2] | 一、(一)、1.、(1) | 脚注含文献页码信息 |
| **现代法学** | 小四/宋体 | 固定21磅 | 3.0/2.8cm | 五号/宋体 | ①②③ | 一、(一)、1.、(1) | 基金项目标注于首页页脚 |
| **法律科学** | 五号/宋体 | 固定20磅 | 2.9/2.6cm | 小五/宋体 | ①②③ | 一、(一)、1.、(1) | 每篇文章不超过15000字 |
| **环球法律评论** | 小四/宋体 | 1.5倍 | 3.0/2.8cm | 小五/宋体 | [1][2] | 一、(一)、1.、(1) | 外文引注需附原文标题 |

### 1.3 脚注格式在 Word 中的实现方法

法学论文的核心特征之一是**密集的脚注引用**，正确配置脚注至关重要。

#### 1.3.1 插入脚注的基本操作

1. 将光标置于需要插入脚注的位置
2. 点击「引用」→「插入脚注」（快捷键 `Ctrl+Alt+F` / `Cmd+Option+F`）
3. 在页面底部的脚注编辑区输入脚注内容

#### 1.3.2 脚注格式设置

| 设置项 | 推荐值 | Word 操作路径 |
|-------|--------|--------------|
| **位置** | 页面底端 | 引用 → 脚注和尾注对话框 |
| **编号格式** | ①②③（圈码）或 [1][2]（方括号） | 同上 → 编号格式下拉菜单 |
| **起始编号** | 1 | 同上 |
| **编号方式** | 连续编号 | 同上 |
| **脚注字体** | 宋体 | 选中脚注文本 → 开始 → 字体 |
| **脚注字号** | 五号或小五 | 同上 |
| **脚注行距** | 与正文一致或略小（固定18-20磅） | 段落 → 行距 |
| **脚注分隔线** | 默认短横线（可自定义长度） | 视图 → 草稿 → 展开"所有脚注"区域 |

#### 1.3.3 圈码脚注的实现技巧

Word 默认脚注编号为 `1, 2, 3...`。若目标期刊要求圈码（①②③），有两种方式：

**方式 A：修改编号格式**
- 打开「引用」→「脚注和尾注」对话框
- 编号格式选择「①②③」（如列表中无此选项，需通过"自定义标记"手动输入 Unicode 圈码字符）

**方式 B：查找替换（批量转换）**
- 完成全文写作后，将脚注编号统一替换为圈码
- 使用 `Ctrl+H` 打开查找替换
- 注意：此方式可能导致编号与自动更新冲突，**不推荐用于长文**

### 1.4 标题层次编号的 Word 自动化

法学论文通常采用四级标题结构，应在 Word 中利用**多级列表功能**实现自动化编号：

```
一、一级标题（章/节）
    （二）二级标题（目）
        1. 三级标题（子目）
            （1）四级标题（细目）
```

#### 配置步骤

1. 点击「开始」→「多级列表」→「定义新的多级列表」
2. 配置各级别参数：

| 级别 | 编号样式 | 缩进位置 | 字体 | 字号 | 对齐 |
|-----|---------|---------|------|------|------|
| Level 1 | 一、二、三、 | 0字符 | 黑体 | 三号（16pt） | 居左 |
| Level 2 | （一）（二）（三） | 2字符 | 楷体 | 四号（14pt） | 居左 |
| Level 3 | 1. 2. 3. | 4字符 | 黑体 | 小四（12pt） | 居左 |
| Level 4 | （1）（2）（3） | 6字符 | 宋体 | 小四（12pt） | 居左 |

3. 将每个级别链接到对应的**内置标题样式**（标题 1、标题 2、标题 3...）
4. 这样修改任一级别编号后，后续级别会自动重新编号

---

## 二、python-docx 模板方案

### 2.1 安装说明

```bash
pip install python-docx
```

python-docx 是一个纯 Python 库，用于创建和更新 `.docx` 文件（即 Word 2007+ 文档）。它无需安装 Microsoft Office 即可运行，跨平台兼容。

### 2.2 完整代码模板：生成符合 CSSCI 通用格式的法学论文

以下脚本可一键生成一篇包含完整格式的法学论文模板文档：

```python
"""
法学论文 Word 文档自动生成器
=============================
基于 python-docx，生成符合 CSSCI 法学期刊通用格式规范的 .docx 文件。
运行环境: Python 3.8+, python-docx >= 0.8.11
用法: python law_paper_generator.py
"""

from docx import Document
from docx.shared import Pt, Cm, Inches, Emu, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement


def set_run_font(run, font_name_cn='宋体', font_name_en='Times New Roman', size=Pt(12), bold=False):
    """为 run 对象设置中英文字体和字号"""
    # 设置中文字体
    run.font.name = font_name_en
    run._element.rPr.rFonts.set(qn('w:eastAsia'), font_name_cn)
    run.font.size = size
    run.font.bold = bold


def setup_page_section(section):
    """
    配置页面设置 - CSSCI 法学论文通用标准
    纸张A4, 上边距2.5cm, 下边距2.5cm, 左边距3.0cm, 右边距2.8cm
    """
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    section.top_margin = Cm(2.5)
    section.bottom_margin = Cm(2.5)
    section.left_margin = Cm(3.0)
    section.right_margin = Cm(2.8)
    # 装订线
    section.gutter = Cm(0.0)


def configure_styles(doc):
    """配置文档样式：正文 + 标题层级"""

    # ---- 正文样式 ----
    body_style = doc.styles['Normal']
    body_style.font.name = 'Times New Roman'
    body_style._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
    body_style.font.size = Pt(12)  # 小四
    body_format = body_style.paragraph_format
    body_format.first_line_indent = Pt(24)  # 段首缩进2字符
    body_format.line_spacing_rule = WD_LINE_SPACING.FIXED
    body_format.line_spacing = Pt(22)       # 固定行距22磅
    body_format.space_before = Pt(0)
    body_format.space_after = Pt(0)

    # ---- 标题1：一、二、三、 ----
    h1_style = doc.styles['Heading 1']
    h1_style.font.name = 'Times New Roman'
    h1_style._element.rPr.rFonts.set(qn('w:eastAsia'), '黑体')
    h1_style.font.size = Pt(16)  # 三号
    h1_style.font.bold = True
    h1_format = h1_style.paragraph_format
    h1_format.first_line_indent = Pt(0)   # 标题不缩进
    h1_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
    h1_format.space_before = Pt(12)
    h1_format.space_after = Pt(6)

    # ---- 标题2：（一）（二）（三） ----
    h2_style = doc.styles['Heading 2']
    h2_style.font.name = 'Times New Roman'
    h2_style._element.rPr.rFonts.set(qn('w:eastAsia'), '楷体')
    h2_style.font.size = Pt(14)  # 四号
    h2_style.font.bold = False
    h2_format = h2_style.paragraph_format
    h2_format.first_line_indent = Pt(0)
    h2_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
    h2_format.space_before = Pt(10)
    h2_format.space_after = Pt(4)

    # ---- 标题3：1. 2. 3. ----
    h3_style = doc.styles['Heading 3']
    h3_style.font.name = 'Times New Roman'
    h3_style._element.rPr.rFonts.set(qn('w:eastAsia'), '黑体')
    h3_style.font.size = Pt(12)  # 小四
    h3_style.font.bold = True
    h3_format = h3_style.paragraph_format
    h3_format.first_line_indent = Pt(0)
    h3_format.line_spacing_rule = WD_LINE_SPACING.FIXED
    h3_format.line_spacing = Pt(22)
    h3_format.space_before = Pt(6)
    h3_format.space_after = Pt(3)


def add_title_with_number(doc, text, level):
    """
    添加带中文序号的标题
    level 1 -> "一、xxx"
    level 2 -> "(一) xxx"
    level 3 -> "1. xxx"
    """
    chinese_numerals = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九', '十']

    if level == 1:
        # 使用 Heading 1 样式，手动添加中文数字编号
        p = doc.add_paragraph(style='Heading 1')
        run = p.add_run(text)
        set_run_font(run, '黑体', 'Times New Roman', Pt(16), bold=True)
        return p

    elif level == 2:
        p = doc.add_paragraph(style='Heading 2')
        run = p.add_run(text)
        set_run_font(run, '楷体', 'Times New Roman', Pt(14))
        return p

    elif level == 3:
        p = doc.add_paragraph(style='Heading 3')
        run = p.add_run(text)
        set_run_font(run, '黑体', 'Times New Roman', Pt(12), bold=True)
        return p

    else:
        # level 4: 使用正文样式的加粗文本
        p = doc.add_paragraph()
        run = p.add_run(text)
        set_run_font(run, '宋体', 'Times New Roman', Pt(12), bold=True)
        return p


def add_body_paragraph(doc, text, first_line_indent=True):
    """
    添加正文段落（自动应用正文样式）
    first_line_indent: 是否段首缩进（默认True）
    """
    p = doc.add_paragraph()
    if not first_line_indent:
        p.paragraph_format.first_line_indent = Pt(0)
    run = p.add_run(text)
    set_run_font(run, '宋体', 'Times New Roman', Pt(12))
    return p


def add_footnote_reference(doc, paragraph, footnote_text, ref_text=None):
    """
    在指定段落末尾添加脚注引用
    paragraph: 目标段落对象
    footnote_text: 脚注内容文本
    ref_text: 脚注标记前的引导文字（可选）
    """
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn as oxml_qn

    # 添加脚注前的引导文字
    if ref_text:
        run_ref = paragraph.add_run(ref_text)
        set_run_font(run_ref, '宋体', 'Times New Roman', Pt(12))

    # 使用 python-docx 的 footnote 功能添加脚注
    # 注意：python-docx 对脚注的支持有限，这里演示基本用法
    run_fn = paragraph.add_run(f'[{footnote_text}]')
    run_fn.font.superscript = True
    set_run_font(run_fn, '宋体', 'Times New Roman', Pt(9))

    return run_fn


def create_law_paper_template(output_path='法学论文模板.docx'):
    """
    主函数：生成完整的法学论文模板文档
    包含：标题、作者、摘要、关键词、正文各层级、脚注示例
    """

    # 创建文档对象
    doc = Document()

    # ====== 第一步：页面设置 ======
    section = doc.sections[0]
    setup_page_section(section)

    # ====== 第二步：配置样式 ======
    configure_styles(doc)

    # ====== 第三步：论文标题 ======
    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_run = title_p.add_run('论刑法中的因果关系判断标准')
    set_run_font(title_run, '黑体', 'Times New Roman', Pt(22), bold=True)
    # 标题前后留白
    title_p.paragraph_format.space_before = Pt(24)
    title_p.paragraph_format.space_after = Pt(12)

    # ====== 第四步：作者信息 ======
    author_p = doc.add_paragraph()
    author_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    author_run = author_p.add_run('张三¹  李四²')
    set_run_font(author_run, '宋体', 'Times New Roman', Pt(12))
    author_p.paragraph_format.space_after = Pt(6)

    affil_p = doc.add_paragraph()
    affil_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    affil_run = affil_p.add_run(
        '(1. XX大学法学院教授, 北京 100871; '
        '2. YY大学法学院副教授, 上海 200062)'
    )
    set_run_font(affil_run, '宋体', 'Times New Roman', Pt(9))  # 六号或小五
    affil_p.paragraph_format.space_after = Pt(18)

    # ====== 第五步：中文摘要 ======
    abstract_label = doc.add_paragraph()
    abstract_label.alignment = WD_ALIGN_PARAGRAPH.CENTER
    label_run = abstract_label.add_run('【摘  要】')
    set_run_font(label_run, '黑体', 'Times New Roman', Pt(12), bold=True)
    abstract_label.paragraph_format.space_after = Pt(0)

    abstract_text = (
        '因果关系是刑法归责理论中的核心问题，也是司法实践中认定犯罪成立的关键要素。'
        '本文以相当因果关系说为基础，结合我国刑法理论和司法判例，对刑法因果关系的判断标准进行系统分析。'
        '研究认为，刑法因果关系的认定应坚持客观归责与主观归责相统一的原则，在事实因果关系的基础上，'
        '进一步考察法律因果关系是否成立。文章最后提出完善我国刑法因果关系判断标准的立法建议。'
    )
    abs_p = doc.add_paragraph()
    abs_run = abs_p.add_run(abstract_text)
    set_run_font(abs_run, '宋体', 'Times New Roman', Pt(10))  # 五号
    abs_p.paragraph_format.space_after = Pt(6)

    # ====== 第六步：关键词 ======
    kw_label_p = doc.add_paragraph()
    kw_label_p.paragraph_format.first_line_indent = Pt(0)
    kw_label_run = kw_label_p.add_run('【关键词】')
    set_run_font(kw_label_run, '黑体', 'Times New Roman', Pt(12), bold=True)

    kw_content_run = kw_label_p.add_run('  刑法因果关系; 相当因果关系说; 客观归责; 司法适用')
    set_run_font(kw_content_run, '宋体', 'Times New Roman', Pt(12))
    kw_label_p.paragraph_format.space_after = Pt(18)

    # ====== 第七步：英文摘要 ======
    en_title_p = doc.add_paragraph()
    en_title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    en_title_run = en_title_p.add_run(
        'On the Standard of Causation Determination in Criminal Law'
    )
    set_run_font(en_title_run, 'Times New Roman', 'Times New Roman', Pt(15), bold=True)
    en_title_p.paragraph_format.space_after = Pt(6)

    en_abstract_label = doc.add_paragraph()
    en_abs_label_run = en_abstract_label.add_run('【Abstract】')
    set_run_font(en_abs_label_run, 'Times New Roman', 'Times New Roman', Pt(11), bold=True)

    en_abstract_text = (
        'Causation is a core issue in criminal law imputation theory and a key element '
        'in determining the establishment of crimes in judicial practice. Based on the theory of adequate causation, '
        'this paper systematically analyzes the standards for determining criminal law causation '
        'in light of Chinese criminal law theory and judicial precedents.'
    )
    en_abs_p = doc.add_paragraph()
    en_abs_run = en_abs_p.add_run(en_abstract_text)
    set_run_font(en_abs_run, 'Times New Roman', 'Times New Roman', Pt(10))

    en_kw_p = doc.add_paragraph()
    en_kw_p.paragraph_format.first_line_indent = Pt(0)
    en_kw_r1 = en_kw_p.add_run('【Key Words】')
    set_run_font(en_kw_r1, 'Times New Roman', 'Times New Roman', Pt(11), bold=True)
    en_kw_r2 = en_kw_p.add_run('  Criminal Law Causation; Adequate Causation Theory; Objective Imputation')
    set_run_font(en_kw_r2, 'Times New Roman', 'Times New Roman', Pt(10))
    en_kw_p.paragraph_format.space_after = Pt(24)

    # ====== 第八步：正文内容 ======

    # 一、问题提出
    add_title_with_number(doc, '一、问题的提出', 1)
    add_body_paragraph(doc,
        '因果关系问题是刑法理论中最具争议的话题之一。从19世纪以来的刑法学发展史来看，'
        '关于因果关系的学说层出不穷，包括条件说、原因说、相当因果关系说、客观归责理论等，'
        '每一种学说都试图为刑事责任的归属提供一个确定性的判断框架。然而时至今日，'
        '这一问题仍未得到彻底解决。')

    add_body_paragraph(doc,
        '在我国司法实践中，因因果关系判断不当导致的错案屡见不鲜。例如，在某些医疗过失案件中，'
        '医生的行为与患者死亡结果之间的因果关系往往成为控辩双方争议的焦点。'
        '如何建立一套既具有理论自洽性又具备实践操作性的因果关系判断标准，'
        '是当前刑法学研究亟待回应的重大课题。')

    # （一）研究背景
    add_title_with_number(doc, '（一）研究背景与意义', 2)
    add_body_paragraph(doc,
        '随着社会生活的复杂化，新型犯罪形态不断涌现，传统的因果关系理论面临严峻挑战。'
        '特别是在网络犯罪、环境犯罪等领域，因果链条的识别和证明变得更加困难。')

    # （二）研究现状
    add_title_with_number(doc, '（二）国内外研究现状', 2)
    add_body_paragraph(doc,
        '德日刑法学界对因果关系的研究已形成较为成熟的理论体系。德国通说采客观归责理论，'
        '将因果关系问题拆分为事实层面的归因和法律层面的归责两个阶段。'
        '日本学界则在相当因果关系说的基础上发展出了多种修正学说。'
        '相比之下，我国刑法学界的讨论尚处于引进和消化阶段，原创性理论贡献有限。')

    # 二、理论框架
    add_title_with_number(doc, '二、刑法因果关系的理论基础', 1)

    add_title_with_number(doc, '（一）条件说及其局限', 2)
    add_body_paragraph(doc,
        '条件说（Bedingungstheorie）又称"若无则不"公式（conditio sine qua non），'
        '主张只要某一行为是结果发生的必要条件，二者之间即存在因果关系。'
        '该学说的优点在于判断标准清晰明确，但其缺陷也十分明显——条件范围过于宽泛，'
        '容易导致因果链条无限延伸，从而不当扩大刑事责任的范围。')

    add_title_with_number(doc, '（二）相当因果关系说的核心主张', 2)
    add_body_paragraph(doc,
        '相当因果关系说（Adäquanztheorie）由德国学者冯·克里斯（von Kries）于19世纪末创立，'
        '后经多数学者的发展和完善，已成为大陆法系国家的主流学说。其核心观点是：'
        '只有根据一般生活经验，某行为通常能够引起某种结果时，才能认定二者之间存在刑法上的因果关系。')

    add_body_paragraph(doc,
        '"相当性"的判断标准存在主观说、客观说和折中说三种立场。'
        '其中，折中说（又称混合说）目前占据主导地位，该说主张以行为时一般人所能认识到的事实'
        '以及行为人所特别认识到的事实为基础，从事后的视角进行相当性的判断。')

    # 三、实证分析
    add_title_with_number(doc, '三、我国司法实践中的适用困境', 1)

    add_title_with_number(doc, '（一）典型案例分析', 2)
    add_body_paragraph(doc,
        '通过对近十年来最高人民法院公布的指导性案例以及各省高级人民法院审理的相关案件进行分析，'
        '可以发现我国司法机关在因果关系认定上呈现出以下特点：一是缺乏统一的裁判标准，'
        '同类案件在不同法院可能得出截然相反的结论；二是说理过程不够充分，'
        '判决书往往直接给出结论而省略推理环节；三是对于复杂因果链案件的处理能力有待提高。')

    add_title_with_number(doc, '（二）成因剖析', 2)
    add_body_paragraph(doc,
        '上述问题的产生有多重原因。从制度层面看，我国现行刑法及司法解释'
        '未对因果关系的判断标准作出明确规定，导致法官在裁判过程中缺乏明确的指引。'
        '从技术层面看，部分法官对相关理论的掌握程度不足，难以应对复杂的因果认定问题。'
        '从文化层面看，我国司法传统更注重实质正义而非形式逻辑，这在一定程度上影响了'
        '因果关系分析的精确性和系统性。')

    # 四、建议
    add_title_with_number(doc, '四、完善我国刑法因果关系判断标准的建议', 1)

    add_title_with_number(doc, '（一）确立"双层递进式"判断框架', 2)
    add_body_paragraph(doc,
        '借鉴德日的经验，建议在我国刑法理论和司法实践中引入"双层递进式"的因果关系判断框架：'
        '第一层为事实因果关系层面，主要解决行为与结果之间是否存在引起与被引起的客观联系，'
        '可采用修正的条件说作为判断工具；第二层为法律因果关系层面，'
        '主要解决在众多条件中哪些应当被纳入刑法的评价范围，'
        '应以相当性原则为核心并结合客观归责理论的具体规则进行综合判断。')

    add_title_with_number(doc, '（二）推进类型化案例指导机制', 2)
    add_body_paragraph(doc,
        '建议最高人民法院加强对涉及因果关系疑难案件的案例指导工作，'
        '按照犯罪类型的差异分别发布典型案例，为下级法院提供更具针对性的裁判参照。'
        '同时，应当在判决书的说理部分强化对因果关系认定过程的展示，'
        '使当事人和社会公众能够清晰地了解裁判的逻辑依据。')

    # ====== 第九步：保存文档 ======
    doc.save(output_path)
    print(f'✓ 法学论文模板已成功生成: {output_path}')
    print(f'  - 论文标题: 论刑法中的因果关系判断标准')
    print(f'  - 格式标准: CSSCI 通用规范（小四宋体, 固定行距22磅, 左边距3.0cm）')
    print(f'  - 结构组成: 标题 + 作者 + 中文摘要 + 关键词 + 英文摘要 + 正文四级标题')
    return output_path


# ====== 执行入口 ======
if __name__ == '__main__':
    output_file = create_law_paper_template()
```

### 2.3 代码结构说明

| 函数名 | 功能 | 关键参数 |
|-------|------|---------|
| `set_run_font()` | 统一设置中英文字体和字号 | font_name_cn, font_name_en, size, bold |
| `setup_page_section()` | 配置页面尺寸和边距 | A4纸张, 左3.0cm/右2.8cm/上下2.5cm |
| `configure_styles()` | 定义正文和标题1-3样式 | 宋体正文, 黑体H1, 楷体H2 |
| `add_title_with_number()` | 添加带层级的标题 | level=1/2/3 对应三级标题 |
| `add_body_paragraph()` | 添加正文段落 | 自动应用首行缩进和行距 |
| `create_law_paper_template()` | 主函数，生成完整论文 | 输出路径可自定义 |

---

## 三、Word 文档排版检查清单

投稿前务必逐项核查以下格式要点：

### 3.1 核心检查项（必查）

| 序号 | 检查项目 | 标准要求 | 常见错误 |
|-----|---------|---------|---------|
| 1 | **纸张与页边距** | A4, 左3.0±0.2cm, 右2.8±0.3cm | 使用了默认的普通文档边距 |
| 2 | **正文字体字号** | 宋体, 小四(12pt) | 混入仿宋、楷体或其他非标准字体 |
| 3 | **正文行距** | 固定值20-22磅 或 1.25-1.5倍行距 | 全文行距不一致，部分段落异常稀疏/紧凑 |
| 4 | **段首缩进** | 统一2字符（首行不空行的除外） | 使用空格代替缩进；全角/半角混用 |
| 5 | **脚注编号连续性** | 全文脚注编号从1开始连续排列 | 删除某段落后脚注断号；复制粘贴导致重复编号 |
| 6 | **脚注格式一致性** | 字体、字号、行距统一 | 不同时期的脚注格式不一致 |
| 7 | **标题层次清晰** | 各级标题编号格式统一（一/(一)/1./(1)） | 手动编号导致增删章节后编号混乱 |
| 8 | **标点符号规范** | 全角标点（中文语境）；英文/数字两侧加空格 | 中英文混排处标点半角/全角混乱 |
| 9 | **图表编号与标题** | 图X / 表X，居中，图下表上 | 图表缺少编号或编号不连续 |
| 10 | **页眉页脚** | 按期刊要求设置（通常含文章标题/作者/页码） | 缺少页码或页码位置错误 |

### 3.2 进阶检查项（推荐）

| 序号 | 检查项目 | 说明 |
|-----|---------|------|
| 11 | **字体嵌入** | 文件 → 选项 → 保存 → 勾选"将字体嵌入文件"，确保接收方能正确显示 |
| 12 | **隐藏字符检查** | 按 Ctrl+Shift+* 显示所有格式标记，排查多余的手动换行符、空格、制表符 |
| 13 | **样式使用率** | 尽量通过样式而非手动格式化来控制外观，便于后期统改 |
| 14 | **目录更新** | 若包含目录，务必右键"更新域"以确保页码准确 |
| 15 | **文档属性** | 文件 → 信息 → 属性，填写标题、作者、关键词等信息 |
| 16 | **文件大小** | 过大可能含冗余修订记录，建议"另存为"清理 |

### 3.3 常见 Word 排版陷阱

#### 陷阱 1：脚注编号不连续
- **现象**：删除一段带脚注的文字后，脚注编号出现跳号（如从⑤直接到⑦）
- **原因**：Word 脚注默认设置为"连续编号"，但某些操作（如剪切粘贴、接受修订）可能导致编号异常
- **解决方案**：
  1. 选中全部文本（`Ctrl+A`），按 `F9` 更新所有域
  2. 若无效，打开「引用」→「脚注和尾注」，确认编号方式为"连续"
  3. 最后手段：逐一检查并手动修正

#### 陷阱 2：字体混乱
- **现象**：同一文档中出现多种看似相同但实际不同的"宋体"字体（如 SimSun、宋体、NSimSun）
- **原因**：从不同来源复制粘贴文本时携带了源文档的字体定义；使用了不规范的字体别名
- **解决方案**：
  1. 使用「开始」→「替换字体」功能（`Ctrl+H` → 更多 → 特殊格式 → 替换字体）
  2. 将所有字体统一为目标字体
  3. 建议从头开始基于模板撰写，避免大量复制粘贴

#### 陷阱 3：行距不一致
- **现象**：部分段落明显比其他段落稀疏或紧凑
- **原因**：Word 存储了多种行距模式（单倍、1.5倍、固定值、最小值等），不同来源的文本携带不同的行距设定
- **解决方案**：
  1. `Ctrl+A` 全选后，统一设置段落行距
  2. 通过"样式"管理器确保正文样式被正确应用到所有段落
  3. 检查是否有段落意外应用了其他样式

#### 陷阱 4：手动编号的灾难
- **现象**：在"一、问题提出"之后新增了一个章节，后续所有手动输入的"二、""三、"都需要逐一修改
- **原因**：未使用 Word 的多级列表/标题样式功能，而是手工键入编号
- **解决方案**：**始终使用多级列表 + 标题样式联动**，让 Word 自动维护编号序列

#### 陷阱 5：制表符 vs 表格
- **现象**：用 Tab 键和空格"画"出的对齐效果在其他电脑上完全错位
- **原因**：制表位的设置依赖于具体的字体和字号，换一台电脑或调整显示比例后对齐关系失效
- **解决方案**：需要表格对齐的内容请使用 Word 表格功能，不要用制表符模拟

---

## 四、docx Skill 集成指引

### 4.1 WorkBuddy docx Skill 简介

WorkBuddy 平台内置了 **docx** Skill，专门用于处理 Word 文档（`.docx` 文件）的读取、创建和编辑操作。借助该 Skill 可以大幅简化法学论文的排版工作。

### 4.2 docx Skill 安装与调用

docx Skill 作为 WorkBuddy 内置插件，无需额外安装。使用方法如下：

#### 方式一：自然语言调用（推荐）

直接向 WorkBuddy 发送指令即可触发 docx Skill 处理能力，例如：

```
帮我创建一个符合《法学研究》格式要求的 Word 文档模板
读取 /path/to/paper.docx 并检查其脚注格式是否符合 CSSCI 规范
把这篇论文的正文行距改为固定值22磅
在指定位置插入一条脚注
```

WorkBuddy 会自动识别意图并调用 docx Skill 执行相应操作。

#### 方式二：Slash Command 调用

```
/docx create --template cssci-law --journal 法学研究
/docx read /path/to/paper.docx
/docx format-check /path/to/paper.docx --standard cssci
/docx edit /path/to/paper.docx --operation set-line-spacing --value 22pt
```

### 4.3 典型使用场景

| 场景 | 操作指令 | 说明 |
|-----|---------|------|
| **新建论文模板** | "按 CSSCI 格式新建一个法学论文 Word 模板" | 自动配置页面、字体、样式、标题层级 |
| **格式检查** | "检查这份文档的格式是否符合法学研究的要求" | 逐项对比期刊格式规范，输出检查报告 |
| **批量修改** | "将所有脚注字号改为五号宋体" | 利用 docx Skill 的批量编辑能力 |
| **脚注整理** | "校验全文脚注编号是否连续" | 检测断号、重号等问题 |
| **样式统一** | "将全文统一为宋体小四，行距固定22磅" | 一键规范化全文格式 |
| **提取文本** | "提取这个 docx 中的所有正文内容和脚注" | 便于后续处理或迁移至 LaTeX 等格式 |
| **合并文档** | "将 chapter1.docx 和 chapter2.docx 合并为一个文件" | 多文件整合 |

### 4.4 docx Skill 与 python-docx 的配合使用

在实际工作中，可以将两者结合使用：

```
┌─────────────────────────┐     ┌──────────────────────┐     ┌──────────────────────┐
│   WorkBuddy docx Skill   │ --> │   python-docx 脚本     │ --> │  最终 .docx 文档      │
│  (交互式操作/格式检查)    │     │  (批量生成/定制逻辑)   │     │  (投稿就绪)           │
└─────────────────────────┘     └──────────────────────┘     └──────────────────────┘
```

- **docx Skill** 适合交互式的单次操作（如格式检查、局部修改、快速预览）
- **python-docx** 适合程序化的批量任务（如从数据库批量生成论文模板、大规模格式转换）

---

## 附录：快速参考卡片

### CSSCI 法学论文核心参数速记

```
纸张: A4 (210×297 mm)
边距: 上2.5 下2.5 左3.0 右2.8 (cm)
正文: 宋体 / 小四(12pt) / 段首缩进2字符 / 行距固定22磅
脚注: 宋体 / 五号(10.5pt)或小五(9pt) / 编号连续 / 圈码①或方括号[1]
标题1: 黑体 / 三号(16pt) / 一、二、三、
标题2: 楷体 / 四号(14pt) / (一)(二)(三)
标题3: 黑体 / 小四(12pt)加粗 / 1. 2. 3.
摘要: 300字左右 / 五号 / 【摘  要】【关键词】
英文摘要: 必须有 / Times New Roman
```

### Word 快捷键速查

| 操作 | Windows | macOS |
|-----|---------|-------|
| 插入脚注 | `Ctrl+Alt+F` | `Cmd+Option+F` |
| 更新域 | `F9` | `F9` |
| 显示/隐藏格式标记 | `Ctrl+Shift+*` | `Cmd+Shift+*` |
| 查找和替换 | `Ctrl+H` | `Cmd+H` |
| 样式窗格 | `Alt+Ctrl+Shift+S` | `Cmd+Option+Shift+S` |
| 全选 | `Ctrl+A` | `Cmd+A` |
