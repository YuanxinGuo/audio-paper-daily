---
title: "语音/音频论文速递 2026-10-27"
date: 2026-10-27T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 6 篇 · 最高分 8.8（#双耳音频）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">6</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.8</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #双耳音频 | 3篇 | `██████████` |
| #音频处理 | 2篇 | `███████` |
| #生物声学 | 2篇 | `███████` |
| #语音增强 | 1篇 | `███` |
| #音频伪造检测 | 1篇 | `███` |
| #音频生成评估 | 1篇 | `███` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="timuse-text-initialized-masked-semantic-token-modeling-for-u-2610-34814/">TIMUSE: Text-Initialized Masked Semantic Token Modeling for Universal Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">8.6</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">用文本预训练扩散语言模型经LoRA恢复语义token，再用条件流匹配重建24kHz语音，兼顾感知质量与内容保真。</div>
</div></div>

### #目标说话人提取

<p class="empty-hint">今日无新论文命中，推荐回顾该方向的经典工作：</p>
<div class="paper-card paper-card-classic">
<div class="card-rank">📚</div>
<div class="card-body">
<a class="card-title" href="https://arxiv.org/abs/1810.04826" target="_blank" rel="noopener">VoiceFilter: Targeted Voice Separation by Speaker-Conditioned Spectrogram Masking</a> <span class="classic-badge">经典</span>
<div class="card-meta">
<span class="card-venue">Interspeech 2019</span>
<span class="tag-pill tag-pill-soft">#目标说话人提取</span>
</div>
<div class="card-tldr">基于 d-vector 条件化的时频域目标说话人提取代表作，TSE 领域绕不开的基线。</div>
<div class="card-authors">Quan Wang, Hannah Muckenhirn, Kevin Wilson, et al.</div>
</div></div>
<div class="paper-card paper-card-classic">
<div class="card-rank">📚</div>
<div class="card-body">
<a class="card-title" href="https://arxiv.org/abs/2005.04686" target="_blank" rel="noopener">SpEx+: A Complete Time Domain Speaker Extraction Network</a> <span class="classic-badge">经典</span>
<div class="card-meta">
<span class="card-venue">Interspeech 2020</span>
<span class="tag-pill tag-pill-soft">#目标说话人提取</span>
</div>
<div class="card-tldr">时域 TSE 系列里程碑，多尺度编码器 + 共享说话人编码器，长期占据 SOTA。</div>
<div class="card-authors">Meng Ge, Chenglin Xu, Longbiao Wang, Eng Siong Chng, Jianwu Dang, Haizhou Li</div>
</div></div>

### #语音分离

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="support-guided-ood-removal-with-diffusion-2610-33194/">Support-guided OOD Removal with Diffusion</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#音频处理</span>
</div>
<div class="card-tldr">用扩散先验加损坏支撑掩码，迭代恢复被局部OOD污染的信号，覆盖图像与乐器/语音音频。</div>
</div></div>

### #双耳音频

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="spatial-audio-generation-and-editing-with-executable-plans-a-2610-34415/">Spatial Audio Generation and Editing with Executable Plans and Self-Distilling Transfusion</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">提出AMBIT统一框架，用可执行ScenePlan与Transfusion主干实现原生FOA空间音频生成与编辑。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="graph-neural-network-for-wide-area-6dof-ambisonic-rendering-2610-35741/">Graph Neural Network for Wide-Area 6DoF Ambisonic Rendering</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">用轻量图神经网络替代DirAC几何插值权重，实现稀疏Ambisonics录音的宽区域6DoF空间音频渲染。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="av-qtss-class-query-target-sound-spatialization-in-multi-sou-2610-34401/">AV-QTSS: Class-Query Target Sound Spatialization in Multi-Source 360$^\circ$ Videos</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">给定单声道多源混合、360°视频与类别查询，定位并渲染出目标声源的FOA空间音频。</div>
</div></div>

