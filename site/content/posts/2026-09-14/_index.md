---
title: "语音/音频论文速递 2026-09-14"
date: 2026-09-14T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 5 篇 · 最高分 8.8（#乐器分离）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">5</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.8</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音分离 | 2篇 | `██████████` |
| #音乐生成 | 2篇 | `██████████` |
| #乐器分离 | 1篇 | `█████` |
| #语音增强 | 1篇 | `█████` |
| #语音到语音翻译 | 1篇 | `█████` |
| #音频生成 | 1篇 | `█████` |
| #双耳音频 | 1篇 | `█████` |
| #音频理解可解释性 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="driftse-speech-enhancement-with-generative-drifting-2609-12252/">DriftSE: Speech Enhancement with Generative Drifting</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">DriftSE 将语音增强建模为潜空间分布漂移平衡问题，用双潜空间（语义+声学）漂移实现 1 NFE 一步增强，并支持无配对跨数据集训练。</div>
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
<a class="card-title" href="neural-multichannel-distant-speaker-diarization-with-heavy-t-2609-12154/">Neural Multichannel Distant Speaker Diarization with Heavy-tailed Source Separation Model</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">用重尾分布（GGD 与 Student's t）替换 FCASA 中的高斯方差建模，联合学习多通道盲源分离与远场说话人日志，DER/JER 一致下降。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="location-based-training-with-complementary-folded-linear-ord-2609-12629/">Location-based Training with Complementary Folded Linear Orderings for Multichannel Speech Separation</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">针对平面阵列多通道语音分离，提出折叠线性排序的LBT-FLO，用方位角引导打分集成多个排序，缓解环形排序的环绕不连续问题。</div>
</div></div>

### #双耳音频

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="continue-adapt-or-yield-in-turn-adaptation-to-overlapping-sp-2609-13117/">Continue, Adapt, or Yield: In-Turn Adaptation to Overlapping Speech in Full-Duplex Agents</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">提出 Duplex Cue 评测框架，将全双工语音代理对听者插话的响应分为继续、轮内适应与让出三类，并用 300 条真实对话线索对比人类与 PersonaPlex。</div>
</div></div>

### #乐器分离

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="real-time-music-source-separation-on-a-low-power-audio-dsp-2609-12201/">Real-Time Music Source Separation on a Low-Power Audio DSP</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#乐器分离</span>
</div>
<div class="card-tldr">在2MB SRAM、2.07 GMAC/s的低功耗音频DSP上实现实时音乐源分离，MUSDB18-HQ达4.70 dB cSDR，10.43 ms/11.6 ms hop。</div>
</div></div>

## 📊 完整排行榜

