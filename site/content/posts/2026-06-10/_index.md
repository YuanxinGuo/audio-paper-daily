---
title: "语音/音频论文速递 2026-06-10"
date: 2026-06-10T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 2 篇 · 最高分 9.2（#目标说话人提取）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">2</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">9.2</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音合成 | 2篇 | `██████████` |
| #目标说话人提取 | 1篇 | `█████` |
| #双耳音频 | 1篇 | `█████` |
| #语音反欺骗 | 1篇 | `█████` |
| #音频深度伪造检测 | 1篇 | `█████` |
| #语音情感识别 | 1篇 | `█████` |
| #多模态大语言模型 | 1篇 | `█████` |
| #生物声学 | 1篇 | `█████` |

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
<a class="card-title" href="memo-attentional-momentum-for-real-time-audio-visual-speaker-2507-15294/">MeMo: Attentional Momentum for Real-time Audio-visual Speaker Extraction under Impaired Visual Conditions</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">提出MeMo框架，通过两个自适应记忆库在视觉线索缺失时维持注意力动量，实现鲁棒的实时视听目标说话人提取。</div>
</div></div>

### #语音分离

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="memo-attentional-momentum-for-real-time-audio-visual-speaker-2507-15294/">MeMo: Attentional Momentum for Real-time Audio-visual Speaker Extraction under Impaired Visual Conditions</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">提出MeMo框架，通过两个自适应记忆库在视觉线索缺失时维持注意力动量，实现鲁棒的实时视听目标说话人提取。</div>
</div></div>

