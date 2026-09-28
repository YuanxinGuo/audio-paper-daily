---
title: "语音/音频论文速递 2026-09-28"
date: 2026-09-28T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 6 篇 · 最高分 8.8（#目标说话人提取）"
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
| #目标说话人提取 | 2篇 | `██████████` |
| #语音增强 | 2篇 | `██████████` |
| #乐器分离 | 1篇 | `█████` |
| #声学模拟 | 1篇 | `█████` |
| #语音识别 | 1篇 | `█████` |
| #音频表示学习 | 1篇 | `█████` |
| #语音转换 | 1篇 | `█████` |
| #音频生成 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="adapting-personalized-speech-enhancement-for-low-latency-aud-2609-30631/">Adapting Personalized Speech Enhancement for Low-Latency Audio-Visual Target-Speaker Extraction</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">从个性化语音增强模型出发，加入嘴部视觉特征并联合微调，实现20ms延迟的在线音视频目标说话人提取，误混率从46%降至1.6%。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="coupled-meta-adaptive-filtering-for-active-noise-control-und-2609-30945/">Coupled Meta-Adaptive Filtering for Active Noise Control Under Time-Varying Acoustic Paths</a>
<div class="card-meta">
<span class="card-score">8.3</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出耦合元自适应滤波ANC方法，联合学习控制滤波器与声路径跟踪，在时变声路径下提升降噪与稳定性。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="room-impulse-response-embeddings-for-speech-enhancement-in-n-2609-31041/">Room Impulse Response Embeddings for Speech Enhancement in Noisy and Reverberant Environments</a>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">自监督学习 RIR 嵌入，用教师-学生蒸馏从含噪混响语音中提取，条件化增强模型并降低 WER。</div>
</div></div>

### #目标说话人提取

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="dialogue-based-streaming-audio-visual-target-speaker-extract-2609-30774/">Dialogue-Based Streaming Audio-Visual Target Speaker Extraction with Predictive Dialogue Information</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">提出首个基于真实双人对话的在线音视频目标说话人提取基准，并用语音LLM预测目标未来语音活动来引导低延迟分离器。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="adapting-personalized-speech-enhancement-for-low-latency-aud-2609-30631/">Adapting Personalized Speech Enhancement for Low-Latency Audio-Visual Target-Speaker Extraction</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">从个性化语音增强模型出发，加入嘴部视觉特征并联合微调，实现20ms延迟的在线音视频目标说话人提取，误混率从46%降至1.6%。</div>
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
<a class="card-title" href="shroom-a-python-framework-for-ambisonics-room-acoustics-simu-2603-27342/">SHroom: A Python Framework for Ambisonics Room Acoustics Simulation and Binaural Rendering</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#声学模拟</span>
</div>
<div class="card-tldr">SHroom 是一个开源 Python 库，将房间声学模拟、Ambisonics 编码、双耳渲染与头动、麦克风阵列仿真整合到统一信号接口中。</div>
</div></div>

### #乐器分离

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="music-source-separation-via-stem-discovery-2609-30912/">Music Source Separation via Stem Discovery</a>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#乐器分离</span>
</div>
<div class="card-tldr">MuS3D 用音频查询迭代发现混音中的活跃音源，正确检测时匹配手动查询基线并超越文本查询 SOTA。</div>
</div></div>

## 📊 完整排行榜

