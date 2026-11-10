---
title: "MUTE: Multi-Level Alignment Uncoupling Against Talking-Head Exploitation for Voice Protection"
date: 2026-11-10T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频对抗保护"]
summary: "提出MUTE音频保护框架，通过多级对齐解耦扰动破坏说话头生成的音视频对齐，同时保持听感质量。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频对抗保护</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#对抗扰动</span> <span class="tag-pill tag-pill-soft">#深度伪造防御</span> <span class="tag-pill tag-pill-soft">#说话头生成</span> <span class="tag-pill tag-pill-soft">#多模态对齐</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.11989</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-09</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/jindl465/MUTE" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">jindl465/MUTE</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.11989" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.11989" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/jindl465/MUTE" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出MUTE音频保护框架，通过多级对齐解耦扰动破坏说话头生成的音视频对齐，同时保持听感质量。
</div>

## 👥 作者与机构

**Donghyun Kim** ¹ · Jin Hong · Seungmin Kim · Dain Kim · Junseok Kwon · Daeseon Choi

**机构**：韩国中央大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做deepfake防御、对抗音频、多模态安全的读者。建议重点看§3的多级扰动设计（对齐级+表示级）与STFT高能量约束，以及表2的跨模型黑盒迁移结果；若关注语音增强/分离则相关性低，可略读。

## 🌍 研究背景

说话头生成（talking-head）模型能从音频合成逼真面部动画，带来多模态deepfake滥用风险。现有防御多集中在图像/视频侧（如加对抗噪声破坏人脸检测），音频侧保护方法稀少；而说话头模型强依赖精确的音视频对齐，理论上音频扰动可高效破坏该对齐。本文要解决：如何在保持音频听感的前提下，用音频对抗扰动稳定破坏白盒与黑盒说话头模型的唇同步。

## 💡 核心创新

1. 对齐级扰动：直接攻击跨模态注意力结构
2. 表示级退化：扰动时序音频嵌入表示
3. STFT高能量区域约束提升鲁棒性
4. 可选说话人级目标防TTS重合成绕过

## 🏗️ 模型架构

输入为原始语音波形，先经STFT变换到频域，仅在能量集中的时频区域施加扰动约束以兼顾鲁棒性与听感。扰动通过多级目标联合优化：(1) 对齐级损失直接干扰说话头模型内部的跨模态注意力图，破坏音视频结构对齐；(2) 表示级损失扰动音频编码器的时序嵌入，退化其表征；(3) 可选说话人级目标约束嵌入，抵御TTS重合成绕过。最终逆STFT回波形输出受保护音频，属优化式对抗扰动框架而非端到端训练网络。

## 📚 数据集

- 说话头生成模型评估集（评估，白盒/黑盒）
- 真实世界变换后处理测试集（评估，鲁棒性）

## 📊 实验结果

摘要仅定性说明：MUTE在白盒与黑盒说话头模型上均持续降低唇同步指标，同时保持感知音频质量；在真实世界变换（后处理、去噪、自适应攻击）下仍有效，并可与图像侧方法叠加获得更强多模态保护。摘要未给出具体LSE-C/LSE-D、PESQ等数值，故无法列表量化。

## 🎯 结论与影响

最强结论是：仅靠音频侧多级对齐解耦扰动即可跨模型稳定破坏说话头唇同步且听感可接受。这为多模态deepfake防御补上音频保护一环，提示后续工作可将音频与图像扰动联合设计；工业上可用于内容发布前的音频预处理防护。

## ⚠️ 局限与未解决问题

摘要未报告具体量化指标与消融，难以判断各级损失贡献；黑盒迁移仅定性描述，缺少对未知商业模型的泛化验证；未讨论推理耗时与实时性；听感保持仅有定性声明，缺PESQ/UTMOS数值；对强自适应攻击的防御边界未量化。

## 🔗 开源资源

- **代码**：<https://github.com/jindl465/MUTE>

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-11-10/">← 返回 2026-11-10 速递</a></div>
