---
title: "Position-Aware Target Speaker Extraction for Long-Form Multi-Party Conversations: A Diarization-Free Framework for ASR"
date: 2026-06-30T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "提出PATSE，利用DOA作为空间先验，在长对话中直接提取目标说话人语音，无需显式说话人日志，提升ASR性能。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#目标说话人提取</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#语音识别</span> <span class="tag-pill tag-pill-soft">#多通道</span> <span class="tag-pill tag-pill-soft">#说话人日志</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.29497</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-30</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.29497" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.29497" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出PATSE，利用DOA作为空间先验，在长对话中直接提取目标说话人语音，无需显式说话人日志，提升ASR性能。
</div>

## 👥 作者与机构

**Yichi Wang** ¹ · Junzhe Chen · Wangjin Zhou · Tatsuya Kawahara

**机构**：京都大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音分离、目标说话人提取及ASR前端研究者。建议重点阅读§3模型架构和§4实验部分，特别是表1-2的ASR结果。可对比CSS和diarization-based方法。

## 🌍 研究背景

长对话中说话人活动高度不平衡且重叠频繁，滑动窗连续语音分离（CSS）存在跨窗说话人不一致和残留串扰问题，通常需要额外的说话人日志（diarization）来可靠地分配说话人。现有方法依赖复杂流水线，且日志错误会传播到ASR。本文利用会议中说话人到达方向（DOA）的稳定性，提出无需显式日志的端到端目标说话人提取框架。

## 💡 核心创新

1. DOA引导的空间编码器提取方位特征
2. 位置感知条件模块将DOA先验注入提取网络
3. 无需显式说话人日志的说话人活动推断
4. 多通道端到端框架直接生成说话人分离流

## 🏗️ 模型架构

输入多通道混合语音 → DOA估计模块提供目标说话人方位 → DOA引导的空间编码器生成方位相关特征 → 位置感知条件模块将方位特征与主网络（如Conformer）结合 → 输出每个目标说话人的干净语音流。后接简单VAD推断说话人活动，无需diarization。

## 📚 数据集

- LibriCSS（训练/评估，模拟会议）
- 真实会议录音（评估，实际场景）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | LibriCSS | CSS+diarization 18.5% | **PATSE 15.2%** | -3.3% |
| WER | 真实会议 | CSS+diarization 22.1% | **PATSE 19.4%** | -2.7% |

在LibriCSS和真实会议数据集上，PATSE相比CSS+diarization基线分别降低WER 3.3%和2.7%。消融实验验证了DOA引导模块和位置感知条件模块的有效性。无需显式日志即可准确推断说话人活动，且对DOA估计误差具有一定鲁棒性。

## 🎯 结论与影响

PATSE利用DOA空间先验，在长对话中实现无需说话人日志的目标说话人提取，显著提升ASR性能。该方法简化了传统流水线，为会议场景的端到端语音处理提供了新思路，有望推动工业级会议转录系统的落地。

## ⚠️ 局限与未解决问题

依赖DOA估计的准确性，在快速移动或远场场景可能退化；仅在模拟和有限真实数据上验证，泛化性需更多测试；未报告计算开销和推理延迟；未与最新端到端说话人日志方法对比。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-30/">← 返回 2026-06-30 速递</a></div>
