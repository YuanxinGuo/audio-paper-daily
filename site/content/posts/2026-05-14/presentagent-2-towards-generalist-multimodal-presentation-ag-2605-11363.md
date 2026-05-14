---
title: "PresentAgent-2: Towards Generalist Multimodal Presentation Agents"
date: 2026-05-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#交互式演示", "#多模态", "#多模态演示生成", "#智能体框架", "#演示视频生成"]
summary: "PresentAgent-2 是一个智能体框架，能从用户查询出发，自动进行深度研究、收集多模态资源，并生成包含语音、动态媒体的演示视频，支持单人讲解、多人讨论和交互问答三种模式。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#多模态演示生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#演示视频生成</span> <span class="tag-pill tag-pill-soft">#智能体框架</span> <span class="tag-pill tag-pill-soft">#多模态</span> <span class="tag-pill tag-pill-soft">#交互式演示</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.11363</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-12</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.11363" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.11363" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/AIGeeksGroup/PresentAgent-2" target="_blank" rel="noopener">💻 代码</a><a class="rsrc rsrc-proj" href="https://aigeeksgroup.github.io/PresentAgent-2" target="_blank" rel="noopener">🌐 项目主页</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>PresentAgent-2 是一个智能体框架，能从用户查询出发，自动进行深度研究、收集多模态资源，并生成包含语音、动态媒体的演示视频，支持单人讲解、多人讨论和交互问答三种模式。
</div>

## 👥 作者与机构

**Wei Wu** ¹ · Ziyang Xu · Zeyu Zhang · Yang Zhao · Hao Tang

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合对多模态内容生成、智能体系统或演示自动化感兴趣的研究者。建议重点阅读 §3 框架设计（尤其是三种模式的统一架构）和 §4 基准构建与评估指标。可先看 §3.2 多模态资源收集与 §3.3 幻灯片构建模块。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| **应用场景** | 从用户查询自动生成包含研究内容、多模态媒体和交互能力的演示视频。 |
| **核心创新** | 提出统一框架支持单人、多人讨论和交互三种演示模式 · 端到端从查询到演示视频的智能体流程，集成深度研究与多模态资源收集 · 构建多模态演示基准，包含针对不同模式的评估标准 |
| **模型架构** | 输入：用户查询和演示模式 → 研究模块（查询总结、深度搜索、多模态资源收集）→ 幻灯片构建模块 → 脚本生成模块（模式特定）→ 视频合成模块（组合幻灯片、音频、动态媒体）→ 输出：演示视频。支持三种模式：Single（单说话人）、Discussion（多说话人角色）、Interaction（问答交互）。未提及参数量。 |
| **数据集** | 多模态演示基准（评估，包含单演示、讨论、交互场景） |
| **关键结果** | 摘要未给出具体指标数字或对比基线，仅说明构建了基准和评估标准。 |

## 🔗 开源资源

- **代码**：<https://github.com/AIGeeksGroup/PresentAgent-2>
- **项目主页**：<https://aigeeksgroup.github.io/PresentAgent-2>

## 🎯 与本站重点领域的关联

与本站五个重点领域无直接关联。但其中的语音合成（TTS）和对话管理技术可迁移至语音增强/分离中的多说话人场景，例如讨论模式中的多说话人角色分配可启发目标说话人提取中的说话人建模。

## ⚠️ 局限与未解决问题

摘要未报告定量结果或与现有系统的对比，缺乏消融实验和推理延迟分析。依赖外部研究工具和媒体资源，可能引入噪声或版权问题。交互模式仅支持基于已生成内容的问答，未实现实时多轮对话。

## 📋 引用

```bibtex
@article{wu20262605,
  title  = {PresentAgent-2: Towards Generalist Multimodal Presentation Agents},
  author = {Wei Wu and  Ziyang Xu and  Zeyu Zhang and  Yang Zhao and  Hao Tang},
  journal = {arXiv preprint arXiv:2605.11363},
  year   = {2026}
}
```

---

<div class="paper-footer"><span>评分：7.5</span><span>原始：7.5</span><a href="/posts/2026-05-14/">← 返回 2026-05-14 速递</a></div>
