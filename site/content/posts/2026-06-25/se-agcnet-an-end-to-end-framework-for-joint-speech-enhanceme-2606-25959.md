---
title: "SE-AGCNet: An End-to-End Framework for Joint Speech Enhancement and Loudness Control in Meeting Scenarios"
date: 2026-06-25T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出SE-AGCNet，端到端联合优化语音增强与自动增益控制，在会议场景中同时提升语音质量和响度一致性。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#自动增益控制</span> <span class="tag-pill tag-pill-soft">#端到端联合优化</span> <span class="tag-pill tag-pill-soft">#会议场景</span> <span class="tag-pill tag-pill-soft">#语音质量</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.25959</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-25</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.25959" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.25959" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出SE-AGCNet，端到端联合优化语音增强与自动增益控制，在会议场景中同时提升语音质量和响度一致性。
</div>

## 👥 作者与机构

**Jinming Zhang** ¹ · Wei Rao · Xionghu Zhong · Eng Siong Chng

**机构**：南洋理工大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强和会议系统研究者。建议重点阅读§3联合优化架构和§4数据仿真流程，先看表1对比结果。

## 🌍 研究背景

传统音频流水线将语音增强(SE)和自动增益控制(AGC)作为独立模块，导致性能受限：先AGC会放大噪声，先SE会过度抑制低音量语音。本文针对会议场景中音量变化大的问题，提出端到端联合优化框架，利用SE保护低音量语音以辅助AGC调整，并引入标准化响度评估指标。

## 💡 核心创新

1. 端到端联合优化SE与AGC
2. SE-AGC-DataGen数据仿真流水线
3. 引入LUFS/St LUFS/LRA标准化响度指标

## 🏗️ 模型架构

输入波形→编码器→SE模块（可能为Conformer或类似结构）→AGC模块（估计增益因子）→解码器输出增强且响度调整后的波形。整体为端到端可训练网络，参数量未提及。

## 📚 数据集

- 会议模拟数据集（训练/评估，由SE-AGC-DataGen生成）

## 📊 实验结果

摘要未给出具体数值，但声称SE-AGCNet在达到目标响度的同时，在语音质量和ASR准确率上均优于竞争基线。

## 🎯 结论与影响

SE-AGCNet通过联合优化SE和AGC，有效解决了传统流水线中的噪声放大和语音过度抑制问题，在会议场景中实现响度一致性和高质量语音。该工作为语音前端处理提供了新范式，有望集成到会议系统等实际应用中。

## ⚠️ 局限与未解决问题

缺乏在真实会议录音上的评估；未报告模型参数量和推理延迟；与现有独立SE+AGC流水线的对比可能不够全面；数据仿真流程的泛化性待验证。

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：7.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-25/">← 返回 2026-06-25 速递</a></div>
