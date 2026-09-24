---
title: "语音/音频论文速递 2026-09-24"
date: 2026-09-24T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 4 篇 · 最高分 8.2（#双耳音频）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">4</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.2</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音增强 | 2篇 | `██████████` |
| #音频理解 | 2篇 | `██████████` |
| #双耳音频 | 1篇 | `█████` |
| #音频处理 | 1篇 | `█████` |
| #情感识别 | 1篇 | `█████` |
| #语音对话系统评测 | 1篇 | `█████` |
| #音乐信息检索 | 1篇 | `█████` |
| #声学模拟 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="neural-field-of-view-for-binaural-signal-matching-with-weara-2609-28343/">Neural Field-of-View for Binaural Signal Matching with Wearable Microphone Arrays</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">用CRNN从可穿戴阵列信号端到端学习FoV参数，替代显式声源定位，改善高DRR下的双耳信号匹配质量。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="lend-me-an-ear-speech-enhancement-using-a-robotic-arm-with-a-2602-17818/">Lend me an Ear: Speech Enhancement Using a Robotic Arm with a Microphone Array</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">将16麦克风阵列装在7自由度机械臂上，通过声源定位与视觉引导重配置阵列几何，结合MVDR波束成形与DNN时频掩蔽提升增强效果。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="sona-personalized-soundscape-mediation-to-support-people-wit-2604-00447/">Sona: Personalized Soundscape Mediation to Support People with Sound Sensitivity</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">Sona 是一个移动端个性化声景调节系统，可实时选择性衰减用户指定的多种重叠声音，并支持免重训练的自定义目标添加。</div>
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
<a class="card-title" href="neural-field-of-view-for-binaural-signal-matching-with-weara-2609-28343/">Neural Field-of-View for Binaural Signal Matching with Wearable Microphone Arrays</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">用CRNN从可穿戴阵列信号端到端学习FoV参数，替代显式声源定位，改善高DRR下的双耳信号匹配质量。</div>
</div></div>

### #乐器分离

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="a-stem-agnostic-approach-to-hybrid-ai-music-detection-2609-26956/">A Stem-Agnostic Approach to Hybrid AI Music Detection</a>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#音频处理</span>
</div>
<div class="card-tldr">提出 inspectrogram 时频表示与 Wiener 滤波结合的单 CNN 框架，在混合音乐中逐 stem 检测 AI 生成内容。</div>
</div></div>

## 📊 完整排行榜

