---
title: "Aliasing-Free Neural Audio Synthesis"
date: 2026-05-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#抗混叠", "#神经声码器", "#神经编解码器", "#语音合成", "#高保真音频"]
summary: "提出Pupu-Vocoder和Pupu-Codec，通过可微抗混叠技术消除非线性激活和上采样产生的混叠伪影，在歌唱、音乐和通用音频上超越现有系统。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前10%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#抗混叠</span> <span class="tag-pill tag-pill-soft">#神经声码器</span> <span class="tag-pill tag-pill-soft">#神经编解码器</span> <span class="tag-pill tag-pill-soft">#高保真音频</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2512.20211</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-14</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2512.20211" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2512.20211" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://VocodexElysium.github.io/AliasingFreeNeuralAudioSynthesis/" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://VocodexElysium.github.io/AliasingFreeNeuralAudioSynthesis/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Pupu-Vocoder和Pupu-Codec，通过可微抗混叠技术消除非线性激活和上采样产生的混叠伪影，在歌唱、音乐和通用音频上超越现有系统。
</div>

## 👥 作者与机构

**Yicheng Gu** ¹ · Junan Zhang · Chaoren Wang · Jerry Li · Zhizheng Wu · Lauri Juvela

**机构**：未知

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事神经声码器、音频编解码或高保真音频合成的研究者。建议通读，重点看§3的抗混叠模块设计和§4的实验结果（表1-3）。可先复现其测试信号基准。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| **应用场景** | 高保真音频合成，包括语音、歌唱、音乐和通用音频的波形重建。 |
| **核心创新** | 将可微抗混叠技术集成到激活函数和上采样模块中 · 构建测试信号基准评估抗混叠效果 · 在歌唱和音乐上显著优于现有声码器和编解码器 |
| **模型架构** | 输入声学特征或潜在表示 → 主干网络（基于HiFi-GAN或EnCodec）→ 关键模块：抗混叠激活（如Leaky ReLU+低通滤波）和抗混叠上采样（插值+低通滤波）→ 输出波形。参数量未明确给出。 |
| **数据集** | LibriTTS（语音训练） · VCTK（语音评估） · MUSDB18（音乐评估） · Singing Voice数据集（歌唱评估） |
| **关键结果** | Pupu-Vocoder在歌唱语音上PESQ达4.12（对比HiFi-GAN v1的3.85），MUSHRA评分85.3（对比72.1）；Pupu-Codec在音乐上SI-SNR达12.5 dB（对比EnCodec的10.8 dB）。语音性能与基线相当。 |

## 🔗 开源资源

- **项目主页**：<https://VocodexElysium.github.io/AliasingFreeNeuralAudioSynthesis/>
- **Demo / 试听**：<https://VocodexElysium.github.io/AliasingFreeNeuralAudioSynthesis/>

## 🎯 与本站重点领域的关联

与本站重点领域中的语音增强和乐器分离有间接关联：抗混叠技术可迁移至语音增强中的上采样模块，减少伪影；乐器分离中编解码器的改进有助于提升分离质量。但主要任务为语音合成，非直接相关。

## ⚠️ 局限与未解决问题

未提供模型参数量和推理延迟；仅在歌唱和音乐上显著优于基线，语音提升有限；抗混叠模块的额外计算开销未分析；测试信号基准的通用性待验证。

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

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/posts/2026-05-14/">← 返回 2026-05-14 速递</a></div>
