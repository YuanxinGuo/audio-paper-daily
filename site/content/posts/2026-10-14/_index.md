---
title: "语音/音频论文速递 2026-10-14"
date: 2026-10-14T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 3 篇 · 最高分 8.8（#乐器分离）"
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
| #语音增强 | 2篇 | `██████████` |
| #语音合成 | 2篇 | `██████████` |
| #乐器分离 | 1篇 | `█████` |
| #音乐生成 | 1篇 | `█████` |
| #音频编码 | 1篇 | `█████` |
| #音频伪造检测 | 1篇 | `█████` |
| #语音检索 | 1篇 | `█████` |
| #声学模拟 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="active-noise-cancellation-extends-the-benefit-of-ai-speech-e-2610-17287/">Active noise cancellation extends the benefit of AI speech enhancement in real hearing-aid recordings</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">在 KEMAR 上实测三种助听器硬件条件，证明 ANC 通过衰减直通路径，使 AI 语音增强的 SNR 收益从 1.6 dB 提升到 5.1 dB。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="multimodal-contrastive-representation-learning-based-voice-c-2610-17716/">Multimodal Contrastive Representation Learning Based Voice Conversion for Electrolaryngeal Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">用语音-文本跨模态对比学习与跨阶段对比学习，把多模态表征迁移到仅语音输入的电子喉语音转正常语音任务。</div>
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
<a class="card-title" href="active-noise-cancellation-extends-the-benefit-of-ai-speech-e-2610-17287/">Active noise cancellation extends the benefit of AI speech enhancement in real hearing-aid recordings</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">在 KEMAR 上实测三种助听器硬件条件，证明 ANC 通过衰减直通路径，使 AI 语音增强的 SNR 收益从 1.6 dB 提升到 5.1 dB。</div>
</div></div>

### #乐器分离

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="flomss-generative-source-separation-by-flow-matching-2610-17821/">FLOMSS: Generative Source Separation by Flow Matching</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#乐器分离</span>
</div>
<div class="card-tldr">系统研究 flow matching 用于四源全频带立体声音乐分离，考察预测目标、流路径、单源/多源建模与混合一致性约束。</div>
</div></div>

## 📊 完整排行榜