| 排名 | 论文 | 评分 | 主任务 |
| --- | --- | --- | --- |
| 🥇 | [Real-Time Music Source Separation on a Low-Power Audio DSP](real-time-music-source-separation-on-a-low-power-audio-dsp-2609-12201/) 🎯 | **8.8** | #乐器分离 |
| 🥈 | [DriftSE: Speech Enhancement with Generative Drifting](driftse-speech-enhancement-with-generative-drifting-2609-12252/) 🎯 | **8.8** | #语音增强 |
| 🥉 | [Neural Multichannel Distant Speaker Diarization with Heavy-t…](neural-multichannel-distant-speaker-diarization-with-heavy-t-2609-12154/) 🎯 | **8.2** | #语音分离 |
| 4. | [Kraken: LLM-based Speech-to-Speech Translation via Low-bitra…](kraken-llm-based-speech-to-speech-translation-via-low-bitrat-2609-13045/) | **7.8** | #语音到语音翻译 |
| 5. | [Location-based Training with Complementary Folded Linear Ord…](location-based-training-with-complementary-folded-linear-ord-2609-12629/) 🎯 | **7.8** | #语音分离 |
| 6. | [PhaseGAN: High-Fidelity Vocoder via Decoupled Amplitude and …](phasegan-high-fidelity-vocoder-via-decoupled-amplitude-and-g-2609-12918/) | **7.0** | #音频生成 |
| 7. | [CMA-OT: Hierarchical Expert Supervision for Dance-to-Music G…](cma-ot-hierarchical-expert-supervision-for-dance-to-music-ge-2609-13118/) | **6.8** | #音乐生成 |
| 8. | [Continue, Adapt, or Yield: In-Turn Adaptation to Overlapping…](continue-adapt-or-yield-in-turn-adaptation-to-overlapping-sp-2609-13117/) 🎯 | **6.8** | #双耳音频 |
| 9. | [DiffSynth-Music: Audio-Conditioned KV-Cache Adapters for Con…](diffsynth-music-audio-conditioned-kv-cache-adapters-for-cont-2609-12774/) | **6.8** | #音乐生成 |
| 10. | [What Did the MLLM Hear? Token-Level Spectro-Temporal Groundi…](what-did-the-mllm-hear-token-level-spectro-temporal-groundin-2609-12663/) | **6.8** | #音频理解可解释性 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="real-time-music-source-separation-on-a-low-power-audio-dsp-2609-12201/">Real-Time Music Source Separation on a Low-Power Audio DSP</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#乐器分离</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">在2MB SRAM、2.07 GMAC/s的低功耗音频DSP上实现实时音乐源分离，MUSDB18-HQ达4.70 dB cSDR，10.43 ms/11.6 ms hop。</div>
<div class="card-action">
<a href="real-time-music-source-separation-on-a-low-power-audio-dsp-2609-12201/">详情 →</a> · <a href="https://arxiv.org/abs/2609.12201" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="driftse-speech-enhancement-with-generative-drifting-2609-12252/">DriftSE: Speech Enhancement with Generative Drifting</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">DriftSE 将语音增强建模为潜空间分布漂移平衡问题，用双潜空间（语义+声学）漂移实现 1 NFE 一步增强，并支持无配对跨数据集训练。</div>
<div class="card-action">
<a href="driftse-speech-enhancement-with-generative-drifting-2609-12252/">详情 →</a> · <a href="https://arxiv.org/abs/2609.12252" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="neural-multichannel-distant-speaker-diarization-with-heavy-t-2609-12154/">Neural Multichannel Distant Speaker Diarization with Heavy-tailed Source Separation Model</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音分离</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用重尾分布（GGD 与 Student's t）替换 FCASA 中的高斯方差建模，联合学习多通道盲源分离与远场说话人日志，DER/JER 一致下降。</div>
<div class="card-action">
<a href="neural-multichannel-distant-speaker-diarization-with-heavy-t-2609-12154/">详情 →</a> · <a href="https://arxiv.org/abs/2609.12154" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="kraken-llm-based-speech-to-speech-translation-via-low-bitrat-2609-13045/">Kraken: LLM-based Speech-to-Speech Translation via Low-bitrate VQ and Dual-path Source Conditioning</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音到语音翻译</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">Kraken 用单层 VQ 低比特率 token 重建 SSL 特征，并加源语音条件化的 Autowave-X 解码器，实现 S2ST 的非语言信息迁移。</div>
<div class="card-action">
<a href="kraken-llm-based-speech-to-speech-translation-via-low-bitrat-2609-13045/">详情 →</a> · <a href="https://arxiv.org/abs/2609.13045" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="location-based-training-with-complementary-folded-linear-ord-2609-12629/">Location-based Training with Complementary Folded Linear Orderings for Multichannel Speech Separation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音分离</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">针对平面阵列多通道语音分离，提出折叠线性排序的LBT-FLO，用方位角引导打分集成多个排序，缓解环形排序的环绕不连续问题。</div>
<div class="card-action">
<a href="location-based-training-with-complementary-folded-linear-ord-2609-12629/">详情 →</a> · <a href="https://arxiv.org/abs/2609.12629" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="phasegan-high-fidelity-vocoder-via-decoupled-amplitude-and-g-2609-12918/">PhaseGAN: High-Fidelity Vocoder via Decoupled Amplitude and GAN-Driven Phase Reconstruction</a>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#音频生成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">PhaseGAN 提出 mel→幅度→相位的解耦重建流程，用 GAN 驱动相位估计，以约 500K 参数实现高保真声码器。</div>
<div class="card-action">
<a href="phasegan-high-fidelity-vocoder-via-decoupled-amplitude-and-g-2609-12918/">详情 →</a> · <a href="https://arxiv.org/abs/2609.12918" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="cma-ot-hierarchical-expert-supervision-for-dance-to-music-ge-2609-13118/">CMA-OT: Hierarchical Expert Supervision for Dance-to-Music Generation</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">用外部音乐专家对生成器隐特征做分层监督，结合课程式多尺度学习与尺度感知最优传输对齐，实现舞蹈到音乐的节奏与风格同步生成。</div>
<div class="card-action">
<a href="cma-ot-hierarchical-expert-supervision-for-dance-to-music-ge-2609-13118/">详情 →</a> · <a href="https://arxiv.org/abs/2609.13118" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="continue-adapt-or-yield-in-turn-adaptation-to-overlapping-sp-2609-13117/">Continue, Adapt, or Yield: In-Turn Adaptation to Overlapping Speech in Full-Duplex Agents</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">提出 Duplex Cue 评测框架，将全双工语音代理对听者插话的响应分为继续、轮内适应与让出三类，并用 300 条真实对话线索对比人类与 PersonaPlex。</div>
<div class="card-action">
<a href="continue-adapt-or-yield-in-turn-adaptation-to-overlapping-sp-2609-13117/">详情 →</a> · <a href="https://arxiv.org/abs/2609.13117" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="diffsynth-music-audio-conditioned-kv-cache-adapters-for-cont-2609-12774/">DiffSynth-Music: Audio-Conditioned KV-Cache Adapters for Controllable Music Generation</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">用逐层KV注入为音乐扩散Transformer加入节拍、人声、伴奏、韵律与参考音频五类可控条件。</div>
<div class="card-action">
<a href="diffsynth-music-audio-conditioned-kv-cache-adapters-for-cont-2609-12774/">详情 →</a> · <a href="https://arxiv.org/abs/2609.12774" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="what-did-the-mllm-hear-token-level-spectro-temporal-groundin-2609-12663/">What Did the MLLM Hear? Token-Level Spectro-Temporal Grounding for Audio MLLM Explainability</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频理解可解释性</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出 STAG，首个针对音频 MLLM 生成 caption 的 token 级时频归因框架，用词汇投影与频谱遮挡合成相关性图。</div>
<div class="card-action">
<a href="what-did-the-mllm-hear-token-level-spectro-temporal-groundin-2609-12663/">详情 →</a> · <a href="https://arxiv.org/abs/2609.12663" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
