---
title: "Structured Speaker Conditioning for Diarization-Guided Target-Speaker ASR"
date: 2026-11-13T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "提出结构化说话人条件化SSC，用日志活动结构与会话级声纹身份构造目标条件，调制ASR编码器，实现日志引导的目标说话人识别。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#说话人日志</span> <span class="tag-pill tag-pill-soft">#目标说话人ASR</span> <span class="tag-pill tag-pill-soft">#说话人条件化</span> <span class="tag-pill tag-pill-soft">#会议转录</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.16371</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-12</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.16371" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.16371" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出结构化说话人条件化SSC，用日志活动结构与会话级声纹身份构造目标条件，调制ASR编码器，实现日志引导的目标说话人识别。
</div>

## 👥 作者与机构

**Ruoyu Wang** ¹ · Shutong Niu · Jun Du · Weixin Zhu · Yannan Wang

**机构**：中国科学技术大学 · 科大讯飞

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做说话人日志引导ASR、目标说话人提取与会议转录的研究者阅读。建议通读，重点看§3的TCRE关系编码与CLRM低秩调制设计，以及表2中四会议测试集cpER对比和跨模型迁移实验；若只关心落地，可先看预测日志+GRPO策略优化那组结果。

## 🌍 研究背景

日志引导的目标说话人ASR需要在多人会议中依据说话人日志只转写目标说话人，现有做法多用四状态对角条件化（DiCoW等）把每帧活动状态送入编码器，但这类条件只刻画局部活动、缺乏会话级声纹一致性，在重叠语音与说话人切换处易混淆；同时条件注入方式多为简单拼接或加性偏置，表达能力有限。本文要解决的是如何构造身份一致、能刻画重叠与切换的目标条件，并以低参数量高效调制声学编码器。

## 💡 核心创新

1. TCRE保留每说话人活动历史并分解二阶/三阶关系，聚合代价随轨数线性
2. RSC用会话级参考声纹消解TCRE局部活动模式的歧义
3. CLRM将联合条件转为通道仿射调制与条件相关核的低秩跨通道残差
4. 仅1.46M条件参数即可跨音频基座模型迁移

## 🏗️ 模型架构

输入为日志给出的每说话人活动轨迹与会话音频；TCRE对每条轨维护活动历史，并构造分解的二阶、三阶关系张量，以线性于轨数的代价聚合出目标中心表示；RSC从会话音频提取参考声纹，提供会话级身份嵌入以消歧局部活动模式；二者拼接成联合条件后送入CLRM，CLRM输出通道级仿射参数（scale/shift）与一个条件相关核的低秩跨通道残差，调制Qwen3-ASR-0.6B声学编码器的中间特征，解码端输出目标说话人文本（时间戳变体额外输出句边界）。条件模块仅1.46M参数。

## 📚 数据集

- 四个会议测试集（评估，具体名称摘要未给出）
- 三个未见域（评估，跨域泛化）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| cpER 平均相对下降 | 四个会议测试集 | 四状态对角条件化 | **SSC（oracle 日志）** | -6.23% |
| cpER 平均相对下降 | 四个会议测试集 | DiCoW | **FireRedAudio 文本系统 + 预测日志 + GRPO** | -17.9% |
| cpER 平均相对下降 | 四个会议测试集 | MOSS-TD | **FireRedAudio 文本系统 + 预测日志 + GRPO** | -17.3% |
| macro-average cpER | 四个会议测试集（预测日志） | — | **15.60%（纯文本）/ 15.96%（带时间戳）** | — |

在Qwen3-ASR-0.6B+oracle日志下，SSC相对四状态对角条件化在四个会议测试集上cpER平均相对降6.23%，且可迁移到其他音频基座模型。换成预测日志并加目标错误组序列策略优化后，FireRedAudio文本系统相对DiCoW与MOSS-TD分别降17.9%与17.3%，并在三个未见域同样领先。场景分析显示重叠条件下的增益更明显，固定检查点干预实验支持会话身份与条件相关核的贡献；时间戳变体可联合输出句边界与文本。

## 🎯 结论与影响

最强结论是结构化、身份一致的条件化能在极小参数量下稳定降低日志引导目标说话人ASR的cpER，并跨基座模型与未见域迁移。这为条件注入设计提供了可复用范式，对会议转录产品意味着更低的适配成本与更好的重叠场景鲁棒性。

## ⚠️ 局限与未解决问题

摘要未给出各测试集名称与绝对cpER基线值，对比仅限少数条件化方案，缺少与端到端TSE-ASR系统的比较；条件模块的推理延迟与显存开销未报告；GRPO策略优化的贡献与SSC本身的贡献在预测日志实验中耦合，消融不够彻底。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-11-13/">← 返回 2026-11-13 速递</a></div>
