---
title: "Confucius4-TTS: Transcript-Free Cross-Lingual Zero-Shot TTS with a Learnable Speaker Encoder"
date: 2026-08-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "Confucius4-TTS提出无需参考音频转录的跨语言零样本TTS系统，支持14种语言，通过可学习说话人编码器提取音色，在CV3-Eval上WER达3.73%。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#零样本TTS</span> <span class="tag-pill tag-pill-soft">#跨语言语音克隆</span> <span class="tag-pill tag-pill-soft">#说话人编码器</span> <span class="tag-pill tag-pill-soft">#流匹配</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.11650</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-14</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/netease-youdao/Confucius4-TTS" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">netease-youdao/Confucius4-TTS</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.11650" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.11650" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/netease-youdao/Confucius4-TTS" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>Confucius4-TTS提出无需参考音频转录的跨语言零样本TTS系统，支持14种语言，通过可学习说话人编码器提取音色，在CV3-Eval上WER达3.73%。
</div>

## 👥 作者与机构

**Huaxuan Wang** ¹ · Huimin Wang · Ruiyu Zhang · Yingjie Li · Yitao Duan

**机构**：网易有道

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合TTS、语音克隆、跨语言合成研究者阅读。建议重点看第3节模型架构和第4节实验部分，尤其是说话人编码器设计和跨语言评估结果。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

零样本TTS近期取得显著进展，但多数系统在推理时依赖音频提示的转录文本，这限制了跨语言语音克隆，因为真实场景中的参考音频往往未转录。现有方法如VALL-E、YourTTS等或需转录，或跨语言性能有限。本文旨在解决无需参考转录的跨语言零样本TTS问题，提出Confucius4-TTS系统。

## 💡 核心创新

1. 提出可学习说话人编码器，从自监督语音表示中提取音色特征，无需参考转录
2. 两阶段架构：LLM-based T2S + 条件流匹配S2A，支持14种语言
3. 支持续写克隆（当参考转录可用时），增强灵活性
4. 在CV3-Eval跨语言基准上实现3.73%平均WER，优于现有系统

## 🏗️ 模型架构

Confucius4-TTS采用两阶段架构：文本到语义（T2S）和语义到声学（S2A）。T2S模块基于LLM，使用可学习说话人编码器从自监督语音表示（如WavLM）中提取音色特征，与文本编码结合生成语义token。S2A模块采用条件流匹配模型，将预测的语义token转换为mel频谱。系统支持14种语言，训练于大规模多语言数据。

## 📚 数据集

- CV3-Eval（跨语言评估，6个方向）
- 内部跨语言测试集（人类评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | CV3-Eval | 未提供 | **3.73%** | N/A |

在CV3-Eval跨语言基准上，Confucius4-TTS在六个方向上平均WER为3.73%，显示高可懂度。在内部跨语言测试集上，人类评估中平均总体排名最佳，优于近期开源和商业系统。但摘要未提供具体对比数值，仅提及排名。

## 🎯 结论与影响

Confucius4-TTS通过可学习说话人编码器实现了无需参考转录的跨语言零样本TTS，支持14种语言，在可懂度和说话人相似度上表现优异。该工作为跨语言语音克隆提供了新思路，可能推动TTS系统在真实场景中的应用，减少对转录文本的依赖。

## ⚠️ 局限与未解决问题

摘要未提及局限，但作为技术报告，可能缺乏与最新SOTA的详细对比，且内部测试集未公开，可复现性受限。此外，未报告推理延迟和模型参数量，可能影响实际部署评估。

## 🔗 开源资源

- **代码**：<https://github.com/netease-youdao/Confucius4-TTS>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-08-14/">← 返回 2026-08-14 速递</a></div>
