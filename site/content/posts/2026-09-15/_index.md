---
title: "语音/音频论文速递 2026-09-15"
date: 2026-09-15T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 4 篇 · 最高分 8.8（#语音增强）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">4</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.8</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音合成 | 3篇 | `██████████` |
| #语音增强 | 2篇 | `███████` |
| #音乐生成 | 1篇 | `███` |
| #语音质量评估 | 1篇 | `███` |
| #音频评测基准 | 1篇 | `███` |
| #语音识别 | 1篇 | `███` |
| #语音深度伪造检测 | 1篇 | `███` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="directivity-conditioned-low-latency-neural-filtering-for-spe-2609-15760/">Directivity-Conditioned Low-Latency Neural Filtering for Speech Enhancement in Hearing Aids</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">面向助听器的10ms低延迟DNN，用FiLM在推理时调节指向性模式，并设计保持跨通道频谱关系的损失函数。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="dualspecse-a-dual-path-speech-enhancement-network-integratin-2609-13911/">DualSpecSE: A Dual-Path Speech Enhancement Network Integrating Mel and Complex Spectrograms</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出双分支语音增强网络，Mel 分支供 ASR、复数谱分支做高保真重建，通过交互与融合模块交换信息。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="the-voicemos-challenge-2026-evaluating-speech-enhancement-em-2609-13792/">The VoiceMOS Challenge 2026: Evaluating Speech Enhancement, Emotional TTS and Accented TTS Systems</a>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#语音质量评估</span>
</div>
<div class="card-tldr">VoiceMOS Challenge 2026 第五届，聚焦语音领域设三条赛道：增强语音绝对/比较评分、情感TTS自然度与情感、编解码合成语音的说话人与口音相似度。</div>
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
<a class="card-title" href="directivity-conditioned-low-latency-neural-filtering-for-spe-2609-15760/">Directivity-Conditioned Low-Latency Neural Filtering for Speech Enhancement in Hearing Aids</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">面向助听器的10ms低延迟DNN，用FiLM在推理时调节指向性模式，并设计保持跨通道频谱关系的损失函数。</div>
</div></div>

### #乐器分离

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="duotok-source-aware-dual-track-music-tokenization-for-vocal--2511-20224/">DuoTok: Source-Aware Dual-Track Music Tokenization for Vocal-Accompaniment Generation</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#音乐生成</span>
</div>
<div class="card-tldr">DuoTok 提出源感知双轨音乐 tokenizer，通过分阶段解耦与硬路由码本，在超低码率下兼顾人声-伴奏生成的可预测性与重建保真度。</div>
</div></div>

## 📊 完整排行榜

