---
title: "语音/音频论文速递 2026-11-13"
date: 2026-11-13T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 3 篇 · 最高分 8.8（#目标说话人提取）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">3</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.8</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音合成 | 2篇 | `██████████` |
| #目标说话人提取 | 1篇 | `█████` |
| #语音分离 | 1篇 | `█████` |
| #双耳音频 | 1篇 | `█████` |
| #声学模拟 | 1篇 | `█████` |
| #语音隐私保护 | 1篇 | `█████` |
| #音乐信息检索 | 1篇 | `█████` |
| #语音识别 | 1篇 | `█████` |

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
<a class="card-title" href="structured-speaker-conditioning-for-diarization-guided-targe-2611-16371/">Structured Speaker Conditioning for Diarization-Guided Target-Speaker ASR</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">提出结构化说话人条件化SSC，用日志活动结构与会话级声纹身份构造目标条件，调制ASR编码器，实现日志引导的目标说话人识别。</div>
</div></div>

### #语音分离

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="kezek-splitting-mono-two-person-conversations-into-per-speak-2611-16933/">Kezek: Splitting Mono Two-Person Conversations into Per-Speaker Tracks for Full-Duplex Dialogue Data</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">Kezek 将单声道双人对话拆成每人一条等长音轨，两阶段：指纹引导的双声活动检测定决策，条件时域分离器执行，输出严格可加。</div>
</div></div>

