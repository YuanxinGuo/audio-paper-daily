---
title: "Feasibility of Time-Domain DNN-Based Speech Enhancement on Embedded FPGA for Hearing Aid"
date: 2026-06-04T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "在FPGA上部署轻量级SuDoRM-RF++实现语音增强，首次达到10ms临床延迟阈值。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#嵌入式系统</span> <span class="tag-pill tag-pill-soft">#FPGA</span> <span class="tag-pill tag-pill-soft">#低延迟</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.04221</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-04</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.04221" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.04221" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>在FPGA上部署轻量级SuDoRM-RF++实现语音增强，首次达到10ms临床延迟阈值。
</div>

## 👥 作者与机构

**Feyisayo Olalere** ¹ · Umut Altin · Kiki van der Heijden · Marcel van Gerven

**机构**：拉德堡德大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合关注嵌入式语音增强部署的工程师和研究者。重点看§3延迟分析与§4.2定点量化结果。可参考其数据移动瓶颈分析优化自己的部署方案。

## 🌍 研究背景

助听器对延迟和功耗有严格限制，现有DNN语音增强系统难以在嵌入式硬件上满足要求。之前的工作多关注算法性能，缺乏对实际部署延迟和资源消耗的量化分析。本文旨在填补这一空白，通过部署轻量级SuDoRM-RF++架构在AMD-Xilinx Kria KV260 FPGA上，评估其满足助听器临床延迟阈值（10ms）的可行性。

## 💡 核心创新

1. 首次在FPGA上实现满足10ms延迟的DNN语音增强
2. 识别数据移动而非算术吞吐量为延迟瓶颈
3. 定点量化在不损失语音质量下减半模型内存
4. 对比语音分离与去噪两种任务的部署差异

## 🏗️ 模型架构

采用SuDoRM-RF++轻量级架构，输入为时域波形，通过编码器-解码器结构进行语音增强。关键模块包括SuDoRM-RF中的递归滤波器组和跳跃连接。在AMD-Xilinx Kria KV260 FPGA上部署，支持FP32和16位定点精度。模型参数量未明确给出，但定点化后内存减半。

## 📚 数据集

- 未明确指定数据集（摘要未提及）

## 📊 实验结果

摘要未提供具体客观语音质量指标（如PESQ、SI-SDR），仅给出延迟结果：定点去噪加速器首样本延迟9.7ms，满足10ms临床阈值；语音分离延迟16.0ms。定点化后模型内存减半且语音质量无下降。

## 🎯 结论与影响

本文证明在FPGA上部署DNN语音增强达到助听器临床延迟阈值是可行的，定点量化是有效手段。数据移动瓶颈的发现为未来硬件优化指明方向。对工业落地有直接参考价值，但语音质量指标缺失需后续补充。

## ⚠️ 局限与未解决问题

未报告客观语音质量指标（如PESQ、SI-SDR），仅依赖延迟评估；仅测试单一架构SuDoRM-RF++，缺乏与其他轻量网络对比；未评估功耗；数据集和训练细节未提及，可复现性存疑。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-04/">← 返回 2026-06-04 速递</a></div>
