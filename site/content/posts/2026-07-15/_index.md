---
title: "语音/音频论文速递 2026-07-15"
date: 2026-07-15T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 7 篇 · 最高分 9.2（#目标说话人提取）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">7</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">9.2</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音增强 | 3篇 | `██████████` |
| #目标说话人提取 | 2篇 | `███████` |
| #乐器分离 | 1篇 | `███` |
| #语音合成 | 1篇 | `███` |
| #语音分离 | 1篇 | `███` |
| #语音识别 | 1篇 | `███` |
| #音频前端处理 | 1篇 | `███` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="breaking-the-quality-intelligibility-trade-off-in-streaming--2607-10191/">Breaking the Quality--Intelligibility Trade-off in Streaming Target Speaker Extraction via Deep-Feature-Anchored Preference Optimization</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">提出WavLM锚定的直接偏好优化策略，打破流式目标说话人提取中质量与可懂度的权衡，在560ms块大小下实现WER从0.138降至0.123。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="cofi-lite-pushing-the-limits-of-ultra-lightweight-speech-enh-2607-10142/">CoFi-Lite: Pushing the Limits of Ultra-Lightweight Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出CoFi-Lite超轻量语音增强模型，通过粗-细双流编码器-解码器及跨路径融合模块，以极低计算量超越现有轻量基线。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="unified-architecture-and-unsupervised-speech-disentanglement-2505-12288/">Unified Architecture and Unsupervised Speech Disentanglement for Speaker Embedding-Free Enrollment in Personalized Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出两种模型USEF-PNet和DSEF-PNet，通过统一架构和无监督语音解耦，实现无需说话人嵌入的个性化语音增强，提升鲁棒性。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="teaching-speech-enhancement-models-to-sing-domain-adaptation-2607-11630/">Teaching Speech Enhancement Models to Sing: Domain Adaptation from Speech Enhancement to Singing Voice Separation</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#乐器分离</span>
</div>
<div class="card-tldr">将歌声分离视为从语音增强到歌声分离的域自适应，通过全微调或LoRA微调预训练语音增强模型，在数据稀缺场景下有效提升歌声分离性能。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="where-speech-enhancement-hurts-recognition-an-inference-time-2607-11157/">Where Speech Enhancement Hurts Recognition: An Inference Time Polar Projection Diagnosis</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出推理时极坐标投影诊断法，分析语音增强中幅度和相位对ASR的影响，发现幅度是关键因素，相位无益，并给出无需重训练的缓解方案。</div>
</div></div>

### #目标说话人提取

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="breaking-the-quality-intelligibility-trade-off-in-streaming--2607-10191/">Breaking the Quality--Intelligibility Trade-off in Streaming Target Speaker Extraction via Deep-Feature-Anchored Preference Optimization</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">提出WavLM锚定的直接偏好优化策略，打破流式目标说话人提取中质量与可懂度的权衡，在560ms块大小下实现WER从0.138降至0.123。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="the-sonicagi-system-for-the-real-tse-challenge-2607-11083/">The SonicAGI System for the REAL-TSE Challenge</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">提出数据驱动方法结合模拟与真实重叠语音，设计低延迟在线系统SwiftNet-Lookahead和离线系统USEF-TFGridNet，在REAL-TSE挑战赛中取得第二和第五名。</div>
</div></div>

### #语音分离

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="the-sonicagi-system-for-the-real-tse-challenge-2607-11083/">The SonicAGI System for the REAL-TSE Challenge</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">提出数据驱动方法结合模拟与真实重叠语音，设计低延迟在线系统SwiftNet-Lookahead和离线系统USEF-TFGridNet，在REAL-TSE挑战赛中取得第二和第五名。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="difference-driven-gating-adaptive-feature-fusion-for-u-net-d-2607-11096/">Difference-Driven Gating: Adaptive Feature Fusion for U-Net Decoder</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">提出基于特征差异和熵差异的门控机制，用于U-Net解码器中的自适应特征融合，在语音分离等任务上超越现有注意力融合方法。</div>
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
<a class="card-title" href="teaching-speech-enhancement-models-to-sing-domain-adaptation-2607-11630/">Teaching Speech Enhancement Models to Sing: Domain Adaptation from Speech Enhancement to Singing Voice Separation</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#乐器分离</span>
</div>
<div class="card-tldr">将歌声分离视为从语音增强到歌声分离的域自适应，通过全微调或LoRA微调预训练语音增强模型，在数据稀缺场景下有效提升歌声分离性能。</div>
</div></div>

