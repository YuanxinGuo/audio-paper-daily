---
title: "Re-evaluating Minimum Bayes Risk Decoding for Automatic Speech Recognition"
date: 2026-05-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#Whisper", "#最小贝叶斯风险解码", "#波束搜索", "#语音翻译", "#语音识别"]
summary: "系统评估最小贝叶斯风险解码在ASR和语音翻译任务中的表现，发现其多数情况下优于波束搜索。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#最小贝叶斯风险解码</span> <span class="tag-pill tag-pill-soft">#波束搜索</span> <span class="tag-pill tag-pill-soft">#Whisper</span> <span class="tag-pill tag-pill-soft">#语音翻译</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2510.19471</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-14</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2510.19471" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2510.19471" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/CyberAgentAILab/mbr-for-asr" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>系统评估最小贝叶斯风险解码在ASR和语音翻译任务中的表现，发现其多数情况下优于波束搜索。
</div>

## 👥 作者与机构

**Yuu Jinnai** ¹

**机构**：CyberAgent

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合ASR和ST研究者，尤其是关注解码策略的读者。建议通读，重点看§3实验设置与§4结果分析，可复现其代码。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| **应用场景** | 离线语音识别和语音翻译任务中替代波束搜索的解码方法。 |
| **核心创新** | 首次系统评估MBR在ASR/ST任务中的有效性 · 在Whisper系列模型上验证MBR优于波束搜索 · 开源代码便于复现 |
| **模型架构** | 输入语音 → Whisper编码器-解码器 → 采样生成候选序列 → MBR解码（基于风险最小化选择输出）。未提及参数量。 |
| **数据集** | LibriSpeech（ASR评估） · Common Voice（ASR评估） · CoVoST 2（ST评估） · JSUT（日语ASR评估） |
| **关键结果** | 在LibriSpeech test-clean上，MBR相比波束搜索WER相对降低约10%；在CoVoST 2英德翻译上，BLEU提升约1.5点。具体数值需参考论文。 |

## 🔗 开源资源

- **代码**：<https://github.com/CyberAgentAILab/mbr-for-asr>

## 🎯 与本站重点领域的关联

与本站重点领域无直接关联，但解码策略可迁移至语音增强/分离中的后处理或重打分步骤。

## ⚠️ 局限与未解决问题

仅评估Whisper系列模型，未测试其他ASR架构；未分析推理延迟增加；未进行消融实验研究采样数量影响。

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

<div class="paper-footer"><span>评分：7.5</span><span>原始：7.5</span><a href="/posts/2026-05-14/">← 返回 2026-05-14 速递</a></div>
