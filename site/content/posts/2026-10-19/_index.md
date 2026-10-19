---
title: "语音/音频论文速递 2026-10-19"
date: 2026-10-19T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 4 篇 · 最高分 9.2（#目标说话人提取）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">4</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">9.2</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #目标说话人提取 | 2篇 | `██████████` |
| #语音识别 | 2篇 | `██████████` |
| #乐器分离 | 1篇 | `█████` |
| #声学模拟 | 1篇 | `█████` |
| #语音质量评估 | 1篇 | `█████` |
| #音频理解评测 | 1篇 | `█████` |
| #语音合成 | 1篇 | `█████` |
| #语音对话系统 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="acousticagent-a-floorplan-centric-simulation-platform-for-di-2610-22936/">AcousticAgent: A Floorplan-Centric Simulation Platform for Distributed Multi-Room Speech Processing</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#声学模拟</span>
</div>
<div class="card-tldr">提出以户型图为中心的多房间声学仿真平台，生成多通道RIR并构建FP-RIR数据集，验证分布式麦克风对远场语音处理的价值。</div>
</div></div>

### #目标说话人提取

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="promptsep-speaker-generative-target-speaker-extraction-via-m-2610-23066/">PromptSep-Speaker: Generative Target Speaker Extraction via Multimodal Prompting and Semantic Alignment</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">用潜扩散生成式框架统一四种目标线索（时序、文本、注册音频、说话人描述）做目标说话人提取，并用冻结 WavLM 对齐损失监督交叉注意力。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="tv-audioremover-joint-text-visual-guided-sound-removal-with--2609-25864/">TV-AudioRemover: Joint Text-Visual Guided Sound Removal with Multi-Task Hard-Mixture Curriculum</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">用编辑后视频与文本指令联合引导，从混合音轨中移除被删物体对应的声音，并构建百万级数据集与评测基准。</div>
</div></div>

### #语音分离

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="promptsep-speaker-generative-target-speaker-extraction-via-m-2610-23066/">PromptSep-Speaker: Generative Target Speaker Extraction via Multimodal Prompting and Semantic Alignment</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">用潜扩散生成式框架统一四种目标线索（时序、文本、注册音频、说话人描述）做目标说话人提取，并用冻结 WavLM 对齐损失监督交叉注意力。</div>
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
<a class="card-title" href="d-composer-language-modeling-for-simultaneous-drum-transcrip-2610-22535/">D-Composer: Language Modeling for Simultaneous Drum Transcription and Sound Event Decomposition</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#乐器分离</span>
</div>
<div class="card-tldr">用自回归语言模型把鼓录音分解为带标签的单次击打事件与起始时间，统一鼓转录与音源分解。</div>
</div></div>

## 📊 完整排行榜

