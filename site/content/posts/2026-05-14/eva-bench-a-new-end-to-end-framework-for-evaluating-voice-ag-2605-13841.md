---
title: "EVA-Bench: A New End-to-end Framework for Evaluating Voice Agents"
date: 2026-05-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#对话系统", "#评估框架", "#语音代理", "#语音代理评估", "#鲁棒性"]
summary: "提出EVA-Bench，一个端到端评估框架，通过模拟对话和复合指标全面衡量语音代理的准确性与体验质量。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音代理评估</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音代理</span> <span class="tag-pill tag-pill-soft">#评估框架</span> <span class="tag-pill tag-pill-soft">#对话系统</span> <span class="tag-pill tag-pill-soft">#鲁棒性</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.13841</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-14</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.13841" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.13841" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出EVA-Bench，一个端到端评估框架，通过模拟对话和复合指标全面衡量语音代理的准确性与体验质量。
</div>

## 👥 作者与机构

**Tara Bogavelli** ¹ · Gabrielle Gauthier Melan\c{c}on · Katrina Stankiewicz · Oluwanifemi Bamgbose · Fanny Riols · Hoang H. Nguyen · Raghav Mehndiratta · Lindsay Devon Brin · … 等 5 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音代理、对话系统及评估方法研究者。建议通读，重点看§3（指标设计）与§5（实验结果），特别是表1和表2。可复现其开源框架进行自定义评估。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| **应用场景** | 评估企业级语音代理在动态多轮对话中的任务完成与用户体验。 |
| **核心创新** | 端到端模拟验证自动重生成对话 · 双复合指标EVA-A与EVA-X覆盖准确性与体验 · 扰动套件测试口音和噪声鲁棒性 |
| **模型架构** | 框架包含用户模拟器与代理模拟器进行bot-to-bot对话，经自动验证后，由评估模块计算EVA-A（任务完成、忠实度、语音保真度）和EVA-X（对话进展、简洁性、轮次时序）指标。 |
| **数据集** | 213个企业场景（评估） · 扰动套件（鲁棒性测试） |
| **关键结果** | 12个系统评估显示：无系统在EVA-A pass@1和EVA-X pass@1上同时超过0.5；峰值与可靠性能差距中位数0.44；口音和噪声扰动导致平均降幅达0.314。 |

## 🎯 与本站重点领域的关联

与本站重点领域无直接关联。但语音增强和噪声鲁棒性评估方法可迁移至语音代理的音频质量测量，双耳音频的空间鲁棒性测试思路也可借鉴。

## ⚠️ 局限与未解决问题

未报告计算开销或推理延迟；场景仅限企业领域，泛化性未知；复合指标权重未消融；用户模拟器真实性未与人类对比。

## 📋 引用

```bibtex
@article{bogavelli20262605,
  title  = {EVA-Bench: A New End-to-end Framework for Evaluating Voice Agents},
  author = {Tara Bogavelli and  Gabrielle Gauthier Melan\c{c}on and  Katrina Stankiewicz and  Oluwanifemi Bamgbose and  Fanny Riols and  Hoang H. Nguyen and  Raghav Mehndiratta and  Lindsay Devon Brin and  Joseph Marinier and  Hari Subramani and  Anil Madamala and  Sridhar Krishna Nemala and  Srinivas Sunkara},
  journal = {arXiv preprint arXiv:2605.13841},
  year   = {2026}
}
```

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/posts/2026-05-14/">← 返回 2026-05-14 速递</a></div>
