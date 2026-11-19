---
title: "RespCCT and FreqCCT: Compact, Explainable and Cost-Aware Convolutional Transformers for Multi-Class Respiratory Disease Classification"
date: 2026-11-19T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#生物声学"]
summary: "提出两个紧凑卷积Transformer用于七类呼吸疾病音分类，参数量仅12万~17万，精度接近ImageNet预训练大模型并给出成本与可解释性分析。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.2</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#生物声学</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#呼吸音分类</span> <span class="tag-pill tag-pill-soft">#卷积Transformer</span> <span class="tag-pill tag-pill-soft">#轻量化模型</span> <span class="tag-pill tag-pill-soft">#可解释性</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.24323</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.24323" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.24323" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出两个紧凑卷积Transformer用于七类呼吸疾病音分类，参数量仅12万~17万，精度接近ImageNet预训练大模型并给出成本与可解释性分析。
</div>

## 👥 作者与机构

**Auntor Chakma** ¹ · Mst. Farhana Akter · Abu Henaf Rashid Ahmad Mufti · Asmana Yasmin

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做医疗声学、边缘端音频分类与轻量化模型的读者。若关注呼吸音分类精度对比，重点看 §3 模型结构与表 2 的 paired bootstrap 结果；若关注部署成本，看 CPU 单线程各阶段耗时与权重存储对比。不建议通读，方法学增量有限。

## 🌍 研究背景

呼吸音听诊依赖医生主观经验，在缺乏受训听诊者的地区需要自动判读软件。此前最准确的公开分类器多微调大型 ImageNet 预训练网络（如 ResNet、EfficientNet 系列），精度虽高但参数量大、推理成本高，且论文很少同时报告运行成本与配对统计显著性。本文针对资源受限场景，试图用随机初始化的小型卷积 Transformer 在多个公开呼吸音数据库上达到接近大模型的精度，并系统量化存储、时间与可解释性代价。

## 💡 核心创新

1. 提出 RespCCT（173,187 参数）与 FreqCCT（124,999 参数）两个紧凑卷积 Transformer，随机初始化训练
2. 融合 mel、constant-Q、倒谱三种时频图像作为输入表示
3. 用 paired bootstrap 区间与五个 ImageNet 预训练网络做统计对比
4. 在单 CPU 线程上逐阶段测量流水线成本，并用线性探针检验特征是否泄露录音来源

## 🏗️ 模型架构

输入为 5 秒帧的 mel 谱、constant-Q 变换与倒谱三种图像表示，分别送入两个紧凑卷积 Transformer。RespCCT 与 FreqCCT 均以卷积层做局部特征提取后接 Transformer 编码块建模全局依赖，从随机初始化开始训练，不加载 ImageNet 权重，最终经分类头输出七类呼吸疾病概率。两模型参数量分别为 173,187 与 124,999，权重存储显著小于预训练大网络；摘要未给出层数、通道数等更细结构。

## 📚 数据集

- ICBHI（训练/评估，公共呼吸音数据库）
- KAUH（训练/评估）
- RD@TR（训练/评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Accuracy | 三库合并测试折 | 最强预训练网络 macro F1 0.984（精度未单列） | **RespCCT 98.13%** | — |
| Macro F1 | 三库合并测试折 | 最强预训练网络 0.984 | **RespCCT 0.970** | -0.014 |
| Macro F1 | 五折平均 | FreqCCT 单种子 0.941 | **RespCCT 三种子 0.959** | +0.018 |
| 权重存储 | — | 预训练网络（相对值 1） | **RespCCT 需少 2.0~64.6 倍** | 存储降低 2.0~64.6× |

测试折上 RespCCT 达 98.13% 精度、macro F1 0.970，FreqCCT 为 97.58% 与 0.951；五折多种子下 RespCCT 为 97.65%/0.959。最强预训练网络 macro F1 0.984，仍略高，但 RespCCT 权重存储少 2.0~64.6 倍。成本分析显示生成三种输入图像比运行模型本身更耗时；线性探针以 0.958 精度识别来源数据库，提示特征中存在明显录音源偏置。

## 🎯 结论与影响

最强结论是：随机初始化的十万级参数卷积 Transformer 可在呼吸音七分类上逼近 ImageNet 预训练大模型，同时大幅降低存储需求。这为资源受限听诊设备提供了可权衡精度与成本的方案，也提示后续研究应把运行成本与配对统计作为标准报告项。工业落地需先解决输入特征提取耗时与跨库来源偏置问题。

## ⚠️ 局限与未解决问题

线性探针 0.958 的来源数据库识别精度说明模型可能学到录音设备/环境捷径而非病理特征，跨库泛化存疑。FreqCCT 仅单种子、五折统计不完整；未报告推理延迟的绝对值与端到端设备实测；与预训练网络的对比缺少同等参数量级的消融；三库合并七类划分的类别不平衡与患者级划分方式未在摘要说明。

---

<div class="paper-footer"><span>评分：6.2</span><span>原始：6.2</span><a href="/audio-paper-daily/posts/2026-11-19/">← 返回 2026-11-19 速递</a></div>
