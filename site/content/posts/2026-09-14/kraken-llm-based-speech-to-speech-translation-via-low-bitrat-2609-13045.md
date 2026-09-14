---
title: "Kraken: LLM-based Speech-to-Speech Translation via Low-bitrate VQ and Dual-path Source Conditioning"
date: 2026-09-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音到语音翻译"]
summary: "Kraken 用单层 VQ 低比特率 token 重建 SSL 特征，并加源语音条件化的 Autowave-X 解码器，实现 S2ST 的非语言信息迁移。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音到语音翻译</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音到语音翻译</span> <span class="tag-pill tag-pill-soft">#语音合成</span> <span class="tag-pill tag-pill-soft">#语音大模型</span> <span class="tag-pill tag-pill-soft">#矢量量化</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.13045</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-14</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.13045" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.13045" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>Kraken 用单层 VQ 低比特率 token 重建 SSL 特征，并加源语音条件化的 Autowave-X 解码器，实现 S2ST 的非语言信息迁移。
</div>

## 👥 作者与机构

**Hayato Futami** ¹ · Hassan Shahmohammadi · Tushar Dhyani · Alkis Koudounas · Rapha\"el Lafargue · Yosuke Kashiwagi · Quentin Jodelet · Emiru Tsunoo

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做 S2ST、语音 LLM、神经编解码的读者。建议通读，重点看 §3 的 VQ token 设计与 Autowave-X 双路源条件机制，以及表 2 的翻译质量与说话人/韵律迁移对比。若只关心工程落地，可先看数据规模与推理成本部分。

## 🌍 研究背景

S2ST 近期由 speech LLM 推动，可联合优化并保留副语言信息。但现有方法在 LLM 中预测高比特率语音 token 困难，且依赖说话人身份与韵律对齐的平行 S2ST 数据。SeamlessM4T-Large v2、Qwen2.5-Omni 等强基线仍受此约束。本文要解决低比特率 token 建模与训练数据约束放松两个问题。

## 💡 核心创新

1. 单层 VQ 低比特率 token，重建 SSL 特征而非波形
2. Autowave-X 解码器以源语音为条件，增强非语言迁移
3. 基于 Qwen3-8B 扩展语音输入与 token 输出
4. 150k 小时多语多任务训练，放松对齐数据依赖

## 🏗️ 模型架构

输入为源语音的 SSL 特征，经投影后送入预训练 Qwen3-8B LLM；LLM 输出低比特率单层 VQ token，该 token 由重建 SSL 特征训练得到。随后 Autowave-X token-to-waveform 解码器在源语音条件下将 token 还原为波形，以迁移说话人与韵律。整体为 LLM + VQ + 源条件声码器三段式，摘要未给参数量。

## 📚 数据集

- 150k 小时多语多任务语音数据（训练）
- SeamlessM4T-Large v2 对比基线（评估）
- Qwen2.5-Omni 对比基线（评估）

## 📊 实验结果

摘要仅称翻译质量优于 SeamlessM4T-Large v2 与 Qwen2.5-Omni，并改善说话人与韵律迁移，未给出 BLEU/COMET/MOS 等具体数值，也无消融与效率指标。因此无法量化提升幅度，需查阅正文表格确认。

## 🎯 结论与影响

最强结论是低比特率 VQ token 加源条件解码器可在放松数据约束下同时提升翻译质量与非语言迁移。该思路可能推动 S2ST 中 token 率与声码器条件化的后续研究，对工业多语同传与配音落地有参考价值。

## ⚠️ 局限与未解决问题

摘要未报推理延迟、token 率与参数量，缺少消融验证 VQ 层数与源条件各自贡献；对比仅两个基线，未与专用 S2ST 系统全面比较；150k 小时数据构成与对齐程度未说明，可能存在语言偏置。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-09-14/">← 返回 2026-09-14 速递</a></div>
