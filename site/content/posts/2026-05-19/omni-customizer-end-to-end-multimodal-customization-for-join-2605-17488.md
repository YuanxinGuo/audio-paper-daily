---
title: "Omni-Customizer: End-to-End MultiModal Customization for Joint Audio-Video Generation"
date: 2026-05-19T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音视频联合生成"]
summary: "提出Omni-Customizer，一种端到端框架，实现联合音视频生成中视觉身份和语音音色的多模态定制化。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音视频联合生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态定制化</span> <span class="tag-pill tag-pill-soft">#语音身份保持</span> <span class="tag-pill tag-pill-soft">#音视频同步</span> <span class="tag-pill tag-pill-soft">#扩散模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.17488</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.17488" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.17488" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Omni-Customizer，一种端到端框架，实现联合音视频生成中视觉身份和语音音色的多模态定制化。
</div>

## 👥 作者与机构

**Yuheng Chen** ¹ · Qingdong He · Teng Hu · Yuji Wang · Yabiao Wang · Lizhuang Ma · Jiangning Zhang ✉

**机构**：上海交通大学 · 阿里巴巴达摩院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事多模态生成、音视频同步、定制化生成的研究者阅读。建议重点读§3.2 Omni-Context Fusion模块和§3.3 Masked TTS Cross-Attention机制，以及§4.2消融实验。可先看表1和表2了解性能提升。

## 🌍 研究背景

现有音视频联合生成模型（如VideoPoet、Make-A-Video）在生成高质量视频和音频方面取得进展，但缺乏对多主体视觉身份和语音音色的联合定制能力。先前工作如DreamBooth和Custom Diffusion仅针对图像或视频，无法同时保持语音特征。本文旨在解决多模态身份信息绑定和融合的挑战，防止语音泄漏问题。

## 💡 核心创新

1. Omni-Context Fusion (OCF)模块融合多模态身份线索
2. Masked TTS Cross-Attention (MTP-CA)防止语音泄漏
3. Semantic-Anchored Multimodal RoPE (SA-MRoPE)实现结构化融合
4. 交错音视频调度训练策略适应多语言场景
5. 渐进式成对到跨对课程学习增强身份特征

## 🏗️ 模型架构

输入：文本提示、视觉参考图像、音频参考片段（含TTS嵌入）。主干：基于扩散模型的音视频联合生成框架。关键模块：Omni-Context Fusion (OCF)模块将视觉和音频身份特征注入文本编码；Masked TTS Cross-Attention (MTP-CA)在交叉注意力中屏蔽非目标语音区域；Semantic-Anchored Multimodal RoPE (SA-MRoPE)将参考token锚定到语义描述。输出：同步的视频和音频。

## 📚 数据集

- VoxCeleb2（训练/评估，身份保持）
- HDTF（训练/评估，视频质量）
- LRS3（训练/评估，唇同步）
- 自定义多语言数据集（训练，多语言适应）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| FID | HDTF | VideoPoet 12.3 | **10.1** | -2.2 |
| FVD | HDTF | VideoPoet 85.6 | **72.3** | -13.3 |
| MOS (音质) | VoxCeleb2 | Make-A-Video 3.2 | **4.1** | +0.9 |
| MOS (同步) | LRS3 | VideoPoet 3.5 | **4.3** | +0.8 |

在HDTF和VoxCeleb2上，Omni-Customizer在FID、FVD、音质MOS和同步MOS上均超越VideoPoet和Make-A-Video。消融实验验证了OCF、MTP-CA和SA-MRoPE各自的有效性。跨语言测试表明多语言适应策略有效，且未损害英文性能。

## 🎯 结论与影响

Omni-Customizer在联合音视频定制化生成中达到SOTA，同时保持视觉身份和语音音色。其模块化设计（OCF、MTP-CA、SA-MRoPE）为多模态身份绑定提供了新范式，有望推动个性化视频生成和虚拟主播等应用。

## ⚠️ 局限与未解决问题

未报告推理时间和模型参数量；仅评估了英文和少量多语言场景，泛化性待验证；未与近期端到端音视频生成模型（如Show-1）对比；缺乏对复杂场景（如多人对话）的评估。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-05-19/">← 返回 2026-05-19 速递</a></div>
