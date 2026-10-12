---
title: "RDSE: Real-Time Directional Speech Enhancement Framework for Dual-Mic Commodity Smartphones"
date: 2026-10-12T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "面向双麦低端手机，用视觉参数化导向矢量，串联去混响、TCN波束成形与MetricGAN去噪，实现实时定向语音增强。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#双耳音频</span> <span class="tag-pill tag-pill-soft">#波束成形</span> <span class="tag-pill tag-pill-soft">#实时推理</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.12476</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-12</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.12476" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.12476" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>面向双麦低端手机，用视觉参数化导向矢量，串联去混响、TCN波束成形与MetricGAN去噪，实现实时定向语音增强。
</div>

## 👥 作者与机构

**Chinmay Deo** ¹ · Danish Mahajan · Soudeep Ghoshal · Himanshu Buckchash

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做移动端/嵌入式语音增强与麦克风阵列工程的读者。建议重点看系统框图与波束成形模块（§3 与 TCN 设计），以及延迟剖析与消融表；若关注 MetricGAN 训练细节可略读。可执行动作：先看系统总览图与实时延迟表，再核对消融是否覆盖各模块贡献。

## 🌍 研究背景

移动端音视频变焦受限于麦克风数量少、算力有限、阵列几何未知，且真实声学条件假设弱。此前方案多为紧耦合 AV 系统，持续使用视觉流或 embedding，计算开销大且对几何标定敏感；传统波束成形在双麦低端设备上难以稳定。本文要解决的是：在双麦商品手机上，用视觉仅参数化导向矢量，解耦视觉交互与特征推理，实现无需精确几何标定的实时定向语音增强。

## 💡 核心创新

1. 视觉仅用于参数化导向矢量，解耦视觉与特征推理
2. 去混响网络 + TCN 波束成形 + MetricGAN 去噪的混合流水线
3. 无需精确阵列几何标定的双麦实时定向增强
4. 统计显著性检验与实时直播延迟剖析的工程验证

## 🏗️ 模型架构

输入为双麦含噪含混响语音，视觉输入仅用于估计导向矢量以参数化空间滤波。流水线含四模块：先去混响网络抑制晚期混响；随后波束成形器结合时序卷积网络（TCN）做空间滤波；再用 MetricGAN 去噪器进一步抑制残余噪声；最终输出增强后的单通道目标方向语音。整体为传统信号处理与深度学习的混合架构，面向低端双麦手机实时运行，摘要未给出参数量。

## 📊 实验结果

摘要仅称在基准数据与真实录音上评估，展示无需精确几何标定的有效变焦，对比实验显示与现有方法性能相当，并做了统计有效性检验、消融、延迟剖析与实时直播验证。但未给出 SI-SDR、PESQ、WER 等具体数值，也未列出对比基线名称与测试集规模，无法量化提升幅度。

## 🎯 结论与影响

最强结论是：视觉仅参数化导向矢量的解耦式混合流水线，可在双麦低端手机上实现无需精确标定的实时定向语音增强。该思路对移动端 AV 语音增强的轻量化设计有参考价值，提示视觉不必持续参与特征推理。工业上利于在商品手机落地实时音视频变焦与定向拾音。

## ⚠️ 局限与未解决问题

摘要未报告任何量化指标与基线数值，难以判断相对 SOTA 的真实增益；未说明去混响、TCN 波束成形、MetricGAN 各模块的消融贡献；未给出模型参数量、内存与端到端延迟具体数字；真实录音的说话人/噪声多样性未知，存在数据集偏差风险；与紧耦合 AV 方法的对比是否公平也未交代。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：6.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-12/">← 返回 2026-10-12 速递</a></div>
