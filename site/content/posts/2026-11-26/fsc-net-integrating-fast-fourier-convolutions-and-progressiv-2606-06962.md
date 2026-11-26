---
title: "FSC-Net: Integrating Fast Fourier Convolutions and Progressive Learning for Speech Bandwidth Extension"
date: 2026-11-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "FSC-Net 用快速傅里叶卷积扩展感受野至全频谱，并以频率渐进课程学习重建高频，实现 1.54M 参数的高效语音带宽扩展。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#带宽扩展</span> <span class="tag-pill tag-pill-soft">#复数谱映射</span> <span class="tag-pill tag-pill-soft">#快速傅里叶卷积</span> <span class="tag-pill tag-pill-soft">#课程学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.06962</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.06962" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.06962" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>FSC-Net 用快速傅里叶卷积扩展感受野至全频谱，并以频率渐进课程学习重建高频，实现 1.54M 参数的高效语音带宽扩展。
</div>

## 👥 作者与机构

**Xinan Chen** ¹ · Xiaobin Rong · Qinwen Hu · Kai Chen · Jing Lu

**机构**：南京大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做语音增强/带宽扩展与轻量声学模型的研究者阅读。建议通读：重点看 §3 中 FFC 如何嵌入复数谱映射主干，以及频率渐进课程的分阶段设计；实验部分先看表 2 的 VCTK 4kHz→48kHz 结果与 EARS 泛化，再看参数量对比。

## 🌍 研究背景

语音带宽扩展（BWE）需从窄带语音重建宽带高频成分，是语音增强与通信后处理的经典问题。此前方法多基于时域或幅度谱映射（如 U-Net、GAN 类），对高频相位与谐波结构建模不足，易产生感知伪影；且高频生成本身是病态问题，模型常需较大参数量才能覆盖长程频带依赖。本文要解决的是：如何在紧凑参数下显式建模跨频带谐波依赖，并稳定地由粗到细重建高频细节。

## 💡 核心创新

1. 将 Fast Fourier Convolution 引入复数谱映射，感受野覆盖全频谱
2. 提出频率渐进学习课程，由粗到细重建高频谱细节
3. 参数高效的全频谱上下文网络 FSC-Net，仅 1.54M 参数
4. 在未见 EARS 数据集上验证跨域泛化能力

## 🏗️ 模型架构

输入为窄带语音的 STFT 复数谱，主干采用复数谱映射框架，将实部与虚部作为双通道特征。核心模块为 Fast Fourier Convolution（FFC），通过频域全局分支与局部分支并联，把感受野扩展到整个频谱以捕捉长程频率交互；网络整体为多尺度编解码结构，逐级融合跨频带谐波信息。训练时采用频率渐进课程：先重建低频段、再逐步扩展到高频段，缓解高频生成的病态性。输出为完整宽带复数谱，经 iSTFT 还原波形，模型参数量 1.54M。

## 📚 数据集

- VCTK（训练与评估，含 4kHz→48kHz 任务）
- EARS（未见数据集，评估泛化）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| LSD | VCTK 4kHz→48kHz | scaled-up baselines（摘要未给具体值） | **摘要称领先但未给数值** | 未提供具体数值 |
| PESQ | VCTK 4kHz→48kHz | scaled-up baselines（摘要未给具体值） | **摘要称领先但未给数值** | 未提供具体数值 |

摘要称在 VCTK 与未见 EARS 上均取得稳定重建质量与泛化，尤其在 VCTK 4kHz→48kHz 任务上 LSD 与 PESQ 领先于放大参数后的基线，同时参数量仅 1.54M。但摘要未给出具体指标数值、消融实验与推理延迟，频率渐进课程与 FFC 模块各自的贡献尚需正文表格确认。

## 🎯 结论与影响

最强结论是：在 1.54M 紧凑参数下，FFC 全频谱感受野加频率渐进课程可在高倍带宽扩展任务上同时取得领先 LSD/PESQ 与良好跨数据集泛化。这为轻量 BWE 提供了可复用的模块与训练策略，对通信与助听等端侧部署场景有实际意义。

## ⚠️ 局限与未解决问题

摘要未报告具体指标数值、推理延迟与实时因子；缺少 FFC 与渐进课程各自的消融；基线仅称 scaled-up，未列明具体方法与参数量；感知指标仅 PESQ，缺 MOS/STOI 等主观或可懂度评估。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-11-26/">← 返回 2026-11-26 速递</a></div>
