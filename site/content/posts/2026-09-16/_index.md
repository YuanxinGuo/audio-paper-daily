---
title: "语音/音频论文速递 2026-09-16"
date: 2026-09-16T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 3 篇 · 最高分 8.8（#语音分离）"
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
| #语音对话系统 | 2篇 | `██████████` |
| #语音分离 | 1篇 | `█████` |
| #语音增强 | 1篇 | `█████` |
| #音频-视觉导航 | 1篇 | `█████` |
| #语音克隆 | 1篇 | `█████` |
| #音频理解基准 | 1篇 | `█████` |
| #音频-视觉说话人轮换预测 | 1篇 | `█████` |
| #语音合成检测 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="ring-mixing-with-auxiliary-signal-to-consistency-error-ratio-2604-08415/">Ring Mixing with Auxiliary Signal-to-Consistency-Error Ratio Loss for Unsupervised Denoising in Speech Separation</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">提出 ring mixing 批次策略与 SCER 辅助损失，打破分离损失对称性，使系统仅用含噪录音即可学会去噪。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="probing-layer-wise-robustness-and-sensitivity-of-speech-enha-2512-00482/">Probing Layer-Wise Robustness and Sensitivity of Speech Enhancement Models</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">用CKA逐层探测MUSE、MP-SENet、Demucs在SNR与C50退化下的表征鲁棒性与敏感性，发现深度非均匀性由增强目标诱导。</div>
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
<a class="card-title" href="ring-mixing-with-auxiliary-signal-to-consistency-error-ratio-2604-08415/">Ring Mixing with Auxiliary Signal-to-Consistency-Error Ratio Loss for Unsupervised Denoising in Speech Separation</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">提出 ring mixing 批次策略与 SCER 辅助损失，打破分离损失对称性，使系统仅用含噪录音即可学会去噪。</div>
</div></div>

