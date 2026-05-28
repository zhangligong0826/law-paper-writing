<p align="center">
  <h1 align="center">Law Paper Writing</h1>
  <p align="center"><strong>面向法学硕博的 AI 论文写作与引用核查工具箱</strong></p>
  <p align="center">
    <a href="#3-分钟开始使用">快速开始</a> ·
    <a href="#我该复制哪个-prompt">复制 Prompt</a> ·
    <a href="#安装为-skill">安装 Skill</a> ·
    <a href="#完整示例">查看示例</a>
  </p>
  <p align="center">
    <img src="https://img.shields.io/badge/Version-1.2.0-blue" alt="version" />
    <img src="https://img.shields.io/badge/License-MIT-green" alt="license" />
    <img src="https://img.shields.io/badge/For-Law%20Students%20%26%20Researchers-9B59B6" alt="audience" />
    <img src="https://img.shields.io/badge/Coverage-CSSCI%20%7C%20SSCI%20%7C%20Thesis-0F766E" alt="coverage" />
  </p>
</p>

---

## 这是什么？

`law-paper-writing` 是一个给法学硕士、博士和青年研究者使用的 AI 写作工具箱。它借鉴 [awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) 的「可复制 Prompt + 可安装 Skill + 场景化工作流」思路，但不是把机器学习论文模板简单翻译成法学版本，而是围绕法学研究的真实工作重构：

- 法条、司法解释、案例、学术观点必须核查，不能让 AI 编造。
- 中文 CSSCI、英文 SSCI、学位论文的写作目标不同。
- 法学论文常用 Word、脚注、案例表、法条结构，而不是只用 LaTeX 和实验图表。
- 去 AI 味不能把正式法学表达改成口语，而要保留严谨、克制、可归因的学术语体。

一句话：**它帮你把 AI 用在法学论文写作、引用核查、投稿准备和论文修改上，但不替代你的法律判断。**

## 适合谁？

| 如果你是 | 可以用它做什么 |
|:---|:---|
| 法学硕士/博士 | 选题、开题、文献综述、章节框架、答辩准备 |
| 准备投 CSSCI 的作者 | 引言打磨、审稿人视角自检、引注和格式检查 |
| 准备写英文法学论文的作者 | SSCI 结构、英文摘要、贡献陈述、Bluebook 辅助整理 |
| 正在使用 ChatGPT/Cursor/WorkBuddy 的法学生 | 直接复制 Prompt，或安装 Skill 获得持续协作 |
| 想建立论文写作流程的人 | 使用 `references/` 中的指南、清单和工作流 |

## 它不做什么？

| 不做 | 原因 |
|:---|:---|
| 个案法律咨询 | 具体权益判断应咨询执业律师 |
| 诉状、合同、律师函等实务文书代写 | 本项目只服务学术写作 |
| 案件胜负预测 | 司法判断不能由通用 AI 替代 |
| 编造法条、案例、文献 | 法学论文的底线是可核查 |
| 规避学术诚信要求 | AI 只能辅助，不能替代作者研究责任 |

## 3 分钟开始使用

### 路径 A：不安装，直接复制 Prompt

这是最适合没有编程背景用户的方式。

1. 打开 [prompts/README.md](prompts/README.md)。
2. 找到你要做的任务，例如「选题」「文献综述」「去 AI 味」「模拟审稿」。
3. 复制对应文件里的 Prompt 模板。
4. 把模板中的 `【】` 内容替换成你的论文题目、研究方向、草稿或目标期刊。
5. 粘贴到 ChatGPT、Cursor、WorkBuddy 或其他 AI 助手中使用。

### 路径 B：安装为 Skill

适合已经在用 Cursor、WorkBuddy 或类似 AI 编程/写作助手的人。安装后，你可以直接说「帮我按法学论文写作 Skill 审一下这段引言」，AI 会按本项目的规则工作。

#### WorkBuddy / CodeBuddy Code

```bash
git clone https://github.com/zhangligong0826/law-paper-writing.git ~/.workbuddy/skills/law-paper-writing
```

这条命令的意思是：把本项目下载到 WorkBuddy 能识别的 Skill 文件夹中。

#### Cursor

```bash
npx openskills install zhangligong0826/law-paper-writing
```

这条命令的意思是：通过 OpenSkills 把本项目安装到 Cursor 可用的 Skill 环境中。

### 路径 C：只看示例，照着改

打开 [examples/](examples/)：

- [个人信息保护法自动化决策论文工作流](examples/pipl-article-workflow.md)
- [CSSCI 模拟审稿示例](examples/cssci-review-demo.md)
- [法条、案例、文献核查示例](examples/citation-check-demo.md)

