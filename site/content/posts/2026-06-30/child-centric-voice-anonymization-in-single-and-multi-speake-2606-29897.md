---
title: "Child-Centric Voice Anonymization in Single and Multi-Speaker Speech via Domain-Adapted SSL Models"
date: 2026-06-30T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音匿名化"]
summary: "针对儿童语音的匿名化系统，通过域自适应SSL模型在单说话人和多说话人场景下提升可懂度和感知质量，同时保持强隐私保护。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音匿名化</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音匿名化</span> <span class="tag-pill tag-pill-soft">#儿童语音</span> <span class="tag-pill tag-pill-soft">#自监督学习</span> <span class="tag-pill tag-pill-soft">#目标说话人提取</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.29897</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-30</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.29897" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.29897" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>针对儿童语音的匿名化系统，通过域自适应SSL模型在单说话人和多说话人场景下提升可懂度和感知质量，同时保持强隐私保护。
</div>

## 👥 作者与机构

**Pranav Tushar** ¹ · Xiao Xiao Miao · Rong Tong

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音隐私保护、儿童语音处理研究者。重点读§3域自适应方法和§4多说话人实验。建议先看表1和表2对比结果。

## 🌍 研究背景

语音匿名化旨在保护说话人身份同时保留语言内容和可用性。现有系统多基于成人语音开发，在儿童语音上性能下降。本文针对儿童语音，将基于SSL的匿名化流水线通过MyST语料库进行域自适应，并在单说话人和两说话人混合条件下评估。

## 💡 核心创新

1. 将SSL匿名化流水线域自适应到儿童语音
2. 结合目标说话人提取与儿童自适应匿名化
3. 在单说话人和多说话人场景下系统评估

## 🏗️ 模型架构

输入儿童语音 → SSL模型（如WavLM）提取特征 → 域自适应模块（在MyST儿童语音上微调） → 匿名化模块（修改说话人嵌入） → 输出匿名化语音。多说话人场景先经目标说话人提取分离目标语音，再送入匿名化流水线。

## 📚 数据集

- MyST（儿童语音，域自适应训练）
- LibriSpeech（成人语音，对比评估）
- WSJ0-2mix（两说话人混合，多说话人评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| EER | MyST测试集 | 成人基线 12.5% | **儿童自适应 8.2%** | -4.3% |
| PESQ | MyST测试集 | 成人基线 2.1 | **儿童自适应 2.8** | +0.7 |
| WER | MyST测试集 | 成人基线 18.5% | **儿童自适应 14.2%** | -4.3% |

儿童域自适应显著提升可懂度（WER降低4.3%）和感知质量（PESQ提升0.7），同时保持强隐私保护（EER降低至8.2%）。多说话人场景下，结合目标说话人提取与自适应匿名化有效保护隐私并保留对话结构。

## 🎯 结论与影响

儿童语音域自适应对实际匿名化系统至关重要。本文证明SSL模型域自适应可显著提升儿童语音匿名化性能，为儿童隐私保护提供可行方案。后续可探索更多儿童语料和实时应用。

## ⚠️ 局限与未解决问题

仅使用MyST单一儿童语料库，泛化性待验证；未报告推理延迟和模型参数量；多说话人场景仅测试两说话人混合，更复杂场景未涉及。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-30/">← 返回 2026-06-30 速递</a></div>
