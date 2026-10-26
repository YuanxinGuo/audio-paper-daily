---
title: "语音/音频论文速递 2026-10-26"
date: 2026-10-26T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 7 篇 · 最高分 8.8（#目标说话人提取）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">7</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.8</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #目标说话人提取 | 3篇 | `██████████` |
| #语音增强 | 2篇 | `███████` |
| #语音对话系统 | 2篇 | `███████` |
| #双耳音频 | 1篇 | `███` |
| #声学模拟 | 1篇 | `███` |
| #声学事件定位 | 1篇 | `███` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="noisy-target-training-meets-drifting-for-weakly-supervised-s-2610-32870/">Noisy Target Training Meets Drifting for Weakly-Supervised Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">8.3</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">在NyTT框架上加入Sinkhorn drifting损失，用无配对干净语音约束增强输出分布，减少残留噪声。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="icassp-2026-radar-acoustic-speech-enhancement-rase-challenge-2610-32202/">ICASSP 2026 Radar Acoustic Speech Enhancement (RASE) Challenge</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">ICASSP 2026 首届毫米波雷达振动测声语音增强挑战赛，发布配对数据集、基线系统与 Codabench 评测框架。</div>
</div></div>

### #目标说话人提取

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="efficient-streaming-audio-visual-target-speaker-extraction-f-2610-32749/">Efficient Streaming Audio-Visual Target Speaker Extraction for Real-World Acoustic Scenes</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">提出 RealSSA 真实场景音视频目标说话人提取基准与 Falcon 因果轻量方法，单次编解码多尺度分离，参数量降 91.9%。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="nectar-automatic-negative-clue-estimation-via-centroid-space-2610-32133/">NECTAR: Automatic Negative Clue Estimation via Centroid-Space Mapping for Target Speaker Extraction</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">利用混合语音质心位于各说话人质心中点的性质，自动估计干扰说话人负线索用于目标说话人提取。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="mg-repa-multi-granularity-representation-alignment-for-gener-2610-32161/">MG-REPA: Multi-Granularity Representation Alignment for Generative Target Speaker Extraction</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">提出多粒度表征对齐 MG-REPA，用帧级 SSL 与句级说话人验证模型双分支对齐，加速生成式目标说话人提取训练收敛。</div>
</div></div>

### #语音分离

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="supervised-source-separation-of-electric-vehicle-interior-no-2610-32310/">Supervised Source Separation of Electric Vehicle Interior Noise Using a Hybrid Transformer Architecture</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#声学模拟</span>
</div>
<div class="card-tldr">将电动车内噪声分解为四类源贡献，用混合Transformer做有监督双耳分离，并以工况信息条件化、物理参数化生成器合成训练数据。</div>
</div></div>

### #双耳音频

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="semac-spherical-energy-matching-ambisonics-codec-for-efficie-2610-32981/">SEMAC: Spherical Energy Matching Ambisonics Codec for Efficient Higher-Order Ambisonics Compression</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">用低阶传输通道加全阶方向能量包络重建高阶Ambisonics，在512/768 kbit/s下MUSHRA优于Opus CMF-3。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="supervised-source-separation-of-electric-vehicle-interior-no-2610-32310/">Supervised Source Separation of Electric Vehicle Interior Noise Using a Hybrid Transformer Architecture</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#声学模拟</span>
</div>
<div class="card-tldr">将电动车内噪声分解为四类源贡献，用混合Transformer做有监督双耳分离，并以工况信息条件化、物理参数化生成器合成训练数据。</div>
</div></div>

### #乐器分离

