---
title: "语音/音频论文速递 2026-11-09"
date: 2026-11-09T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 3 篇 · 最高分 8.2（#乐器分离）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">3</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.2</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #乐器分离 | 1篇 | `██████████` |
| #语音分离 | 1篇 | `██████████` |
| #目标说话人提取 | 1篇 | `██████████` |
| #声学事件检测与定位 | 1篇 | `██████████` |
| #语音表征学习 | 1篇 | `██████████` |
| #情感识别 | 1篇 | `██████████` |
| #异常声音检测 | 1篇 | `██████████` |
| #声学场景分类 | 1篇 | `██████████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<p class="empty-hint">今日无新论文命中，推荐回顾该方向的经典工作：</p>
<div class="paper-card paper-card-classic">
<div class="card-rank">📚</div>
<div class="card-body">
<a class="card-title" href="https://ieeexplore.ieee.org/document/6932438" target="_blank" rel="noopener">A Regression Approach to Speech Enhancement Based on Deep Neural Networks</a> <span class="classic-badge">经典</span>
<div class="card-meta">
<span class="card-venue">TASLP 2015</span>
<span class="tag-pill tag-pill-soft">#语音增强</span>
</div>
<div class="card-tldr">首次系统验证 DNN 直接回归对数功率谱的语音增强范式，奠定后续大量 mask / mapping 方法的基础。</div>
<div class="card-authors">Yong Xu, Jun Du, Li-Rong Dai, Chin-Hui Lee</div>
</div></div>
<div class="paper-card paper-card-classic">
<div class="card-rank">📚</div>
<div class="card-body">
<a class="card-title" href="https://arxiv.org/abs/1809.07454" target="_blank" rel="noopener">Conv-TasNet: Surpassing Ideal Time-Frequency Magnitude Masking</a> <span class="classic-badge">经典</span>
<div class="card-meta">
<span class="card-venue">TASLP 2019</span>
<span class="tag-pill tag-pill-soft">#语音增强</span>
</div>
<div class="card-tldr">时域端到端分离/增强里程碑，证明 1D 卷积可超越 STFT 域 IRM/IBM 上限。</div>
<div class="card-authors">Yi Luo, Nima Mesgarani</div>
</div></div>

### #目标说话人提取

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="aishell8-fisheye-a-fisheye-audio-visual-dataset-for-target-s-2611-09368/">AISHELL8-FISHEYE: A Fisheye Audio-Visual Dataset for Target Speaker Extraction with Distortion-Aware Baselines</a>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">发布47小时中文鱼眼音视频数据集AISHELL8-FISHEYE，并提出融合畸变感知分支的音视频目标说话人提取基线。</div>
</div></div>

### #语音分离

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="gtcrn-ss-lightweight-causal-speech-separation-with-residual--2611-09358/">GTCRN-SS: Lightweight Causal Speech Separation with Residual Allocation and Reconstruction Refinement</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">将轻量GTCRN增强骨干改造为两阶段因果语音分离器，用残差分配与重建条件精炼，参数量不足百万即在Libri2Mix取得10.1 dB SDRi。</div>
</div></div>

### #双耳音频

<p class="empty-hint">今日无新论文命中，推荐回顾该方向的经典工作：</p>
<div class="paper-card paper-card-classic">
<div class="card-rank">📚</div>
<div class="card-body">
<a class="card-title" href="https://arxiv.org/abs/2111.10882" target="_blank" rel="noopener">Binaural Audio Generation via Multi-task Learning</a> <span class="classic-badge">经典</span>
<div class="card-meta">
<span class="card-venue">ACM TOG 2021</span>
<span class="tag-pill tag-pill-soft">#双耳音频</span>
</div>
<div class="card-tldr">联合 mono-to-binaural 与几何信息预测，提升合成空间感。</div>
<div class="card-authors">Sijia Li, Sagar Vaze, et al.</div>
</div></div>
<div class="paper-card paper-card-classic">
<div class="card-rank">📚</div>
<div class="card-body">
<a class="card-title" href="https://arxiv.org/abs/1812.04204" target="_blank" rel="noopener">2.5D Visual Sound</a> <span class="classic-badge">经典</span>
<div class="card-meta">
<span class="card-venue">CVPR 2019</span>
<span class="tag-pill tag-pill-soft">#双耳音频</span>
</div>
<div class="card-tldr">用单视频引导 mono → binaural，视听双耳音频合成开创性工作。</div>
<div class="card-authors">Ruohan Gao, Kristen Grauman</div>
</div></div>

