---
title: "Design and Architecture of Airmod: An Active Noise Cancellation and Deep Learning System for Real-Time Respiratory Rate Estimation from Tracheal Sounds"
date: 2026-10-28T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "Airmod 用双麦克风主动降噪加 CNN-BiGRU 检测气管音吸呼气事件，实时估计呼吸率，已获 FDA 510(k) 认证。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#主动降噪</span> <span class="tag-pill tag-pill-soft">#呼吸率估计</span> <span class="tag-pill tag-pill-soft">#生物声学</span> <span class="tag-pill tag-pill-soft">#医疗音频</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.37083</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.37083" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.37083" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>Airmod 用双麦克风主动降噪加 CNN-BiGRU 检测气管音吸呼气事件，实时估计呼吸率，已获 FDA 510(k) 认证。
</div>

## 👥 作者与机构

**Shang-Ran Huang** ¹ · Fu-Shun Hsu · Ji-Chang Huang · Chuan Chen · Shou-Zen Fan · Chang-Fu Su · Eng-Che Huang · Yuan-Ren Cheng

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做医疗音频、可穿戴声学监测、嵌入式实时系统的工程与研究读者。若关注算法细节，重点看主动降噪（NLMS 自适应滤波）与 CNN-BiGRU 事件检测两节，以及重叠窗推理与后处理（去不完整事件、低能量误检、重复计数）的设计；若关注临床价值，看测试集灵敏度/PPV 与实时性描述。不建议逐字通读，属系统描述型论文。

## 🌍 研究背景

临床指南建议在镇静与麻醉监护中持续听诊气管音以监测通气，但传统听诊器难以长时间连续使用、易受环境噪声干扰且判读依赖经验。此前呼吸率监测多依赖胸腹带、ECG 派生或摄像头，声学方案则受噪声与事件检测精度限制。本文要解决的是：在真实临床噪声环境下，用电子听诊器连续采集气管音并实时、逐次呼吸地估计呼吸率，形成可落地的医疗器械系统。

## 💡 核心创新

1. 双麦克风电子听诊器 + NLMS 自适应主动降噪抑制环境噪声
2. CNN-BiGRU 多类模型在 15 s 窗口内检测吸气/呼气事件
3. 重叠窗流式推理 + 后处理去除不完整事件、低能量误检与重复计数
4. 以最近三次呼吸平均周期估计呼吸率，并实时广播降噪音频与频谱图

## 🏗️ 模型架构

输入为双麦克风电子听诊器采集的气管音，先经归一化最小均方（NLMS）自适应滤波器做主动噪声控制，输出降噪信号。降噪音频以 15 s 重叠窗送入多类 CNN-BiGRU：卷积层提取局部时频特征，双向 GRU 建模时序上下文，输出吸气/呼气/背景多类帧级判定。流式推理时对重叠窗结果做事件级后处理（剔除不完整事件、低能量误检、重复计数），拼接为呼吸历史列表，取最近三次呼吸平均周期换算呼吸率；同时广播降噪音频并显示实时频谱图。摘要未给出参数量。

## 📚 数据集

- HF_Tracheal_V2（训练与评估，373 段连续气管音录音，8,521 分钟，107,644 个标注吸气，369 名受试者，镇静状态）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Sensitivity | HF_Tracheal_V2 测试集 | 未给出对比基线 | **0.828** | — |
| PPV | HF_Tracheal_V2 测试集 | 未给出对比基线 | **0.832** | — |
| F1-score | HF_Tracheal_V2 测试集 | 未给出对比基线 | **0.830** | — |

在默认 2 s 预测间隔并启用后处理的设置下，吸气检测灵敏度 0.828、阳性预测值 0.832、F1 0.830。摘要未报告与现有呼吸率估计方法的对比、消融实验（如去掉主动降噪或后处理的影响）、推理延迟与功耗等效率指标，也未给出呼吸率本身的误差指标（如 MAE / RMSE）。

## 🎯 结论与影响

本文最强结论是：一套集成主动降噪与 CNN-BiGRU 事件检测的实时系统可在临床镇静场景下以约 0.83 的 F1 检测呼吸事件并逐次输出呼吸率，且已获 FDA 510(k)  clearance。对声学生理监测方向，其流式重叠窗 + 事件级后处理范式有参考价值；工业上展示了医疗音频设备从算法到认证的完整落地路径。

## ⚠️ 局限与未解决问题

作为系统描述论文，缺少与基线方法的定量对比和消融实验，无法判断主动降噪与后处理各自贡献；仅在自建 HF_Tracheal_V2 上评估，跨机构、跨设备泛化未知；未报告呼吸率误差指标、推理延迟与功耗；受试者均处于镇静状态，清醒或运动场景适用性未验证。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：6.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-28/">← 返回 2026-10-28 速递</a></div>
