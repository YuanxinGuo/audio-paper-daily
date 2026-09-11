---
title: "Unadapted Multilingual ASR on a Garrusi Kurdish Evaluation Set: A Common-Reference Staged Normalization Analysis"
date: 2026-09-11T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "在Garrusi库尔德语评测集上，用统一参考的归一化设计重新度量MMS-1B-all的WER/CER，指出书写系统差异会污染评分。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">4.5</div>
<div class="score-stars">★★☆☆☆</div>
<div class="score-tier">后50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#低资源语音识别</span> <span class="tag-pill tag-pill-soft">#多语言ASR</span> <span class="tag-pill tag-pill-soft">#评价方法</span> <span class="tag-pill tag-pill-soft">#正字法归一化</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.16379</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-11</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.16379" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.16379" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>在Garrusi库尔德语评测集上，用统一参考的归一化设计重新度量MMS-1B-all的WER/CER，指出书写系统差异会污染评分。
</div>

## 👥 作者与机构

**Hiwa Asadpour** ¹

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做低资源/多语言ASR评测、以及关注WER计算口径的研究者阅读。建议重点看§3的common-reference设计与归一化流程、以及结果表中RAW/TRANSLIT/FOLDED三档对比；实验部分只需扫读。若你关心库尔德语或阿拉伯字母-拉丁转写评测，值得通读方法节并复用其固定参考思路。

## 🌍 研究背景

库尔德语等低资源语言缺乏标准书面正字法，模型常输出阿拉伯字母而参考为拉丁转写，直接打分会把书写系统差异算成识别错误，导致WER虚高、跨系统不可比。此前多语言ASR（如MMS、Whisper）在库尔德语上多以ckb适配器直接评测，缺少对评分口径的显式控制，也少有对同一固定参考下不同假设表示的系统比较。本文要解决的是：在Garrusi库尔德语上建立一个可复现、参考固定的评测协议，分离归一化收益与识别误差。

## 💡 核心创新

1. common-reference设计：参考折叠一次并固定为9763 token，仅变化假设表示
2. 三级评分对比：RAW阿拉伯字母 / 拉丁转写 / 折叠到参考简化正字法
3. 量化归一化贡献：区分转写与折叠各自带来的WER/CER下降
4. 公开固定参考与分段级结果以支持独立复核

## 🏗️ 模型架构

本文不是新模型，而是评测协议研究。输入为1722段Garrusi问卷语音（5位说话人，117.9分钟），使用MMS-1B-all并挂载Central Kurdish (ckb) adapter，按发布状态不做任何微调。流程为：模型输出阿拉伯字母假设 → 分别做RAW、拉丁转写、折叠到参考简化正字法三种表示 → 与固定参考（9763词token）对齐计算WER/CER。另以Southern Kurdish微调系统（aranemini/southern-kurdish-asr）在同一设计下做对照。

## 📚 数据集

- Garrusi Kurdish问卷语音（评估，1722段/5说话人/117.9分钟/9763参考词token）
- aranemini/southern-kurdish-asr对照系统所用数据（评估，1703段）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | Garrusi Kurdish | RAW阿拉伯字母 111.70% | **FOLDED 97.85%** | -13.85 百分点 |
| CER | Garrusi Kurdish | RAW 100.92% | **FOLDED 51.20%** | -49.72 百分点 |
| WER | Garrusi Kurdish | TRANSLIT 102.36% | **FOLDED 97.85%** | -4.51 百分点 |
| CER | Garrusi Kurdish | TRANSLIT 57.89% | **FOLDED 51.20%** | -6.69 百分点 |
| WER | Garrusi Kurdish | Southern Kurdish微调系统 109.56% | **MMS-1B-all FOLDED 97.85%** | -11.71 百分点 |

MMS-1B-all在FOLDED表示下WER 97.85%、CER 51.20%，仍远高于可用水平；仅14.53%参考token精确匹配，编辑以替换为主，短段WER更高。Southern Kurdish微调系统在同一设计下每个说话人都更差（WER 109.56%、CER 55.85%）。作者指出12330个输出字符落在折叠表外，且MMS输出含613个未转换/未映射字符，说明部分残差来自评分管线而非识别本身。

## 🎯 结论与影响

最强结论是：在库尔德语这类书写系统不统一的场景，评分口径本身可造成十余个WER百分点的差异，必须用固定参考设计才能公平比较。这会影响后续低资源ASR评测的规范，提醒研究者报告归一化细节。工业落地含义是：部署前需先对齐正字法与评分管线，否则模型选型可能被评分假象误导。

## ⚠️ 局限与未解决问题

作者承认折叠表覆盖不全（12330字符未覆盖、613字符未映射），导致WER/CER需对修正参考重算，当前数值不可直接引用。此外仅5位说话人、单一方言，无置信区间与显著性检验；未报告推理延迟与模型规模；对照系统仅一个，缺少与Whisper等主流多语言ASR的横向比较。

---

<div class="paper-footer"><span>评分：4.5</span><span>原始：4.5</span><a href="/audio-paper-daily/posts/2026-09-11/">← 返回 2026-09-11 速递</a></div>