| 排名 | 论文 | 评分 | 主任务 |
| --- | --- | --- | --- |
| 🥇 | [Neural Field-of-View for Binaural Signal Matching with Weara…](neural-field-of-view-for-binaural-signal-matching-with-weara-2609-28343/) 🎯 | **8.2** | #双耳音频 |
| 🥈 | [Lend me an Ear: Speech Enhancement Using a Robotic Arm with …](lend-me-an-ear-speech-enhancement-using-a-robotic-arm-with-a-2602-17818/) 🎯 | **7.8** | #语音增强 |
| 🥉 | [Mizar: A 159M-Parameter Audio-Language Model for Audio Under…](mizar-a-159m-parameter-audio-language-model-for-audio-unders-2609-28344/) | **7.0** | #音频理解 |
| 4. | [A Stem-Agnostic Approach to Hybrid AI Music Detection](a-stem-agnostic-approach-to-hybrid-ai-music-detection-2609-26956/) 🎯 | **7.0** | #音频处理 |
| 5. | [Causal Tracing of Audio-Text Fusion in Large Audio Language …](causal-tracing-of-audio-text-fusion-in-large-audio-language--2603-13768/) | **6.8** | #音频理解 |
| 6. | [BiCFlow-MER: Orchestrating Discriminative and Generative Mul…](bicflow-mer-orchestrating-discriminative-and-generative-mult-2609-27615/) | **6.8** | #情感识别 |
| 7. | [Neither Silence nor Overlap Is Failure: Intent-Conditioned E…](neither-silence-nor-overlap-is-failure-intent-conditioned-ev-2609-27372/) | **6.8** | #语音对话系统评测 |
| 8. | [MIDIBack: Harmony-Aware Singing Pitch Correction via Joint V…](midiback-harmony-aware-singing-pitch-correction-via-joint-vo-2609-28008/) | **6.8** | #音乐信息检索 |
| 9. | [Echo Detection in Spatial Room Impulse Responses Measured wi…](echo-detection-in-spatial-room-impulse-responses-measured-wi-2609-28068/) | **6.8** | #声学模拟 |
| 10. | [Sona: Personalized Soundscape Mediation to Support People wi…](sona-personalized-soundscape-mediation-to-support-people-wit-2604-00447/) 🎯 | **6.5** | #语音增强 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="neural-field-of-view-for-binaural-signal-matching-with-weara-2609-28343/">Neural Field-of-View for Binaural Signal Matching with Wearable Microphone Arrays</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用CRNN从可穿戴阵列信号端到端学习FoV参数，替代显式声源定位，改善高DRR下的双耳信号匹配质量。</div>
<div class="card-action">
<a href="neural-field-of-view-for-binaural-signal-matching-with-weara-2609-28343/">详情 →</a> · <a href="https://arxiv.org/abs/2609.28343" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="lend-me-an-ear-speech-enhancement-using-a-robotic-arm-with-a-2602-17818/">Lend me an Ear: Speech Enhancement Using a Robotic Arm with a Microphone Array</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">将16麦克风阵列装在7自由度机械臂上，通过声源定位与视觉引导重配置阵列几何，结合MVDR波束成形与DNN时频掩蔽提升增强效果。</div>
<div class="card-action">
<a href="lend-me-an-ear-speech-enhancement-using-a-robotic-arm-with-a-2602-17818/">详情 →</a> · <a href="https://arxiv.org/abs/2602.17818" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="mizar-a-159m-parameter-audio-language-model-for-audio-unders-2609-28344/">Mizar: A 159M-Parameter Audio-Language Model for Audio Understanding</a>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#音频理解</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">Mizar 用 159.3M 参数把 CED-Small 音频编码器接到 SmolLM2-135M，经三阶段训练在 MMAU/MMAR/ADQA 上超过同规模 ALM。</div>
<div class="card-action">
<a href="mizar-a-159m-parameter-audio-language-model-for-audio-unders-2609-28344/">详情 →</a> · <a href="https://arxiv.org/abs/2609.28344" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="a-stem-agnostic-approach-to-hybrid-ai-music-detection-2609-26956/">A Stem-Agnostic Approach to Hybrid AI Music Detection</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#音频处理</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">提出 inspectrogram 时频表示与 Wiener 滤波结合的单 CNN 框架，在混合音乐中逐 stem 检测 AI 生成内容。</div>
<div class="card-action">
<a href="a-stem-agnostic-approach-to-hybrid-ai-music-detection-2609-26956/">详情 →</a> · <a href="https://arxiv.org/abs/2609.26956" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="causal-tracing-of-audio-text-fusion-in-large-audio-language--2603-13768/">Causal Tracing of Audio-Text Fusion in Large Audio Language Models</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频理解</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">用因果追踪方法分析 DeSTA、Qwen、Voxtral 三类大音频语言模型内部声学与文本的融合位置与机制。</div>
<div class="card-action">
<a href="causal-tracing-of-audio-text-fusion-in-large-audio-language--2603-13768/">详情 →</a> · <a href="https://arxiv.org/abs/2603.13768" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="bicflow-mer-orchestrating-discriminative-and-generative-mult-2609-27615/">BiCFlow-MER: Orchestrating Discriminative and Generative Multimodal Emotion Recognition via Conditional Transport</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#情感识别</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出 BiCFlow-MER，用双向条件整流流把音文情感识别建模为结构化情感空间中的证据传输，在 IEMOCAP、MELD 与零样本 CASE 上超过对比方法。</div>
<div class="card-action">
<a href="bicflow-mer-orchestrating-discriminative-and-generative-mult-2609-27615/">详情 →</a> · <a href="https://arxiv.org/abs/2609.27615" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="neither-silence-nor-overlap-is-failure-intent-conditioned-ev-2609-27372/">Neither Silence nor Overlap Is Failure: Intent-Conditioned Evaluation of Turn-Taking in Full-Duplex Spoken Dialogue Models</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音对话系统评测</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出 TACT 基准，用意图条件化的连续评分替代二值窗口规则，评估全双工语音对话模型的轮次转换时机。</div>
<div class="card-action">
<a href="neither-silence-nor-overlap-is-failure-intent-conditioned-ev-2609-27372/">详情 →</a> · <a href="https://arxiv.org/abs/2609.27372" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="midiback-harmony-aware-singing-pitch-correction-via-joint-vo-2609-28008/">MIDIBack: Harmony-Aware Singing Pitch Correction via Joint Vocal-Accompaniment Symbolic Modeling</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音乐信息检索</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">MIDIBack 用共享 OctupleMIDI 序列联合建模人声与伴奏音符事件，实现和声感知的自动音高修正，伴奏条件使 RPA 从 35.8% 提升至 81.5%。</div>
<div class="card-action">
<a href="midiback-harmony-aware-singing-pitch-correction-via-joint-vo-2609-28008/">详情 →</a> · <a href="https://arxiv.org/abs/2609.28008" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="echo-detection-in-spatial-room-impulse-responses-measured-wi-2609-28068/">Echo Detection in Spatial Room Impulse Responses Measured with Spherical Microphone Arrays Using the Herglotz Wavefunction</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#声学模拟</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">用 Herglotz 波函数在球谐域构造定位函数，配合自适应径向高斯拟合，检测并定位 SRIR 中的早期反射。</div>
<div class="card-action">
<a href="echo-detection-in-spatial-room-impulse-responses-measured-wi-2609-28068/">详情 →</a> · <a href="https://arxiv.org/abs/2609.28068" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="sona-personalized-soundscape-mediation-to-support-people-wit-2604-00447/">Sona: Personalized Soundscape Mediation to Support People with Sound Sensitivity</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">Sona 是一个移动端个性化声景调节系统，可实时选择性衰减用户指定的多种重叠声音，并支持免重训练的自定义目标添加。</div>
<div class="card-action">
<a href="sona-personalized-soundscape-mediation-to-support-people-wit-2604-00447/">详情 →</a> · <a href="https://arxiv.org/abs/2604.00447" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