这些示例不需要运行代码，适合先理解「AI 应该怎样参与法学论文写作」。

## 我该复制哪个 Prompt？

| 我想做什么 | 复制哪个文件 | 你需要替换什么 | 输出会是什么 |
|:---|:---|:---|:---|
| 判断题目能不能写 | [topic-selection.md](prompts/topic-selection.md) | 研究方向、初步题目、目标期刊/学位论文 | 题目评分、问题意识、修改题目、材料清单 |
| 写文献综述 | [literature-review.md](prompts/literature-review.md) | 已读文献、主题、研究问题 | 观点分类、研究缺口、综述结构 |
| 核查法条/案例/文献 | [legal-verification.md](prompts/legal-verification.md) | 法条、案号、文献条目 | 核查清单、风险等级、待确认项 |
| 整理脚注和参考文献 | [citation-and-footnotes.md](prompts/citation-and-footnotes.md) | 引用条目、目标格式 | 格式建议、疑点标记、人工核对清单 |
| 投稿前自查 | [reviewer-mode.md](prompts/reviewer-mode.md) | 摘要、引言、目录、正文片段 | 模拟审稿意见、主要问题、修改建议 |
| 去 AI 味和润色 | [de-ai-polishing.md](prompts/de-ai-polishing.md) | 需要修改的段落 | 痕迹识别、改写稿、保留术语说明 |
| 开题/答辩准备 | [thesis-defense.md](prompts/thesis-defense.md) | 题目、摘要、目录、导师意见 | 开题问题、答辩问题、修改说明 |

## Prompt 和 Skill 有什么区别？

| 类型 | 适合场景 | 使用方式 |
|:---|:---|:---|
| Prompt | 单次任务，例如改一段引言、检查一个题目 | 复制 `prompts/` 中的模板 |
| Skill | 连续任务，例如从选题到完整论文工作流 | 安装后自然语言触发 |
| references | 需要查方法、格式、清单、期刊信息 | 打开对应 Markdown 文件阅读 |
| examples | 不知道怎么开始，希望照着例子改 | 打开 `examples/` 中的完整示例 |

### 安装 Skill 后可以这样说

```text
帮我用法学论文写作 Skill 审一下这篇引言，目标期刊是《法学研究》。

我想写个人信息保护法第24条自动化决策，帮我判断题目是否适合 CSSCI。

请按法学论文去 AI 味规则修改下面 3 段，保留法条和案例引用。

帮我检查这些脚注是否有法条、案号或文献出处风险。

我准备硕士论文开题，题目是 XXX，请帮我模拟导师可能追问的问题。
```

## 核心能力

| 能力 | 法学版本的重点 |
|:---|:---|
| 选题与问题意识 | 从真实法律困境、解释争议、制度缺口中提炼可写问题 |
| 文献综述 | 不罗列学者观点，而是归类、比较、评价并定位研究缺口 |
| 法条与案例核查 | 标出必须核实的条文、案号、裁判要旨、引用页码 |
| 引用与脚注 | 辅助整理 GB/T 7714、脚注式、Bluebook，但最终必须人工核对 |
| CSSCI/SSCI 投稿 | 区分中文法学期刊、英文法学期刊和学位论文要求 |
| Word 文档工作流 | 支持脚注、标题层级、摘要关键词、格式检查的写作思路 |
| 去 AI 味 | 保留法学正式语体，去掉虚高表达、模糊归因和模板化结构 |
| 模拟审稿 | 从选题价值、创新性、论证深度、文献覆盖、案例运用等维度审视 |

## 法学写作的反幻觉规则

法学论文中，AI 最危险的错误不是「写得不够好」，而是「看起来很专业但事实是假的」。本项目把下面规则放在最高优先级：

- 不编造法条内容。引用前必须核实法律名称、条号、条文原文和现行有效状态。
- 不编造案例。案例名称、案号、法院、裁判日期、裁判要旨都应可追溯。
- 不编造学术观点。不能写「学界普遍认为」却没有具体作者和文献。
- 不夸大政策意义。避免「里程碑」「重大突破」「根本性变革」这类没有论证的表述。
- 不把 AI 输出直接当最终稿。所有引用、格式、期刊要求都要以最新官方来源为准。

## 典型工作流

```text
选题判断
  -> 文献检索关键词
  -> 法条和案例材料清单
  -> 论文框架
  -> 引言和摘要
  -> 正文分章写作
  -> 引用与脚注核查
  -> 去 AI 味和语言润色
  -> 模拟审稿
  -> 投稿/答辩前检查
```

