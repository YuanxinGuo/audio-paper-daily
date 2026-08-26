---
title: "AT-ADD: A Benchmark and Challenge for Robust and All-Type Audio Deepfake Detection"
date: 2026-08-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频伪造检测"]
summary: "提出AT-ADD基准与挑战赛，评估鲁棒语音和全类型音频深度伪造检测，涵盖语音、环境声、歌声和音乐。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.2</div>
<div class="score-stars">★★★★★</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频伪造检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频伪造检测</span> <span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#鲁棒性</span> <span class="tag-pill tag-pill-soft">#基准测试</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.23437</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.23437" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.23437" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出AT-ADD基准与挑战赛，评估鲁棒语音和全类型音频深度伪造检测，涵盖语音、环境声、歌声和音乐。
</div>

## 👥 作者与机构

**Yuankun Xie** ¹ · Haonan Cheng · Jiayi Zhou · Xiaoxuan Guo · Tao Wang · Changhao Zhang · Jian Liu · Weiqiang Wang · … 等 6 人

**机构**：中国科学院 · 中国传媒大学 · 上海交通大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频伪造检测、语音增强和鲁棒性研究者阅读。值得通读，重点看第3节数据集构建和第4节评估协议，以及第5节基线结果和第6节挑战赛系统分析。可先看摘要和结论，再深入方法部分。

## 🌍 研究背景

音频生成模型可合成高保真语音、环境声、歌声和音乐，对多媒体信任构成威胁。现有音频深度伪造检测基准主要聚焦语音，且未充分覆盖真实信道变化和多种音频类型。本文提出AT-ADD基准，包含两个赛道：赛道1评估未知生成器、多样录音条件、信号扰动和重放效应下的二分类语音检测；赛道2评估音频类型未知时的跨类型真实/伪造检测。旨在推动鲁棒和全类型音频伪造检测研究。

## 💡 核心创新

1. 构建大规模多类型音频伪造检测基准AT-ADD
2. 双赛道评估协议：鲁棒语音检测与全类型检测
3. 提供可复现基线和挑战赛系统分析
4. 揭示自监督表征、条件增强、多crop推理和结构化融合的重要性

## 🏗️ 模型架构

AT-ADD基准包含数据集构建、评估协议和基线系统。数据集涵盖语音、环境声、歌声和音乐，包含多种生成器和信道变化。基线系统采用自监督预训练模型（如Wav2Vec2）提取特征，结合分类头进行二分类。挑战赛系统采用多crop推理、条件增强、结构化融合或路由等策略。具体架构细节未在摘要中详述。

## 📚 数据集

- AT-ADD（训练/评估，大规模，包含语音、环境声、歌声和音乐）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Macro-F1 | Track 1 evaluation set | 官方基线 76.73% | **挑战赛冠军 90.71%** | +13.98% |
| Macro-F1 | Track 2 evaluation set | 官方基线 79.47% | **挑战赛冠军 96.10%** | +16.63% |

官方基线在赛道1和赛道2上分别获得76.73%和79.47%的Macro-F1，而挑战赛获胜系统分别达到90.71%和96.10%。对前五名系统的样本级分析考察了生成器和类型级别的难度、跨系统错误互补性和排名稳定性。结果表明，大规模自监督表征、条件感知增强、多crop推理和结构化融合或路由对泛化至关重要，但生成器特定鲁棒性和跨音频类型的一致性能仍未解决。

## 🎯 结论与影响

AT-ADD基准和挑战赛为鲁棒和全类型音频伪造检测提供了全面评估平台。获胜系统显著优于基线，表明自监督学习和增强策略的有效性。该基准将推动音频伪造检测研究向更真实和多样化的场景发展，对多媒体取证和内容审核有重要应用价值。

## ⚠️ 局限与未解决问题

摘要未提及作者承认的局限。作为审稿人，可能存在的问题包括：基准可能未覆盖所有真实场景，如不同语言、低资源环境；未报告推理延迟和计算成本；挑战赛系统可能过拟合评估集；跨类型检测的泛化能力仍需进一步验证。

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-08-26/">← 返回 2026-08-26 速递</a></div>
