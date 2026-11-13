---
title: "ZONOS3-Mini Technical Report"
date: 2026-11-13T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "ZONOS3-Mini 是 886M 参数（每 token 激活 100M）的零样本语音克隆 TTS，配 44.1kHz/15Hz 帧率的 ZAC-1 编解码器，可在手机实时运行。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#零样本语音克隆</span> <span class="tag-pill tag-pill-soft">#语音合成</span> <span class="tag-pill tag-pill-soft">#音频编解码</span> <span class="tag-pill tag-pill-soft">#MoE</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.16525</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-12</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.16525" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.16525" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>ZONOS3-Mini 是 886M 参数（每 token 激活 100M）的零样本语音克隆 TTS，配 44.1kHz/15Hz 帧率的 ZAC-1 编解码器，可在手机实时运行。
</div>

## 👥 作者与机构

**Gabriel Clark** ¹ · Sofian Mejjoute · George Close · Beren Millidge

**机构**：Zyphra

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做轻量 TTS / 端侧语音合成的工程与研究读者。值得通读，重点看 §ZAC-1 编解码器设计与 latent MoE 主干（激活参数如何控制），以及 ZTTS2-Eval 的 55 语言集评测协议与表 1 的 WER 对比；复现可直接用其开源训练/推理代码。

## 🌍 研究背景

零样本语音克隆 TTS 近年由大参数量自回归与扩散模型推动，音质与克隆相似度提升明显，但推理慢、显存占用高，难以在笔记本或手机端实时部署。此前 SOTA 多为数十亿参数模型，依赖高帧率声学 token 或多次采样迭代，延迟与算力成本高。本文要解决的是在极小参数量与极低延迟约束下，仍保持有竞争力的克隆保真度与可懂度，并配套设计低帧率、高采样率的音频编解码器。

## 💡 核心创新

1. latent MoE 主干，886M 总参但每 token 仅激活 100M
2. ZAC-1 编解码器：44.1kHz 音频压缩到 15Hz 帧率
3. 端侧实时推理，笔记本/手机可跑
4. 提出 ZTTS2-Eval 多语种零样本克隆评测基准

## 🏗️ 模型架构

输入为文本 token 与参考语音的说话人/音色条件，参考语音先经 ZAC-1 编码器压缩为 15Hz 的 44.1kHz 表示；主干为 latent MoE 架构，总参数 886M、每 token 仅路由激活约 100M，在隐空间自回归/流式生成声学 latent；再由 ZAC-1 解码器还原为 44.1kHz 波形。整体面向低延迟流式推理，适配端侧部署。摘要未给出更多层数、专家数等细节。

## 📚 数据集

- ZTTS2-Eval（评估，55 个语言集：35 clean + 20 in the wild）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| macro-average WER | ZTTS2-Eval（55 语言集） | 更大更慢的 SOTA 模型（摘要未给具体数值） | **6.71%** | 摘要称具竞争力，未给具体差值 |

摘要仅报告 ZTTS2-Eval 上 55 个语言集（35 clean、20 in the wild）的宏平均 WER 为 6.71%，称与更大更慢的 SOTA 模型相当。未给出说话人相似度（SECS/SIM）、MOS、RTF 或延迟的具体数字，也未列各基线逐项对比，因此克隆保真度与实时性仅有定性描述。

## 🎯 结论与影响

最强结论是：在 886M 总参、每 token 100M 激活的极小预算下，配合 15Hz 帧率 ZAC-1 编解码器，零样本克隆 TTS 的 WER 仍可与大模型竞争。这为端侧实时 TTS 提供了可行路线，并开源权重与训练代码，利于后续在低资源部署与多语种克隆方向复现与改进。

## ⚠️ 局限与未解决问题

技术报告性质，缺少与具体 SOTA 的逐项数值对比、说话人相似度与 MOS 主观评测、RTF/延迟实测；MoE 路由与 ZAC-1 均无消融；ZTTS2-Eval 为自建基准，外部可比性有限；55 语言集的 in-the-wild 子集分布与偏差未说明。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-11-13/">← 返回 2026-11-13 速递</a></div>
