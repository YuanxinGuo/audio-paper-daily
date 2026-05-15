---
title: "PresentAgent-2: Towards Generalist Multimodal Presentation Agents"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#交互式", "#多模态", "#智能体", "#演示生成", "#演示视频生成"]
summary: "PresentAgent-2是一个多模态智能体框架，能从用户查询出发，经研究收集多模态资源，生成含单人/多人对话及交互问答的演示视频。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#演示生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态</span> <span class="tag-pill tag-pill-soft">#智能体</span> <span class="tag-pill tag-pill-soft">#演示视频生成</span> <span class="tag-pill tag-pill-soft">#交互式</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.11363</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-12</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.11363" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.11363" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/AIGeeksGroup/PresentAgent-2" target="_blank" rel="noopener">💻 代码</a><a class="rsrc rsrc-proj" href="https://aigeeksgroup.github.io/PresentAgent-2" target="_blank" rel="noopener">🌐 项目主页</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>PresentAgent-2是一个多模态智能体框架，能从用户查询出发，经研究收集多模态资源，生成含单人/多人对话及交互问答的演示视频。
</div>

## 👥 作者与机构

**Wei Wu** ¹ · Ziyang Xu · Zeyu Zhang · Yang Zhao · Hao Tang

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合对多模态内容生成、智能体系统或演示自动化感兴趣的研究者。建议重点阅读§3系统架构和§4实验部分，了解三种模式的设计与评估。可先看表1和表2了解性能对比。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| **应用场景** | 从用户查询自动生成包含研究支撑、多模态媒体和交互能力的演示视频。 |
| **核心创新** | 统一框架支持单人、多人讨论和交互问答三种演示模式 · 基于查询的深度研究自动收集文本、图像、GIF和视频资源 · 构建多模态演示基准，含内容质量、媒体相关性等评估标准 |
| **模型架构** | 输入：用户查询和演示模式 → 查询摘要与深度研究模块（收集多模态资源）→ 幻灯片构建与脚本生成 → 媒体合成模块（整合幻灯片、音频、动态媒体）→ 输出：完整演示视频。支持三种模式：单人、多人讨论（带角色分工）、交互问答（基于幻灯片和上下文）。 |
| **数据集** | 自建多模态演示基准（评估） |
| **关键结果** | 摘要未给出具体指标数值，仅描述了评估标准（内容质量、媒体相关性、动态媒体使用、对话自然度、交互接地）。 |

## 🔗 开源资源

- **代码**：<https://github.com/AIGeeksGroup/PresentAgent-2>
- **项目主页**：<https://aigeeksgroup.github.io/PresentAgent-2>

## 🎯 与本站重点领域的关联

与本站五个重点领域无直接关联。但其中的多模态资源收集与合成技术（如音频与幻灯片对齐）可迁移至语音增强或双耳音频中的视听融合任务。

## ⚠️ 局限与未解决问题

摘要未提供定量结果，缺乏与基线方法的对比；自建基准可能引入偏差；未报告推理延迟或计算开销；交互模式中问答的准确性未深入评估。

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

<div class="paper-footer"><span>评分：7.5</span><span>原始：7.5</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
