---
title: "语音/音频论文速递 2026-09-09"
date: 2026-09-09T09:00:00+08:00
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
| #语音增强 | 1篇 | `██████████` |
| #语音数据处理 | 1篇 | `██████████` |
| #双耳音频 | 1篇 | `██████████` |
| #空间音频编码 | 1篇 | `██████████` |
| #语音识别 | 1篇 | `██████████` |
| #音频表示学习 | 1篇 | `██████████` |
| #音频取证 | 1篇 | `██████████` |
| #声学场景理解 | 1篇 | `██████████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="noise-adaptive-streaming-audio-visual-speech-token-enhanceme-2609-08390/">Noise Adaptive Streaming Audio-Visual Speech Token Enhancement for Robust Full-Duplex Spoken Dialogue Models</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出模块化流式音视频前端AV-STE，在噪声和重叠语音下恢复语义语音token，冻结下游对话模型，提升响应连贯性。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="spatial-audio-coding-through-relative-room-impulse-response--2609-08542/">Spatial Audio Coding Through Relative Room Impulse Response Estimation</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#空间音频编码</span>
</div>
<div class="card-tldr">提出基于相对空间房间冲激响应估计的HOA编码方案，在单传输通道下压缩率优于IVAS且质量相当。</div>
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
<a class="card-title" href="conversationalvoice-full-duplex-speech-data-from-real-conver-2609-08147/">ConversationalVoice: Full-Duplex Speech Data from Real Conversations through Source-Faithful Reconstruction and Conversation-Grounded Expansion</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音数据处理</span>
</div>
<div class="card-tldr">提出从真实双人对话中生成分离、重建和扩展三阶段训练数据的流水线，用于全双工语音模型训练。</div>
</div></div>

