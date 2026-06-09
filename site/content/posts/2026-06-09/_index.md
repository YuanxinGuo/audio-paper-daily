---
title: "语音/音频论文速递 2026-06-09"
date: 2026-06-09T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 7 篇 · 最高分 9.5（#语音增强）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">7</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">9.5</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音增强 | 3篇 | `██████████` |
| #目标说话人提取 | 3篇 | `██████████` |
| #语音转换 | 2篇 | `███████` |
| #语音分离 | 1篇 | `███` |
| #语音合成 | 1篇 | `███` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="semamba-a-general-speech-restoration-framework-leveraging-gl-2603-11669/">SEMamba++: A General Speech Restoration Framework Leveraging Global, Local, and Periodic Spectral Patterns</a>
<div class="card-meta">
<span class="card-score">9.5</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出SEMamba++，通过全局-局部-周期频域模块和多分辨率时频双处理块，在多种语音恢复任务上达到最优性能且保持高效。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="gentse-enhancing-target-speaker-extraction-via-a-coarse-to-f-2512-20978/">GenTSE: Enhancing Target Speaker Extraction via a Coarse-to-Fine Generative Language Model</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">提出GenTSE，一种两阶段解码器仅生成式语言模型，通过粗到细的语义和声学令牌预测实现高保真目标说话人提取。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="your-u-net-dereverberation-model-is-secretly-an-rir-encoder-2606-09557/">Your U-Net Dereverberation Model is Secretly an RIR Encoder</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">发现基于U-Net的去混响模型在深层隐式编码了房间冲激响应特征，并利用该发现通过预训练RIR嵌入条件化提升去混响性能。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="training-free-intelligibility-guided-observation-addition-fo-2602-20967/">Training-Free Intelligibility-Guided Observation Addition for Noisy ASR</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出一种无需训练的智能引导观测融合方法，利用后端ASR的清晰度估计动态融合带噪与增强语音，提升噪声环境下的ASR性能。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="enroll-on-wakeup-a-first-comparative-study-of-target-speech--2602-15519/">Enroll-on-Wakeup: A First Comparative Study of Target Speech Extraction for Seamless Interaction in Real Noisy Human-Machine Dialogue Scenarios</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">提出Enroll-on-Wakeup框架，利用唤醒词片段作为注册语音进行目标说话人提取，首次系统评估了判别式和生成式模型在真实噪声场景下的表现。</div>
</div></div>

### #目标说话人提取

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="detect-attend-and-extract-keyword-guided-target-speaker-extr-2602-07977/">Detect, Attend and Extract: Keyword Guided Target Speaker Extraction</a>
<div class="card-meta">
<span class="card-score">9.5</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">提出DAE-TSE框架，利用关键词（部分转录）作为线索提取目标说话人语音，无需干净注册语音。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="gentse-enhancing-target-speaker-extraction-via-a-coarse-to-f-2512-20978/">GenTSE: Enhancing Target Speaker Extraction via a Coarse-to-Fine Generative Language Model</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">提出GenTSE，一种两阶段解码器仅生成式语言模型，通过粗到细的语义和声学令牌预测实现高保真目标说话人提取。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="enroll-on-wakeup-a-first-comparative-study-of-target-speech--2602-15519/">Enroll-on-Wakeup: A First Comparative Study of Target Speech Extraction for Seamless Interaction in Real Noisy Human-Machine Dialogue Scenarios</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">提出Enroll-on-Wakeup框架，利用唤醒词片段作为注册语音进行目标说话人提取，首次系统评估了判别式和生成式模型在真实噪声场景下的表现。</div>
</div></div>

