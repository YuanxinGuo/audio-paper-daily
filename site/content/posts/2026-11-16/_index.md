---
title: "语音/音频论文速递 2026-11-16"
date: 2026-11-16T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 1 篇 · 最高分 8.8（#双耳音频）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">1</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.8</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #音频生成 | 2篇 | `██████████` |
| #语音识别 | 2篇 | `██████████` |
| #双耳音频 | 1篇 | `█████` |
| #说话人日志 | 1篇 | `█████` |
| #音频安全 | 1篇 | `█████` |
| #语音对话系统 | 1篇 | `█████` |
| #音频处理 | 1篇 | `█████` |
| #认知障碍检测 | 1篇 | `█████` |

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

<p class="empty-hint">今日无新论文命中，推荐回顾该方向的经典工作：</p>
<div class="paper-card paper-card-classic">
<div class="card-rank">📚</div>
<div class="card-body">
<a class="card-title" href="https://arxiv.org/abs/1508.04306" target="_blank" rel="noopener">Deep Clustering: Discriminative Embeddings for Segmentation and Separation</a> <span class="classic-badge">经典</span>
<div class="card-meta">
<span class="card-venue">ICASSP 2016</span>
<span class="tag-pill tag-pill-soft">#语音分离</span>
</div>
<div class="card-tldr">用嵌入聚类绕开 permutation 问题的开山之作，SS 领域必读。</div>
<div class="card-authors">John R. Hershey, Zhuo Chen, Jonathan Le Roux, Shinji Watanabe</div>
</div></div>
<div class="paper-card paper-card-classic">
<div class="card-rank">📚</div>
<div class="card-body">
<a class="card-title" href="https://arxiv.org/abs/1607.00325" target="_blank" rel="noopener">Permutation Invariant Training of Deep Models for Speaker-Independent Multi-talker Speech Separation</a> <span class="classic-badge">经典</span>
<div class="card-meta">
<span class="card-venue">ICASSP 2017</span>
<span class="tag-pill tag-pill-soft">#语音分离</span>
</div>
<div class="card-tldr">PIT 提出，至今仍是大多数分离/TSE 工作的训练目标。</div>
<div class="card-authors">Dong Yu, Morten Kolbæk, Zheng-Hua Tan, Jesper Jensen</div>
</div></div>

