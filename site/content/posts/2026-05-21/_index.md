---
title: "语音/音频论文速递 2026-05-21"
date: 2026-05-21T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 2 篇 · 最高分 9.5（#语音增强）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">2</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">9.5</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #音乐生成 | 3篇 | `██████████` |
| #语音增强 | 1篇 | `███` |
| #目标说话人提取 | 1篇 | `███` |
| #音频叙事生成 | 1篇 | `███` |
| #语音合成 | 1篇 | `███` |
| #声景分类 | 1篇 | `███` |
| #语音合成评估 | 1篇 | `███` |
| #语音对话系统 | 1篇 | `███` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="speech-enhancement-based-on-drifting-models-2604-24199/">Speech Enhancement Based on Drifting Models</a>
<div class="card-meta">
<span class="card-score">9.5</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出DriftSE，一种基于漂移模型的单步语音增强框架，将去噪建模为均衡问题，无需迭代采样即可实现高质量增强。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="discriminative-generative-target-speaker-extraction-with-dec-2601-06006/">Discriminative-Generative Target Speaker Extraction with Decoder-Only Language Models</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">提出判别-生成两阶段框架，用解码器语言模型作为生成后端，结合判别前端实现高质量目标说话人提取。</div>
</div></div>

### #目标说话人提取

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="discriminative-generative-target-speaker-extraction-with-dec-2601-06006/">Discriminative-Generative Target Speaker Extraction with Decoder-Only Language Models</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">提出判别-生成两阶段框架，用解码器语言模型作为生成后端，结合判别前端实现高质量目标说话人提取。</div>
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
| 🥇 | [Speech Enhancement Based on Drifting Models](speech-enhancement-based-on-drifting-models-2604-24199/) 🎯 | **9.5** | #语音增强 |
| 🥈 | [Discriminative-Generative Target Speaker Extraction with Dec…](discriminative-generative-target-speaker-extraction-with-dec-2601-06006/) 🎯 | **9.2** | #目标说话人提取 |
| 🥉 | [AuDirector: A Self-Reflective Closed-Loop Framework for Imme…](audirector-a-self-reflective-closed-loop-framework-for-immer-2605-11866/) | **7.8** | #音频叙事生成 |
| 4. | [Instrumental Text-to-Music Generation with Auxiliary Conditi…](instrumental-text-to-music-generation-with-auxiliary-conditi-2605-21433/) | **7.8** | #音乐生成 |
| 5. | [Voice ''Cloning'' is Style Transfer](voice-cloning-is-style-transfer-2605-16578/) | **7.2** | #语音合成 |
| 6. | [CoarseSoundNet: Building a reliable model for ecological sou…](coarsesoundnet-building-a-reliable-model-for-ecological-soun-2605-21143/) | **7.2** | #声景分类 |
| 7. | [Musical Attention Transformer: Music Generation Using a Musi…](musical-attention-transformer-music-generation-using-a-music-2605-21081/) | **7.2** | #音乐生成 |
| 8. | [Evaluating Speech Articulation Synthesis with Articulatory P…](evaluating-speech-articulation-synthesis-with-articulatory-p-2605-20920/) | **6.5** | #语音合成评估 |
| 9. | [Synchronization and Turn-Taking in Full-Duplex Speech Dialog…](synchronization-and-turn-taking-in-full-duplex-speech-dialog-2605-20356/) | **6.5** | #语音对话系统 |
| 10. | [Music of Changing Lines: Toward a Culturally Situated Approa…](music-of-changing-lines-toward-a-culturally-situated-approac-2605-20386/) | **5.5** | #音乐生成 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="speech-enhancement-based-on-drifting-models-2604-24199/">Speech Enhancement Based on Drifting Models</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.5</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前10%</span>
</div>
<div class="card-tldr">提出DriftSE，一种基于漂移模型的单步语音增强框架，将去噪建模为均衡问题，无需迭代采样即可实现高质量增强。</div>
<div class="card-action">
<a href="speech-enhancement-based-on-drifting-models-2604-24199/">详情 →</a> · <a href="https://arxiv.org/abs/2604.24199" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="discriminative-generative-target-speaker-extraction-with-dec-2601-06006/">Discriminative-Generative Target Speaker Extraction with Decoder-Only Language Models</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#目标说话人提取</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出判别-生成两阶段框架，用解码器语言模型作为生成后端，结合判别前端实现高质量目标说话人提取。</div>
<div class="card-action">
<a href="discriminative-generative-target-speaker-extraction-with-dec-2601-06006/">详情 →</a> · <a href="https://arxiv.org/abs/2601.06006" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="audirector-a-self-reflective-closed-loop-framework-for-immer-2605-11866/">AuDirector: A Self-Reflective Closed-Loop Framework for Immersive Audio Storytelling</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音频叙事生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出AuDirector，一个自反思闭环多智能体框架，通过身份感知预制作、协作合成与校正、人机交互精炼模块，实现连贯且情感丰富的长音频叙事生成。</div>
<div class="card-action">
<a href="audirector-a-self-reflective-closed-loop-framework-for-immer-2605-11866/">详情 →</a> · <a href="https://arxiv.org/abs/2605.11866" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="instrumental-text-to-music-generation-with-auxiliary-conditi-2605-21433/">Instrumental Text-to-Music Generation with Auxiliary Conditioning Branches</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">本文研究在数据受限条件下，辅助条件分支（歌词和音色）对文本到乐器音乐生成的影响，发现即使退化输入，这些分支仍作为训练锚点提升性能。</div>
<div class="card-action">
<a href="instrumental-text-to-music-generation-with-auxiliary-conditi-2605-21433/">详情 →</a> · <a href="https://arxiv.org/abs/2605.21433" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="voice-cloning-is-style-transfer-2605-16578/">Voice ''Cloning'' is Style Transfer</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">发现语音克隆并非忠实复制声音，而是系统性地对源语音进行风格迁移，使克隆声音更权威、温暖、像客服，并导致说话人特征同质化。</div>
<div class="card-action">
<a href="voice-cloning-is-style-transfer-2605-16578/">详情 →</a> · <a href="https://arxiv.org/abs/2605.16578" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="coarsesoundnet-building-a-reliable-model-for-ecological-soun-2605-21143/">CoarseSoundNet: Building a reliable model for ecological soundscape analysis</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#声景分类</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出CoarseSoundNet，在被动声学监测条件下对生物声、地质声和人为声进行粗粒度分类，并系统研究训练策略与后处理方法。</div>
<div class="card-action">
<a href="coarsesoundnet-building-a-reliable-model-for-ecological-soun-2605-21143/">详情 →</a> · <a href="https://arxiv.org/abs/2605.21143" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="musical-attention-transformer-music-generation-using-a-music-2605-21081/">Musical Attention Transformer: Music Generation Using a Music-Specific Attention Model</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出Musical Attention机制，将小节号、调号、拍号、速度等元信息融入Transformer注意力，改善音乐生成中的重复和音符复制问题。</div>
<div class="card-action">
<a href="musical-attention-transformer-music-generation-using-a-music-2605-21081/">详情 →</a> · <a href="https://arxiv.org/abs/2605.21081" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="evaluating-speech-articulation-synthesis-with-articulatory-p-2605-20920/">Evaluating Speech Articulation Synthesis with Articulatory Phoneme Recognition</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#语音合成评估</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出用发音音素识别作为代理任务，评估发音语音合成质量，优于传统点对点距离指标。</div>
<div class="card-action">
<a href="evaluating-speech-articulation-synthesis-with-articulatory-p-2605-20920/">详情 →</a> · <a href="https://arxiv.org/abs/2605.20920" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="synchronization-and-turn-taking-in-full-duplex-speech-dialog-2605-20356/">Synchronization and Turn-Taking in Full-Duplex Speech Dialogue Models</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#语音对话系统</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">通过模拟Moshi模型全双工对话，研究说话人间的表征同步与话轮转换预测。</div>
<div class="card-action">
<a href="synchronization-and-turn-taking-in-full-duplex-speech-dialog-2605-20356/">详情 →</a> · <a href="https://arxiv.org/abs/2605.20356" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="music-of-changing-lines-toward-a-culturally-situated-approac-2605-20386/">Music of Changing Lines: Toward a Culturally Situated Approach to the I-Ching</a>
<div class="card-meta">
<span class="card-score">5.5</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">后50%</span>
</div>
<div class="card-tldr">提出一个交互系统，将易经占卜与LLM和生成音乐模型结合，实现文化意义驱动的音乐生成。</div>
<div class="card-action">
<a href="music-of-changing-lines-toward-a-culturally-situated-approac-2605-20386/">详情 →</a> · <a href="https://arxiv.org/abs/2605.20386" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
