<p align="center">
  <h1 align="center">Law Paper Writing</h1>
  <p align="center">
    <strong>AI 法学论文写作 Skill</strong>
  </p>
  <p align="center">
    <a href="#功能全景">功能</a> ·
    <a href="#快速开始">安装</a> ·
    <a href="#使用方式">使用</a> ·
    <a href="#项目结构">结构</a> ·
    <a href="#灵感来源">致谢</a>
  </p>
  <p align="center">
    <img src="https://img.shields.io/badge/Version-1.1.0-blue" alt="version" />
    <img src="https://img.shields.io/badge/License-MIT-green" alt="license" />
    <img src="https://img.shields.io/badge/Language-CN-%23E34F26" alt="language" />
    <img src="https://img.shields.io/badge/Coverage-CSSCI%20%7C%20SSCI%20%7C%20Degree_Thesis-9B59B6" alt="coverage" />
  </p>
</p>

---

## 这是什么？

一个为**法学研究生**（硕士/博士）设计的 AI 学术写作辅助技能。基于 [awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) 的 ML 论文写作技能体系，**全面适配法学研究的独特需求**重构而成。

**一句话说明**：从选题到投稿，从中文 CSSCI 到英文 SSCI，从法条核实到去 AI 痕迹——一个 Skill 覆盖法学论文写作全流程。

> **为什么从 ML 领域改编？** ML 论文写作的核心方法论（反幻觉、结构化写作、去 AI 味）完全适用于法学，但法学在引用规范、论证范式、交付格式（Word 为主）等方面有本质差异。本 Skill 不是简单翻译，而是针对法学研究的特性重新设计。

---

## 功能全景

### 写作全流程

```
选题 → 案例检索 → 文献综述 → 论证结构 → 引言 → 正文 → 结论 → 引用规范 → 润色 → 去 AI 味
```

每个步骤都有详细的方法论指引和检查清单，不是空泛的建议，而是**可操作的执行框架**。

### 12 大核心能力

| 能力 | 说明 | 适用场景 |
|:-----|:-----|:---------|
| **论文写作全流程** | 10 步工作流，每步有方法论 | 从零开始写论文 |
| **引用规范** | 法条/案例/文献/英文全覆盖（GB/T 7714 + Bluebook） | 规范引注格式 |
| **引用格式转换** | Python 脚本批量转换 GB/T 7714 ↔ Bluebook | 切换引注格式 |
| **期刊投稿速查** | CSSCI 10 大核心期刊 + SSCI 期刊 | 查格式要求 |
| **期刊选择决策** | 15+ 期刊对比矩阵 + 选刊策略 | 选择投稿目标 |
| **学位论文格式** | 通用框架 + 答辩前检查清单 | 准备学位论文 |
| **Word 文档生成** | CSSCI 期刊 Word 格式规范 + python-docx 模板 | 生成投稿文档 |
| **审稿人模拟** | 8 维度评估 + 结构化审稿意见 | 投稿前自检 |
| **法律核查工具** | 法条/案例/文献的可执行核实流程 | 防止引用幻觉 |
| **法学分支模板** | 民法/刑法/行政法/国际法/经济法/法理学 | 特定分支写作 |
| **英文写作支持** | IRAC/CREAC、SSCI 指南、英文去 AI 味 | 投 SSCI 期刊 |
| **去 AI 味** | 26 种法学专属 AI 痕迹 + 4 步改写流程 | 消除 AI 写作痕迹 |

### 反幻觉机制

法学论文的 AI 辅助有一个独特风险：**AI 可能编造法条、案例或法律命题**。本 Skill 从机制层面解决：

- **绝对禁止**编造法条内容、虚构案例裁判要旨、捏造学术观点
- 提供可执行的核实流程（WebFetch 模板 + 核查脚本）
- 模糊归因拦截：「学界普遍认为」→ 必须归因到具体学者 + 文献

---

## 快速开始

### WorkBuddy / CodeBuddy Code

```bash
# 克隆到 Skill 目录
git clone https://github.com/zhangligong0826/law-paper-writing.git ~/.workbuddy/skills/law-paper-writing
```

### Cursor

```bash
npx openskills install zhangligong0826/law-paper-writing
```

### 手动安装

下载全部文件，放置到你的 AI 助手的 Skill 目录中即可。

> **系统要求**：WorkBuddy 0.10+ / Cursor 最新版。Python 3.8+（仅引用转换脚本需要）。

---

## 使用方式

### 触发词

在对话中使用以下关键词即可激活本 Skill：

| 类别 | 触发词 |
|:-----|:-------|
| **写作** | 法学论文写作、法律写作、学位论文、dissertation |
| **投稿** | CSSCI投稿、SSCI投稿 |
| **辅助** | 论文润色、去AI味、法律文献综述、案例引用 |
| **分支** | 民法论文、刑法论文、行政法论文 |
| **英文** | legal writing、law paper |
| **审查** | 帮我审一下、模拟审稿、审稿意见 |

### 典型工作流示例

```
你：帮我审一下这篇刑法学论文的引言部分，看看能不能投法学研究。
AI：（进入审稿人模式，8 维度评估，输出结构化审稿意见）

你：把参考文献从 GB/T 7714 转成 Bluebook 格式。
AI：（调用 citation-converter.py 批量转换）

你：这篇论文去一下 AI 味。
AI：（执行 4 步去 AI 味流程：识别→草稿改写→审计→最终改写）

你：我想写一篇关于个人信息保护法第 XX 条的解释论文章，帮我选期刊。
AI：（调用 journal-selector.md，按主题匹配推荐 2-3 个目标期刊）
```

