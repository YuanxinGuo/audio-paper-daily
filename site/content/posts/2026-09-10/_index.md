---
title: "语音/音频论文速递 2026-09-10"
date: 2026-09-10T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 2 篇 · 最高分 8.6（#语音增强）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">2</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.6</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #音频深度伪造检测 | 2篇 | `██████████` |
| #语音增强 | 1篇 | `█████` |
| #自监督语音表征分析 | 1篇 | `█████` |
| #语音合成 | 1篇 | `█████` |
| #语音安全 | 1篇 | `█████` |
| #音频处理 | 1篇 | `█████` |
| #语音理解 | 1篇 | `█████` |
| #语音识别 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="teacher-free-self-distilled-consistency-trajectory-learning--2609-10392/">Teacher-Free Self-Distilled Consistency Trajectory Learning for Fast Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">8.6</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">用EMA自蒸馏替代外部教师，实现无教师一致性轨迹语音增强，VoiceBank+DEMAND上PESQ 3.01、SI-SDR 19.07 dB。</div>
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

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="timecues-studio-a-workspace-for-music-annotation-and-algorit-2609-10338/">TimeCues Studio: A Workspace for Music Annotation and Algorithm Prototyping</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#音频处理</span>
</div>
<div class="card-tldr">TimeCues Studio 是一个开源音乐标注与算法原型工作台，支持团队批量标注、基线对比与 Python 沙盒开发。</div>
</div></div>

## 📊 完整排行榜