| 排名 | 论文 | 评分 | 主任务 |
| --- | --- | --- | --- |
| 🥇 | [Dialogue-Based Streaming Audio-Visual Target Speaker Extract…](dialogue-based-streaming-audio-visual-target-speaker-extract-2609-30774/) 🎯 | **8.8** | #目标说话人提取 |
| 🥈 | [Adapting Personalized Speech Enhancement for Low-Latency Aud…](adapting-personalized-speech-enhancement-for-low-latency-aud-2609-30631/) 🎯 | **8.8** | #目标说话人提取 |
| 🥉 | [Coupled Meta-Adaptive Filtering for Active Noise Control Und…](coupled-meta-adaptive-filtering-for-active-noise-control-und-2609-30945/) 🎯 | **8.3** | #语音增强 |
| 4. | [Room Impulse Response Embeddings for Speech Enhancement in N…](room-impulse-response-embeddings-for-speech-enhancement-in-n-2609-31041/) 🎯 | **8.0** | #语音增强 |
| 5. | [Music Source Separation via Stem Discovery](music-source-separation-via-stem-discovery-2609-30912/) 🎯 | **8.0** | #乐器分离 |
| 6. | [SHroom: A Python Framework for Ambisonics Room Acoustics Sim…](shroom-a-python-framework-for-ambisonics-room-acoustics-simu-2603-27342/) 🎯 | **7.8** | #声学模拟 |
| 7. | [Direct Preference Optimization for English-Mandarin Code-Swi…](direct-preference-optimization-for-english-mandarin-code-swi-2605-23975/) | **7.0** | #语音识别 |
| 8. | [Joint Analysis of Latent Dimensionality and Frame Rate in Co…](joint-analysis-of-latent-dimensionality-and-frame-rate-in-co-2609-29780/) | **6.8** | #音频表示学习 |
| 9. | [Provable Speech Attributes Conversion via Latent Independenc…](provable-speech-attributes-conversion-via-latent-independenc-2510-05191/) | **6.8** | #语音转换 |
| 10. | [AV-GRPO: Modality-Anchored Decoupling Diffusion Reinforcemen…](av-grpo-modality-anchored-decoupling-diffusion-reinforcement-2609-29816/) | **6.5** | #音频生成 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="dialogue-based-streaming-audio-visual-target-speaker-extract-2609-30774/">Dialogue-Based Streaming Audio-Visual Target Speaker Extraction with Predictive Dialogue Information</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#目标说话人提取</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出首个基于真实双人对话的在线音视频目标说话人提取基准，并用语音LLM预测目标未来语音活动来引导低延迟分离器。</div>
<div class="card-action">
<a href="dialogue-based-streaming-audio-visual-target-speaker-extract-2609-30774/">详情 →</a> · <a href="https://arxiv.org/abs/2609.30774" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="adapting-personalized-speech-enhancement-for-low-latency-aud-2609-30631/">Adapting Personalized Speech Enhancement for Low-Latency Audio-Visual Target-Speaker Extraction</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#目标说话人提取</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">从个性化语音增强模型出发，加入嘴部视觉特征并联合微调，实现20ms延迟的在线音视频目标说话人提取，误混率从46%降至1.6%。</div>
<div class="card-action">
<a href="adapting-personalized-speech-enhancement-for-low-latency-aud-2609-30631/">详情 →</a> · <a href="https://arxiv.org/abs/2609.30631" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="coupled-meta-adaptive-filtering-for-active-noise-control-und-2609-30945/">Coupled Meta-Adaptive Filtering for Active Noise Control Under Time-Varying Acoustic Paths</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.3</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出耦合元自适应滤波ANC方法，联合学习控制滤波器与声路径跟踪，在时变声路径下提升降噪与稳定性。</div>
<div class="card-action">
<a href="coupled-meta-adaptive-filtering-for-active-noise-control-und-2609-30945/">详情 →</a> · <a href="https://arxiv.org/abs/2609.30945" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="room-impulse-response-embeddings-for-speech-enhancement-in-n-2609-31041/">Room Impulse Response Embeddings for Speech Enhancement in Noisy and Reverberant Environments</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">自监督学习 RIR 嵌入，用教师-学生蒸馏从含噪混响语音中提取，条件化增强模型并降低 WER。</div>
<div class="card-action">
<a href="room-impulse-response-embeddings-for-speech-enhancement-in-n-2609-31041/">详情 →</a> · <a href="https://arxiv.org/abs/2609.31041" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="music-source-separation-via-stem-discovery-2609-30912/">Music Source Separation via Stem Discovery</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#乐器分离</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">MuS3D 用音频查询迭代发现混音中的活跃音源，正确检测时匹配手动查询基线并超越文本查询 SOTA。</div>
<div class="card-action">
<a href="music-source-separation-via-stem-discovery-2609-30912/">详情 →</a> · <a href="https://arxiv.org/abs/2609.30912" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="shroom-a-python-framework-for-ambisonics-room-acoustics-simu-2603-27342/">SHroom: A Python Framework for Ambisonics Room Acoustics Simulation and Binaural Rendering</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#声学模拟</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">SHroom 是一个开源 Python 库，将房间声学模拟、Ambisonics 编码、双耳渲染与头动、麦克风阵列仿真整合到统一信号接口中。</div>
<div class="card-action">
<a href="shroom-a-python-framework-for-ambisonics-room-acoustics-simu-2603-27342/">详情 →</a> · <a href="https://arxiv.org/abs/2603.27342" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="direct-preference-optimization-for-english-mandarin-code-swi-2605-23975/">Direct Preference Optimization for English-Mandarin Code-Switching Speech Recognition in Audio LLMs</a>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用DPO对齐Audio LLM，构造偏好对纠正英汉语码切换识别中的漏语、翻译替代与幻觉三类失败模式。</div>
<div class="card-action">
<a href="direct-preference-optimization-for-english-mandarin-code-swi-2605-23975/">详情 →</a> · <a href="https://arxiv.org/abs/2605.23975" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="joint-analysis-of-latent-dimensionality-and-frame-rate-in-co-2609-29780/">Joint Analysis of Latent Dimensionality and Frame Rate in Continuous Audio Encoders</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频表示学习</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">系统训练16个不同隐宽度与帧率的连续音频编码器，发现ASR与SQA偏好中等宽度高帧率，且宽度-帧率存在交互作用。</div>
<div class="card-action">
<a href="joint-analysis-of-latent-dimensionality-and-frame-rate-in-co-2609-29780/">详情 →</a> · <a href="https://arxiv.org/abs/2609.29780" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="provable-speech-attributes-conversion-via-latent-independenc-2510-05191/">Provable Speech Attributes Conversion via Latent Independence</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音转换</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出语音属性转换的理论框架，用潜空间独立性约束给出精确转换的充分条件，并落地为实用语音转换方法。</div>
<div class="card-action">
<a href="provable-speech-attributes-conversion-via-latent-independenc-2510-05191/">详情 →</a> · <a href="https://arxiv.org/abs/2510.05191" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="av-grpo-modality-anchored-decoupling-diffusion-reinforcement-2609-29816/">AV-GRPO: Modality-Anchored Decoupling Diffusion Reinforcement Learning for Joint Audio-Video Generation</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#音频生成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出AV-GRPO，用模态锚定的解耦扩散强化学习框架与5DAV数据集，提升音视频联合生成的质量、语义对齐与跨模态同步。</div>
<div class="card-action">
<a href="av-grpo-modality-anchored-decoupling-diffusion-reinforcement-2609-29816/">详情 →</a> · <a href="https://arxiv.org/abs/2609.29816" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