### #语音分离

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="detect-attend-and-extract-keyword-guided-target-speaker-extr-2602-07977/">Detect, Attend and Extract: Keyword Guided Target Speaker Extraction</a>
<div class="card-meta">
<span class="card-score">9.5</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">提出DAE-TSE框架，利用关键词（部分转录）作为线索提取目标说话人语音，无需干净注册语音。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="meco-one-step-meanflow-based-corrector-for-multi-channel-spe-2606-09677/">MeCo: One-Step MeanFlow-based Corrector for Multi-Channel Speech Separation</a>
<div class="card-meta">
<span class="card-score">9.5</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">提出MeCo，一种基于MeanFlow的一步生成式校正器，将判别式分离结果映射到干净语音流形，同时提升信号保真度和听觉质量。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="gentse-enhancing-target-speaker-extraction-via-a-coarse-to-f-2512-20978/">GenTSE: Enhancing Target Speaker Extraction via a Coarse-to-Fine Generative Language Model</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">提出GenTSE，一种两阶段解码器仅生成式语言模型，通过粗到细的语义和声学令牌预测实现高保真目标说话人提取。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="enroll-on-wakeup-a-first-comparative-study-of-target-speech--2602-15519/">Enroll-on-Wakeup: A First Comparative Study of Target Speech Extraction for Seamless Interaction in Real Noisy Human-Machine Dialogue Scenarios</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">提出Enroll-on-Wakeup框架，利用唤醒词片段作为注册语音进行目标说话人提取，首次系统评估了判别式和生成式模型在真实噪声场景下的表现。</div>
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
| 🥇 | [SEMamba++: A General Speech Restoration Framework Leveraging…](semamba-a-general-speech-restoration-framework-leveraging-gl-2603-11669/) 🎯 | **9.5** | #语音增强 |
| 🥈 | [Detect, Attend and Extract: Keyword Guided Target Speaker Ex…](detect-attend-and-extract-keyword-guided-target-speaker-extr-2602-07977/) 🎯 | **9.5** | #目标说话人提取 |
| 🥉 | [MeCo: One-Step MeanFlow-based Corrector for Multi-Channel Sp…](meco-one-step-meanflow-based-corrector-for-multi-channel-spe-2606-09677/) 🎯 | **9.5** | #语音分离 |
| 4. | [GenTSE: Enhancing Target Speaker Extraction via a Coarse-to-…](gentse-enhancing-target-speaker-extraction-via-a-coarse-to-f-2512-20978/) 🎯 | **9.2** | #目标说话人提取 |
| 5. | [Your U-Net Dereverberation Model is Secretly an RIR Encoder](your-u-net-dereverberation-model-is-secretly-an-rir-encoder-2606-09557/) 🎯 | **8.5** | #语音增强 |
| 6. | [Training-Free Intelligibility-Guided Observation Addition fo…](training-free-intelligibility-guided-observation-addition-fo-2602-20967/) 🎯 | **8.2** | #语音增强 |
| 7. | [Enroll-on-Wakeup: A First Comparative Study of Target Speech…](enroll-on-wakeup-a-first-comparative-study-of-target-speech--2602-15519/) 🎯 | **8.2** | #目标说话人提取 |
| 8. | [From A to B to A: Palindromic Zero-Shot Voice Conversion wit…](from-a-to-b-to-a-palindromic-zero-shot-voice-conversion-with-2606-08843/) | **7.8** | #语音转换 |
| 9. | [Cross-Modal Masking for Robust Silent Speech Synthesis Using…](cross-modal-masking-for-robust-silent-speech-synthesis-using-2606-09667/) | **7.8** | #语音合成 |
| 10. | [Universal Speech Content Factorization](universal-speech-content-factorization-2603-08977/) | **7.5** | #语音转换 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="semamba-a-general-speech-restoration-framework-leveraging-gl-2603-11669/">SEMamba++: A General Speech Restoration Framework Leveraging Global, Local, and Periodic Spectral Patterns</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.5</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出SEMamba++，通过全局-局部-周期频域模块和多分辨率时频双处理块，在多种语音恢复任务上达到最优性能且保持高效。</div>
<div class="card-action">
<a href="semamba-a-general-speech-restoration-framework-leveraging-gl-2603-11669/">详情 →</a> · <a href="https://arxiv.org/abs/2603.11669" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="detect-attend-and-extract-keyword-guided-target-speaker-extr-2602-07977/">Detect, Attend and Extract: Keyword Guided Target Speaker Extraction</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.5</span>
<span class="tag-pill">#目标说话人提取</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出DAE-TSE框架，利用关键词（部分转录）作为线索提取目标说话人语音，无需干净注册语音。</div>
<div class="card-action">
<a href="detect-attend-and-extract-keyword-guided-target-speaker-extr-2602-07977/">详情 →</a> · <a href="https://arxiv.org/abs/2602.07977" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="meco-one-step-meanflow-based-corrector-for-multi-channel-spe-2606-09677/">MeCo: One-Step MeanFlow-based Corrector for Multi-Channel Speech Separation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.5</span>
<span class="tag-pill">#语音分离</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出MeCo，一种基于MeanFlow的一步生成式校正器，将判别式分离结果映射到干净语音流形，同时提升信号保真度和听觉质量。</div>
<div class="card-action">
<a href="meco-one-step-meanflow-based-corrector-for-multi-channel-spe-2606-09677/">详情 →</a> · <a href="https://arxiv.org/abs/2606.09677" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="gentse-enhancing-target-speaker-extraction-via-a-coarse-to-f-2512-20978/">GenTSE: Enhancing Target Speaker Extraction via a Coarse-to-Fine Generative Language Model</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#目标说话人提取</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出GenTSE，一种两阶段解码器仅生成式语言模型，通过粗到细的语义和声学令牌预测实现高保真目标说话人提取。</div>
<div class="card-action">
<a href="gentse-enhancing-target-speaker-extraction-via-a-coarse-to-f-2512-20978/">详情 →</a> · <a href="https://arxiv.org/abs/2512.20978" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="your-u-net-dereverberation-model-is-secretly-an-rir-encoder-2606-09557/">Your U-Net Dereverberation Model is Secretly an RIR Encoder</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">发现基于U-Net的去混响模型在深层隐式编码了房间冲激响应特征，并利用该发现通过预训练RIR嵌入条件化提升去混响性能。</div>
<div class="card-action">
<a href="your-u-net-dereverberation-model-is-secretly-an-rir-encoder-2606-09557/">详情 →</a> · <a href="https://arxiv.org/abs/2606.09557" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="training-free-intelligibility-guided-observation-addition-fo-2602-20967/">Training-Free Intelligibility-Guided Observation Addition for Noisy ASR</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出一种无需训练的智能引导观测融合方法，利用后端ASR的清晰度估计动态融合带噪与增强语音，提升噪声环境下的ASR性能。</div>
<div class="card-action">
<a href="training-free-intelligibility-guided-observation-addition-fo-2602-20967/">详情 →</a> · <a href="https://arxiv.org/abs/2602.20967" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="enroll-on-wakeup-a-first-comparative-study-of-target-speech--2602-15519/">Enroll-on-Wakeup: A First Comparative Study of Target Speech Extraction for Seamless Interaction in Real Noisy Human-Machine Dialogue Scenarios</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#目标说话人提取</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出Enroll-on-Wakeup框架，利用唤醒词片段作为注册语音进行目标说话人提取，首次系统评估了判别式和生成式模型在真实噪声场景下的表现。</div>
<div class="card-action">
<a href="enroll-on-wakeup-a-first-comparative-study-of-target-speech--2602-15519/">详情 →</a> · <a href="https://arxiv.org/abs/2602.15519" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="from-a-to-b-to-a-palindromic-zero-shot-voice-conversion-with-2606-08843/">From A to B to A: Palindromic Zero-Shot Voice Conversion with Non-Parallel Data</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音转换</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出基于KNN检索WavLM表征的零样本语音转换框架，利用非平行数据构建合成训练对，支持多语言且仅用英文数据训练。</div>
<div class="card-action">
<a href="from-a-to-b-to-a-palindromic-zero-shot-voice-conversion-with-2606-08843/">详情 →</a> · <a href="https://arxiv.org/abs/2606.08843" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="cross-modal-masking-for-robust-silent-speech-synthesis-using-2606-09667/">Cross-Modal Masking for Robust Silent Speech Synthesis Using sEMG and Lipreading</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出跨模态掩蔽框架，联合sEMG和唇读信号实现鲁棒静音语音合成，在低比特率和模态缺失条件下显著优于单模态基线。</div>
<div class="card-action">
<a href="cross-modal-masking-for-robust-silent-speech-synthesis-using-2606-09667/">详情 →</a> · <a href="https://arxiv.org/abs/2606.09667" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="universal-speech-content-factorization-2603-08977/">Universal Speech Content Factorization</a>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#语音转换</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出一种可逆线性方法，从语音中提取低秩表示，抑制音色同时保留内容，实现零样本语音转换和音色提示的TTS。</div>
<div class="card-action">
<a href="universal-speech-content-factorization-2603-08977/">详情 →</a> · <a href="https://arxiv.org/abs/2603.08977" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