| 排名 | 论文 | 评分 | 主任务 |
| --- | --- | --- | --- |
| 🥇 | [Teacher-Free Self-Distilled Consistency Trajectory Learning …](teacher-free-self-distilled-consistency-trajectory-learning--2609-10392/) 🎯 | **8.6** | #语音增强 |
| 🥈 | [Do speech foundation models really learn words?](do-speech-foundation-models-really-learn-words-2609-10434/) | **6.8** | #自监督语音表征分析 |
| 🥉 | [Zero-Shot Temporal Localisation of Audio Deepfakes in Multi-…](zero-shot-temporal-localisation-of-audio-deepfakes-in-multi--2609-10051/) | **6.8** | #音频深度伪造检测 |
| 4. | [Deterministic Prompting for Speaker-Stable Low-Resource Gree…](deterministic-prompting-for-speaker-stable-low-resource-gree-2609-10022/) | **6.8** | #语音合成 |
| 5. | [Audio Deepfake Detection Using Temporal Coherence Analysis](audio-deepfake-detection-using-temporal-coherence-analysis-2609-09489/) | **6.5** | #音频深度伪造检测 |
| 6. | [DuplexJail: Safety Alignment Breaks Under Spoken Interruptio…](duplexjail-safety-alignment-breaks-under-spoken-interruption-2609-09420/) | **6.5** | #语音安全 |
| 7. | [TimeCues Studio: A Workspace for Music Annotation and Algori…](timecues-studio-a-workspace-for-music-annotation-and-algorit-2609-10338/) 🎯 | **6.5** | #音频处理 |
| 8. | [Who Are They to Each Other? Multi-Agent Reasoning for Speake…](who-are-they-to-each-other-multi-agent-reasoning-for-speaker-2609-09628/) | **6.0** | #语音理解 |
| 9. | [NOPE-HYPE: A Structured Simulation Workflow for Robust Speec…](nope-hype-a-structured-simulation-workflow-for-robust-speech-2609-10058/) | **5.5** | #语音识别 |
| 10. | [Population Ecology of Tunes](population-ecology-of-tunes-2609-09501/) | **3.5** | #音乐信息检索 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="teacher-free-self-distilled-consistency-trajectory-learning--2609-10392/">Teacher-Free Self-Distilled Consistency Trajectory Learning for Fast Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.6</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用EMA自蒸馏替代外部教师，实现无教师一致性轨迹语音增强，VoiceBank+DEMAND上PESQ 3.01、SI-SDR 19.07 dB。</div>
<div class="card-action">
<a href="teacher-free-self-distilled-consistency-trajectory-learning--2609-10392/">详情 →</a> · <a href="https://arxiv.org/abs/2609.10392" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="do-speech-foundation-models-really-learn-words-2609-10434/">Do speech foundation models really learn words?</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#自监督语音表征分析</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">通过残差化剔除音素信息，验证 HuBERT 与 wav2vec 2.0 后层确实编码了独立于音素形式的词级表征。</div>
<div class="card-action">
<a href="do-speech-foundation-models-really-learn-words-2609-10434/">详情 →</a> · <a href="https://arxiv.org/abs/2609.10434" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="zero-shot-temporal-localisation-of-audio-deepfakes-in-multi--2609-10051/">Zero-Shot Temporal Localisation of Audio Deepfakes in Multi-Speaker Conversations</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频深度伪造检测</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出多说话人对话中音频深度伪造的时序定位任务TDLMC，用免训练五阶段流水线包装冻结二分类检测器，实现片段级定位。</div>
<div class="card-action">
<a href="zero-shot-temporal-localisation-of-audio-deepfakes-in-multi--2609-10051/">详情 →</a> · <a href="https://arxiv.org/abs/2609.10051" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="deterministic-prompting-for-speaker-stable-low-resource-gree-2609-10022/">Deterministic Prompting for Speaker-Stable Low-Resource Greek TTS</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">用确定性提示替代LLM生成提示，配合3.5小时单说话人LoRA微调Parler-TTS，实现稳定的低资源希腊语TTS。</div>
<div class="card-action">
<a href="deterministic-prompting-for-speaker-stable-low-resource-gree-2609-10022/">详情 →</a> · <a href="https://arxiv.org/abs/2609.10022" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="audio-deepfake-detection-using-temporal-coherence-analysis-2609-09489/">Audio Deepfake Detection Using Temporal Coherence Analysis</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#音频深度伪造检测</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">基于 CLAP 嵌入的时序一致性分析，用轻量集成分类器区分真实与合成语音及音乐。</div>
<div class="card-action">
<a href="audio-deepfake-detection-using-temporal-coherence-analysis-2609-09489/">详情 →</a> · <a href="https://arxiv.org/abs/2609.09489" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="duplexjail-safety-alignment-breaks-under-spoken-interruption-2609-09420/">DuplexJail: Safety Alignment Breaks Under Spoken Interruption in Full-Duplex Models</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#语音安全</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">提出 DuplexJail，通过用户音频通道注入与请求无关的固定语音提示，打断全双工模型生成，使 AdvBench 攻击成功率最高升至 48.7%。</div>
<div class="card-action">
<a href="duplexjail-safety-alignment-breaks-under-spoken-interruption-2609-09420/">详情 →</a> · <a href="https://arxiv.org/abs/2609.09420" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="timecues-studio-a-workspace-for-music-annotation-and-algorit-2609-10338/">TimeCues Studio: A Workspace for Music Annotation and Algorithm Prototyping</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#音频处理</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">TimeCues Studio 是一个开源音乐标注与算法原型工作台，支持团队批量标注、基线对比与 Python 沙盒开发。</div>
<div class="card-action">
<a href="timecues-studio-a-workspace-for-music-annotation-and-algorit-2609-10338/">详情 →</a> · <a href="https://arxiv.org/abs/2609.10338" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="who-are-they-to-each-other-multi-agent-reasoning-for-speaker-2609-09628/">Who Are They to Each Other? Multi-Agent Reasoning for Speaker Relationship Inference</a>
<div class="card-meta">
<span class="card-score">6.0</span>
<span class="tag-pill">#语音理解</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">提出免训练多智能体推理框架，通过角色化辩论与竞争式裁决，从对话中推断说话人关系。</div>
<div class="card-action">
<a href="who-are-they-to-each-other-multi-agent-reasoning-for-speaker-2609-09628/">详情 →</a> · <a href="https://arxiv.org/abs/2609.09628" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="nope-hype-a-structured-simulation-workflow-for-robust-speech-2609-10058/">NOPE-HYPE: A Structured Simulation Workflow for Robust Speech-to-Text Across Diverse Acoustic Environments</a>
<div class="card-meta">
<span class="card-score">5.5</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">提出 NOPE-HYPE 仿真工作流，用可控环境模拟器加 PSD 覆盖最优环境缩减，提升 Whisper 与 SeamlessM4T 在多样声学环境下的语音转文本鲁棒性。</div>
<div class="card-action">
<a href="nope-hype-a-structured-simulation-workflow-for-robust-speech-2609-10058/">详情 →</a> · <a href="https://arxiv.org/abs/2609.10058" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="population-ecology-of-tunes-2609-09501/">Population Ecology of Tunes</a>
<div class="card-meta">
<span class="card-score">3.5</span>
<span class="tag-pill">#音乐信息检索</span>
<span class="card-tier">后50%</span>
</div>
<div class="card-tldr">用13年约2万首爱尔兰传统曲目的周流行度数据，拟合生态学生灭过程模型，量化曲调适应度差异与多样性维持机制。</div>
<div class="card-action">
<a href="population-ecology-of-tunes-2609-09501/">详情 →</a> · <a href="https://arxiv.org/abs/2609.09501" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
