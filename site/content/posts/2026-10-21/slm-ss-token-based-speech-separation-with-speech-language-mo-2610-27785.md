---
title: "SLM-SS: Token-Based Speech Separation with Speech Language Models"
date: 2026-10-21T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音分离"]
summary: "用神经编解码器离散化语音，以自回归 SLM 预测零阶 token 建立说话人顺序，再用非自回归模块精修高阶残差码本，实现生成式语音分离。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音分离</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#语音语言模型</span> <span class="tag-pill tag-pill-soft">#神经音频编解码器</span> <span class="tag-pill tag-pill-soft">#生成式模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.27785</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-21</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.27785" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.27785" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用神经编解码器离散化语音，以自回归 SLM 预测零阶 token 建立说话人顺序，再用非自回归模块精修高阶残差码本，实现生成式语音分离。
</div>

## 👥 作者与机构

**Chenda Li** ¹ · Tianhua Li · Yiming Chen · Wei Wang · Jiahe Wang · Xin Zhou · Yanmin Qian ✉

**机构**：上海交通大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做生成式语音分离、codec-based 语音建模的研究者与工程团队阅读。建议通读，重点看 §3 的 SOT 序列化与 per-talker NAR 设计，以及表 2 的 WER 与主观质量对比；若关注落地，额外看跨域（噪声/中文）泛化实验与推理效率讨论。

## 🌍 研究背景

当前语音分离主流是判别式方法（Conv-TasNet、SepFormer、BSRNN 等），以 SI-SDR 等信号级指标为优化目标，在 Libri2Mix / WSJ0-2mix 上已接近上限。但信号级最优并不等于下游可懂度最优，输出常残留伪影、影响 ASR 与主观听感。近期神经编解码器与语音语言模型（SLM）在生成式语音建模上进展迅速，本文试图把分离重构为 token 序列生成问题，用语言先验替代纯信号回归。

## 💡 核心创新

1. 用神经编解码器多码本离散化，将分离转为 token 序列生成
2. SOT 序列化多说话人目标，单模型处理变说话人数
3. AR 预测零阶 token 定说话人顺序与粗内容
4. per-talker NAR 精修高阶残差码本，提升稳定性
5. WavTokenizer 变体免 NAR 精修，主观质量最优

## 🏗️ 模型架构

输入为混合语音波形，先经神经编解码器（如 WavTokenizer / EnCodec 类）编码为多码本离散 token 序列；多说话人目标通过 Serialized Output Training (SOT) 串行化为单一序列。主干为 encoder-decoder 自回归语音语言模型，先预测零阶（coarse）token 序列，确定说话人排序与粗粒度语言内容；随后非自回归模块以零阶结果为条件，精修高阶残差码本以重建细节。进一步提出 per-talker NAR 策略，将高阶建模按说话人拆分，简化建模难度并提升稳定性。输出为各说话人的 token 序列，经解码器还原波形。摘要未给出参数量。

## 📚 数据集

- Libri2Mix（训练与评估，2 说话人混合）
- 未见噪声混合与中文混合数据（跨域评估，未微调）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | Libri2Mix | 判别式基线（摘要未给具体值） | **6.92%** | 接近 codec-only 重建上限 |
| UTMOS / DNSMOS | Libri2Mix 及未见噪声/中文混合 | 判别式基线（摘要未给具体值） | **优于判别式基线** | 主观质量领先 |

在 Libri2Mix 上，per-talker NAR 变体取得 6.92% WER，接近仅用 codec 重建的上限，说明生成式分离在可懂度上已具竞争力。WavTokenizer 变体去掉 NAR 精修后取得所评估分离系统中最高的平均主观质量分，且其 UTMOS / DNSMOS 优势在未见噪声与中文混合上无需微调即可保持，体现一定跨域泛化。摘要未给出 SI-SDR 等信号级指标与推理延迟。

## 🎯 结论与影响

最强结论是：token 级生成式分离可在 WER 与主观质量上对标甚至超越判别式系统，并具备跨域泛化。这为语音分离提供了语言先验驱动的新范式，后续可探索更强 SLM 与码本设计。工业上对可懂度敏感的下游（ASR 前端、会议转写）有潜在价值，但需关注推理成本。

## ⚠️ 局限与未解决问题

摘要未报告 SI-SDR 等信号级指标，与判别式 SOTA 的全面对比不足；缺少消融细节与推理延迟/实时率数据；跨域评估仅提及噪声与中文，规模与设置不明；生成式方法可能引入语言先验导致的幻觉或内容偏置，未讨论。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-21/">← 返回 2026-10-21 速递</a></div>
