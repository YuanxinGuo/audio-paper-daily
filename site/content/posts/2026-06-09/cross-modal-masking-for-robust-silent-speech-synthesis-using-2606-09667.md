---
title: "Cross-Modal Masking for Robust Silent Speech Synthesis Using sEMG and Lipreading"
date: 2026-06-09T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "提出跨模态掩蔽框架，联合sEMG和唇读信号实现鲁棒静音语音合成，在低比特率和模态缺失条件下显著优于单模态基线。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#静音语音合成</span> <span class="tag-pill tag-pill-soft">#表面肌电图</span> <span class="tag-pill tag-pill-soft">#唇读</span> <span class="tag-pill tag-pill-soft">#多模态融合</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.09667</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-09</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.09667" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.09667" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出跨模态掩蔽框架，联合sEMG和唇读信号实现鲁棒静音语音合成，在低比特率和模态缺失条件下显著优于单模态基线。
</div>

## 👥 作者与机构

**Eder del Blanco** ¹ · David Gimeno-G\'omez · Eva Navas · Carlos-D. Mart\'inez-Hinarejos · Inma Hern\'aez

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音合成、人机交互领域研究者。建议重点阅读§3掩蔽策略和§4.2鲁棒性实验。可先看表1的WER对比，再深入方法细节。

## 🌍 研究背景

静音语音接口通过非侵入式传感器（如sEMG、唇读）为喉部受损者恢复语音。现有方法多依赖单模态，多模态融合研究不足，且缺乏对传感器退化或缺失的鲁棒性。本文旨在通过跨模态掩蔽训练，提升多模态语音合成在低比特率和模态缺失下的性能。

## 💡 核心创新

1. 提出模态掩蔽训练策略，随机丢弃模态以增强鲁棒性
2. 联合sEMG和唇读特征进行多说话人语音合成
3. 在模态缺失条件下优于特定退化的数据增强方法
4. 音素级分析揭示模态互补性，元音和特定辅音受益显著

## 🏗️ 模型架构

输入为sEMG信号和唇读视频帧，分别通过编码器提取特征。采用模态掩蔽策略随机丢弃某一模态的特征，然后融合多模态特征送入基于Transformer的语音合成网络（如Tacotron2或FastSpeech变体），输出Mel谱图，再经声码器合成波形。模型支持多说话人条件。

## 📚 数据集

- sEMG和唇读数据集（多说话人，训练/评估，具体规模未提及）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | 内部测试集 | 最强单模态基线（具体值未给出） | **降低14个绝对百分点** | -14% |

实验表明，掩蔽策略在低比特率条件下显著提升性能，且泛化能力优于特定退化的数据增强。音素级分析显示，元音和特定辅音组受益最大，验证了模态互补性。

## 🎯 结论与影响

跨模态掩蔽框架有效提升了静音语音合成的鲁棒性，尤其在传感器退化场景下。该工作为多模态SSI的实际部署提供了新思路，但需进一步适配喉切除患者。

## ⚠️ 局限与未解决问题

未在真实喉切除患者数据上验证；未报告模型参数量和推理延迟；对比基线仅提及单模态，缺少与最新多模态方法的比较；数据集规模未明确。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-06-09/">← 返回 2026-06-09 速递</a></div>