### 不做什么

| 不做 | 原因 |
|:-----|:-----|
| 法律咨询 | 建议咨询执业律师 |
| 实务文书起草 | 诉状、合同、律师函不是学术论文 |
| 司法考试辅导 | 考试辅导有专门的备考资料 |
| 法律翻译 | 不替代专业法律翻译 |

---

## 项目结构

```
law-paper-writing/
│
├── SKILL.md                              # Skill 定义主文件（11 个章节）
├── README.md                             # 你正在看的文件
│
└── references/                           # 参考文档库
    │
    │  ── 核心写作 ──────────────────────
    ├── writing-guide.md                  # 法学论文写作深度指南
    │                                     # 选题方法、论证结构、文献综述、案例分析、表达规范
    │
    │  ── 引用规范 ──────────────────────
    ├── citation-workflow.md              # 引用规范详解
    │                                     # 法条引用、案例引用、学术文献引用（GB/T 7714 + Bluebook）
    ├── citation-converter.py             # 引用格式转换脚本（可运行）
    │                                     # python citation-converter.py --input refs.txt --from gbt7714 --to bluebook
    │
    │  ── 去 AI 味 ──────────────────────
    ├── de-ai-patterns.md                 # 法学 AI 写作痕迹完整清单
    │                                     # 26 种模式（5 类）、25 个高频 AI 词汇、改写技术
    │
    │  ── 期刊投稿 ──────────────────────
    ├── journal-selector.md               # 期刊对比决策矩阵
    │                                     # 15+ 期刊对比、选刊流程、投稿策略、SSCI 速查
    ├── checklists.md                     # 投稿/答辩检查清单
    │                                     # CSSCI 投稿清单、SSCI 投稿清单、学位论文答辩清单
    │
    │  ── 文档生成 ──────────────────────
    ├── docx-workflow.md                  # Word 文档工作流
    │                                     # CSSCI 期刊 Word 格式规范、python-docx 完整模板、排版检查
    │
    │  ── 法学分支 ──────────────────────
    ├── subdomain-templates.md            # 6 大法学分支专项模板
    │                                     # 民法/刑法/行政法/国际法/经济法/法理学
    │                                     # 每分支含：论证范式、经典文献、选题热点、写作注意事项
    │
    │  ── 核查工具 ──────────────────────
    ├── verification-guide.md             # 法律核查工具集成指引
    │                                     # 法条/案例/文献核实流程、WebFetch 核实模板
    │
    │  ── 英文写作 ──────────────────────
    └── english-writing-guide.md          # 英文法学论文写作指南
                                          # SSCI 投稿、IRAC/CREAC、Common Law vs Civil Law、英文去 AI 味
```

### 各参考文档速查

| 想做什么 | 看哪个文档 |
|:---------|:-----------|
| 不知如何选题 | `writing-guide.md` → 选题方法 |
| 论文论证缺乏层次 | `writing-guide.md` → 论证结构 |
| 不知道引注格式怎么写 | `citation-workflow.md` |
| 投 SSCI 需要转引注格式 | `citation-converter.py` |
| 担心论文有 AI 味道 | `de-ai-patterns.md` |
| 不知道投哪个期刊 | `journal-selector.md` |
| 投稿前的格式检查 | `checklists.md` |
| 需要生成 Word 格式投稿稿 | `docx-workflow.md` |
| 写民法/刑法/行政法论文 | `subdomain-templates.md` |
| 不确定某个法条/案例是否真实 | `verification-guide.md` |
| 要写英文法学论文 | `english-writing-guide.md` |

---

## 与 ML 领域 Skills 的对比

本 Skill 的设计源自 ML 领域的论文写作技能体系，但针对法学研究的特殊性做了全面重构：

| 维度 | ML 论文写作 | 法学论文写作（本 Skill） |
|:-----|:------------|:------------------------|
| **核心输出格式** | LaTeX | Word（.docx）为主 |
| **引用系统** | BibTeX / Semantic Scholar | GB/T 7714 / Bluebook / 北大法宝 |
| **投稿目标** | NeurIPS/ICML/ICLR/ACL | CSSCI 期刊 / SSCI 期刊 / 学位论文 |
| **图表** | 架构图、实验图表 | 案例对比表、法条结构图、比较法矩阵 |
| **反幻觉重点** | 论文引用是否真实 | 法条/案例/法律命题是否真实 |
| **AI 痕迹** | 技术写作 AI 词汇 | 法学写作 AI 词汇（公式化平衡、案例膨胀等） |
| **论证范式** | 实验验证、消融实验 | 法教义学分析、案例比较、规范分析 |
| **语言** | 以英文为主 | 以中文为主（含英文模块） |

---

## 灵感来源

基于 [awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing)（25.9k stars）仓库中的三个 ML 领域 Skills 改编：

| 原始 Skill | 作者 | 本 Skill 中的对应 |
|:-----------|:-----|:------------------|
| [20-ml-paper-writing](https://github.com/zechenzhangAGI/AI-research-SKILLs) | zechenzhangAGI | 论文写作全流程、反幻觉、引用规范 |
| [academic-plotting](https://github.com/zechenzhangAGI/AI-research-SKILLs) | zechenzhangAGI | （适配为法学分支模板和 Word 工作流） |
| [humanizer](https://github.com/blader/humanizer) | blader | 去 AI 味（全面重构为法学领域版本） |

---

## 许可

[MIT License](LICENSE) — 自由使用、修改、分发。