### #双耳音频

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="any-channel-count-one-token-stream-incorporating-spatial-aud-2611-18112/">Any Channel Count, One Token Stream: Incorporating Spatial Audio Understanding and Reasoning into Large Audio-Language Models</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">提出SpheraAudio，将任意通道数（单声道/立体声/FOA）空间音频映射为统一token流，结合SMRoPE与三阶段训练实现空间定位与推理。</div>
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
| 🥇 | [Any Channel Count, One Token Stream: Incorporating Spatial A…](any-channel-count-one-token-stream-incorporating-spatial-aud-2611-18112/) 🎯 | **8.8** | #双耳音频 |
| 🥈 | [eDIAR: Training-Free Open-Speaker Streaming Diarization for …](ediar-training-free-open-speaker-streaming-diarization-for-l-2611-18529/) | **7.2** | #说话人日志 |
| 🥉 | [CoTTAGE: An Explainable Judge for Text-to-Audio Generation](cottage-an-explainable-judge-for-text-to-audio-generation-2611-17644/) | **7.2** | #音频生成 |
| 4. | [The Alignment Curse: Modality Alignment Supercharges Audio A…](the-alignment-curse-modality-alignment-supercharges-audio-at-2602-02557/) | **6.8** | #音频安全 |
| 5. | [RECOVER: Robust Entity Correction via agentic Orchestration …](recover-robust-entity-correction-via-agentic-orchestration-o-2603-16411/) | **6.8** | #语音识别 |
| 6. | [Integrate the Reward, Don't Sample It: Window Likelihood for…](integrate-the-reward-don-t-sample-it-window-likelihood-for-i-2610-35581/) | **6.8** | #语音对话系统 |
| 7. | [FEND: Far-End Detection in Outbound Voice AI Calls](fend-far-end-detection-in-outbound-voice-ai-calls-2611-18050/) | **6.8** | #音频处理 |
| 8. | [Cross-Linguistic Acoustic Biomarkers of Cognitive Impairment…](cross-linguistic-acoustic-biomarkers-of-cognitive-impairment-2611-17710/) | **6.8** | #认知障碍检测 |
| 9. | [CamSpokenNLI: A Pilot Resource for Cross-Variety Transfer Ev…](camspokennli-a-pilot-resource-for-cross-variety-transfer-eva-2611-17573/) | **4.5** | #语音识别 |
| 10. | [Activation Steering the Nan-Shan in Typhoon](activation-steering-the-nan-shan-in-typhoon-2611-17768/) | **3.0** | #音频生成 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="any-channel-count-one-token-stream-incorporating-spatial-aud-2611-18112/">Any Channel Count, One Token Stream: Incorporating Spatial Audio Understanding and Reasoning into Large Audio-Language Models</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出SpheraAudio，将任意通道数（单声道/立体声/FOA）空间音频映射为统一token流，结合SMRoPE与三阶段训练实现空间定位与推理。</div>
<div class="card-action">
<a href="any-channel-count-one-token-stream-incorporating-spatial-aud-2611-18112/">详情 →</a> · <a href="https://arxiv.org/abs/2611.18112" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="ediar-training-free-open-speaker-streaming-diarization-for-l-2611-18529/">eDIAR: Training-Free Open-Speaker Streaming Diarization for Long Meetings and Large Archives via e-means</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#说话人日志</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用 e-means 聚类替换固定槽位上限，实现免训练、说话人数不限的流式说话人日志。</div>
<div class="card-action">
<a href="ediar-training-free-open-speaker-streaming-diarization-for-l-2611-18529/">详情 →</a> · <a href="https://arxiv.org/abs/2611.18529" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="cottage-an-explainable-judge-for-text-to-audio-generation-2611-17644/">CoTTAGE: An Explainable Judge for Text-to-Audio Generation</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音频生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出基于推理的文本到音频评估器 CoTTAGE，先诊断后打分，用 Thurstone 偏好目标做强化学习，提升与人类判断的相关性。</div>
<div class="card-action">
<a href="cottage-an-explainable-judge-for-text-to-audio-generation-2611-17644/">详情 →</a> · <a href="https://arxiv.org/abs/2611.17644" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="the-alignment-curse-modality-alignment-supercharges-audio-at-2602-02557/">The Alignment Curse: Modality Alignment Supercharges Audio Attacks via Text Transfer</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频安全</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">提出“对齐诅咒”原则：文本-音频模态对齐越强，文本越狱攻击越易迁移到音频，对Qwen2.5-Omni等全模态模型做黑盒评估验证。</div>
<div class="card-action">
<a href="the-alignment-curse-modality-alignment-supercharges-audio-at-2602-02557/">详情 →</a> · <a href="https://arxiv.org/abs/2602.02557" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="recover-robust-entity-correction-via-agentic-orchestration-o-2603-16411/">RECOVER: Robust Entity Correction via agentic Orchestration of hypothesis Variants for Evidence-based Recovery</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">用多路ASR假设作证据，结合实体检索与LLM批评者迭代纠错，降低实体短语E-WER。</div>
<div class="card-action">
<a href="recover-robust-entity-correction-via-agentic-orchestration-o-2603-16411/">详情 →</a> · <a href="https://arxiv.org/abs/2603.16411" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="integrate-the-reward-don-t-sample-it-window-likelihood-for-i-2610-35581/">Integrate the Reward, Don't Sample It: Window Likelihood for Interruptions and Backchannels in Full-Duplex Speech Models</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音对话系统</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">用窗口似然替代GRPO采样估计停止概率，精确积分停止决策以改进全双工对话中打断与附和判别。</div>
<div class="card-action">
<a href="integrate-the-reward-don-t-sample-it-window-likelihood-for-i-2610-35581/">详情 →</a> · <a href="https://arxiv.org/abs/2610.35581" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="fend-far-end-detection-in-outbound-voice-ai-calls-2611-18050/">FEND: Far-End Detection in Outbound Voice AI Calls</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频处理</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出FEND框架，用远端音频与流式转写多检测器区分真人、语音信箱、IVR与AI接听者，20秒内给出单标签。</div>
<div class="card-action">
<a href="fend-far-end-detection-in-outbound-voice-ai-calls-2611-18050/">详情 →</a> · <a href="https://arxiv.org/abs/2611.18050" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="cross-linguistic-acoustic-biomarkers-of-cognitive-impairment-2611-17710/">Cross-Linguistic Acoustic Biomarkers of Cognitive Impairment Across Interactive and Single-Speaker Speech Tasks</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#认知障碍检测</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">跨四语言、跨任务分析语音声学特征对认知障碍的判别力，发现时序特征稳健、语速依赖任务、音高特征依赖语言。</div>
<div class="card-action">
<a href="cross-linguistic-acoustic-biomarkers-of-cognitive-impairment-2611-17710/">详情 →</a> · <a href="https://arxiv.org/abs/2611.17710" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="camspokennli-a-pilot-resource-for-cross-variety-transfer-eva-2611-17573/">CamSpokenNLI: A Pilot Resource for Cross-Variety Transfer Evaluation in Cameroon Pidgin English and Camfranglais</a>
<div class="card-meta">
<span class="card-score">4.5</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">后50%</span>
</div>
<div class="card-tldr">发布喀麦隆皮钦英语与Camfranglais各114条口语NLI试点数据，用XLM-R与Whisper做基线评估。</div>
<div class="card-action">
<a href="camspokennli-a-pilot-resource-for-cross-variety-transfer-eva-2611-17573/">详情 →</a> · <a href="https://arxiv.org/abs/2611.17573" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="activation-steering-the-nan-shan-in-typhoon-2611-17768/">Activation Steering the Nan-Shan in Typhoon</a>
<div class="card-meta">
<span class="card-score">3.0</span>
<span class="tag-pill">#音频生成</span>
<span class="card-tier">后50%</span>
</div>
<div class="card-tldr">以康拉德小说《台风》为文本基础，让大模型自噬式生成文本，并用自适应激活引导控制叙事节奏，做成音视频装置。</div>
<div class="card-action">
<a href="activation-steering-the-nan-shan-in-typhoon-2611-17768/">详情 →</a> · <a href="https://arxiv.org/abs/2611.17768" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