### #双耳音频

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="beyond-localisation-accuracy-sensorimotor-effects-of-hrtf-in-2609-08422/">Beyond Localisation Accuracy: Sensorimotor Effects of HRTF Individualisation</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">通过听觉引导的视觉搜索任务，发现个性化HRTF在无回声条件下能加快反应时间约200ms，主要影响运动启动，表明HRTF个性化对感觉运动行为有影响。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="spatial-audio-coding-through-relative-room-impulse-response--2609-08542/">Spatial Audio Coding Through Relative Room Impulse Response Estimation</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#空间音频编码</span>
</div>
<div class="card-tldr">提出基于相对空间房间冲激响应估计的HOA编码方案，在单传输通道下压缩率优于IVAS且质量相当。</div>
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
| 🥇 | [Noise Adaptive Streaming Audio-Visual Speech Token Enhanceme…](noise-adaptive-streaming-audio-visual-speech-token-enhanceme-2609-08390/) 🎯 | **8.8** | #语音增强 |
| 🥈 | [ConversationalVoice: Full-Duplex Speech Data from Real Conve…](conversationalvoice-full-duplex-speech-data-from-real-conver-2609-08147/) 🎯 | **8.2** | #语音数据处理 |
| 🥉 | [Beyond Localisation Accuracy: Sensorimotor Effects of HRTF I…](beyond-localisation-accuracy-sensorimotor-effects-of-hrtf-in-2609-08422/) 🎯 | **8.2** | #双耳音频 |
| 4. | [Spatial Audio Coding Through Relative Room Impulse Response …](spatial-audio-coding-through-relative-room-impulse-response--2609-08542/) 🎯 | **8.2** | #空间音频编码 |
| 5. | [X2Streaming-ASR: wait when uncertain, emit when ready for st…](x2streaming-asr-wait-when-uncertain-emit-when-ready-for-stre-2609-08672/) | **8.2** | #语音识别 |
| 6. | [Semantic Refinement of Universal Audio Representations throu…](semantic-refinement-of-universal-audio-representations-throu-2609-08429/) | **7.8** | #音频表示学习 |
| 7. | [Clean Accuracy Does Not Guarantee Provenance Robustness: A P…](clean-accuracy-does-not-guarantee-provenance-robustness-a-pr-2609-07981/) | **7.2** | #音频取证 |
| 8. | [Geometry-Informed Distributed Acoustic Scene Understanding](geometry-informed-distributed-acoustic-scene-understanding-2609-08026/) | **7.2** | #声学场景理解 |
| 9. | [Stabilizing Instruction Supervision for Instruct-TTS via Con…](stabilizing-instruction-supervision-for-instruct-tts-via-con-2609-08204/) | **7.2** | #语音合成 |
| 10. | [Rescuing Performance from the Demo: Co-Designing Drum Gestur…](rescuing-performance-from-the-demo-co-designing-drum-gesture-2609-08587/) | **6.5** | #音乐表演交互 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="noise-adaptive-streaming-audio-visual-speech-token-enhanceme-2609-08390/">Noise Adaptive Streaming Audio-Visual Speech Token Enhancement for Robust Full-Duplex Spoken Dialogue Models</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出模块化流式音视频前端AV-STE，在噪声和重叠语音下恢复语义语音token，冻结下游对话模型，提升响应连贯性。</div>
<div class="card-action">
<a href="noise-adaptive-streaming-audio-visual-speech-token-enhanceme-2609-08390/">详情 →</a> · <a href="https://arxiv.org/abs/2609.08390" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="conversationalvoice-full-duplex-speech-data-from-real-conver-2609-08147/">ConversationalVoice: Full-Duplex Speech Data from Real Conversations through Source-Faithful Reconstruction and Conversation-Grounded Expansion</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音数据处理</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出从真实双人对话中生成分离、重建和扩展三阶段训练数据的流水线，用于全双工语音模型训练。</div>
<div class="card-action">
<a href="conversationalvoice-full-duplex-speech-data-from-real-conver-2609-08147/">详情 →</a> · <a href="https://arxiv.org/abs/2609.08147" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="beyond-localisation-accuracy-sensorimotor-effects-of-hrtf-in-2609-08422/">Beyond Localisation Accuracy: Sensorimotor Effects of HRTF Individualisation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">通过听觉引导的视觉搜索任务，发现个性化HRTF在无回声条件下能加快反应时间约200ms，主要影响运动启动，表明HRTF个性化对感觉运动行为有影响。</div>
<div class="card-action">
<a href="beyond-localisation-accuracy-sensorimotor-effects-of-hrtf-in-2609-08422/">详情 →</a> · <a href="https://arxiv.org/abs/2609.08422" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="spatial-audio-coding-through-relative-room-impulse-response--2609-08542/">Spatial Audio Coding Through Relative Room Impulse Response Estimation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#空间音频编码</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出基于相对空间房间冲激响应估计的HOA编码方案，在单传输通道下压缩率优于IVAS且质量相当。</div>
<div class="card-action">
<a href="spatial-audio-coding-through-relative-room-impulse-response--2609-08542/">详情 →</a> · <a href="https://arxiv.org/abs/2609.08542" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="x2streaming-asr-wait-when-uncertain-emit-when-ready-for-stre-2609-08672/">X2Streaming-ASR: wait when uncertain, emit when ready for streaming ASR</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出X2Streaming-ASR，将流式识别分解为何时提交与提交什么，通过三阶段训练优化提交策略，在多个中文数据集上实现低延迟和高准确率。</div>
<div class="card-action">
<a href="x2streaming-asr-wait-when-uncertain-emit-when-ready-for-stre-2609-08672/">详情 →</a> · <a href="https://arxiv.org/abs/2609.08672" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="semantic-refinement-of-universal-audio-representations-throu-2609-08429/">Semantic Refinement of Universal Audio Representations through Audio-Description Alignment</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音频表示学习</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">通过在BEST-RQ基础上加入音频描述对齐，语义细化通用音频表示，线性探针分类提升4.66点，LLM读取提升2.59点。</div>
<div class="card-action">
<a href="semantic-refinement-of-universal-audio-representations-throu-2609-08429/">详情 →</a> · <a href="https://arxiv.org/abs/2609.08429" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="clean-accuracy-does-not-guarantee-provenance-robustness-a-pr-2609-07981/">Clean Accuracy Does Not Guarantee Provenance Robustness: A Prospective Codec-Stress Evaluation of Audio Attribution</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音频取证</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">系统评估音频溯源模型在编解码传输后的性能下降，发现干净准确率无法预测部署鲁棒性。</div>
<div class="card-action">
<a href="clean-accuracy-does-not-guarantee-provenance-robustness-a-pr-2609-07981/">详情 →</a> · <a href="https://arxiv.org/abs/2609.07981" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="geometry-informed-distributed-acoustic-scene-understanding-2609-08026/">Geometry-Informed Distributed Acoustic Scene Understanding</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#声学场景理解</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出几何信息引导的分布式声学场景理解框架，融合分布式麦克风与房间几何，生成物理一致的场景叙述。</div>
<div class="card-action">
<a href="geometry-informed-distributed-acoustic-scene-understanding-2609-08026/">详情 →</a> · <a href="https://arxiv.org/abs/2609.08026" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="stabilizing-instruction-supervision-for-instruct-tts-via-con-2609-08204/">Stabilizing Instruction Supervision for Instruct-TTS via Controllable Diversification and Drift Filtering</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">针对Instruct-TTS中指令重写导致的语义漂移问题，提出可控多样化与漂移过滤的数据稳定化方案，提升指令跟随率。</div>
<div class="card-action">
<a href="stabilizing-instruction-supervision-for-instruct-tts-via-con-2609-08204/">详情 →</a> · <a href="https://arxiv.org/abs/2609.08204" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="rescuing-performance-from-the-demo-co-designing-drum-gesture-2609-08587/">Rescuing Performance from the Demo: Co-Designing Drum Gesture Mappings with a Percussionist</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#音乐表演交互</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">通过与专业打击乐手共同设计手势映射工具并录制专辑，探索技术约束与音乐家美学之间的张力，提出“知道何时”的隐性知识概念。</div>
<div class="card-action">
<a href="rescuing-performance-from-the-demo-co-designing-drum-gesture-2609-08587/">详情 →</a> · <a href="https://arxiv.org/abs/2609.08587" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