### #乐器分离

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="spdmx-large-scale-open-stem-audio-from-symbolic-music-2611-09140/">SPDMX: Large-Scale Open Stem Audio From Symbolic Music</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#乐器分离</span>
</div>
<div class="card-tldr">将公有领域 PDMX 乐谱渲染成大规模开放许可多轨 stem 语料，含 25.4 万首歌、54.7 万条单声道 stem。</div>
</div></div>

## 📊 完整排行榜

| 排名 | 论文 | 评分 | 主任务 |
| --- | --- | --- | --- |
| 🥇 | [SPDMX: Large-Scale Open Stem Audio From Symbolic Music](spdmx-large-scale-open-stem-audio-from-symbolic-music-2611-09140/) 🎯 | **8.2** | #乐器分离 |
| 🥈 | [GTCRN-SS: Lightweight Causal Speech Separation with Residual…](gtcrn-ss-lightweight-causal-speech-separation-with-residual--2611-09358/) 🎯 | **8.2** | #语音分离 |
| 🥉 | [AISHELL8-FISHEYE: A Fisheye Audio-Visual Dataset for Target …](aishell8-fisheye-a-fisheye-audio-visual-dataset-for-target-s-2611-09368/) 🎯 | **8.0** | #目标说话人提取 |
| 4. | [AudioSphere: Towards Self-Supervised Spatial Audio Represent…](audiosphere-towards-self-supervised-spatial-audio-representa-2611-09275/) | **7.8** | #声学事件检测与定位 |
| 5. | [Asymmetric Correspondence Learning for Lexical and Style Emb…](asymmetric-correspondence-learning-for-lexical-and-style-emb-2611-09313/) | **6.8** | #语音表征学习 |
| 6. | [Mind the Divergence: Divergence-Guided Reliability-Aware Fus…](mind-the-divergence-divergence-guided-reliability-aware-fusi-2611-08860/) | **6.8** | #情感识别 |
| 7. | [AnomSep: Bridging Optimization-Based Separation and Deep Neu…](anomsep-bridging-optimization-based-separation-and-deep-neur-2611-09279/) | **6.8** | #异常声音检测 |
| 8. | [SAS: Scene-Annotated AudioSet Strong for Joint Scene-Event A…](sas-scene-annotated-audioset-strong-for-joint-scene-event-an-2611-09199/) | **6.8** | #声学场景分类 |
| 9. | [LEMMO: A Large Electromagnetic Model leveraging Pretrained L…](lemmo-a-large-electromagnetic-model-leveraging-pretrained-ll-2611-09476/) | **6.0** | #电磁信号理解 |
| 10. | [AUTEUR: Acoustic Plan Learning for Red-Teaming Text-to-Audio…](auteur-acoustic-plan-learning-for-red-teaming-text-to-audio--2611-09351/) | **5.8** | #音频生成 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="spdmx-large-scale-open-stem-audio-from-symbolic-music-2611-09140/">SPDMX: Large-Scale Open Stem Audio From Symbolic Music</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#乐器分离</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">将公有领域 PDMX 乐谱渲染成大规模开放许可多轨 stem 语料，含 25.4 万首歌、54.7 万条单声道 stem。</div>
<div class="card-action">
<a href="spdmx-large-scale-open-stem-audio-from-symbolic-music-2611-09140/">详情 →</a> · <a href="https://arxiv.org/abs/2611.09140" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="gtcrn-ss-lightweight-causal-speech-separation-with-residual--2611-09358/">GTCRN-SS: Lightweight Causal Speech Separation with Residual Allocation and Reconstruction Refinement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音分离</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">将轻量GTCRN增强骨干改造为两阶段因果语音分离器，用残差分配与重建条件精炼，参数量不足百万即在Libri2Mix取得10.1 dB SDRi。</div>
<div class="card-action">
<a href="gtcrn-ss-lightweight-causal-speech-separation-with-residual--2611-09358/">详情 →</a> · <a href="https://arxiv.org/abs/2611.09358" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="aishell8-fisheye-a-fisheye-audio-visual-dataset-for-target-s-2611-09368/">AISHELL8-FISHEYE: A Fisheye Audio-Visual Dataset for Target Speaker Extraction with Distortion-Aware Baselines</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#目标说话人提取</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">发布47小时中文鱼眼音视频数据集AISHELL8-FISHEYE，并提出融合畸变感知分支的音视频目标说话人提取基线。</div>
<div class="card-action">
<a href="aishell8-fisheye-a-fisheye-audio-visual-dataset-for-target-s-2611-09368/">详情 →</a> · <a href="https://arxiv.org/abs/2611.09368" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="audiosphere-towards-self-supervised-spatial-audio-representa-2611-09275/">AudioSphere: Towards Self-Supervised Spatial Audio Representation Models</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#声学事件检测与定位</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出多通道掩码自编码器AudioSphere，用时空联合掩码同时重建频谱与强度矢量，实现冻结骨干的帧级SELD。</div>
<div class="card-action">
<a href="audiosphere-towards-self-supervised-spatial-audio-representa-2611-09275/">详情 →</a> · <a href="https://arxiv.org/abs/2611.09275" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="asymmetric-correspondence-learning-for-lexical-and-style-emb-2611-09313/">Asymmetric Correspondence Learning for Lexical and Style Embeddings: Interpreting Latent Space via Acoustic Features</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音表征学习</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出非对称对应学习ACL，将HuBERT特征蒸馏为词汇与风格两个隐空间，并用eGeMAPS特征重要性解释其拓扑结构。</div>
<div class="card-action">
<a href="asymmetric-correspondence-learning-for-lexical-and-style-emb-2611-09313/">详情 →</a> · <a href="https://arxiv.org/abs/2611.09313" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="mind-the-divergence-divergence-guided-reliability-aware-fusi-2611-08860/">Mind the Divergence: Divergence-Guided Reliability-Aware Fusion and Adaptive LLM Prompting for Conversational Emotion Recognition</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#情感识别</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">用单模态预测分布间的归一化散度量化模态分歧，指导门控、可靠性加权与自适应LLM提示，提升对话情感识别。</div>
<div class="card-action">
<a href="mind-the-divergence-divergence-guided-reliability-aware-fusi-2611-08860/">详情 →</a> · <a href="https://arxiv.org/abs/2611.08860" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="anomsep-bridging-optimization-based-separation-and-deep-neur-2611-09279/">AnomSep: Bridging Optimization-Based Separation and Deep Neural Refinement for Anomaly Detection with Listenable Explanations</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#异常声音检测</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">用优化分离加深度潜空间精修，把异常声分离出来作为可听解释，能量作异常分数。</div>
<div class="card-action">
<a href="anomsep-bridging-optimization-based-separation-and-deep-neur-2611-09279/">详情 →</a> · <a href="https://arxiv.org/abs/2611.09279" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="sas-scene-annotated-audioset-strong-for-joint-scene-event-an-2611-09199/">SAS: Scene-Annotated AudioSet Strong for Joint Scene-Event Analysis</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#声学场景分类</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">为 AudioSet Strong 增加片段级场景标注，构建场景-事件联合数据集，并分析场景特异性事件对场景表征的作用。</div>
<div class="card-action">
<a href="sas-scene-annotated-audioset-strong-for-joint-scene-event-an-2611-09199/">详情 →</a> · <a href="https://arxiv.org/abs/2611.09199" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="lemmo-a-large-electromagnetic-model-leveraging-pretrained-ll-2611-09476/">LEMMO: A Large Electromagnetic Model leveraging Pretrained LLMs for Million-Sample Signal Understanding</a>
<div class="card-meta">
<span class="card-score">6.0</span>
<span class="tag-pill">#电磁信号理解</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">构建面向长原始IQ电磁信号的大模型LEMMO，用线性注意力编码器加抗混叠重采样处理八百万复数样本，并发布1.38TB语料。</div>
<div class="card-action">
<a href="lemmo-a-large-electromagnetic-model-leveraging-pretrained-ll-2611-09476/">详情 →</a> · <a href="https://arxiv.org/abs/2611.09476" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="auteur-acoustic-plan-learning-for-red-teaming-text-to-audio--2611-09351/">AUTEUR: Acoustic Plan Learning for Red-Teaming Text-to-Audio Models</a>
<div class="card-meta">
<span class="card-score">5.8</span>
<span class="tag-pill">#音频生成</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">用结构化声学计划（前景声/上下文/人声属性）做文本到音频模型的红队测试，通过波形反馈的强化学习迭代改写提示词。</div>
<div class="card-action">
<a href="auteur-acoustic-plan-learning-for-red-teaming-text-to-audio--2611-09351/">详情 →</a> · <a href="https://arxiv.org/abs/2611.09351" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
