# AI 法学论文写作 Skill (Law Paper Writing)

为法学研究生（硕士/博士）设计的 AI 辅助学术写作技能，适配 CSSCI/SSCI 期刊投稿与学位论文写作。

## 功能

- **论文写作全流程**：10 步工作流（选题→案例检索→文献综述→论证→引言→正文→结论→引用规范→润色→去AI味）
- **引用规范**：法律条文/案例/学术文献/英文文献（GB/T 7714 + Bluebook）
- **期刊投稿速查**：CSSCI 核心期刊 + SSCI 期刊格式要求
- **学位论文格式**：通用框架 + 答辩前检查清单
- **去 AI 味**：26 种法学专属 AI 痕迹模式，4 步改写流程
- **反幻觉**：绝不编造法条/案例/法律命题

## 灵感来源

基于 [awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) 仓库中的三个 ML 领域 Skills 改编：

- [20-ml-paper-writing](https://github.com/zechenzhangAGI/AI-research-SKILLs) — ML 论文全流程写作
- [academic-plotting](https://github.com/zechenzhangAGI/AI-research-SKILLs) — 学术配图
- [humanizer](https://github.com/blader/humanizer) — 去 AI 写作痕迹

## 文件结构

```
law-paper-writing/
├── SKILL.md                  # 主文件（Skill 定义，10 个章节）
└── references/
    ├── de-ai-patterns.md      # 法学 AI 写作痕迹完整清单
    ├── citation-workflow.md  # 引用规范详解
    ├── writing-guide.md      # 法学论文写作深度指南
    └── checklists.md         # 投稿/答辩检查清单
```

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

- 法学论文写作、CSSCI投稿、学位论文、法律文献综述、案例引用
- 论文润色、去AI味、法学写作

## 许可

MIT License
