---
title: "LEMMO: A Large Electromagnetic Model leveraging Pretrained LLMs for Million-Sample Signal Understanding"
date: 2026-11-09T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#电磁信号理解"]
summary: "构建面向长原始IQ电磁信号的大模型LEMMO，用线性注意力编码器加抗混叠重采样处理八百万复数样本，并发布1.38TB语料。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.0</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#电磁信号理解</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态大模型</span> <span class="tag-pill tag-pill-soft">#信号理解</span> <span class="tag-pill tag-pill-soft">#长序列建模</span> <span class="tag-pill tag-pill-soft">#指令微调</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.09476</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-09</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/N1rv4n4/LEMMO" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">N1rv4n4/LEMMO</span></span></a><a class="oc-chip oc-chip-hf" href="https://huggingface.co/datasets/DaftJun/RFLAS" target="_blank" rel="noopener"><span class="oc-icon">🤗</span><span class="oc-text"><span class="oc-label">HuggingFace</span><span class="oc-sub">🤗 datasets/DaftJun/RFLAS</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.09476" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.09476" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/N1rv4n4/LEMMO" target="_blank" rel="noopener">💻 代码</a><a class="rsrc rsrc-hf" href="https://huggingface.co/datasets/DaftJun/RFLAS" target="_blank" rel="noopener">🤗 HuggingFace</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>构建面向长原始IQ电磁信号的大模型LEMMO，用线性注意力编码器加抗混叠重采样处理八百万复数样本，并发布1.38TB语料。
</div>

## 👥 作者与机构

**Mingkai Li** ¹ · Jiajun Wu · Yihan Mao · Zilin Sang · Taosong Yu · Yuan Ma · Minghe Liu · Qianqian Yang · … 等 1 人

**机构**：浙江大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做无线/射频信号理解、多模态大模型跨模态扩展的研究者阅读。若关注长序列信号编码与指令驱动描述，值得通读；重点看§3的线性注意力编码器与抗混叠重采样设计、§4的EM-text交互模块与结构化查询，以及表2/表3的EM-Bench与LEMMO-ShortQA对比。若只关心语音/音频五类任务，可略读。

## 🌍 研究背景

LLM已扩展到视觉、音频等模态，但原始电磁信号理解仍困难。宽带记录可达数百万样本，而现有基于波形的EM模型（如MERLIN-LoRA）主要在短IQ片段上评估，缺乏长记录理解与细粒度描述能力。本文要解决长原始IQ记录的指令驱动识别与描述问题，并补齐长记录评测与数据缺口。

## 💡 核心创新

1. 线性注意力EM编码器+抗混叠时间重采样，支持八百万复数样本
2. EM-text交互模块：指令条件化可学习查询再检索信号证据
3. 紧凑查询做识别、结构化查询加辅助事实监督做场景级描述
4. 构建并开源1.38TB真实与合成EM信号统一语料

## 🏗️ 模型架构

输入为长原始IQ复数序列，先经抗混叠时间重采样降采样以控制序列长度，再由线性注意力EM编码器提取长程特征，可处理至八百万复数样本。EM-text交互模块将指令作为条件作用于一组可学习查询，从编码特征中检索信号证据：紧凑查询用于识别任务，结构化查询配合辅助事实监督组织场景属性、信号属性与跨信号关系用于详细描述。输出经语言主干生成文本，摘要未给参数量。

## 📚 数据集

- LEMMO-ShortQA（训练/评估，短问答子集）
- LEMMO-LongDesc（训练/评估，长描述子集）
- EM-Bench（评估，感知与策略生成）
- 1.38TB真实与合成EM信号统一语料（训练）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| EM-Bench 平均感知准确率 | EM-Bench | MERLIN-LoRA | **LEMMO** | +15.77% |
| 策略生成 ROUGE-L F1 | EM-Bench | MERLIN-LoRA | **LEMMO** | +4.38 |
| LEMMO-ShortQA 准确率 | LEMMO-ShortQA | MERLIN-LoRA | **LEMMO** | +14.31% |

摘要给出相对MERLIN-LoRA的三项均值提升：EM-Bench感知准确率+15.77%、策略生成ROUGE-L F1+4.38、ShortQA准确率+14.31%。LEMMO-LongDesc的分类与数值事实F1均有提升，且保留语言主干MMLU性能，说明多模态训练未明显损害语言能力。摘要未给绝对数值与消融细节。

## ⚠️ 局限与未解决问题

摘要仅给相对提升，缺绝对指标与消融；未报推理延迟与显存占用，长序列八百万样本的实际效率不明；1.38TB语料含合成数据，真实/合成比例与偏差未说明；对比基线仅MERLIN-LoRA，缺少更多EM模型与通用音频大模型对照。

## 🔗 开源资源

- **代码**：<https://github.com/N1rv4n4/LEMMO>
- **HuggingFace**：<https://huggingface.co/datasets/DaftJun/RFLAS>
- **数据集**：<https://huggingface.co/datasets/DaftJun/RFLAS>

---

<div class="paper-footer"><span>评分：6.0</span><span>原始：6.0</span><a href="/audio-paper-daily/posts/2026-11-09/">← 返回 2026-11-09 速递</a></div>
