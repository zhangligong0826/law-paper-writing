# AI 法学论文写作 Skill (Law Paper Writing)

为法学研究生（硕士/博士）设计的 AI 辅助学术写作技能，适配 CSSCI/SSCI 期刊投稿与学位论文写作。

## 功能

- **论文写作全流程**：10 步工作流（选题→案例检索→文献综述→论证→引言→正文→结论→引用规范→润色→去AI味）
- **引用规范**：法律条文/案例/学术文献/英文文献（GB/T 7714 + Bluebook）
- **引用格式转换**：Python 脚本批量转换 GB/T 7714 ↔ Bluebook
- **期刊投稿速查**：CSSCI 核心期刊 + SSCI 期刊格式要求
- **期刊选择决策**：选刊流程、各刊选题偏好、投稿策略
- **学位论文格式**：通用框架 + 答辩前检查清单
- **Word 文档生成**：CSSCI 期刊 Word 格式规范 + python-docx 模板
- **审稿人模拟**：模拟 CSSCI 匿名审稿人给出结构化反馈
- **法律核查工具**：法条/案例/文献的可执行核实流程
- **法学分支模板**：民法/刑法/行政法/国际法/经济法/法理学 6 大分支专项指导
- **英文写作支持**：IRAC/CREAC 方法、SSCI 投稿指南、英文去 AI 味
- **去 AI 味**：26 种法学专属 AI 痕迹模式，4 步改写流程
- **反幻觉**：绝不编造法条/案例/法律命题

## 文件结构

```
law-paper-writing/
├── SKILL.md                           # 主文件（Skill 定义，11 个章节）
├── README.md                          # 项目说明
└── references/
    ├── de-ai-patterns.md               # 法学 AI 写作痕迹完整清单（26 种模式）
    ├── citation-workflow.md           # 引用规范详解（GB/T 7714 + Bluebook）
    ├── writing-guide.md               # 法学论文写作深度指南
    ├── checklists.md                  # 投稿/答辩检查清单
    ├── docx-workflow.md              # Word 文档工作流 + python-docx 模板
    ├── subdomain-templates.md        # 法学 6 大分支领域专项模板
    ├── verification-guide.md         # 法律核查工具集成指引
    ├── citation-converter.py         # 引用格式转换脚本（GB/T 7714 ↔ Bluebook）
    ├── english-writing-guide.md      # 英文法学论文写作指南（SSCI 投稿）
    └── journal-selector.md           # 期刊对比决策矩阵
```

## 灵感来源

基于 [awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) 仓库中的三个 ML 领域 Skills 改编：

- [20-ml-paper-writing](https://github.com/zechenzhangAGI/AI-research-SKILLs) — ML 论文全流程写作
- [academic-plotting](https://github.com/zechenzhangAGI/AI-research-SKILLs) — 学术配图
- [humanizer](https://github.com/blader/humanizer) — 去 AI 写作痕迹

## 安装

### WorkBuddy / CodeBuddy Code

将本仓库克隆到 `~/.workbuddy/skills/law-paper-writing/` 即可：

```bash
git clone https://github.com/zhangligong0826/law-paper-writing.git ~/.workbuddy/skills/law-paper-writing
```

### Cursor

```bash
npx openskills install zhangligong0826/law-paper-writing
```

## 使用

在对话中使用以下触发词激活：

- 法学论文写作、法律写作、CSSCI投稿、SSCI投稿、学位论文、法律文献综述、案例引用
- 论文润色、去AI味、法学写作、legal writing、law paper、dissertation
- 民法论文、刑法论文、行政法论文

## 许可

MIT License