| 排名 | 论文 | 评分 | 主任务 |
| --- | --- | --- | --- |
| 🥇 | [FLOMSS: Generative Source Separation by Flow Matching](flomss-generative-source-separation-by-flow-matching-2610-17821/) 🎯 | **8.8** | #乐器分离 |
| 🥈 | [Active noise cancellation extends the benefit of AI speech e…](active-noise-cancellation-extends-the-benefit-of-ai-speech-e-2610-17287/) 🎯 | **8.2** | #语音增强 |
| 🥉 | [Multimodal Contrastive Representation Learning Based Voice C…](multimodal-contrastive-representation-learning-based-voice-c-2610-17716/) 🎯 | **8.2** | #语音增强 |
| 4. | [MSVAE: Rethinking Musical Semantics in Continuous Latent Spa…](msvae-rethinking-musical-semantics-in-continuous-latent-spac-2610-17187/) | **7.8** | #音乐生成 |
| 5. | [Co-Adaptive Entropy Modeling and Rate-Distortion-Optimal Bit…](co-adaptive-entropy-modeling-and-rate-distortion-optimal-bit-2610-17459/) | **7.2** | #音频编码 |
| 6. | [What Do Deepfake Audio Detectors Hear? From Self-Supervised …](what-do-deepfake-audio-detectors-hear-from-self-supervised-m-2610-17617/) | **7.0** | #音频伪造检测 |
| 7. | [Fish Audio Drama 3 Technical Report](fish-audio-drama-3-technical-report-2610-18010/) | **7.0** | #语音合成 |
| 8. | [SSEmb: Training a Generalizable Speech Retrieval Model Using…](ssemb-training-a-generalizable-speech-retrieval-model-using--2610-17813/) | **6.8** | #语音检索 |
| 9. | [Beyond Fixed Targets: On-Policy One-Shot Speaker Personaliza…](beyond-fixed-targets-on-policy-one-shot-speaker-personalizat-2610-17838/) | **6.8** | #语音合成 |
| 10. | [Modeling and Design of a Diaphragm-Integrated Photonic Waveg…](modeling-and-design-of-a-diaphragm-integrated-photonic-waveg-2610-17745/) | **4.5** | #声学模拟 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="flomss-generative-source-separation-by-flow-matching-2610-17821/">FLOMSS: Generative Source Separation by Flow Matching</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#乐器分离</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">系统研究 flow matching 用于四源全频带立体声音乐分离，考察预测目标、流路径、单源/多源建模与混合一致性约束。</div>
<div class="card-action">
<a href="flomss-generative-source-separation-by-flow-matching-2610-17821/">详情 →</a> · <a href="https://arxiv.org/abs/2610.17821" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="active-noise-cancellation-extends-the-benefit-of-ai-speech-e-2610-17287/">Active noise cancellation extends the benefit of AI speech enhancement in real hearing-aid recordings</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">在 KEMAR 上实测三种助听器硬件条件，证明 ANC 通过衰减直通路径，使 AI 语音增强的 SNR 收益从 1.6 dB 提升到 5.1 dB。</div>
<div class="card-action">
<a href="active-noise-cancellation-extends-the-benefit-of-ai-speech-e-2610-17287/">详情 →</a> · <a href="https://arxiv.org/abs/2610.17287" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="multimodal-contrastive-representation-learning-based-voice-c-2610-17716/">Multimodal Contrastive Representation Learning Based Voice Conversion for Electrolaryngeal Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用语音-文本跨模态对比学习与跨阶段对比学习，把多模态表征迁移到仅语音输入的电子喉语音转正常语音任务。</div>
<div class="card-action">
<a href="multimodal-contrastive-representation-learning-based-voice-c-2610-17716/">详情 →</a> · <a href="https://arxiv.org/abs/2610.17716" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="msvae-rethinking-musical-semantics-in-continuous-latent-spac-2610-17187/">MSVAE: Rethinking Musical Semantics in Continuous Latent Spaces</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出 MSVAE，用工作级与歌词级双流语义潜空间替代纯重建自编码器，改善歌词到歌曲与文本到音乐生成。</div>
<div class="card-action">
<a href="msvae-rethinking-musical-semantics-in-continuous-latent-spac-2610-17187/">详情 →</a> · <a href="https://arxiv.org/abs/2610.17187" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="co-adaptive-entropy-modeling-and-rate-distortion-optimal-bit-2610-17459/">Co-Adaptive Entropy Modeling and Rate-Distortion-Optimal Bit Allocation for Perceptual Audio Coding</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音频编码</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出熵编码模型与比特分配跨块协同自适应的感知音频编码器，无需模型边信息，噪声掩蔽比失真降低15-24%。</div>
<div class="card-action">
<a href="co-adaptive-entropy-modeling-and-rate-distortion-optimal-bit-2610-17459/">详情 →</a> · <a href="https://arxiv.org/abs/2610.17459" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="what-do-deepfake-audio-detectors-hear-from-self-supervised-m-2610-17617/">What Do Deepfake Audio Detectors Hear? From Self-Supervised Models to Audio LLMs</a>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#音频伪造检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">在 CompSpoof V2 混合音频上系统比较 SSL 与音频 LLM 检测器，发现假事件比假语音更易检出，且子带探测显示前端编码器决定频带证据。</div>
<div class="card-action">
<a href="what-do-deepfake-audio-detectors-hear-from-self-supervised-m-2610-17617/">详情 →</a> · <a href="https://arxiv.org/abs/2610.17617" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="fish-audio-drama-3-technical-report-2610-18010/">Fish Audio Drama 3 Technical Report</a>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">开源35B MoE语音生成模型，支持多轮修订、场景配音、infilling编辑与流式合成，单H200解码271帧/秒。</div>
<div class="card-action">
<a href="fish-audio-drama-3-technical-report-2610-18010/">详情 →</a> · <a href="https://arxiv.org/abs/2610.18010" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="ssemb-training-a-generalizable-speech-retrieval-model-using--2610-17813/">SSEmb: Training a Generalizable Speech Retrieval Model Using Only Automatic Speech Recognition Data</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音检索</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">用ASR语料的语音-文本对训练轻量适配器，将冻结语音编码器输出投影到冻结文本嵌入空间，实现可泛化的语音检索。</div>
<div class="card-action">
<a href="ssemb-training-a-generalizable-speech-retrieval-model-using--2610-17813/">详情 →</a> · <a href="https://arxiv.org/abs/2610.17813" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="beyond-fixed-targets-on-policy-one-shot-speaker-personalizat-2610-17838/">Beyond Fixed Targets: On-Policy One-Shot Speaker Personalization for Autoregressive Text-To-Speech Models</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">针对自回归TTS单样本说话人个性化中SFT失效问题，提出GRPO与在线自蒸馏两种on-policy方法，提升相似度并保持可懂度。</div>
<div class="card-action">
<a href="beyond-fixed-targets-on-policy-one-shot-speaker-personalizat-2610-17838/">详情 →</a> · <a href="https://arxiv.org/abs/2610.17838" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="modeling-and-design-of-a-diaphragm-integrated-photonic-waveg-2610-17745/">Modeling and Design of a Diaphragm-Integrated Photonic Waveguide Microphone</a>
<div class="card-meta">
<span class="card-score">4.5</span>
<span class="tag-pill">#声学模拟</span>
<span class="card-tier">后50%</span>
</div>
<div class="card-tldr">用解析模型把MZI波导集成振膜麦克风的压力-弯曲-光电流链路打通，预测紧凑型信噪比78 dB、过载124 dB。</div>
<div class="card-action">
<a href="modeling-and-design-of-a-diaphragm-integrated-photonic-waveg-2610-17745/">详情 →</a> · <a href="https://arxiv.org/abs/2610.17745" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
