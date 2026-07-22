---
title: "Harness TTS: Towards Context-Aware Expressive Speech Synthesis with Harness Layer"
date: 2026-07-22T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "提出Harness TTS，通过轻量控制层将风格控制转化为闭集提示工具路由，实现上下文感知的表达性语音合成。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#表达性语音合成</span> <span class="tag-pill tag-pill-soft">#风格控制</span> <span class="tag-pill tag-pill-soft">#大语言模型</span> <span class="tag-pill tag-pill-soft">#提示路由</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.17900</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.17900" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.17900" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Harness TTS，通过轻量控制层将风格控制转化为闭集提示工具路由，实现上下文感知的表达性语音合成。
</div>

## 👥 作者与机构

**Shengfan Shen** ¹ · Di Wu · Xingchen Song · Dinghao Zhou · Pengyu Cheng · Sixiang Lyu · Jian Luan · Shuai Wang

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音合成和语音助手方向的研究者。建议重点阅读§3（Harness层设计）和§4（路由与合成实验）。可先看表1和表2了解路由准确率和合成质量提升。

## 🌍 研究背景

现有表达性语音合成方法通常依赖显式风格标签或参考音频，难以灵活适应隐式上下文和冲突指令。LLM在语音合成中的应用多限于文本增强或情感分类，缺乏对风格控制的系统化路由机制。本文提出Harness层，将风格控制外部化为可审计的提示工具路由，解决上下文感知表达性合成问题。

## 💡 核心创新

1. 提出Harness层，将风格控制重构为闭集提示工具路由
2. 设计优先级感知观察模式，处理显式、隐式和冲突指令
3. LLM规划器实现毫秒级工具推荐，引入延迟可忽略
4. 在CosyVoice3和VoxCPM2上验证，指令跟随胜率提升13.8-35.6点

## 🏗️ 模型架构

Harness TTS包含离线构建的提示工具注册表和在线LLM规划器。注册表存储带结构化元数据的风格提示音频。在线阶段，LLM规划器（如Qwen3-4B）根据优先级感知观察模式选择工具，TTS执行器（CosyVoice3或VoxCPM2）使用对应提示音频合成语音。整体为轻量控制层包裹TTS引擎。

## 📚 数据集

- 内部数据集（路由评估，含显式、隐式、冲突子集）
- 内部数据集（合成评估，指令跟随和自然度测试）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Top-1准确率 | 显式子集 | 无 | **74.3%** | — |
| Top-1准确率 | 隐式子集 | 无 | **43.0%** | — |
| Top-1准确率 | 冲突子集 | 无 | **64.6%** | — |
| 指令跟随胜率 | CosyVoice3 | 指令仅控制 | **23.1-35.6点提升** | +23.1~35.6点 |
| UTMOSv2 | CosyVoice3 | 指令仅控制 | **提升0.11-0.38** | +0.11~0.38 |

路由任务中，Qwen3-4B在显式、隐式、冲突子集上分别达到74.3%、43.0%、64.6%的Top-1准确率。合成任务中，Harness TTS在CosyVoice3和VoxCPM2上均显著优于指令仅控制基线，指令跟随胜率提升13.8-35.6点，UTMOSv2提升0.11-0.38。4B规划器在标准模式下首工具推荐延迟低于50ms。

## 🎯 结论与影响

Harness TTS通过轻量Harness层将风格控制外部化为可审计的提示路由，显著提升表达性语音合成的指令跟随能力和自然度，且引入延迟可忽略。该方案为语音助手表达控制提供了实用、可审计的上下文感知解决方案，有望推动LLM在语音合成中的系统化应用。

## ⚠️ 局限与未解决问题

路由准确率在隐式子集上仅43%，仍有较大提升空间。实验仅基于两个TTS引擎，泛化性待验证。未报告不同LLM规划器的对比。缺乏对提示工具注册表构建的消融研究。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-07-22/">← 返回 2026-07-22 速递</a></div>
