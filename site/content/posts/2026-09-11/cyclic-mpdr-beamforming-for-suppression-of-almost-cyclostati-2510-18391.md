---
title: "Cyclic MPDR Beamforming for Suppression of Almost-Cyclostationary Acoustic Interference"
date: 2026-09-11T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出循环MPDR波束成形，利用近周期噪声在谐波频率间的谱相关性，联合空域与频域抑制发动机/风扇类干扰。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#波束成形</span> <span class="tag-pill tag-pill-soft">#循环平稳信号处理</span> <span class="tag-pill tag-pill-soft">#FRESH滤波</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2510.18391</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-11</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/Screeen/cMPDR" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">Screeen/cMPDR</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2510.18391" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2510.18391" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/Screeen/cMPDR" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出循环MPDR波束成形，利用近周期噪声在谐波频率间的谱相关性，联合空域与频域抑制发动机/风扇类干扰。
</div>

## 👥 作者与机构

**Giovanni Bologni** ¹ · Martin Bo M{\o}ller · Richard Heusdens · Richard C. Hendriks

**机构**：代尔夫特理工大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做波束成形、阵列处理与噪声抑制的研究者与工程人员。建议通读：先看 §2 的 ACS 信号建模与 FRESH 频移滤波推导，再看 §3 的 cMPDR 闭式解与单调性证明，最后重点核对表 1/2 的 SI-SDR 与 STOI 对比及单麦克风实验。

## 🌍 研究背景

传统声学波束成形（如 MPDR/MVDR）假设短时平稳、逐频点独立处理，忽略频间相关性。对发动机、风扇、乐器等近周期噪声，其谐波分量在频域强相关，逐频点处理会残留大量相干噪声。已有 FRESH 滤波在通信中利用循环平稳性，但尚未与空间波束成形联合用于声学干扰抑制。本文要解决的核心问题是：如何在存在非谐性（partials 偏离整数倍基频）时，联合空域与谱域相关性进一步压低残余噪声。

## 💡 核心创新

1. 将 MPDR 扩展为 cMPDR，联合利用空间与谱相关协方差
2. 基于 FRESH 频移滤波构造循环分量约束
3. 用周期图估计共振频率、由成对间距导出频移以应对非谐性
4. 给出残余噪声闭式解并证明输出功率随循环分量数单调下降

## 🏗️ 模型架构

输入为多通道（或单通道）时域信号，经 STFT 得到频域表示。核心是构造扩展的频移观测向量：对每个频点 k，引入由周期图估计的共振频率成对间距导出的频移集合，将谐波相关频点堆叠。随后在该扩展空间上求解 cMPDR 权重，即在无失真约束下最小化输出功率，等价于对扩展协方差矩阵做 MVDR 型求解。输出为滤波后单通道增强语音。摘要未给出参数量，方法为解析闭式解，无训练参数。

## 📚 数据集

- 合成谐波噪声（评估，低 SNR 场景）
- 真实 UAV 电机录音（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SI-SDR | 合成谐波噪声 / UAV 电机录音（低 SNR） | MPDR | **cMPDR** | +5 dB |

摘要报告：低 SNR 下 cMPDR 相对 MPDR 的 SI-SDR 提升最高达 5 dB，STOI 有一致增益；单麦克风条件下仍有效；当谱相关性不存在时退化为常规 MPDR 且性能不下降。理论部分给出残余噪声闭式表达并证明输出功率随循环分量数单调递减。摘要未提供 PESQ、WER 或推理延迟等指标，也未列出完整消融表。

## 🎯 结论与影响

最强结论是：对近周期声学干扰，联合空域与谱域循环平稳建模可带来最高 5 dB SI-SDR 增益，且无谱相关时无退化。这为波束成形开辟了循环处理方向，后续可探索更多 ACS 干扰类型与自适应频移估计。工业上对 UAV、风扇、发动机等场景的麦克风阵列降噪有直接参考价值，单麦可用性也利于嵌入式部署。

## ⚠️ 局限与未解决问题

实验仅限合成谐波噪声与 UAV 电机录音，缺少与深度学习方法（如 DNN 后滤波、SEPFormer 类）的对比；未报告推理延迟与计算复杂度；非谐性下周期图估计共振频率的鲁棒性、频移集合选择对性能的敏感性均未见消融；真实场景混响与多干扰源情形未验证。

## 🔗 开源资源

- **代码**：<https://github.com/Screeen/cMPDR>

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-11/">← 返回 2026-09-11 速递</a></div>
