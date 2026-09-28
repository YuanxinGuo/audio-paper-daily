---
title: "Dialogue-Based Streaming Audio-Visual Target Speaker Extraction with Predictive Dialogue Information"
date: 2026-09-28T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "提出首个基于真实双人对话的在线音视频目标说话人提取基准，并用语音LLM预测目标未来语音活动来引导低延迟分离器。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#目标说话人提取</span> <span class="tag-pill tag-pill-soft">#音视频语音处理</span> <span class="tag-pill tag-pill-soft">#流式处理</span> <span class="tag-pill tag-pill-soft">#语音活动预测</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.30774</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://jjjjiaozi.github.io/TS-VAP/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">jjjjiaozi.github.io/TS-VAP/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.30774" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.30774" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://jjjjiaozi.github.io/TS-VAP/" target="_blank" rel="noopener">🌐 项目主页</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出首个基于真实双人对话的在线音视频目标说话人提取基准，并用语音LLM预测目标未来语音活动来引导低延迟分离器。
</div>

## 👥 作者与机构

**Shuhan Zhang** ¹ · Wenxuan Wu · Haizhou Li ✉

**机构**：香港中文大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做 AV-TSE、流式分离与对话场景语音处理的读者。建议通读：先看 §3 的 TS-VAP 模块设计与 LLM 输入构造，再看表 2 的多骨干对比与预测/历史/同步上下文的消融，最后看基准构建与干扰源设置。

## 🌍 研究背景

现有 TSE 研究多在模拟混合（WSJ0-2mix、LibriMix 式全重叠或稀疏重叠）上评测，忽略了真实对话中的停顿、轮替与反馈音，导致模型在在线场景下难以跟踪目标。此前 AV-TSE 的 SOTA 多为离线或固定重叠假设下的 Conformer/DPRNN 类分离器，缺乏对说话人未来活动的前瞻建模。本文要解决的是：在真实双人交互、含第三方干扰的流式条件下，如何利用语义、声学与面部线索预测目标未来活动并指导低延迟提取。

## 💡 核心创新

1. 首个基于真实双人对话、含独立第三方干扰的在线 AV-TSE 基准
2. LLM 驱动的目标说话人语音活动投影 TS-VAP，直接从重叠混合预测未来活动
3. 将预测上下文与历史、同步说话人上下文融合以引导低延迟分离器

## 🏗️ 模型架构

输入为流式音视频帧：音频经编码后送入 speech-LLM 主干，视频侧提取面部/唇动特征。核心 TS-VAP 模块不依赖分离的说话人通道，而是直接在重叠混合上预测目标与对话伙伴的未来语音活动，借助 speech-LLM 的语言与对话知识输出活动投影。该预测与历史说话人上下文、同步说话人上下文拼接，作为条件送入低延迟分离器（在多种 AV-TSE 骨干上验证，如 Conformer/DPRNN 类）。输出为目标说话人的流式增强语音。摘要未给出参数量。

## 📚 数据集

- 真实双人对话数据集（构建在线 AV-TSE 基准，含第三方干扰，训练/评估）
- 模拟混合数据集（用于对比与骨干验证，评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 提取性能增益 | 真实 AV 对话 | 仅历史+同步上下文 | **历史+同步+预测上下文** | 约 +1 dB |

摘要报告 TS-VAP 在多种 AV-TSE 骨干上一致提升流式提取性能，且历史、同步与预测三类上下文结合后在真实 AV 对话上取得近 1 dB 增益。摘要未给出 SI-SDR、PESQ、WER 等具体数值，也未提供推理延迟与参数量，消融细节需查阅正文。

## 🎯 结论与影响

最强结论是：用 speech-LLM 预测目标未来语音活动可为在线 AV-TSE 提供有效前瞻线索，并在真实对话上带来近 1 dB 提升。该工作把评测从模拟混合推向真实轮替对话，可能推动后续研究关注流式、低延迟与对话动态建模。工业上对视频会议、助听器与实时字幕的目标语音跟踪有直接参考价值。

## ⚠️ 局限与未解决问题

摘要未给出具体指标数值、推理延迟与模型规模，难以判断低延迟是否达标；基准仅覆盖双人对话，多人场景与跨语言泛化未知；第三方干扰的统计特性与数据集偏差未说明；缺少与最新离线 AV-TSE 的公平对比。

## 🔗 开源资源

- **项目主页**：<https://jjjjiaozi.github.io/TS-VAP/>

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-28/">← 返回 2026-09-28 速递</a></div>
