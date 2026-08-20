---
title: "FireRedTTS3: Unified Speech Generation and Editing with Semantically Enriched Speech Representations"
date: 2026-08-20T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音生成"]
summary: "FireRedTTS3通过冻结的语义教师网络正则化连续语音表示，实现稳定可控的语音生成与编辑，在多项基准上取得最优。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音编辑</span> <span class="tag-pill tag-pill-soft">#零样本语音克隆</span> <span class="tag-pill tag-pill-soft">#连续自回归</span> <span class="tag-pill tag-pill-soft">#语义增强</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.17492</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-20</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/FireRedTeam/FireRedTTS3" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">FireRedTeam/FireRedTTS3</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.17492" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.17492" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/FireRedTeam/FireRedTTS3" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>FireRedTTS3通过冻结的语义教师网络正则化连续语音表示，实现稳定可控的语音生成与编辑，在多项基准上取得最优。
</div>

## 👥 作者与机构

**Feiyu Shen** ¹ · Kun Xie · Yichen Wu · Ziqi Dai · Yichen Han · Junjie Li · Xuelong Geng · Fenglong Xie · … 等 3 人

**机构**：阿里巴巴 · 西北工业大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音合成、语音编辑方向的研究者。建议重点阅读第3节方法部分和第4节实验部分，尤其是表1和表2的对比结果。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

连续自回归TTS模型直接在连续语音表示上生成，保留声学细节并利用文本LLM的指令跟随能力，但存在自回归生成中的误差累积问题。现有方案常需额外语义模块、多阶段tokenizer训练或复杂架构。本文旨在通过语义增强的连续表示简化系统，同时提升稳定性和可控性。

## 💡 核心创新

1. 利用冻结的Audio Encoder作为语义教师，正则化音频特征空间
2. 提出FireRedTTS3-Base和-Instruct两个变体，统一生成与编辑
3. 在表示层面缓解误差累积，无需复杂架构
4. 实现多语言多方言零样本克隆和指令控制语音设计

## 🏗️ 模型架构

FireRedTTS3采用连续自回归架构，输入文本和参考音频，通过冻结的Audio Encoder提取语义特征作为教师信号，正则化音频特征空间。主干网络为基于Transformer的LLM，生成连续语音表示，再经声码器合成波形。系统包含Base和Instruct两个变体，后者支持指令控制。

## 📚 数据集

- Seed-TTS-Eval（评估，语音可懂度和相似度）
- MiniMax-MLS-Test（评估，多语言多方言）
- InstructTTSEval（评估，指令控制）
- Ming-Freeform-Audio-Edit（评估，语音编辑）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 语音可懂度 | Seed-TTS-Eval | 未给出具体值 | **最佳** | 未给出 |
| 说话人相似度 | Seed-TTS-Eval | 未给出具体值 | **最佳** | 未给出 |
| 综合性能 | InstructTTSEval | 未给出具体值 | **优于对比系统** | 未给出 |

实验表明FireRedTTS3-Base在Seed-TTS-Eval和MiniMax-MLS-Test上取得最佳平均语音可懂度和说话人相似度，FireRedTTS3-Instruct在InstructTTSEval和Ming-Freeform-Audio-Edit上优于对比系统。摘要未提供具体数值，但强调语义增强的连续表示结合简单架构能实现稳定、可控、高保真的语音生成与编辑。

## 🎯 结论与影响

FireRedTTS3通过语义增强的连续语音表示，在简化架构的同时提升了生成稳定性和可控性，在多个基准上达到最优。该工作表明语义信息对连续自回归TTS的重要性，为后续研究提供了新思路，有望推动语音克隆和编辑技术的工业应用。

## ⚠️ 局限与未解决问题

摘要未提及具体局限，但作为审稿人可看出：缺乏与最新SOTA的详细数值对比，未报告推理延迟和模型参数量，未进行消融实验验证语义教师的作用，且评估数据集可能偏向特定场景。

## 🔗 开源资源

- **代码**：<https://github.com/FireRedTeam/FireRedTTS3>

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-08-20/">← 返回 2026-08-20 速递</a></div>
