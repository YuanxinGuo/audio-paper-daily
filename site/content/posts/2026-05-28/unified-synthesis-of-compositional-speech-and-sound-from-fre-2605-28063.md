---
title: "Unified Synthesis of Compositional Speech and Sound from Free-Form Text Prompts"
date: 2026-05-28T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频生成"]
summary: "提出PlanAudio，基于LLM的自回归框架，从自由文本提示直接合成包含语音和声音的复合音频。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音生成</span> <span class="tag-pill tag-pill-soft">#声音生成</span> <span class="tag-pill tag-pill-soft">#大语言模型</span> <span class="tag-pill tag-pill-soft">#链式推理</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.28063</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.28063" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.28063" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出PlanAudio，基于LLM的自回归框架，从自由文本提示直接合成包含语音和声音的复合音频。
</div>

## 👥 作者与机构

**Yuyue Wang** ¹ · Xihua Wang · Xin Cheng · Yijing Chen · Ruihua Song

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频生成、多模态LLM研究者。值得通读，重点看§3的语义潜在链式推理机制和§4的PlanAudio-Bench基准。建议先看§3.2与表2。

## 🌍 研究背景

当前音频生成方法要么使用分离的流水线（如先合成语音再合成声音），难以捕捉细粒度交互；要么需要结构化输入或外部文本改写，限制了自由文本提示的灵活性。本文提出新任务：从自由文本直接合成包含语音和声音的复合音频，并设计PlanAudio框架解决该问题。

## 💡 核心创新

1. 利用LLM内在推理能力替代传统文本编码器
2. 提出语义潜在链式推理机制，桥接高层语义与低层声学合成
3. 构建PlanAudio-Bench复合音频评估基准
4. 采用连续多场景训练课程提升泛化性

## 🏗️ 模型架构

输入自由文本提示，通过LLM（如GPT）进行语义理解，经语义潜在链式推理模块生成中间语义表示，再通过自回归声学模型（如AudioLM风格）合成音频波形。整体为端到端自回归框架，无需外部文本改写或结构化输入。

## 📚 数据集

- PlanAudio-Bench（评估复合音频场景）
- LibriTTS（语音训练）
- AudioSet（声音训练）
- 内部复合音频数据集（训练）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| MOS（语音质量） | PlanAudio-Bench | Pipeline baseline 3.2 | **3.8** | +0.6 |
| MOS（声音质量） | PlanAudio-Bench | Pipeline baseline 3.0 | **3.6** | +0.6 |
| MOS（复合一致性） | PlanAudio-Bench | Pipeline baseline 2.8 | **3.5** | +0.7 |

PlanAudio在语音、声音及复合场景的MOS上均优于流水线基线，且与单场景专用模型竞争力相当。消融实验表明语义潜在CoT优于其他CoT机制，连续多场景训练课程对性能提升至关重要。

## 🎯 结论与影响

PlanAudio首次实现从自由文本直接合成复合语音和声音，语义潜在链式推理有效提升了合成质量与一致性。该工作为统一音频生成开辟了新方向，对多模态内容创作和虚拟助手等工业应用具有潜力。

## ⚠️ 局限与未解决问题

未报告推理延迟和模型参数量；复合音频场景的评估依赖主观MOS，缺乏客观指标；训练数据规模未明确；与单场景专用模型相比优势不明显，可能受限于LLM的声学建模能力。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-05-28/">← 返回 2026-05-28 速递</a></div>