## 📊 完整排行榜

| 排名 | 论文 | 评分 | 主任务 |
| --- | --- | --- | --- |
| 🥇 | [Breaking the Quality--Intelligibility Trade-off in Streaming…](breaking-the-quality-intelligibility-trade-off-in-streaming--2607-10191/) 🎯 | **9.2** | #目标说话人提取 |
| 🥈 | [CoFi-Lite: Pushing the Limits of Ultra-Lightweight Speech En…](cofi-lite-pushing-the-limits-of-ultra-lightweight-speech-enh-2607-10142/) 🎯 | **9.2** | #语音增强 |
| 🥉 | [The SonicAGI System for the REAL-TSE Challenge](the-sonicagi-system-for-the-real-tse-challenge-2607-11083/) 🎯 | **8.8** | #目标说话人提取 |
| 4. | [Unified Architecture and Unsupervised Speech Disentanglement…](unified-architecture-and-unsupervised-speech-disentanglement-2505-12288/) 🎯 | **8.8** | #语音增强 |
| 5. | [Teaching Speech Enhancement Models to Sing: Domain Adaptatio…](teaching-speech-enhancement-models-to-sing-domain-adaptation-2607-11630/) 🎯 | **8.8** | #乐器分离 |
| 6. | [Where Speech Enhancement Hurts Recognition: An Inference Tim…](where-speech-enhancement-hurts-recognition-an-inference-time-2607-11157/) 🎯 | **8.5** | #语音增强 |
| 7. | [Fr\'echet Distance Loss on Speech Representations for Text-t…](fr-echet-distance-loss-on-speech-representations-for-text-to-2607-06027/) | **8.2** | #语音合成 |
| 8. | [Difference-Driven Gating: Adaptive Feature Fusion for U-Net …](difference-driven-gating-adaptive-feature-fusion-for-u-net-d-2607-11096/) 🎯 | **8.2** | #语音分离 |
| 9. | [PRiSM: Benchmarking Phone Realization in Speech Models](prism-benchmarking-phone-realization-in-speech-models-2601-14046/) | **7.8** | #语音识别 |
| 10. | [MelT: A Portable, Single-GEMM Mel Audio Frontend via Non-Uni…](melt-a-portable-single-gemm-mel-audio-frontend-via-non-unifo-2606-01009/) | **7.8** | #音频前端处理 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="breaking-the-quality-intelligibility-trade-off-in-streaming--2607-10191/">Breaking the Quality--Intelligibility Trade-off in Streaming Target Speaker Extraction via Deep-Feature-Anchored Preference Optimization</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#目标说话人提取</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出WavLM锚定的直接偏好优化策略，打破流式目标说话人提取中质量与可懂度的权衡，在560ms块大小下实现WER从0.138降至0.123。</div>
<div class="card-action">
<a href="breaking-the-quality-intelligibility-trade-off-in-streaming--2607-10191/">详情 →</a> · <a href="https://arxiv.org/abs/2607.10191" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="cofi-lite-pushing-the-limits-of-ultra-lightweight-speech-enh-2607-10142/">CoFi-Lite: Pushing the Limits of Ultra-Lightweight Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出CoFi-Lite超轻量语音增强模型，通过粗-细双流编码器-解码器及跨路径融合模块，以极低计算量超越现有轻量基线。</div>
<div class="card-action">
<a href="cofi-lite-pushing-the-limits-of-ultra-lightweight-speech-enh-2607-10142/">详情 →</a> · <a href="https://arxiv.org/abs/2607.10142" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="the-sonicagi-system-for-the-real-tse-challenge-2607-11083/">The SonicAGI System for the REAL-TSE Challenge</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#目标说话人提取</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出数据驱动方法结合模拟与真实重叠语音，设计低延迟在线系统SwiftNet-Lookahead和离线系统USEF-TFGridNet，在REAL-TSE挑战赛中取得第二和第五名。</div>
<div class="card-action">
<a href="the-sonicagi-system-for-the-real-tse-challenge-2607-11083/">详情 →</a> · <a href="https://arxiv.org/abs/2607.11083" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="unified-architecture-and-unsupervised-speech-disentanglement-2505-12288/">Unified Architecture and Unsupervised Speech Disentanglement for Speaker Embedding-Free Enrollment in Personalized Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出两种模型USEF-PNet和DSEF-PNet，通过统一架构和无监督语音解耦，实现无需说话人嵌入的个性化语音增强，提升鲁棒性。</div>
<div class="card-action">
<a href="unified-architecture-and-unsupervised-speech-disentanglement-2505-12288/">详情 →</a> · <a href="https://arxiv.org/abs/2505.12288" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="teaching-speech-enhancement-models-to-sing-domain-adaptation-2607-11630/">Teaching Speech Enhancement Models to Sing: Domain Adaptation from Speech Enhancement to Singing Voice Separation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#乐器分离</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">将歌声分离视为从语音增强到歌声分离的域自适应，通过全微调或LoRA微调预训练语音增强模型，在数据稀缺场景下有效提升歌声分离性能。</div>
<div class="card-action">
<a href="teaching-speech-enhancement-models-to-sing-domain-adaptation-2607-11630/">详情 →</a> · <a href="https://arxiv.org/abs/2607.11630" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="where-speech-enhancement-hurts-recognition-an-inference-time-2607-11157/">Where Speech Enhancement Hurts Recognition: An Inference Time Polar Projection Diagnosis</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出推理时极坐标投影诊断法，分析语音增强中幅度和相位对ASR的影响，发现幅度是关键因素，相位无益，并给出无需重训练的缓解方案。</div>
<div class="card-action">
<a href="where-speech-enhancement-hurts-recognition-an-inference-time-2607-11157/">详情 →</a> · <a href="https://arxiv.org/abs/2607.11157" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="fr-echet-distance-loss-on-speech-representations-for-text-to-2607-06027/">Fr\'echet Distance Loss on Speech Representations for Text-to-Speech Synthesis</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出SR-FD损失，通过匹配语音表示的分布来提升少步扩散TTS的可懂度，在Seed-TTS上降低WER 36.5%。</div>
<div class="card-action">
<a href="fr-echet-distance-loss-on-speech-representations-for-text-to-2607-06027/">详情 →</a> · <a href="https://arxiv.org/abs/2607.06027" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="difference-driven-gating-adaptive-feature-fusion-for-u-net-d-2607-11096/">Difference-Driven Gating: Adaptive Feature Fusion for U-Net Decoder</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音分离</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出基于特征差异和熵差异的门控机制，用于U-Net解码器中的自适应特征融合，在语音分离等任务上超越现有注意力融合方法。</div>
<div class="card-action">
<a href="difference-driven-gating-adaptive-feature-fusion-for-u-net-d-2607-11096/">详情 →</a> · <a href="https://arxiv.org/abs/2607.11096" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="prism-benchmarking-phone-realization-in-speech-models-2601-14046/">PRiSM: Benchmarking Phone Realization in Speech Models</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">PRiSM 是首个开源音素识别基准，通过内在和外在评估暴露语音模型在音素感知上的盲点，发现多语言训练是关键，编码器-CTC 模型最稳定。</div>
<div class="card-action">
<a href="prism-benchmarking-phone-realization-in-speech-models-2601-14046/">详情 →</a> · <a href="https://arxiv.org/abs/2601.14046" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="melt-a-portable-single-gemm-mel-audio-frontend-via-non-unifo-2606-01009/">MelT: A Portable, Single-GEMM Mel Audio Frontend via Non-Uniform DFT with Measured Latency and Energy Gains on GPUs</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音频前端处理</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出MelT，将Mel频谱提取转化为单次GEMM操作，在GPU上实现1.64-3.29倍延迟降低和最高3.03倍能耗降低，且不损失下游任务精度。</div>
<div class="card-action">
<a href="melt-a-portable-single-gemm-mel-audio-frontend-via-non-unifo-2606-01009/">详情 →</a> · <a href="https://arxiv.org/abs/2606.01009" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
