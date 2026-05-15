---
title: "Aliasing-Free Neural Audio Synthesis"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#抗混叠", "#神经声码器", "#神经编解码器", "#语音合成", "#高保真音频"]
summary: "提出可微抗混叠技术集成到激活和上采样模块，构建Pupu-Vocoder和Pupu-Codec，在歌声、音乐和音频上超越现有系统，语音性能相当。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#抗混叠</span> <span class="tag-pill tag-pill-soft">#神经声码器</span> <span class="tag-pill tag-pill-soft">#神经编解码器</span> <span class="tag-pill tag-pill-soft">#高保真音频</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2512.20211</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2512.20211" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2512.20211" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://VocodexElysium.github.io/AliasingFreeNeuralAudioSynthesis/" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://VocodexElysium.github.io/AliasingFreeNeuralAudioSynthesis/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出可微抗混叠技术集成到激活和上采样模块，构建Pupu-Vocoder和Pupu-Codec，在歌声、音乐和音频上超越现有系统，语音性能相当。
</div>

## 👥 作者与机构

**Yicheng Gu** ¹ · Junan Zhang · Chaoren Wang · Jerry Li · Zhizheng Wu · Lauri Juvela

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事神经声码器、编解码器或高保真音频合成的研究者。建议重点阅读§3（抗混叠模块设计）和§4（实验与消融），先看表2和表3对比结果。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| **应用场景** | 高保真音频合成，包括语音、歌声、音乐和通用音频的波形重建。 |
| **核心创新** | 将可微抗混叠技术集成到激活函数和上采样层 · 构建测试信号基准评估抗混叠模块 · 在多种音频域上验证有效性 |
| **模型架构** | 输入声学或潜在表示 → 主干网络（基于HiFi-GAN或类似架构）→ 关键模块：抗混叠激活（如Leaky ReLU+低通滤波）和抗混叠上采样（如插值+低通滤波）→ 输出波形。参数量未在摘要中给出。 |
| **数据集** | 语音数据集（训练与评估） · 歌声数据集（训练与评估） · 音乐数据集（训练与评估） · 通用音频数据集（训练与评估） |
| **关键结果** | Pupu-Vocoder和Pupu-Codec在歌声、音乐和音频上优于现有系统，语音性能相当。具体指标未在摘要中给出，需参考论文正文。 |

## 🔗 开源资源

- **项目主页**：<https://VocodexElysium.github.io/AliasingFreeNeuralAudioSynthesis/>
- **Demo / 试听**：<https://VocodexElysium.github.io/AliasingFreeNeuralAudioSynthesis/>

## 🎯 与本站重点领域的关联

与语音增强、目标说话人提取、语音分离、双耳音频、乐器分离无直接关联。但抗混叠技术可迁移至这些领域的生成模型，例如语音增强中的上采样模块或乐器分离中的激活函数，以减少伪影。

## ⚠️ 局限与未解决问题

摘要未报告参数量、推理延迟或模型复杂度；未提供具体指标数值，仅定性描述；抗混叠模块可能增加计算开销；在语音任务上仅达到可比性能，未显著提升。

## 📋 引用

```bibtex
@article{gu20262512,
  title  = {Aliasing-Free Neural Audio Synthesis},
  author = {Yicheng Gu and  Junan Zhang and  Chaoren Wang and  Jerry Li and  Zhizheng Wu and  Lauri Juvela},
  journal = {arXiv preprint arXiv:2512.20211},
  year   = {2026}
}
```

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