<p class="empty-hint">今日无新论文命中，推荐回顾该方向的经典工作：</p>
<div class="paper-card paper-card-classic">
<div class="card-rank">📚</div>
<div class="card-body">
<a class="card-title" href="https://archives.ismir.net/ismir2017/paper/000171.pdf" target="_blank" rel="noopener">Singing Voice Separation with Deep U-Net Convolutional Networks</a> <span class="classic-badge">经典</span>
<div class="card-meta">
<span class="card-venue">ISMIR 2017</span>
<span class="tag-pill tag-pill-soft">#乐器分离</span>
</div>
<div class="card-tldr">Spotify 的 U-Net 人声分离，奠定频域 MSS 主流框架。</div>
<div class="card-authors">Andreas Jansson, Eric Humphrey, Nicola Montecchio, et al.</div>
</div></div>
<div class="paper-card paper-card-classic">
<div class="card-rank">📚</div>
<div class="card-body">
<a class="card-title" href="https://arxiv.org/abs/1906.04032" target="_blank" rel="noopener">Open-Unmix - A Reference Implementation for Music Source Separation</a> <span class="classic-badge">经典</span>
<div class="card-meta">
<span class="card-venue">JOSS 2019</span>
<span class="tag-pill tag-pill-soft">#乐器分离</span>
</div>
<div class="card-tldr">MUSDB18 上最常被引的开源基线，BLSTM 频域分离的「教科书」实现。</div>
<div class="card-authors">Fabian-Robert Stöter, Stefan Uhlich, Antoine Liutkus, Yuki Mitsufuji</div>
</div></div>

## 📊 完整排行榜