### #双耳音频

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="ctan-cycle-temporal-attention-network-for-embodied-audio-vis-2609-17420/">CTAN: Cycle-Temporal Attention Network for Embodied Audio-Visual Navigation</a>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#音频-视觉导航</span>
</div>
<div class="card-tldr">提出循环-时序注意力网络CTAN，用双向循环一致性约束与跨模态记忆增强视听语义融合，提升具身音频导航成功率。</div>
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
| 🥇 | [Ring Mixing with Auxiliary Signal-to-Consistency-Error Ratio…](ring-mixing-with-auxiliary-signal-to-consistency-error-ratio-2604-08415/) 🎯 | **8.8** | #语音分离 |
| 🥈 | [VoxMind: An End-to-End Agentic Spoken Dialogue System](voxmind-an-end-to-end-agentic-spoken-dialogue-system-2604-15710/) | **7.8** | #语音对话系统 |
| 🥉 | [Probing Layer-Wise Robustness and Sensitivity of Speech Enha…](probing-layer-wise-robustness-and-sensitivity-of-speech-enha-2512-00482/) 🎯 | **7.8** | #语音增强 |
| 4. | [CTAN: Cycle-Temporal Attention Network for Embodied Audio-Vi…](ctan-cycle-temporal-attention-network-for-embodied-audio-vis-2609-17420/) 🎯 | **7.0** | #音频-视觉导航 |
| 5. | [Liberating LLM Capabilities in Full-Duplex Speech Models](liberating-llm-capabilities-in-full-duplex-speech-models-2606-07547/) | **6.8** | #语音对话系统 |
| 6. | [Acoustic and perceptual differences between standard and acc…](acoustic-and-perceptual-differences-between-standard-and-acc-2604-01562/) | **6.8** | #语音克隆 |
| 7. | [PARSA-Bench: A Comprehensive Persian Audio-Language Model Be…](parsa-bench-a-comprehensive-persian-audio-language-model-ben-2603-14456/) | **6.5** | #音频理解基准 |
| 8. | [Audio-Visual Turn-taking Prediction in Cocktail Party Scenar…](audio-visual-turn-taking-prediction-in-cocktail-party-scenar-2609-17056/) | **6.5** | #音频-视觉说话人轮换预测 |
| 9. | [The Machines Are Calling: Measuring Automated and Synthetic …](the-machines-are-calling-measuring-automated-and-synthetic-v-2609-11137/) | **6.0** | #语音合成检测 |
| 10. | [Enhancing Law-Enforcement Audio Transcription: A LoRA-Based …](enhancing-law-enforcement-audio-transcription-a-lora-based-a-2607-27245/) | **5.5** | #语音识别 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="ring-mixing-with-auxiliary-signal-to-consistency-error-ratio-2604-08415/">Ring Mixing with Auxiliary Signal-to-Consistency-Error Ratio Loss for Unsupervised Denoising in Speech Separation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音分离</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出 ring mixing 批次策略与 SCER 辅助损失，打破分离损失对称性，使系统仅用含噪录音即可学会去噪。</div>
<div class="card-action">
<a href="ring-mixing-with-auxiliary-signal-to-consistency-error-ratio-2604-08415/">详情 →</a> · <a href="https://arxiv.org/abs/2604.08415" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="voxmind-an-end-to-end-agentic-spoken-dialogue-system-2604-15710/">VoxMind: An End-to-End Agentic Spoken Dialogue System</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音对话系统</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">VoxMind 为端到端语音对话模型引入工具调用能力，通过 Think-before-Speak 与多智能体动态工具管理，任务完成率从 34.88% 提升至 74.57%。</div>
<div class="card-action">
<a href="voxmind-an-end-to-end-agentic-spoken-dialogue-system-2604-15710/">详情 →</a> · <a href="https://arxiv.org/abs/2604.15710" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="probing-layer-wise-robustness-and-sensitivity-of-speech-enha-2512-00482/">Probing Layer-Wise Robustness and Sensitivity of Speech Enhancement Models</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">用CKA逐层探测MUSE、MP-SENet、Demucs在SNR与C50退化下的表征鲁棒性与敏感性，发现深度非均匀性由增强目标诱导。</div>
<div class="card-action">
<a href="probing-layer-wise-robustness-and-sensitivity-of-speech-enha-2512-00482/">详情 →</a> · <a href="https://arxiv.org/abs/2512.00482" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="ctan-cycle-temporal-attention-network-for-embodied-audio-vis-2609-17420/">CTAN: Cycle-Temporal Attention Network for Embodied Audio-Visual Navigation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#音频-视觉导航</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">提出循环-时序注意力网络CTAN，用双向循环一致性约束与跨模态记忆增强视听语义融合，提升具身音频导航成功率。</div>
<div class="card-action">
<a href="ctan-cycle-temporal-attention-network-for-embodied-audio-vis-2609-17420/">详情 →</a> · <a href="https://arxiv.org/abs/2609.17420" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="liberating-llm-capabilities-in-full-duplex-speech-models-2606-07547/">Liberating LLM Capabilities in Full-Duplex Speech Models</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音对话系统</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出 Listen-Write-Speak 三通道范式，让单一自回归 LLM 在共享因果注意力下同时听、写可见文本、并行说话，无需改架构。</div>
<div class="card-action">
<a href="liberating-llm-capabilities-in-full-duplex-speech-models-2606-07547/">详情 →</a> · <a href="https://arxiv.org/abs/2606.07547" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="acoustic-and-perceptual-differences-between-standard-and-acc-2604-01562/">Acoustic and perceptual differences between standard and accented speech and their voice clones</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音克隆</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">对比标准与重口音普通话及其克隆语音，发现口音影响克隆的感知相似度与可懂度，但说话人嵌入距离在基线校正后无差异。</div>
<div class="card-action">
<a href="acoustic-and-perceptual-differences-between-standard-and-acc-2604-01562/">详情 →</a> · <a href="https://arxiv.org/abs/2604.01562" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="parsa-bench-a-comprehensive-persian-audio-language-model-ben-2603-14456/">PARSA-Bench: A Comprehensive Persian Audio-Language Model Benchmark</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#音频理解基准</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">首个波斯语音频-语言模型基准，含16项任务（10项新），覆盖语音理解、副语言与文化音频推理。</div>
<div class="card-action">
<a href="parsa-bench-a-comprehensive-persian-audio-language-model-ben-2603-14456/">详情 →</a> · <a href="https://arxiv.org/abs/2603.14456" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="audio-visual-turn-taking-prediction-in-cocktail-party-scenar-2609-17056/">Audio-Visual Turn-taking Prediction in Cocktail Party Scenarios</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#音频-视觉说话人轮换预测</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">评估清洁数据训练的视听轮换预测模型在鸡尾酒会噪声场景下的泛化与微调适应行为。</div>
<div class="card-action">
<a href="audio-visual-turn-taking-prediction-in-cocktail-party-scenar-2609-17056/">详情 →</a> · <a href="https://arxiv.org/abs/2609.17056" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="the-machines-are-calling-measuring-automated-and-synthetic-v-2609-11137/">The Machines Are Calling: Measuring Automated and Synthetic Voices in Unwanted Inbound Calls</a>
<div class="card-meta">
<span class="card-score">6.0</span>
<span class="tag-pill">#语音合成检测</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">用语音蜜罐在66天内接听10987通来电，结合音频指纹、商用合成语音检测器与盲听标注，量化机器与合成语音在骚扰电话中的占比。</div>
<div class="card-action">
<a href="the-machines-are-calling-measuring-automated-and-synthetic-v-2609-11137/">详情 →</a> · <a href="https://arxiv.org/abs/2609.11137" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="enhancing-law-enforcement-audio-transcription-a-lora-based-a-2607-27245/">Enhancing Law-Enforcement Audio Transcription: A LoRA-Based Adaptation of Whisper for BWC Footage</a>
<div class="card-meta">
<span class="card-score">5.5</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">用 LoRA 在消费级 4GB 显卡上微调 Whisper，适配执法随身摄像头录音，并接入本体推理生成事件图。</div>
<div class="card-action">
<a href="enhancing-law-enforcement-audio-transcription-a-lora-based-a-2607-27245/">详情 →</a> · <a href="https://arxiv.org/abs/2607.27245" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