### #乐器分离

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="support-guided-ood-removal-with-diffusion-2610-33194/">Support-guided OOD Removal with Diffusion</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#音频处理</span>
</div>
<div class="card-tldr">用扩散先验加损坏支撑掩码，迭代恢复被局部OOD污染的信号，覆盖图像与乐器/语音音频。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="multimodal-concert-video-editing-system-design-and-explorato-2610-35816/">Multimodal Concert Video Editing: System Design and Exploratory Evaluation</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频处理</span>
</div>
<div class="card-tldr">提出模块化多机位音乐会视频剪辑框架，融合乐器活动、可见乐器、图像清晰度与节拍时序做概率化选镜。</div>
</div></div>

## 📊 完整排行榜

| 排名 | 论文 | 评分 | 主任务 |
| --- | --- | --- | --- |
| 🥇 | [Spatial Audio Generation and Editing with Executable Plans a…](spatial-audio-generation-and-editing-with-executable-plans-a-2610-34415/) 🎯 | **8.8** | #双耳音频 |
| 🥈 | [TIMUSE: Text-Initialized Masked Semantic Token Modeling for …](timuse-text-initialized-masked-semantic-token-modeling-for-u-2610-34814/) 🎯 | **8.6** | #语音增强 |
| 🥉 | [Support-guided OOD Removal with Diffusion](support-guided-ood-removal-with-diffusion-2610-33194/) 🎯 | **8.2** | #音频处理 |
| 4. | [Graph Neural Network for Wide-Area 6DoF Ambisonic Rendering](graph-neural-network-for-wide-area-6dof-ambisonic-rendering-2610-35741/) 🎯 | **8.2** | #双耳音频 |
| 5. | [AV-QTSS: Class-Query Target Sound Spatialization in Multi-So…](av-qtss-class-query-target-sound-spatialization-in-multi-sou-2610-34401/) 🎯 | **8.2** | #双耳音频 |
| 6. | [Do Compact SSL Backbones Matter for Audio Deepfake Detection…](do-compact-ssl-backbones-matter-for-audio-deepfake-detection-2603-06164/) | **7.2** | #音频伪造检测 |
| 7. | [Multimodal Concert Video Editing: System Design and Explorat…](multimodal-concert-video-editing-system-design-and-explorato-2610-35816/) 🎯 | **6.8** | #音频处理 |
| 8. | [Finite-Sample Sensitivity of Kernel Metrics for Generative E…](finite-sample-sensitivity-of-kernel-metrics-for-generative-e-2610-34477/) | **6.8** | #音频生成评估 |
| 9. | [Structure Across Voices: Comparing acoustic-event type accum…](structure-across-voices-comparing-acoustic-event-type-accumu-2609-16612/) | **5.8** | #生物声学 |
| 10. | [Feature Scaling Beats Architecture Choice in Offline Respira…](feature-scaling-beats-architecture-choice-in-offline-respira-2610-33030/) | **5.8** | #生物声学 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="spatial-audio-generation-and-editing-with-executable-plans-a-2610-34415/">Spatial Audio Generation and Editing with Executable Plans and Self-Distilling Transfusion</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出AMBIT统一框架，用可执行ScenePlan与Transfusion主干实现原生FOA空间音频生成与编辑。</div>
<div class="card-action">
<a href="spatial-audio-generation-and-editing-with-executable-plans-a-2610-34415/">详情 →</a> · <a href="https://arxiv.org/abs/2610.34415" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="timuse-text-initialized-masked-semantic-token-modeling-for-u-2610-34814/">TIMUSE: Text-Initialized Masked Semantic Token Modeling for Universal Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.6</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用文本预训练扩散语言模型经LoRA恢复语义token，再用条件流匹配重建24kHz语音，兼顾感知质量与内容保真。</div>
<div class="card-action">
<a href="timuse-text-initialized-masked-semantic-token-modeling-for-u-2610-34814/">详情 →</a> · <a href="https://arxiv.org/abs/2610.34814" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="support-guided-ood-removal-with-diffusion-2610-33194/">Support-guided OOD Removal with Diffusion</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#音频处理</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用扩散先验加损坏支撑掩码，迭代恢复被局部OOD污染的信号，覆盖图像与乐器/语音音频。</div>
<div class="card-action">
<a href="support-guided-ood-removal-with-diffusion-2610-33194/">详情 →</a> · <a href="https://arxiv.org/abs/2610.33194" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="graph-neural-network-for-wide-area-6dof-ambisonic-rendering-2610-35741/">Graph Neural Network for Wide-Area 6DoF Ambisonic Rendering</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用轻量图神经网络替代DirAC几何插值权重，实现稀疏Ambisonics录音的宽区域6DoF空间音频渲染。</div>
<div class="card-action">
<a href="graph-neural-network-for-wide-area-6dof-ambisonic-rendering-2610-35741/">详情 →</a> · <a href="https://arxiv.org/abs/2610.35741" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="av-qtss-class-query-target-sound-spatialization-in-multi-sou-2610-34401/">AV-QTSS: Class-Query Target Sound Spatialization in Multi-Source 360$^\circ$ Videos</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">给定单声道多源混合、360°视频与类别查询，定位并渲染出目标声源的FOA空间音频。</div>
<div class="card-action">
<a href="av-qtss-class-query-target-sound-spatialization-in-multi-sou-2610-34401/">详情 →</a> · <a href="https://arxiv.org/abs/2610.34401" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="do-compact-ssl-backbones-matter-for-audio-deepfake-detection-2603-06164/">Do Compact SSL Backbones Matter for Audio Deepfake Detection? A Controlled Study with RAPTOR</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音频伪造检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">系统对比紧凑SSL骨干（HuBERT/WavLM）在音频深伪检测中的跨域表现，发现多语言HuBERT预训练比模型规模更关键。</div>
<div class="card-action">
<a href="do-compact-ssl-backbones-matter-for-audio-deepfake-detection-2603-06164/">详情 →</a> · <a href="https://arxiv.org/abs/2603.06164" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="multimodal-concert-video-editing-system-design-and-explorato-2610-35816/">Multimodal Concert Video Editing: System Design and Exploratory Evaluation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频处理</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">提出模块化多机位音乐会视频剪辑框架，融合乐器活动、可见乐器、图像清晰度与节拍时序做概率化选镜。</div>
<div class="card-action">
<a href="multimodal-concert-video-editing-system-design-and-explorato-2610-35816/">详情 →</a> · <a href="https://arxiv.org/abs/2610.35816" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="finite-sample-sensitivity-of-kernel-metrics-for-generative-e-2610-34477/">Finite-Sample Sensitivity of Kernel Metrics for Generative Evaluation</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频生成评估</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">系统分析KID/KAD默认核在小样本下对均值漂移、收缩、旋转三类变化的检测灵敏度，并给出带宽与核函数改进建议。</div>
<div class="card-action">
<a href="finite-sample-sensitivity-of-kernel-metrics-for-generative-e-2610-34477/">详情 →</a> · <a href="https://arxiv.org/abs/2610.34477" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="structure-across-voices-comparing-acoustic-event-type-accumu-2609-16612/">Structure Across Voices: Comparing acoustic-event type accumulation and sequence dependence across four vocal corpora using frozen audio encoders</a>
<div class="card-meta">
<span class="card-score">5.8</span>
<span class="tag-pill">#生物声学</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">用冻结音频编码器与匹配采样，跨抹香鲸、人类语音、孟加拉雀、狨猴四类声库比较声学事件类型累积与序列依赖。</div>
<div class="card-action">
<a href="structure-across-voices-comparing-acoustic-event-type-accumu-2609-16612/">详情 →</a> · <a href="https://arxiv.org/abs/2609.16612" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="feature-scaling-beats-architecture-choice-in-offline-respira-2610-33030/">Feature Scaling Beats Architecture Choice in Offline Respiratory Screening for Low-Resource Clinics</a>
<div class="card-meta">
<span class="card-score">5.8</span>
<span class="tag-pill">#生物声学</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">在1211段五类呼吸音上比较SVM与卷积循环网络，发现特征标准化带来的提升远大于模型架构差异。</div>
<div class="card-action">
<a href="feature-scaling-beats-architecture-choice-in-offline-respira-2610-33030/">详情 →</a> · <a href="https://arxiv.org/abs/2610.33030" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