| 排名 | 论文 | 评分 | 主任务 |
| --- | --- | --- | --- |
| 🥇 | [Efficient Streaming Audio-Visual Target Speaker Extraction f…](efficient-streaming-audio-visual-target-speaker-extraction-f-2610-32749/) 🎯 | **8.8** | #目标说话人提取 |
| 🥈 | [SEMAC: Spherical Energy Matching Ambisonics Codec for Effici…](semac-spherical-energy-matching-ambisonics-codec-for-efficie-2610-32981/) 🎯 | **8.8** | #双耳音频 |
| 🥉 | [NECTAR: Automatic Negative Clue Estimation via Centroid-Spac…](nectar-automatic-negative-clue-estimation-via-centroid-space-2610-32133/) 🎯 | **8.8** | #目标说话人提取 |
| 4. | [Noisy Target Training Meets Drifting for Weakly-Supervised S…](noisy-target-training-meets-drifting-for-weakly-supervised-s-2610-32870/) 🎯 | **8.3** | #语音增强 |
| 5. | [MG-REPA: Multi-Granularity Representation Alignment for Gene…](mg-repa-multi-granularity-representation-alignment-for-gener-2610-32161/) 🎯 | **8.2** | #目标说话人提取 |
| 6. | [Why Full-Duplex Speech Models Collapse in Long Conversations](why-full-duplex-speech-models-collapse-in-long-conversations-2610-32349/) | **7.8** | #语音对话系统 |
| 7. | [Supervised Source Separation of Electric Vehicle Interior No…](supervised-source-separation-of-electric-vehicle-interior-no-2610-32310/) 🎯 | **7.8** | #声学模拟 |
| 8. | [ICASSP 2026 Radar Acoustic Speech Enhancement (RASE) Challen…](icassp-2026-radar-acoustic-speech-enhancement-rase-challenge-2610-32202/) 🎯 | **7.8** | #语音增强 |
| 9. | [Sounding Surgical Instrument Localisation through Audio-Visu…](sounding-surgical-instrument-localisation-through-audio-visu-2610-32816/) | **6.5** | #声学事件定位 |
| 10. | [CounselPlex: A Stressor-Aware Full-Duplex Counseling Model](counselplex-a-stressor-aware-full-duplex-counseling-model-2610-32702/) | **6.0** | #语音对话系统 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="efficient-streaming-audio-visual-target-speaker-extraction-f-2610-32749/">Efficient Streaming Audio-Visual Target Speaker Extraction for Real-World Acoustic Scenes</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#目标说话人提取</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出 RealSSA 真实场景音视频目标说话人提取基准与 Falcon 因果轻量方法，单次编解码多尺度分离，参数量降 91.9%。</div>
<div class="card-action">
<a href="efficient-streaming-audio-visual-target-speaker-extraction-f-2610-32749/">详情 →</a> · <a href="https://arxiv.org/abs/2610.32749" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="semac-spherical-energy-matching-ambisonics-codec-for-efficie-2610-32981/">SEMAC: Spherical Energy Matching Ambisonics Codec for Efficient Higher-Order Ambisonics Compression</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用低阶传输通道加全阶方向能量包络重建高阶Ambisonics，在512/768 kbit/s下MUSHRA优于Opus CMF-3。</div>
<div class="card-action">
<a href="semac-spherical-energy-matching-ambisonics-codec-for-efficie-2610-32981/">详情 →</a> · <a href="https://arxiv.org/abs/2610.32981" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="nectar-automatic-negative-clue-estimation-via-centroid-space-2610-32133/">NECTAR: Automatic Negative Clue Estimation via Centroid-Space Mapping for Target Speaker Extraction</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#目标说话人提取</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">利用混合语音质心位于各说话人质心中点的性质，自动估计干扰说话人负线索用于目标说话人提取。</div>
<div class="card-action">
<a href="nectar-automatic-negative-clue-estimation-via-centroid-space-2610-32133/">详情 →</a> · <a href="https://arxiv.org/abs/2610.32133" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="noisy-target-training-meets-drifting-for-weakly-supervised-s-2610-32870/">Noisy Target Training Meets Drifting for Weakly-Supervised Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.3</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">在NyTT框架上加入Sinkhorn drifting损失，用无配对干净语音约束增强输出分布，减少残留噪声。</div>
<div class="card-action">
<a href="noisy-target-training-meets-drifting-for-weakly-supervised-s-2610-32870/">详情 →</a> · <a href="https://arxiv.org/abs/2610.32870" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="mg-repa-multi-granularity-representation-alignment-for-gener-2610-32161/">MG-REPA: Multi-Granularity Representation Alignment for Generative Target Speaker Extraction</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#目标说话人提取</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出多粒度表征对齐 MG-REPA，用帧级 SSL 与句级说话人验证模型双分支对齐，加速生成式目标说话人提取训练收敛。</div>
<div class="card-action">
<a href="mg-repa-multi-granularity-representation-alignment-for-gener-2610-32161/">详情 →</a> · <a href="https://arxiv.org/abs/2610.32161" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="why-full-duplex-speech-models-collapse-in-long-conversations-2610-32349/">Why Full-Duplex Speech Models Collapse in Long Conversations</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音对话系统</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出FD-LHB长时程全双工对话基准，诊断滑动窗口模型崩溃机制并给出免训练修复。</div>
<div class="card-action">
<a href="why-full-duplex-speech-models-collapse-in-long-conversations-2610-32349/">详情 →</a> · <a href="https://arxiv.org/abs/2610.32349" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="supervised-source-separation-of-electric-vehicle-interior-no-2610-32310/">Supervised Source Separation of Electric Vehicle Interior Noise Using a Hybrid Transformer Architecture</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#声学模拟</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">将电动车内噪声分解为四类源贡献，用混合Transformer做有监督双耳分离，并以工况信息条件化、物理参数化生成器合成训练数据。</div>
<div class="card-action">
<a href="supervised-source-separation-of-electric-vehicle-interior-no-2610-32310/">详情 →</a> · <a href="https://arxiv.org/abs/2610.32310" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="icassp-2026-radar-acoustic-speech-enhancement-rase-challenge-2610-32202/">ICASSP 2026 Radar Acoustic Speech Enhancement (RASE) Challenge</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">ICASSP 2026 首届毫米波雷达振动测声语音增强挑战赛，发布配对数据集、基线系统与 Codabench 评测框架。</div>
<div class="card-action">
<a href="icassp-2026-radar-acoustic-speech-enhancement-rase-challenge-2610-32202/">详情 →</a> · <a href="https://arxiv.org/abs/2610.32202" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="sounding-surgical-instrument-localisation-through-audio-visu-2610-32816/">Sounding Surgical Instrument Localisation through Audio-Visual Correspondence</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#声学事件定位</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">用单麦克风与相机学习手术器械外观与声音的对应关系，弱监督生成发声器械热力图。</div>
<div class="card-action">
<a href="sounding-surgical-instrument-localisation-through-audio-visu-2610-32816/">详情 →</a> · <a href="https://arxiv.org/abs/2610.32816" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="counselplex-a-stressor-aware-full-duplex-counseling-model-2610-32702/">CounselPlex: A Stressor-Aware Full-Duplex Counseling Model</a>
<div class="card-meta">
<span class="card-score">6.0</span>
<span class="tag-pill">#语音对话系统</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">提出 CounselPlex 全双工心理咨询框架，用压力源状态更新与注入缓解模型只关注最新话语的 Stressor Blindness 问题。</div>
<div class="card-action">
<a href="counselplex-a-stressor-aware-full-duplex-counseling-model-2610-32702/">详情 →</a> · <a href="https://arxiv.org/abs/2610.32702" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
