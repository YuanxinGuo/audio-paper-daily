---
title: "Fine-grained Soundscape Control for Augmented Hearing"
date: 2026-07-13T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出Aurchestra系统，在资源受限的耳戴设备上实现实时、细粒度的多类声音独立控制，支持最多5个重叠目标。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.5</div>
<div class="score-stars">★★★★★</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#目标说话人提取</span> <span class="tag-pill tag-pill-soft">#声音事件检测</span> <span class="tag-pill tag-pill-soft">#实时系统</span> <span class="tag-pill tag-pill-soft">#可穿戴设备</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.00395</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-13</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.00395" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.00395" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Aurchestra系统，在资源受限的耳戴设备上实现实时、细粒度的多类声音独立控制，支持最多5个重叠目标。
</div>

## 👥 作者与机构

**Seunghyun Oh** ¹ · Malek Itani · Aseem Gauri · Shyamnath Gollakota ✉

**机构**：华盛顿大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强、可穿戴音频、实时系统方向的研究者。建议通读，重点看§3（多输出提取网络架构）和§4（动态接口与实时优化）。可复现其模型压缩与设备部署策略。

## 🌍 研究背景

现有耳戴设备的声音控制方式单一，要么全局降噪，要么聚焦单一目标，无法独立调节场景中多个同时声源。之前的工作多关注单目标提取或通用增强，缺乏对多类声音的细粒度、实时控制。本文旨在解决在计算受限的耳戴设备上实现多输出、低延迟的声音场景控制问题。

## 💡 核心创新

1. 动态接口：仅显示当前活跃的声音类别，减少用户选择负担
2. 多输出提取网络：单模型同时分离最多5个目标类，输出独立流
3. 实时优化：在6ms音频块上运行，适配多种低功耗平台

## 🏗️ 模型架构

输入为6ms音频块，经特征提取后送入多输出提取网络。主干采用轻量级卷积循环网络，包含共享编码器和多个并行解码器，每个解码器对应一个目标声音类。网络输出为各目标类的独立音频流，用户可调节每类音量实现混合。模型针对ARM Cortex-M和DSP等平台进行量化与剪枝优化。

## 📚 数据集

- FSD50K（训练声音事件检测与提取）
- ESC-50（评估声音分类与分离）
- 自采真实室内外场景数据（评估系统性能）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SI-SDRi (dB) | 自采混合场景（5类重叠） | 单输出提取网络 | **多输出提取网络** | +3.2 dB |
| 干扰抑制比 (dB) | 自采混合场景（5类重叠） | 全局降噪 | **Aurchestra** | -8.5 dB |

在真实室内外场景中，Aurchestra实现了对目标类的显著增强（SI-SDRi提升3.2 dB）和干扰抑制（干扰抑制比-8.5 dB）。系统在6ms块上实时运行，模型大小适配多种低功耗平台。消融实验验证了动态接口和多输出架构的有效性。

## 🎯 结论与影响

Aurchestra首次在耳戴设备上实现了可编程的声音场景控制，用户可像混音师一样独立调节多个声源音量。该工作推动了增强听觉从全局处理向细粒度交互的转变，对消费级助听器和AR/VR设备有重要应用价值。

## ⚠️ 局限与未解决问题

系统目前仅支持预定义的有限声音类别（如语音、音乐、警报等），无法处理未知类别。多输出网络在超过5个目标时性能下降。未报告用户主观听感测试。实时性评估仅基于特定硬件平台，泛化性待验证。

---

<div class="paper-footer"><span>评分：9.5</span><span>原始：8.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-13/">← 返回 2026-07-13 速递</a></div>
