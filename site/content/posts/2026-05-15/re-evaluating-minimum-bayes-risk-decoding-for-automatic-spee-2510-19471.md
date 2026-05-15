---
title: "Re-evaluating Minimum Bayes Risk Decoding for Automatic Speech Recognition"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#Whisper", "#最小贝叶斯风险解码", "#束搜索", "#语音翻译", "#语音识别"]
summary: "系统评估最小贝叶斯风险解码在ASR和语音翻译任务上的表现，发现其多数情况下优于束搜索。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#最小贝叶斯风险解码</span> <span class="tag-pill tag-pill-soft">#束搜索</span> <span class="tag-pill tag-pill-soft">#Whisper</span> <span class="tag-pill tag-pill-soft">#语音翻译</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2510.19471</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2510.19471" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2510.19471" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/CyberAgentAILab/mbr-for-asr" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>系统评估最小贝叶斯风险解码在ASR和语音翻译任务上的表现，发现其多数情况下优于束搜索。
</div>

## 👥 作者与机构

**Yuu Jinnai** ¹

**机构**：CyberAgent

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合ASR和ST研究者，尤其是对解码策略感兴趣者。建议通读，重点看§3实验设置与§4结果分析，可复现其代码。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| **应用场景** | 离线ASR和语音翻译任务，追求高准确率。 |
| **核心创新** | 首次系统评估MBR解码在ASR/ST任务上的有效性 · 在Whisper及其衍生模型上验证 · 开源代码便于复现 |
| **模型架构** | 输入为语音特征，使用Whisper或衍生模型作为编码器-解码器主干，解码时采用样本MBR解码：从模型采样多个候选，用风险函数（如词错误率）选择最优输出。无额外参数。 |
| **数据集** | LibriSpeech（英语ASR评估） · Common Voice（英语ASR评估） · JSUT（日语ASR评估） · CoVoST2（英语-日语语音翻译评估） |
| **关键结果** | 在LibriSpeech test-clean上，MBR解码相比束搜索词错误率降低约5%（相对）；在日语ASR任务上，字符错误率降低约3%；在语音翻译任务上，BLEU提升约1点。所有结果均基于Whisper large-v3。 |

## 🔗 开源资源

- **代码**：<https://github.com/CyberAgentAILab/mbr-for-asr>

## 🎯 与本站重点领域的关联

与本站重点领域中的语音增强、目标说话人提取、语音分离等无直接关联，但MBR解码作为通用解码策略，可迁移至这些任务的序列生成环节，例如在语音增强中优化感知指标。

## ⚠️ 局限与未解决问题

仅评估离线场景，未考虑实时性；实验仅使用Whisper系列模型，泛化性待验证；未提供推理延迟对比，MBR解码计算成本高于束搜索。

## 📋 引用

```bibtex
@article{jinnai20262510,
  title  = {Re-evaluating Minimum Bayes Risk Decoding for Automatic Speech Recognition},
  author = {Yuu Jinnai},
  journal = {arXiv preprint arXiv:2510.19471},
  year   = {2026}
}
```

---

<div class="paper-footer"><span>评分：7.5</span><span>原始：7.5</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
