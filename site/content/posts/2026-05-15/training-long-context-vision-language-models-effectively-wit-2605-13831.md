---
title: "Training Long-Context Vision-Language Models Effectively with Generalization Beyond 128K Context"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#持续预训练", "#数据混合", "#视觉语言模型", "#长上下文", "#长上下文视觉语言模型"]
summary: "系统研究长上下文视觉语言模型的持续预训练策略，发现长文档VQA优于OCR转录，平衡数据分布优于聚焦长序列，检索是主要瓶颈，并提出MMProLong模型在128K训练窗口外泛化至512K。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#长上下文视觉语言模型</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#长上下文</span> <span class="tag-pill tag-pill-soft">#视觉语言模型</span> <span class="tag-pill tag-pill-soft">#持续预训练</span> <span class="tag-pill tag-pill-soft">#数据混合</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.13831</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-13</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.13831" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.13831" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>系统研究长上下文视觉语言模型的持续预训练策略，发现长文档VQA优于OCR转录，平衡数据分布优于聚焦长序列，检索是主要瓶颈，并提出MMProLong模型在128K训练窗口外泛化至512K。
</div>

## 👥 作者与机构

**Zhaowei Wang** ¹ · Lishu Luo · Haodong Duan · Weiwei Liu · Sijin Wu · Ji Luo · Shen Yan · Shuai Peng · … 等 4 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事多模态大模型长上下文训练的研究者。建议重点阅读§3的消融实验和§4的泛化结果，尤其是数据混合策略和检索瓶颈分析。可先看表1和表2了解关键发现。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| **应用场景** | 长文档理解、视频分析、多轮工具使用等需要长上下文建模的视觉语言任务。 |
| **核心创新** | 发现长文档VQA比OCR转录更有效 · 平衡序列长度分布优于聚焦长序列 · 检索是长上下文能力的主要瓶颈 |
| **模型架构** | 基于Qwen2.5-VL-7B，通过长上下文持续预训练从32K扩展到128K。输入为图像和文本，主干为视觉编码器+语言模型，关键模块包括长文档VQA数据生成和混合策略，输出为文本响应。参数量7B。 |
| **数据集** | 长文档VQA数据（训练） · OCR转录数据（消融对比） · 短上下文VQA数据（评估短能力） |
| **关键结果** | MMProLong在长文档VQA上提升7.1%，在256K和512K上下文上保持强性能，无需额外训练。在网页多模态检索、长上下文视觉文本压缩和长视频理解上展现泛化能力。 |

## 🎯 与本站重点领域的关联

与本站重点领域无直接关联。但长上下文建模技术可迁移至语音/音频领域的长序列处理，如长语音识别、长音频事件检测等，其数据混合策略和检索瓶颈分析对设计长音频模型有参考价值。

## ⚠️ 局限与未解决问题

实验仅基于7B模型，未验证更大规模模型；长上下文泛化至512K但未测试更长；缺乏与同类方法的直接对比（如LongVA等）；未报告推理延迟和显存占用。

## 📋 引用

```bibtex
@article{wang20262605,
  title  = {Training Long-Context Vision-Language Models Effectively with Generalization Beyond 128K Context},
  author = {Zhaowei Wang and  Lishu Luo and  Haodong Duan and  Weiwei Liu and  Sijin Wu and  Ji Luo and  Shen Yan and  Shuai Peng and  Sihang Yuan and  Chaoyi Huang and  Yi Lin and  Yangqiu Song},
  journal = {arXiv preprint arXiv:2605.13831},
  year   = {2026}
}
```

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
