---
title: "JAM-Flow: Joint Audio-Motion Synthesis with Flow Matching"
date: 2026-05-18T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#多模态生成"]
summary: "提出JAM-Flow，利用流匹配和MM-DiT架构统一联合生成面部运动与语音，支持多种条件输入。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#多模态生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音驱动面部动画</span> <span class="tag-pill tag-pill-soft">#文本转语音</span> <span class="tag-pill tag-pill-soft">#流匹配</span> <span class="tag-pill tag-pill-soft">#扩散Transformer</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2506.23552</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-18</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://joonghyuk.com/jamflow-web" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">joonghyuk.com/jamflow-web</span></span></a><a class="oc-chip oc-chip-demo" href="https://joonghyuk.com/jamflow-web" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">joonghyuk.com/jamflow-web</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2506.23552" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2506.23552" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://joonghyuk.com/jamflow-web" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://joonghyuk.com/jamflow-web" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出JAM-Flow，利用流匹配和MM-DiT架构统一联合生成面部运动与语音，支持多种条件输入。
</div>

## 👥 作者与机构

**Mingi Kwon** ¹ · Joonghyuk Shin · Jaeseok Jung · Jaesik Park · Youngjung Uh ✉

**机构**：延世大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合多模态生成、语音驱动动画、TTS研究者。建议通读，重点看§3的MM-DiT架构和§4的inpainting训练策略。可复现实验部分。

## 🌍 研究背景

现有说话头生成和TTS通常作为独立任务处理，忽略了面部运动与语音的内在联系。先前工作如Wav2Lip、PC-AVS等仅单向驱动，缺乏联合建模。本文旨在统一框架，同时合成并相互条件化面部运动与语音，实现更自然的音视频同步。

## 💡 核心创新

1. 提出MM-DiT架构，含Motion-DiT和Audio-DiT模块
2. 选择性联合注意力层实现跨模态交互
3. 时间对齐位置编码和局部联合注意力掩码
4. 基于inpainting目标的统一训练范式
5. 支持文本、参考音频、参考运动等多种条件输入

## 🏗️ 模型架构

输入为文本/参考音频/参考运动等条件，经编码器提取特征。主干为MM-DiT，包含Motion-DiT和Audio-DiT两个独立DiT模块，通过选择性联合注意力层交互，并采用时间对齐位置编码和局部联合注意力掩码。输出为同步的面部运动序列和语音波形。

## 📚 数据集

- VoxCeleb2（训练/评估，含视频和音频）
- HDTF（评估，高分辨率说话头视频）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| FID | VoxCeleb2 | Wav2Lip 12.3 | **9.8** | -2.5 |
| LSE-D | VoxCeleb2 | Wav2Lip 7.2 | **6.5** | -0.7 |
| MOS (语音质量) | VoxCeleb2 | Tacotron2 3.8 | **4.1** | +0.3 |

JAM-Flow在VoxCeleb2上FID降低2.5，LSE-D降低0.7，语音MOS提升0.3。消融实验验证了联合注意力、时间对齐编码等模块的有效性。在HDTF上零样本泛化表现良好，且支持多种条件组合生成。

## 🎯 结论与影响

JAM-Flow首次实现面部运动与语音的联合生成，通过流匹配和MM-DiT架构取得SOTA性能。该工作为多模态音视频合成提供了统一框架，有望推动数字人、虚拟助手等应用发展。

## ⚠️ 局限与未解决问题

未报告推理速度或参数量；仅使用VoxCeleb2训练，可能受限于数据集多样性；缺乏与更多基线（如PC-AVS、MakeItTalk）的定量对比；联合生成质量在极端表情或噪声条件下可能下降。

## 🔗 开源资源

- **项目主页**：<https://joonghyuk.com/jamflow-web>
- **Demo / 试听**：<https://joonghyuk.com/jamflow-web>

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-05-18/">← 返回 2026-05-18 速递</a></div>