每一步都可以只用 Prompt，也可以安装 Skill 后让 AI 按完整工作流陪你推进。

## 完整示例

| 示例 | 适合谁 | 看完能学到什么 |
|:---|:---|:---|
| [个人信息保护法自动化决策论文工作流](examples/pipl-article-workflow.md) | 不知道如何从题目开始的人 | 从研究想法到论文框架的完整路径 |
| [CSSCI 模拟审稿示例](examples/cssci-review-demo.md) | 准备投稿或修改引言的人 | 审稿人会如何挑问题、如何改 |
| [法条、案例、文献核查示例](examples/citation-check-demo.md) | 担心 AI 编造引用的人 | 如何列出核查项和风险等级 |

## 项目结构

```text
law-paper-writing/
├── README.md                 # 新手入口，先看这里
├── SKILL.md                  # 可安装 Skill 的主规则
├── prompts/                  # 可直接复制的 Prompt 模板
├── examples/                 # 完整使用示例
├── references/               # 深度指南、清单、期刊和格式资料
├── tests/                    # 引用转换脚本测试
├── ROADMAP.md                # 后续计划
├── CONTRIBUTING.md           # 贡献指南
├── CHANGELOG.md              # 版本记录
└── LICENSE                   # MIT 开源许可
```

### 推荐阅读顺序

1. 第一次使用：先看本 README。
2. 想马上用：打开 [prompts/README.md](prompts/README.md)。
3. 想看完整过程：打开 [examples/](examples/)。
4. 想深入学习：按问题查 [references/](references/)。
5. 想安装到 AI 助手：看上面的「安装为 Skill」。

## 参考资料速查

| 问题 | 看哪里 |
|:---|:---|
| 如何选题、写综述、组织论证 | [references/writing-guide.md](references/writing-guide.md) |
| 如何引用法条、案例、文献 | [references/citation-workflow.md](references/citation-workflow.md) |
| 如何做法律材料核查 | [references/verification-guide.md](references/verification-guide.md) |
| 如何识别和修改 AI 痕迹 | [references/de-ai-patterns.md](references/de-ai-patterns.md) |
| 如何选择投稿期刊 | [references/journal-selector.md](references/journal-selector.md) |
| 投稿/答辩前检查什么 | [references/checklists.md](references/checklists.md) |
| 如何处理 Word 文档格式 | [references/docx-workflow.md](references/docx-workflow.md) |
| 民法、刑法、行政法等分支怎么写 | [references/subdomain-templates.md](references/subdomain-templates.md) |
| 英文法学论文怎么写 | [references/english-writing-guide.md](references/english-writing-guide.md) |

## 与 awesome-ai-research-writing 的关系

本项目受到 [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) 启发，继承了它的三个优点：

- Prompt 可以直接复制使用。
- Skill 可以处理更长流程。
- 场景比抽象理论更重要。

但法学版本做了实质重构：

| 维度 | 通用/ML 论文写作 | 法学论文写作工具箱 |
|:---|:---|:---|
| 事实核查重点 | 论文引用、实验结论 | 法条、案例、裁判要旨、学术观点 |
| 交付格式 | LaTeX、图表、实验结果 | Word、脚注、法条结构、案例表 |
| 投稿目标 | NeurIPS/ICML/ACL 等 | CSSCI、SSCI、学位论文 |
| 论证方式 | 实验验证、消融实验 | 规范分析、法教义学、案例分析、比较法 |
| AI 痕迹 | 技术写作套话 | 模糊归因、政策意义虚高、过度平衡、案例堆砌 |

## 信息更新与核验声明

本项目中的期刊、格式、影响因子、投稿方式、审稿周期等信息只作为写作准备参考。它们可能随期刊官网、学校规定、数据库版本和 JCR/CSSCI 目录更新而变化。

投稿、答辩或正式引用前，请务必核对：

- 目标期刊官网最新投稿须知。
- 学校研究生院最新学位论文格式文件。
- 国家法律法规数据库、最高人民法院官网、裁判文书数据库等权威来源。
- CNKI、万方、HeinOnline、Westlaw、LexisNexis、Google Scholar 等数据库中的文献原文。

## 贡献

欢迎贡献：

- 新的法学二级学科 Prompt。
- 真实但已脱敏的使用示例。
- 期刊格式和投稿要求更新。
- 引用转换脚本测试样例。
- 法条、案例、文献核查流程优化。

贡献前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。所有高变动信息必须标注来源和核验日期。

## 许可

本项目使用 [MIT License](LICENSE)。你可以自由使用、修改、分发，但请保留许可声明，并自行承担对法律资料进行最终核查的责任。
