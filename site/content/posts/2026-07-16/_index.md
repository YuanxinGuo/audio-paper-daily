---
title: "语音/音频论文速递 2026-07-16"
date: 2026-07-16T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 2 篇 · 最高分 8.8（#语音增强）"
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
| #语音增强 | 1篇 | `██████████` |
| #语音识别 | 1篇 | `██████████` |
| #语音生成 | 1篇 | `██████████` |
| #生物声学 | 1篇 | `██████████` |
| #语音增强评估 | 1篇 | `██████████` |
| #音乐分析 | 1篇 | `██████████` |
| #音乐评估 | 1篇 | `██████████` |
| #语音表示学习 | 1篇 | `██████████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="llm-guided-reinforcement-learning-for-audio-visual-speech-en-2603-13952/">LLM-Guided Reinforcement Learning for Audio-Visual Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出基于LLM可解释奖励模型的强化学习框架，用于优化视听语音增强的感知质量。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="when-audio-separation-hurts-zero-shot-asr-evaluating-sam-aud-2603-04710/">When Audio Separation Hurts Zero-Shot ASR: Evaluating SAM-Audio with Whisper on Bengali and English Speech</a>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#语音增强评估</span>
</div>
<div class="card-tldr">研究发现语音增强预处理SAM-Audio虽提升信号质量（PSNR），却一致降低Whisper零样本ASR的WER/CER，挑战了“更干净音频→更准确转录”的假设。</div>
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
| 🥇 | [LLM-Guided Reinforcement Learning for Audio-Visual Speech En…](llm-guided-reinforcement-learning-for-audio-visual-speech-en-2603-13952/) 🎯 | **8.8** | #语音增强 |
| 🥈 | [REDDIT: Correcting Model-Generated Timestamp Drift in ASR wi…](reddit-correcting-model-generated-timestamp-drift-in-asr-wit-2607-05364/) | **8.2** | #语音识别 |
| 🥉 | [AutoSIFT: Automatic Style Sifting for Controllable Speech Ge…](autosift-automatic-style-sifting-for-controllable-speech-gen-2607-12706/) | **7.8** | #语音生成 |
| 4. | [MetaPerch: Learning from metadata for bioacoustics foundatio…](metaperch-learning-from-metadata-for-bioacoustics-foundation-2607-14072/) | **7.8** | #生物声学 |
| 5. | [When Audio Separation Hurts Zero-Shot ASR: Evaluating SAM-Au…](when-audio-separation-hurts-zero-shot-asr-evaluating-sam-aud-2603-04710/) 🎯 | **7.5** | #语音增强评估 |
| 6. | [From Prediction to Collaboration: Interactive Symbolic Music…](from-prediction-to-collaboration-interactive-symbolic-music--2607-13587/) | **7.5** | #音乐分析 |
| 7. | [Genre Bias or Aesthetic Perception? Identifying and Mitigati…](genre-bias-or-aesthetic-perception-identifying-and-mitigatin-2607-13903/) | **7.2** | #音乐评估 |
| 8. | [Rethinking Speech Foundation Model Fine-tuning: Better SFT o…](rethinking-speech-foundation-model-fine-tuning-better-sft-or-2607-13864/) | **7.2** | #语音表示学习 |
| 9. | [Adapting a Diffusion-Based Music Synthesis Model to Human Vo…](adapting-a-diffusion-based-music-synthesis-model-to-human-vo-2607-13278/) | **7.2** | #语音转换 |
| 10. | [From Continuous Deployment to Queryable Dataset: Terabyte-Sc…](from-continuous-deployment-to-queryable-dataset-terabyte-sca-2607-13840/) | **6.5** | #声学数据处理 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="llm-guided-reinforcement-learning-for-audio-visual-speech-en-2603-13952/">LLM-Guided Reinforcement Learning for Audio-Visual Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出基于LLM可解释奖励模型的强化学习框架，用于优化视听语音增强的感知质量。</div>
<div class="card-action">
<a href="llm-guided-reinforcement-learning-for-audio-visual-speech-en-2603-13952/">详情 →</a> · <a href="https://arxiv.org/abs/2603.13952" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="reddit-correcting-model-generated-timestamp-drift-in-asr-wit-2607-05364/">REDDIT: Correcting Model-Generated Timestamp Drift in ASR without Forgetting via Replay-Based Distribution Editing</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出REDDIT框架，通过重放式分布编辑纠正ASR模型生成的时间戳漂移，避免灾难性遗忘。</div>
<div class="card-action">
<a href="reddit-correcting-model-generated-timestamp-drift-in-asr-wit-2607-05364/">详情 →</a> · <a href="https://arxiv.org/abs/2607.05364" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="autosift-automatic-style-sifting-for-controllable-speech-gen-2607-12706/">AutoSIFT: Automatic Style Sifting for Controllable Speech Generation with Arbitrary Style Infilling</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出AutoSIFT框架，通过解耦语音风格为已知文本描述类别和未知残差风格，实现细粒度、可控制的类别级风格编辑。</div>
<div class="card-action">
<a href="autosift-automatic-style-sifting-for-controllable-speech-gen-2607-12706/">详情 →</a> · <a href="https://arxiv.org/abs/2607.12706" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="metaperch-learning-from-metadata-for-bioacoustics-foundation-2607-14072/">MetaPerch: Learning from metadata for bioacoustics foundation models</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#生物声学</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">利用录音元数据（位置、时间等）作为辅助监督信号，训练生物声学基础模型MetaPerch，提升物种识别泛化性。</div>
<div class="card-action">
<a href="metaperch-learning-from-metadata-for-bioacoustics-foundation-2607-14072/">详情 →</a> · <a href="https://arxiv.org/abs/2607.14072" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="when-audio-separation-hurts-zero-shot-asr-evaluating-sam-aud-2603-04710/">When Audio Separation Hurts Zero-Shot ASR: Evaluating SAM-Audio with Whisper on Bengali and English Speech</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#语音增强评估</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">研究发现语音增强预处理SAM-Audio虽提升信号质量（PSNR），却一致降低Whisper零样本ASR的WER/CER，挑战了“更干净音频→更准确转录”的假设。</div>
<div class="card-action">
<a href="when-audio-separation-hurts-zero-shot-asr-evaluating-sam-aud-2603-04710/">详情 →</a> · <a href="https://arxiv.org/abs/2603.04710" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="from-prediction-to-collaboration-interactive-symbolic-music--2607-13587/">From Prediction to Collaboration: Interactive Symbolic Music Analysis</a>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#音乐分析</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出统一框架，将罗马数字分析从全谱预测扩展到交互式局部补全与修正，通过复用预训练表示实现高效迭代。</div>
<div class="card-action">
<a href="from-prediction-to-collaboration-interactive-symbolic-music--2607-13587/">详情 →</a> · <a href="https://arxiv.org/abs/2607.13587" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="genre-bias-or-aesthetic-perception-identifying-and-mitigatin-2607-13903/">Genre Bias or Aesthetic Perception? Identifying and Mitigating Shortcut Learning in Music Evaluation</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音乐评估</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">发现音乐评估模型存在基于体裁的捷径学习，提出联合重加权与正则化训练目标以缓解偏差，提升与人类偏好的一致性。</div>
<div class="card-action">
<a href="genre-bias-or-aesthetic-perception-identifying-and-mitigatin-2607-13903/">详情 →</a> · <a href="https://arxiv.org/abs/2607.13903" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="rethinking-speech-foundation-model-fine-tuning-better-sft-or-2607-13864/">Rethinking Speech Foundation Model Fine-tuning: Better SFT or Better Match?</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音表示学习</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">系统研究表明，语音基础模型微调中的小增益常源于特定预训练实例的匹配，而非方法本身的普遍提升。</div>
<div class="card-action">
<a href="rethinking-speech-foundation-model-fine-tuning-better-sft-or-2607-13864/">详情 →</a> · <a href="https://arxiv.org/abs/2607.13864" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="adapting-a-diffusion-based-music-synthesis-model-to-human-vo-2607-13278/">Adapting a Diffusion-Based Music Synthesis Model to Human Voice Conversion</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音转换</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">将多乐器音乐合成扩散模型适配为语音/歌声转换统一框架，利用PPG和音高条件控制，实现自然度和相似性匹敌专用系统。</div>
<div class="card-action">
<a href="adapting-a-diffusion-based-music-synthesis-model-to-human-vo-2607-13278/">详情 →</a> · <a href="https://arxiv.org/abs/2607.13278" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="from-continuous-deployment-to-queryable-dataset-terabyte-sca-2607-13840/">From Continuous Deployment to Queryable Dataset: Terabyte-Scale AIS-Aligned Passive Acoustic Labelling</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#声学数据处理</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出一种数据库原生工作流，将水听器录音与AIS位置报告对齐，生成可查询的结构化表格，支持大规模被动声学数据的机器学习分析。</div>
<div class="card-action">
<a href="from-continuous-deployment-to-queryable-dataset-terabyte-sca-2607-13840/">详情 →</a> · <a href="https://arxiv.org/abs/2607.13840" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