### #双耳音频

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="spatial-omni-spatial-audio-understanding-integration-in-mult-2606-10738/">Spatial-Omni: Spatial Audio Understanding Integration in Multimodal LLMs via FOA Encoding</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">提出Spatial-Omni，通过SO-Encoder将一阶Ambisonics空间音频注入多模态大语言模型，实现空间音频理解，无需修改原音频编码器。</div>
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
| 🥇 | [MeMo: Attentional Momentum for Real-time Audio-visual Speake…](memo-attentional-momentum-for-real-time-audio-visual-speaker-2507-15294/) 🎯 | **9.2** | #目标说话人提取 |
| 🥈 | [Spatial-Omni: Spatial Audio Understanding Integration in Mul…](spatial-omni-spatial-audio-understanding-integration-in-mult-2606-10738/) 🎯 | **9.2** | #双耳音频 |
| 🥉 | [MultiAPI Spoof: A Multi-API Dataset and Local-Attention Netw…](multiapi-spoof-a-multi-api-dataset-and-local-attention-netwo-2512-07352/) | **8.2** | #语音反欺骗 |
| 4. | [Optimality of FSQ Tokens for Continuous Diffusion for Catego…](optimality-of-fsq-tokens-for-continuous-diffusion-for-catego-2606-09962/) | **8.2** | #语音合成 |
| 5. | [OpenBibleTTS: Large-Scale Speech Resources and TTS Models fo…](openbibletts-large-scale-speech-resources-and-tts-models-for-2606-09553/) | **7.8** | #语音合成 |
| 6. | [What Do Deepfake Speech Detectors Actually Hear?](what-do-deepfake-speech-detectors-actually-hear-2606-10912/) | **7.5** | #音频深度伪造检测 |
| 7. | [ERM-MinMaxGAP: Benchmarking and Mitigating Gender Bias in Mu…](erm-minmaxgap-benchmarking-and-mitigating-gender-bias-in-mul-2603-21050/) | **7.2** | #语音情感识别 |
| 8. | [From Senses to Decisions: The Information Flow of Auditory a…](from-senses-to-decisions-the-information-flow-of-auditory-an-2606-10147/) | **7.2** | #多模态大语言模型 |
| 9. | [Passive Acoustic-based Composite Indices for Reef Health Mon…](passive-acoustic-based-composite-indices-for-reef-health-mon-2511-05349/) | **6.5** | #生物声学 |
| 10. | [Profy: Interpretable Visualization of Expertise-Dependent Mo…](profy-interpretable-visualization-of-expertise-dependent-mot-2606-10627/) | **6.5** | #音乐技能评估 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="memo-attentional-momentum-for-real-time-audio-visual-speaker-2507-15294/">MeMo: Attentional Momentum for Real-time Audio-visual Speaker Extraction under Impaired Visual Conditions</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#目标说话人提取</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出MeMo框架，通过两个自适应记忆库在视觉线索缺失时维持注意力动量，实现鲁棒的实时视听目标说话人提取。</div>
<div class="card-action">
<a href="memo-attentional-momentum-for-real-time-audio-visual-speaker-2507-15294/">详情 →</a> · <a href="https://arxiv.org/abs/2507.15294" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="spatial-omni-spatial-audio-understanding-integration-in-mult-2606-10738/">Spatial-Omni: Spatial Audio Understanding Integration in Multimodal LLMs via FOA Encoding</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出Spatial-Omni，通过SO-Encoder将一阶Ambisonics空间音频注入多模态大语言模型，实现空间音频理解，无需修改原音频编码器。</div>
<div class="card-action">
<a href="spatial-omni-spatial-audio-understanding-integration-in-mult-2606-10738/">详情 →</a> · <a href="https://arxiv.org/abs/2606.10738" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="multiapi-spoof-a-multi-api-dataset-and-local-attention-netwo-2512-07352/">MultiAPI Spoof: A Multi-API Dataset and Local-Attention Network for Speech Anti-spoofing Detection</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音反欺骗</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出MultiAPI Spoof多API语音反欺骗数据集（230小时，30个API），并设计Nes2Net-LA局部注意力网络提升检测鲁棒性。</div>
<div class="card-action">
<a href="multiapi-spoof-a-multi-api-dataset-and-local-attention-netwo-2512-07352/">详情 →</a> · <a href="https://arxiv.org/abs/2512.07352" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="optimality-of-fsq-tokens-for-continuous-diffusion-for-catego-2606-09962/">Optimality of FSQ Tokens for Continuous Diffusion for Categorical Data with Application to Text-to-Speech</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">理论证明FSQ分词方案在连续扩散框架下最优，并在TTS任务中验证其优于LLM基模型且更小更快。</div>
<div class="card-action">
<a href="optimality-of-fsq-tokens-for-continuous-diffusion-for-catego-2606-09962/">详情 →</a> · <a href="https://arxiv.org/abs/2606.09962" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="openbibletts-large-scale-speech-resources-and-tts-models-for-2606-09553/">OpenBibleTTS: Large-Scale Speech Resources and TTS Models for Low-Resource Languages</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">OpenBibleTTS 是一个覆盖37种低资源语言的语音合成基准，系统比较了多种TTS架构，发现无单一模型在所有语言和指标上占优。</div>
<div class="card-action">
<a href="openbibletts-large-scale-speech-resources-and-tts-models-for-2606-09553/">详情 →</a> · <a href="https://arxiv.org/abs/2606.09553" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="what-do-deepfake-speech-detectors-actually-hear-2606-10912/">What Do Deepfake Speech Detectors Actually Hear?</a>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#音频深度伪造检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出基于集成梯度的可解释性方法，揭示三个WavLM深度伪造语音检测器依赖的不同声学线索。</div>
<div class="card-action">
<a href="what-do-deepfake-speech-detectors-actually-hear-2606-10912/">详情 →</a> · <a href="https://arxiv.org/abs/2606.10912" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="erm-minmaxgap-benchmarking-and-mitigating-gender-bias-in-mul-2603-21050/">ERM-MinMaxGAP: Benchmarking and Mitigating Gender Bias in Multilingual Multimodal Speech-LLM Emotion Recognition</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音情感识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出多语言多模态情感识别性别偏见基准，并设计ERM-MinMaxGAP方法缓解偏见，在Qwen2-Audio上提升性能并缩小性别差距。</div>
<div class="card-action">
<a href="erm-minmaxgap-benchmarking-and-mitigating-gender-bias-in-mul-2603-21050/">详情 →</a> · <a href="https://arxiv.org/abs/2603.21050" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="from-senses-to-decisions-the-information-flow-of-auditory-an-2606-10147/">From Senses to Decisions: The Information Flow of Auditory and Visual Perception in Multimodal LLMs</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#多模态大语言模型</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">系统分析音频-视觉大语言模型中音频和视觉信息流的路径与机制，揭示其顺序与并行路由模式。</div>
<div class="card-action">
<a href="from-senses-to-decisions-the-information-flow-of-auditory-an-2606-10147/">详情 →</a> · <a href="https://arxiv.org/abs/2606.10147" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="passive-acoustic-based-composite-indices-for-reef-health-mon-2511-05349/">Passive Acoustic-based Composite Indices for Reef Health Monitoring in Noisy Tropical waters</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#生物声学</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">利用CNN去噪器处理噪声掩蔽的珊瑚礁水下录音，提取声学指标与礁健康参数相关，证明被动声学监测可行性。</div>
<div class="card-action">
<a href="passive-acoustic-based-composite-indices-for-reef-health-mon-2511-05349/">详情 →</a> · <a href="https://arxiv.org/abs/2511.05349" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="profy-interpretable-visualization-of-expertise-dependent-mot-2606-10627/">Profy: Interpretable Visualization of Expertise-Dependent Motor Skills Toward Supporting Piano Practice</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#音乐技能评估</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出弱监督系统Profy，利用聚合听众评分作为标签，生成时间对齐的高亮片段辅助钢琴练习，无需局部标注即可识别专家与业余演奏差异。</div>
<div class="card-action">
<a href="profy-interpretable-visualization-of-expertise-dependent-mot-2606-10627/">详情 →</a> · <a href="https://arxiv.org/abs/2606.10627" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
