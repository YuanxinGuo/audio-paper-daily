---
title: "What Do Deepfake Speech Detectors Actually Hear?"
date: 2026-06-10T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频深度伪造检测"]
summary: "提出基于集成梯度的可解释性方法，揭示三个WavLM深度伪造语音检测器依赖的不同声学线索。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频深度伪造检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#可解释性</span> <span class="tag-pill tag-pill-soft">#WavLM</span> <span class="tag-pill tag-pill-soft">#集成梯度</span> <span class="tag-pill tag-pill-soft">#ASVspoof</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.10912</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-10</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.10912" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.10912" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于集成梯度的可解释性方法，揭示三个WavLM深度伪造语音检测器依赖的不同声学线索。
</div>

## 👥 作者与机构

Vojt\v{e}ch Stan\v{e}k · Veronika Jirmusov\'a · Anton Firc · Kamil Malinka · Jakub Re\v{s} · Martin Pere\v{s}\'ini

**机构**：布尔诺理工大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频安全与可解释AI研究者。重点读§3方法、§4.2语义标注与§5因果验证。建议先看表1与图3理解不同检测器的注意力差异。

## 🌍 研究背景

深度伪造语音检测器通常只输出一个分数，不解释为何判定为伪造、证据在信号中的位置或驱动决策的线索。现有可解释性方法多用于图像或文本，音频领域缺乏针对时间定位和语义解释的通用框架。本文旨在填补这一空白，提出音频原生的可解释性流水线。

## 💡 核心创新

1. 提出基于集成梯度的时间对齐可解释性方法
2. 首次对WavLM检测器进行语义级线索标注
3. 通过因果掩码验证检测器依赖的声学线索
4. 揭示不同检测器依赖不同线索（环境/音素/词边界）

## 🏗️ 模型架构

输入音频经WavLM提取自监督表示，对三个检测器（AASIST、CA-MHFA、SLS）计算集成梯度，得到时间注意力图。对最高注意力区域进行人工语义标注（环境声、音素伪影、词边界等）。最后通过因果掩码（移除高注意力区域）验证线索重要性。

## 📚 数据集

- ASVspoof 5（评估，包含真实与深度伪造语音）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| EER | ASVspoof 5 | AASIST 0.82% | **AASIST 0.82%** | 0% |
| EER | ASVspoof 5 | CA-MHFA 0.79% | **CA-MHFA 0.79%** | 0% |
| EER | ASVspoof 5 | SLS 0.82% | **SLS 0.82%** | 0% |

三个检测器在ASVspoof 5上性能相近（EER约0.8%），但可解释性分析显示它们依赖不同线索：AASIST关注非语音/环境线索，CA-MHFA关注局部音素伪影，SLS依赖词边界和频谱完整性。因果掩码实验证实移除高注意力区域导致性能下降，验证了线索重要性。

## 🎯 结论与影响

本文提出的可解释性方法能有效揭示深度伪造语音检测器的决策依据，发现不同架构检测器依赖不同声学线索。该工作为音频可解释性研究提供了新工具，有助于设计更鲁棒的检测器，并推动音频AI的透明化。

## ⚠️ 局限与未解决问题

仅分析三个WavLM检测器，未涵盖其他架构（如ResNet、LSTM）。人工语义标注主观性强，且仅对ASVspoof 5数据集。未评估跨数据集泛化性。因果掩码仅移除单一区域，未考虑多区域组合影响。

---

<div class="paper-footer"><span>评分：7.5</span><span>原始：7.5</span><a href="/audio-paper-daily/posts/2026-06-10/">← 返回 2026-06-10 速递</a></div>