| 排名 | 论文 | 评分 | 主任务 |
| --- | --- | --- | --- |
| 🥇 | [PromptSep-Speaker: Generative Target Speaker Extraction via …](promptsep-speaker-generative-target-speaker-extraction-via-m-2610-23066/) 🎯 | **9.2** | #目标说话人提取 |
| 🥈 | [TV-AudioRemover: Joint Text-Visual Guided Sound Removal with…](tv-audioremover-joint-text-visual-guided-sound-removal-with--2609-25864/) 🎯 | **8.2** | #目标说话人提取 |
| 🥉 | [D-Composer: Language Modeling for Simultaneous Drum Transcri…](d-composer-language-modeling-for-simultaneous-drum-transcrip-2610-22535/) 🎯 | **8.2** | #乐器分离 |
| 4. | [AcousticAgent: A Floorplan-Centric Simulation Platform for D…](acousticagent-a-floorplan-centric-simulation-platform-for-di-2610-22936/) 🎯 | **8.2** | #声学模拟 |
| 5. | [SpeechCritic: Learning a Diagnostic Speech Judge from Limite…](speechcritic-learning-a-diagnostic-speech-judge-from-limited-2609-34582/) | **7.2** | #语音质量评估 |
| 6. | [VocalGrad: Evaluating Acoustic Perception in Audio Language …](vocalgrad-evaluating-acoustic-perception-in-audio-language-m-2610-23745/) | **7.2** | #音频理解评测 |
| 7. | [Flash RNN-T: Memory-Efficient Joint Network and Transducer L…](flash-rnn-t-memory-efficient-joint-network-and-transducer-lo-2610-23409/) | **7.0** | #语音识别 |
| 8. | [Beyond the Benchmark: Conditioning, Domains and Failure Mode…](beyond-the-benchmark-conditioning-domains-and-failure-modes--2610-23678/) | **6.8** | #语音合成 |
| 9. | [Jarvis: Coordination Deserves a Brain of Its Own in Agentic …](jarvis-coordination-deserves-a-brain-of-its-own-in-agentic-i-2610-23804/) | **6.5** | #语音对话系统 |
| 10. | [SEA-HELM Audio: Evaluating Multilingual ASR-LLM Pipeline Per…](sea-helm-audio-evaluating-multilingual-asr-llm-pipeline-perf-2610-19869/) | **6.0** | #语音识别 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="promptsep-speaker-generative-target-speaker-extraction-via-m-2610-23066/">PromptSep-Speaker: Generative Target Speaker Extraction via Multimodal Prompting and Semantic Alignment</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#目标说话人提取</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用潜扩散生成式框架统一四种目标线索（时序、文本、注册音频、说话人描述）做目标说话人提取，并用冻结 WavLM 对齐损失监督交叉注意力。</div>
<div class="card-action">
<a href="promptsep-speaker-generative-target-speaker-extraction-via-m-2610-23066/">详情 →</a> · <a href="https://arxiv.org/abs/2610.23066" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="tv-audioremover-joint-text-visual-guided-sound-removal-with--2609-25864/">TV-AudioRemover: Joint Text-Visual Guided Sound Removal with Multi-Task Hard-Mixture Curriculum</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#目标说话人提取</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用编辑后视频与文本指令联合引导，从混合音轨中移除被删物体对应的声音，并构建百万级数据集与评测基准。</div>
<div class="card-action">
<a href="tv-audioremover-joint-text-visual-guided-sound-removal-with--2609-25864/">详情 →</a> · <a href="https://arxiv.org/abs/2609.25864" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="d-composer-language-modeling-for-simultaneous-drum-transcrip-2610-22535/">D-Composer: Language Modeling for Simultaneous Drum Transcription and Sound Event Decomposition</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#乐器分离</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用自回归语言模型把鼓录音分解为带标签的单次击打事件与起始时间，统一鼓转录与音源分解。</div>
<div class="card-action">
<a href="d-composer-language-modeling-for-simultaneous-drum-transcrip-2610-22535/">详情 →</a> · <a href="https://arxiv.org/abs/2610.22535" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="acousticagent-a-floorplan-centric-simulation-platform-for-di-2610-22936/">AcousticAgent: A Floorplan-Centric Simulation Platform for Distributed Multi-Room Speech Processing</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#声学模拟</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出以户型图为中心的多房间声学仿真平台，生成多通道RIR并构建FP-RIR数据集，验证分布式麦克风对远场语音处理的价值。</div>
<div class="card-action">
<a href="acousticagent-a-floorplan-centric-simulation-platform-for-di-2610-22936/">详情 →</a> · <a href="https://arxiv.org/abs/2610.22936" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="speechcritic-learning-a-diagnostic-speech-judge-from-limited-2609-34582/">SpeechCritic: Learning a Diagnostic Speech Judge from Limited Human Preferences</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音质量评估</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用约300条人类偏好标注校准前沿音频语言模型，构建可解释的多维度语音诊断评判器，并训练7B学生模型。</div>
<div class="card-action">
<a href="speechcritic-learning-a-diagnostic-speech-judge-from-limited-2609-34582/">详情 →</a> · <a href="https://arxiv.org/abs/2609.34582" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="vocalgrad-evaluating-acoustic-perception-in-audio-language-m-2610-23745/">VocalGrad: Evaluating Acoustic Perception in Audio Language Models</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音频理解评测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出 VocalGrad 基准，用时间变化方向二分类检验音频语言模型的低层声学感知，发现其接近随机水平。</div>
<div class="card-action">
<a href="vocalgrad-evaluating-acoustic-perception-in-audio-language-m-2610-23745/">详情 →</a> · <a href="https://arxiv.org/abs/2610.23745" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="flash-rnn-t-memory-efficient-joint-network-and-transducer-lo-2610-23409/">Flash RNN-T: Memory-Efficient Joint Network and Transducer Loss Computation</a>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出 Flash RNN-T，用专用 kernel 与可选分块重计算实现联合网络与 Transducer loss 的省显存高吞吐训练。</div>
<div class="card-action">
<a href="flash-rnn-t-memory-efficient-joint-network-and-transducer-lo-2610-23409/">详情 →</a> · <a href="https://arxiv.org/abs/2610.23409" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="beyond-the-benchmark-conditioning-domains-and-failure-modes--2610-23678/">Beyond the Benchmark: Conditioning, Domains and Failure Modes of Qwen3-TTS</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">系统评测 Qwen3-TTS 的 ICL 与 X-Vector 两种克隆接口，在朗读、会议、情感、ATC 语音上对比四个 TTS 系统并分析失败模式。</div>
<div class="card-action">
<a href="beyond-the-benchmark-conditioning-domains-and-failure-modes--2610-23678/">详情 →</a> · <a href="https://arxiv.org/abs/2610.23678" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="jarvis-coordination-deserves-a-brain-of-its-own-in-agentic-i-2610-23804/">Jarvis: Coordination Deserves a Brain of Its Own in Agentic Interactive Models</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#语音对话系统</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">提出 Jarvis 协调框架，用类型化决策模型 JEV 与代码校验管理前后台模型的任务版本，提升全双工语音智能体的任务成功率。</div>
<div class="card-action">
<a href="jarvis-coordination-deserves-a-brain-of-its-own-in-agentic-i-2610-23804/">详情 →</a> · <a href="https://arxiv.org/abs/2610.23804" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="sea-helm-audio-evaluating-multilingual-asr-llm-pipeline-perf-2610-19869/">SEA-HELM Audio: Evaluating Multilingual ASR-LLM Pipeline Performance Across SEA-HELM Subsets</a>
<div class="card-meta">
<span class="card-score">6.0</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">提出 SEA-HELM Audio 基准，用合成语音评测东南亚多语言 ASR-LLM 级联管线，量化语音与文本输入间的性能落差。</div>
<div class="card-action">
<a href="sea-helm-audio-evaluating-multilingual-asr-llm-pipeline-perf-2610-19869/">详情 →</a> · <a href="https://arxiv.org/abs/2610.19869" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
