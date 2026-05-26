---
title: "Focus Then Listen: Exploring Plug-and-Play Audio Enhancer for Noise-Robust Large Audio Language Models"
date: 2026-05-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出即插即用的音频增强模块FTL，通过语音/非语音分离和模态路由，提升大音频语言模型在噪声环境下的鲁棒性，无需微调。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#大音频语言模型</span> <span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#即插即用</span> <span class="tag-pill tag-pill-soft">#噪声鲁棒性</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.04862</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.04862" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.04862" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出即插即用的音频增强模块FTL，通过语音/非语音分离和模态路由，提升大音频语言模型在噪声环境下的鲁棒性，无需微调。
</div>

## 👥 作者与机构

**Han Yin** ¹ · Yang Xiao · Younghoo Kwon · Ting Dang · Jung-Woo Choi ✉

**机构**：韩国科学技术院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合研究大音频语言模型噪声鲁棒性的读者。建议重点阅读§3方法部分和§4实验部分，尤其是表1-3的跨模型、跨任务结果。可先看图2的架构概览。

## 🌍 研究背景

大音频语言模型（LALMs）在真实噪声环境下性能显著下降。现有噪声感知微调方法需要特定噪声数据和昂贵重训练，可扩展性差。本文提出即插即用的音频增强模块FTL，无需微调即可提升LALMs的噪声鲁棒性。

## 💡 核心创新

1. 语音/非语音分离预处理
2. 基于指令的模态路由预测目标模态
3. 模态感知融合块生成任务自适应增强信号

## 🏗️ 模型架构

输入波形首先通过语音分离模块（如SepFormer）分离为语音和非语音流。模态路由器根据用户指令预测目标模态（如语音），输出权重。模态感知融合块将分离后的语音和非语音流加权融合，生成增强信号，输入下游LALM。整个模块即插即用，无需微调LALM。

## 📚 数据集

- AudioSet（训练分离模型）
- LibriSpeech（评估语音理解）
- ESC-50（评估非语音事件分类）
- VocalSound（评估声音事件检测）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | LibriSpeech test-clean (SNR 0dB) | SALMONN 42.3% | **SALMONN+FTL 28.1%** | -14.2% |
| Accuracy | ESC-50 (SNR 0dB) | Qwen2-Audio 52.5% | **Qwen2-Audio+FTL 68.3%** | +15.8% |

FTL在多个LALM（SALMONN、Qwen2-Audio、LLaMA-Omni）和任务（语音识别、音频分类、音频问答）上均显著提升噪声鲁棒性，尤其在低SNR下效果明显。消融实验验证了分离和模态路由的有效性。

## 🎯 结论与影响

FTL作为即插即用模块，无需微调即可有效提升LALMs的噪声鲁棒性，为实际部署提供了低成本解决方案。未来可探索更高效的分离模块和自适应融合策略。

## ⚠️ 局限与未解决问题

依赖预训练分离模型，可能引入额外延迟；模态路由依赖指令质量；未在极低SNR或非平稳噪声下充分测试；未报告计算开销。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-05-26/">← 返回 2026-05-26 速递</a></div>