| 排名 | 论文 | 评分 | 主任务 |
| --- | --- | --- | --- |
| 🥇 | [Directivity-Conditioned Low-Latency Neural Filtering for Spe…](directivity-conditioned-low-latency-neural-filtering-for-spe-2609-15760/) 🎯 | **8.8** | #语音增强 |
| 🥈 | [DuoTok: Source-Aware Dual-Track Music Tokenization for Vocal…](duotok-source-aware-dual-track-music-tokenization-for-vocal--2511-20224/) 🎯 | **8.2** | #音乐生成 |
| 🥉 | [DualSpecSE: A Dual-Path Speech Enhancement Network Integrati…](dualspecse-a-dual-path-speech-enhancement-network-integratin-2609-13911/) 🎯 | **7.8** | #语音增强 |
| 4. | [The VoiceMOS Challenge 2026: Evaluating Speech Enhancement, …](the-voicemos-challenge-2026-evaluating-speech-enhancement-em-2609-13792/) 🎯 | **7.0** | #语音质量评估 |
| 5. | [Putting HUMANS first: Efficient LAM Evaluation with Human Pr…](putting-humans-first-efficient-lam-evaluation-with-human-pre-2605-00022/) | **6.8** | #音频评测基准 |
| 6. | [Sparse Weight and Edge Circuit Discovery in Transformer-base…](sparse-weight-and-edge-circuit-discovery-in-transformer-base-2609-10645/) | **6.8** | #语音识别 |
| 7. | [Speech Generation Speaker Poisoning: Capability Erasure in Z…](speech-generation-speaker-poisoning-capability-erasure-in-ze-2603-07551/) | **6.8** | #语音合成 |
| 8. | [How Well Do Current Speech Deepfake Detection Methods Genera…](how-well-do-current-speech-deepfake-detection-methods-genera-2603-05852/) | **6.8** | #语音深度伪造检测 |
| 9. | [Controllable Dysarthric Speech Synthesis with Patient-Specif…](controllable-dysarthric-speech-synthesis-with-patient-specif-2602-08696/) | **6.8** | #语音合成 |
| 10. | [Mask, Sample, Revise: A Revisable CTMC Inference Stack for G…](mask-sample-revise-a-revisable-ctmc-inference-stack-for-guid-2606-13989/) | **6.5** | #语音合成 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="directivity-conditioned-low-latency-neural-filtering-for-spe-2609-15760/">Directivity-Conditioned Low-Latency Neural Filtering for Speech Enhancement in Hearing Aids</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">面向助听器的10ms低延迟DNN，用FiLM在推理时调节指向性模式，并设计保持跨通道频谱关系的损失函数。</div>
<div class="card-action">
<a href="directivity-conditioned-low-latency-neural-filtering-for-spe-2609-15760/">详情 →</a> · <a href="https://arxiv.org/abs/2609.15760" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="duotok-source-aware-dual-track-music-tokenization-for-vocal--2511-20224/">DuoTok: Source-Aware Dual-Track Music Tokenization for Vocal-Accompaniment Generation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">DuoTok 提出源感知双轨音乐 tokenizer，通过分阶段解耦与硬路由码本，在超低码率下兼顾人声-伴奏生成的可预测性与重建保真度。</div>
<div class="card-action">
<a href="duotok-source-aware-dual-track-music-tokenization-for-vocal--2511-20224/">详情 →</a> · <a href="https://arxiv.org/abs/2511.20224" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="dualspecse-a-dual-path-speech-enhancement-network-integratin-2609-13911/">DualSpecSE: A Dual-Path Speech Enhancement Network Integrating Mel and Complex Spectrograms</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出双分支语音增强网络，Mel 分支供 ASR、复数谱分支做高保真重建，通过交互与融合模块交换信息。</div>
<div class="card-action">
<a href="dualspecse-a-dual-path-speech-enhancement-network-integratin-2609-13911/">详情 →</a> · <a href="https://arxiv.org/abs/2609.13911" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="the-voicemos-challenge-2026-evaluating-speech-enhancement-em-2609-13792/">The VoiceMOS Challenge 2026: Evaluating Speech Enhancement, Emotional TTS and Accented TTS Systems</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#语音质量评估</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">VoiceMOS Challenge 2026 第五届，聚焦语音领域设三条赛道：增强语音绝对/比较评分、情感TTS自然度与情感、编解码合成语音的说话人与口音相似度。</div>
<div class="card-action">
<a href="the-voicemos-challenge-2026-evaluating-speech-enhancement-em-2609-13792/">详情 →</a> · <a href="https://arxiv.org/abs/2609.13792" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="putting-humans-first-efficient-lam-evaluation-with-human-pre-2605-00022/">Putting HUMANS first: Efficient LAM Evaluation with Human Preference Alignment</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频评测基准</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">研究用50条样本子集替代完整基准评测大音频模型，与全量分数相关性达0.93，并开源HUMANS基准。</div>
<div class="card-action">
<a href="putting-humans-first-efficient-lam-evaluation-with-human-pre-2605-00022/">详情 →</a> · <a href="https://arxiv.org/abs/2605.00022" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="sparse-weight-and-edge-circuit-discovery-in-transformer-base-2609-10645/">Sparse Weight and Edge Circuit Discovery in Transformer-based Acoustic Models</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">首次将 DiscoGP 电路发现扩展到语音编码器，在 HuBERT 与 Wav2Vec 2.0 上找到极紧凑子图，性能常匹配甚至超过完整编码器。</div>
<div class="card-action">
<a href="sparse-weight-and-edge-circuit-discovery-in-transformer-base-2609-10645/">详情 →</a> · <a href="https://arxiv.org/abs/2609.10645" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="speech-generation-speaker-poisoning-capability-erasure-in-ze-2603-07551/">Speech Generation Speaker Poisoning: Capability Erasure in Zero-Shot Text-to-Speech</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出零样本TTS的说话人投毒任务SGSP，用推理过滤与参数修改抑制目标说话人，并给出AUC与FSSIM评估协议。</div>
<div class="card-action">
<a href="speech-generation-speaker-poisoning-capability-erasure-in-ze-2603-07551/">详情 →</a> · <a href="https://arxiv.org/abs/2603.07551" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="how-well-do-current-speech-deepfake-detection-methods-genera-2603-05852/">How Well Do Current Speech Deepfake Detection Methods Generalize to the Real World?</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音深度伪造检测</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">构建多语言真实场景语音深伪检测数据集ML-ITW，覆盖14种语言、7个平台、180位公众人物共28.39小时，评测三类检测范式并揭示泛化性能显著下降。</div>
<div class="card-action">
<a href="how-well-do-current-speech-deepfake-detection-methods-genera-2603-05852/">详情 →</a> · <a href="https://arxiv.org/abs/2603.05852" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="controllable-dysarthric-speech-synthesis-with-patient-specif-2602-08696/">Controllable Dysarthric Speech Synthesis with Patient-Specific Conditioning for Speaker-Diverse ASR Augmentation</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">用可学习病理前缀与音色前缀解耦，基于LoRA微调的codec语言模型合成构音障碍语音，用于ASR数据增强。</div>
<div class="card-action">
<a href="controllable-dysarthric-speech-synthesis-with-patient-specif-2602-08696/">详情 →</a> · <a href="https://arxiv.org/abs/2602.08696" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="mask-sample-revise-a-revisable-ctmc-inference-stack-for-guid-2606-13989/">Mask, Sample, Revise: A Revisable CTMC Inference Stack for Guided Discrete Flow Matching Text-to-Speech</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">面向无对齐DFM-TTS的推理期CTMC栈，用无预测器引导、提示匹配耦合与SC-ReMask重掩码提升低步数下的可懂度。</div>
<div class="card-action">
<a href="mask-sample-revise-a-revisable-ctmc-inference-stack-for-guid-2606-13989/">详情 →</a> · <a href="https://arxiv.org/abs/2606.13989" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
