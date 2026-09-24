---
title: "Neural Field-of-View for Binaural Signal Matching with Wearable Microphone Arrays"
date: 2026-09-24T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#双耳音频"]
summary: "用CRNN从可穿戴阵列信号端到端学习FoV参数，替代显式声源定位，改善高DRR下的双耳信号匹配质量。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#双耳音频</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#双耳音频</span> <span class="tag-pill tag-pill-soft">#麦克风阵列</span> <span class="tag-pill tag-pill-soft">#空间音频</span> <span class="tag-pill tag-pill-soft">#语音增强</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.28343</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-24</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.28343" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.28343" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用CRNN从可穿戴阵列信号端到端学习FoV参数，替代显式声源定位，改善高DRR下的双耳信号匹配质量。
</div>

## 👥 作者与机构

**Matan Yifrach** ¹ · Boaz Rafaely

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做双耳渲染、可穿戴阵列空间音频的研究者与工程团队阅读。建议通读，重点看 §3 的 FoV-BSM-Net 网络结构与 FoV 参数化方式，以及 §4 中随 DRR 变化的 NMSE / 双耳线索误差曲线和感知评测表。若只关心结论，可先看结果图与消融。

## 🌍 研究背景

可穿戴麦克风阵列的双耳复现是 AR/VR 空间音频的关键。BSM 在扩散场假设下表现良好，但在高 DRR（直达声主导）时明显退化。已有工作引入 FoV 加权，或用固定孔径，或依赖显式声源定位，前者空间覆盖粗糙，后者受定位误差拖累。本文要解决的是：如何在不做显式声源估计的前提下，自适应地确定 FoV，从而在高 DRR 下稳定提升双耳匹配精度。

## 💡 核心创新

1. 提出信号相关的 FoV-BSM 形式，FoV 参数由网络预测而非固定
2. 用 CRNN 从多通道麦克风信号端到端学习 FoV 参数，免显式定位
3. 在仿真房间中验证增益随 DRR 增大而扩大，并给出感知评测支持

## 🏗️ 模型架构

输入为可穿戴阵列的多通道时域/频域麦克风信号，主干为卷积循环神经网络（CRNN）：卷积层提取局部空间-频谱特征，循环层建模时间依赖，输出层回归信号相关的 FoV 参数（如角度范围/加权系数）。这些参数随后代入 FoV-BSM 的匹配滤波器求解框架，生成双耳左右耳信号。整体为端到端可训练，损失作用于双耳 NMSE 与双耳线索误差。摘要未给出参数量与具体层数。

## 📚 数据集

- 仿真房间数据集（训练与评估，含不同混响条件与 DRR 设置）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 双耳 NMSE | 仿真房间（不同 DRR） | BSM 与固定 FoV-BSM | **FoV-BSM-Net** | 随 DRR 增大而增益扩大（摘要未给具体数值） |
| 双耳线索误差（interaural cue errors） | 仿真房间（不同 DRR） | BSM 与固定 FoV-BSM | **FoV-BSM-Net** | 随 DRR 增大而增益扩大（摘要未给具体数值） |

摘要仅给出定性结论：FoV-BSM-Net 在双耳 NMSE 与双耳线索误差上一致优于 BSM，且增益随 DRR 升高而增大；感知评测显示在低 DRR 与高 DRR 条件下均明显优于 BSM 与固定 FoV-BSM 两个基线。未报告具体数值、消融实验、推理延迟或跨房间泛化结果。

## 🎯 结论与影响

最强结论是：用 CRNN 端到端学习 FoV 参数可免去显式声源定位，并在高 DRR 下显著优于 BSM 与固定 FoV 基线。这为可穿戴阵列双耳渲染提供了数据驱动的 FoV 建模范式，后续可探索与定位/波束成形联合优化。工业上对 AR/VR 耳机与智能眼镜的空间音频管线有直接参考价值。

## ⚠️ 局限与未解决问题

实验全部基于仿真房间，缺少真实录音验证，存在仿真到现实差距；未报告模型参数量、推理延迟与实时性；未与基于显式定位的 FoV-BSM 做直接对比；感知评测细节（听者数、MOS 类型）摘要未交代；缺少对 CRNN 结构选择的消融。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-24/">← 返回 2026-09-24 速递</a></div>