### #双耳音频

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="mesh-multi-receiver-evaluation-of-spatial-hearing-across-ego-2611-16787/">MESH: Multi-receiver Evaluation of Spatial Hearing across Egocentric and Allocentric Views</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">提出MESH基准，用自我中心与异中心视角评测多接收器共享声场景中的声源关联与空间理解。</div>
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
| 🥇 | [Structured Speaker Conditioning for Diarization-Guided Targe…](structured-speaker-conditioning-for-diarization-guided-targe-2611-16371/) 🎯 | **8.8** | #目标说话人提取 |
| 🥈 | [Kezek: Splitting Mono Two-Person Conversations into Per-Spea…](kezek-splitting-mono-two-person-conversations-into-per-speak-2611-16933/) 🎯 | **8.2** | #语音分离 |
| 🥉 | [MESH: Multi-receiver Evaluation of Spatial Hearing across Eg…](mesh-multi-receiver-evaluation-of-spatial-hearing-across-ego-2611-16787/) 🎯 | **7.8** | #双耳音频 |
| 4. | [Convolutional VocalTrax: Replacing Backpropagation Through T…](convolutional-vocaltrax-replacing-backpropagation-through-ti-2611-17181/) | **7.2** | #声学模拟 |
| 5. | [ZONOS3-Mini Technical Report](zonos3-mini-technical-report-2611-16525/) | **6.8** | #语音合成 |
| 6. | [The Unseen Threat: How Complementary Combinations of Acousti…](the-unseen-threat-how-complementary-combinations-of-acoustic-2611-16637/) | **6.8** | #语音隐私保护 |
| 7. | [MusicRWKV: A Multimodal RWKV Framework for Music Representat…](musicrwkv-a-multimodal-rwkv-framework-for-music-representati-2611-16718/) | **6.8** | #音乐信息检索 |
| 8. | [Beyond Word Error Rate: A Failure Taxonomy of Streaming Dict…](beyond-word-error-rate-a-failure-taxonomy-of-streaming-dicta-2611-16919/) | **6.8** | #语音识别 |
| 9. | [Evaluation of Music Version Retrieval Methods for Setlist Id…](evaluation-of-music-version-retrieval-methods-for-setlist-id-2611-17070/) | **6.8** | #音乐版本检索 |
| 10. | [Human-Likeness and Conversational Preference Diverge for Syn…](human-likeness-and-conversational-preference-diverge-for-syn-2611-16051/) | **6.2** | #语音合成 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="structured-speaker-conditioning-for-diarization-guided-targe-2611-16371/">Structured Speaker Conditioning for Diarization-Guided Target-Speaker ASR</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#目标说话人提取</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出结构化说话人条件化SSC，用日志活动结构与会话级声纹身份构造目标条件，调制ASR编码器，实现日志引导的目标说话人识别。</div>
<div class="card-action">
<a href="structured-speaker-conditioning-for-diarization-guided-targe-2611-16371/">详情 →</a> · <a href="https://arxiv.org/abs/2611.16371" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="kezek-splitting-mono-two-person-conversations-into-per-speak-2611-16933/">Kezek: Splitting Mono Two-Person Conversations into Per-Speaker Tracks for Full-Duplex Dialogue Data</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音分离</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">Kezek 将单声道双人对话拆成每人一条等长音轨，两阶段：指纹引导的双声活动检测定决策，条件时域分离器执行，输出严格可加。</div>
<div class="card-action">
<a href="kezek-splitting-mono-two-person-conversations-into-per-speak-2611-16933/">详情 →</a> · <a href="https://arxiv.org/abs/2611.16933" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="mesh-multi-receiver-evaluation-of-spatial-hearing-across-ego-2611-16787/">MESH: Multi-receiver Evaluation of Spatial Hearing across Egocentric and Allocentric Views</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">提出MESH基准，用自我中心与异中心视角评测多接收器共享声场景中的声源关联与空间理解。</div>
<div class="card-action">
<a href="mesh-multi-receiver-evaluation-of-spatial-hearing-across-ego-2611-16787/">详情 →</a> · <a href="https://arxiv.org/abs/2611.16787" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="convolutional-vocaltrax-replacing-backpropagation-through-ti-2611-17181/">Convolutional VocalTrax: Replacing Backpropagation Through Time with Convolution in Differentiable Articulatory Synthesis</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#声学模拟</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用FFT因果卷积替代Pink Trombone波导的逐样本递归，实现可微分声道合成的快速精确梯度回传。</div>
<div class="card-action">
<a href="convolutional-vocaltrax-replacing-backpropagation-through-ti-2611-17181/">详情 →</a> · <a href="https://arxiv.org/abs/2611.17181" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="zonos3-mini-technical-report-2611-16525/">ZONOS3-Mini Technical Report</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">ZONOS3-Mini 是 886M 参数（每 token 激活 100M）的零样本语音克隆 TTS，配 44.1kHz/15Hz 帧率的 ZAC-1 编解码器，可在手机实时运行。</div>
<div class="card-action">
<a href="zonos3-mini-technical-report-2611-16525/">详情 →</a> · <a href="https://arxiv.org/abs/2611.16525" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="the-unseen-threat-how-complementary-combinations-of-acoustic-2611-16637/">The Unseen Threat: How Complementary Combinations of Acoustic Features Compromise Speech Privacy</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音隐私保护</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">研究RMS电平、基频与平滑降采样Mel谱组合后对ASR与说话人验证攻击的隐私泄露，发现特征融合会放大内容泄露。</div>
<div class="card-action">
<a href="the-unseen-threat-how-complementary-combinations-of-acoustic-2611-16637/">详情 →</a> · <a href="https://arxiv.org/abs/2611.16637" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="musicrwkv-a-multimodal-rwkv-framework-for-music-representati-2611-16718/">MusicRWKV: A Multimodal RWKV Framework for Music Representation Learning</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音乐信息检索</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">提出基于RWKV的多模态音乐表征学习框架，联合建模波形、频谱与元数据，用可逆压缩与FiLM条件化提升长序列效率。</div>
<div class="card-action">
<a href="musicrwkv-a-multimodal-rwkv-framework-for-music-representati-2611-16718/">详情 →</a> · <a href="https://arxiv.org/abs/2611.16718" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="beyond-word-error-rate-a-failure-taxonomy-of-streaming-dicta-2611-16919/">Beyond Word Error Rate: A Failure Taxonomy of Streaming Dictation ASR</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出超越WER的流式听写ASR失败分类法，按识别、格式、语种、丢音频四级归类，揭示同WER系统失败模式差异巨大。</div>
<div class="card-action">
<a href="beyond-word-error-rate-a-failure-taxonomy-of-streaming-dicta-2611-16919/">详情 →</a> · <a href="https://arxiv.org/abs/2611.16919" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="evaluation-of-music-version-retrieval-methods-for-setlist-id-2611-17070/">Evaluation of Music Version Retrieval Methods for Setlist Identification in Live Concerts</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音乐版本检索</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">在 ASID 基准上评测 Re-MOVE、CLEWS 与自研 NAVE 三种音乐版本检索方法用于演唱会歌单识别，NAVE 以 256 维嵌入取得最佳检索性能。</div>
<div class="card-action">
<a href="evaluation-of-music-version-retrieval-methods-for-setlist-id-2611-17070/">详情 →</a> · <a href="https://arxiv.org/abs/2611.17070" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="human-likeness-and-conversational-preference-diverge-for-syn-2611-16051/">Human-Likeness and Conversational Preference Diverge for Synthesized Agent Speech in Customer-Service Calls</a>
<div class="card-meta">
<span class="card-score">6.2</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">在客服场景配对听测中发现，合成语音的拟人度与对话偏好排序不一致，且单音色测试会误判系统优劣。</div>
<div class="card-action">
<a href="human-likeness-and-conversational-preference-diverge-for-syn-2611-16051/">详情 →</a> · <a href="https://arxiv.org/abs/2611.16051" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
