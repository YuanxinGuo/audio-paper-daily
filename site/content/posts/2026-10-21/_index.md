---
title: "语音/音频论文速递 2026-10-21"
date: 2026-10-21T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 2 篇 · 最高分 8.8（#语音分离）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">2</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.8</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音识别 | 4篇 | `██████████` |
| #语音分离 | 1篇 | `██` |
| #双耳音频 | 1篇 | `██` |
| #说话人日志 | 1篇 | `██` |
| #语音合成 | 1篇 | `██` |
| #语音健康监测 | 1篇 | `██` |
| #音频处理 | 1篇 | `██` |

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
<a class="card-title" href="slm-ss-token-based-speech-separation-with-speech-language-mo-2610-27785/">SLM-SS: Token-Based Speech Separation with Speech Language Models</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">用神经编解码器离散化语音，以自回归 SLM 预测零阶 token 建立说话人顺序，再用非自回归模块精修高阶残差码本，实现生成式语音分离。</div>
</div></div>

### #双耳音频

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="binaural-audio-visual-instance-segmentation-2609-32180/">Binaural Audio-Visual Instance Segmentation</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">提出双耳视听实例分割新任务BiAVIS，用双耳空间线索把发声实例从同类物体中区分开，并构建两个基准。</div>
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
| 🥇 | [SLM-SS: Token-Based Speech Separation with Speech Language M…](slm-ss-token-based-speech-separation-with-speech-language-mo-2610-27785/) 🎯 | **8.8** | #语音分离 |
| 🥈 | [Binaural Audio-Visual Instance Segmentation](binaural-audio-visual-instance-segmentation-2609-32180/) 🎯 | **8.8** | #双耳音频 |
| 🥉 | [Preference-Aware Pareto Steering for Multi-Task Speech LLMs](preference-aware-pareto-steering-for-multi-task-speech-llms-2610-27200/) | **7.2** | #语音识别 |
| 4. | [Slots Are Not Speakers: Training-Free Speaker Linking for Fr…](slots-are-not-speakers-training-free-speaker-linking-for-fro-2610-28053/) | **7.2** | #说话人日志 |
| 5. | [Improved automatic speech-based cognitive assessment using n…](improved-automatic-speech-based-cognitive-assessment-using-n-2610-28288/) | **7.0** | #语音识别 |
| 6. | [LoCA: Local Credit Assignment for Reinforcement Learning of …](loca-local-credit-assignment-for-reinforcement-learning-of-a-2610-28035/) | **7.0** | #语音合成 |
| 7. | [SpikCTU: A Compact Spiking Network with Adaptive Recurrent C…](spikctu-a-compact-spiking-network-with-adaptive-recurrent-co-2610-14594/) | **6.8** | #语音识别 |
| 8. | [Speaker-Disentangled Remote Speech Detection of Asthma and C…](speaker-disentangled-remote-speech-detection-of-asthma-and-c-2605-16878/) | **6.8** | #语音健康监测 |
| 9. | [You Are the Trigger: Speaker-Activated Backdoors](you-are-the-trigger-speaker-activated-backdoors-2610-27210/) | **6.8** | #语音识别 |
| 10. | [WaveCommitments: Private and Verifiable Speech-Agent Marketp…](wavecommitments-private-and-verifiable-speech-agent-marketpl-2610-26867/) | **5.5** | #音频处理 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="slm-ss-token-based-speech-separation-with-speech-language-mo-2610-27785/">SLM-SS: Token-Based Speech Separation with Speech Language Models</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音分离</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用神经编解码器离散化语音，以自回归 SLM 预测零阶 token 建立说话人顺序，再用非自回归模块精修高阶残差码本，实现生成式语音分离。</div>
<div class="card-action">
<a href="slm-ss-token-based-speech-separation-with-speech-language-mo-2610-27785/">详情 →</a> · <a href="https://arxiv.org/abs/2610.27785" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="binaural-audio-visual-instance-segmentation-2609-32180/">Binaural Audio-Visual Instance Segmentation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出双耳视听实例分割新任务BiAVIS，用双耳空间线索把发声实例从同类物体中区分开，并构建两个基准。</div>
<div class="card-action">
<a href="binaural-audio-visual-instance-segmentation-2609-32180/">详情 →</a> · <a href="https://arxiv.org/abs/2609.32180" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="preference-aware-pareto-steering-for-multi-task-speech-llms-2610-27200/">Preference-Aware Pareto Steering for Multi-Task Speech LLMs</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出 EA-SURF，一种先验式多任务标量化权重自适应方法，使语音 LLM 的 ASR/时间戳/翻译权衡贴合部署偏好。</div>
<div class="card-action">
<a href="preference-aware-pareto-steering-for-multi-task-speech-llms-2610-27200/">详情 →</a> · <a href="https://arxiv.org/abs/2610.27200" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="slots-are-not-speakers-training-free-speaker-linking-for-fro-2610-28053/">Slots Are Not Speakers: Training-Free Speaker Linking for Frozen Streaming Diarizers</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#说话人日志</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出免训练的因果链接器，让固定槽位的流式说话人日志模型能跟踪超过槽位数的说话人。</div>
<div class="card-action">
<a href="slots-are-not-speakers-training-free-speaker-linking-for-fro-2610-28053/">详情 →</a> · <a href="https://arxiv.org/abs/2610.28053" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="improved-automatic-speech-based-cognitive-assessment-using-n-2610-28288/">Improved automatic speech-based cognitive assessment using neuropsychologically calibrated diagnostic labels</a>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用神经心理学阈值与z-score重新校准不可靠诊断标签，提升对话语音认知障碍分类的F1与跨数据集泛化。</div>
<div class="card-action">
<a href="improved-automatic-speech-based-cognitive-assessment-using-n-2610-28288/">详情 →</a> · <a href="https://arxiv.org/abs/2610.28288" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="loca-local-credit-assignment-for-reinforcement-learning-of-a-2610-28035/">LoCA: Local Credit Assignment for Reinforcement Learning of Autoregressive Flow-Matching TTS</a>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用ASR对齐定位内容错误，将句级优势重分配到声学帧，并用参考相对阈值稳定流匹配TTS的强化学习训练。</div>
<div class="card-action">
<a href="loca-local-credit-assignment-for-reinforcement-learning-of-a-2610-28035/">详情 →</a> · <a href="https://arxiv.org/abs/2610.28035" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="spikctu-a-compact-spiking-network-with-adaptive-recurrent-co-2610-14594/">SpikCTU: A Compact Spiking Network with Adaptive Recurrent Computation for Speech Command Recognition</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出紧凑脉冲网络SpikCTU，用共享连续思考单元做自适应循环计算，仅0.16-0.17M参数在语音命令识别上取得有竞争力精度。</div>
<div class="card-action">
<a href="spikctu-a-compact-spiking-network-with-adaptive-recurrent-co-2610-14594/">详情 →</a> · <a href="https://arxiv.org/abs/2610.14594" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="speaker-disentangled-remote-speech-detection-of-asthma-and-c-2605-16878/">Speaker-Disentangled Remote Speech Detection of Asthma and COPD Exacerbations</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音健康监测</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">用梯度反转对抗训练从语音中解耦说话人身份信息，提升哮喘/COPD急性加重的检测精度与隐私性。</div>
<div class="card-action">
<a href="speaker-disentangled-remote-speech-detection-of-asthma-and-c-2605-16878/">详情 →</a> · <a href="https://arxiv.org/abs/2605.16878" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="you-are-the-trigger-speaker-activated-backdoors-2610-27210/">You Are the Trigger: Speaker-Activated Backdoors</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出以目标说话人自然语音为触发器的后门攻击，两阶段微调将说话人身份绑定到恶意载荷，在Whisper与Parakeet上成功率超90%。</div>
<div class="card-action">
<a href="you-are-the-trigger-speaker-activated-backdoors-2610-27210/">详情 →</a> · <a href="https://arxiv.org/abs/2610.27210" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="wavecommitments-private-and-verifiable-speech-agent-marketpl-2610-26867/">WaveCommitments: Private and Verifiable Speech-Agent Marketplaces</a>
<div class="card-meta">
<span class="card-score">5.5</span>
<span class="tag-pill">#音频处理</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">提出 WaveCommitments，用 TEE 内 Data Shapley 估值语音资产，配合多元多项式承诺实现选择性披露与防篡改溯源。</div>
<div class="card-action">
<a href="wavecommitments-private-and-verifiable-speech-agent-marketpl-2610-26867/">详情 →</a> · <a href="https://arxiv.org/abs/2610.26867" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
