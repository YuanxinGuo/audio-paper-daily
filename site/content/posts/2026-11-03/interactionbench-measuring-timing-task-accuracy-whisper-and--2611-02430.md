---
title: "InteractionBench: Measuring Timing, Task Accuracy, Whisper and Volume, and Grounding in Real-Time Voice Systems"
date: 2026-11-03T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音交互系统评测"]
summary: "提出 InteractionBench，用同一批录音音频在 13 个场景下同时评测实时语音系统的时序、任务准确率、耳语与音量、多轮接地四项能力。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音交互系统评测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#实时语音系统</span> <span class="tag-pill tag-pill-soft">#全双工对话</span> <span class="tag-pill tag-pill-soft">#基准评测</span> <span class="tag-pill tag-pill-soft">#副语言控制</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.02430</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-02</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.02430" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.02430" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出 InteractionBench，用同一批录音音频在 13 个场景下同时评测实时语音系统的时序、任务准确率、耳语与音量、多轮接地四项能力。
</div>

## 👥 作者与机构

**Richard Yucheng He** ¹ · Chen Xu · Yihang Liu · Tairan Chen · Baodong Cao

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做实时语音对话系统（GPT-Realtime / Gemini Live / Moshi 类）评测与产品化的读者。值得通读，重点看 §3 指标定义（尤其 timing 如何计入网络延迟）与 §4 结果表，以及 GPT-Live 去掉 1.5 s 延迟后时序分从 86% 掉到 56% 的分析段。

## 🌍 研究背景

实时语音系统评测目前碎片化：turn-taking、指令跟随、副语言控制、对话记忆各有独立数据集与系统集合，无法横向比较。已有工作多只测单一维度，且时序测量点不统一，导致网络延迟与模型能力混在一起。本文要解决的是：在同一批录制用户音频、同一套系统上，同时测量时序、口述任务准确率、耳语/音量控制与长对话接地四项，并明确协议差异。

## 💡 核心创新

1. 同一录音音频上联合评测时序、任务、副语言、接地四维
2. 口述任务的地板控制动作由规则预先固定，答案取自脚本对话
3. 从音频信号直接判定耳语，而非依赖系统自报
4. 区分客户端听到的时序与服务器时钟，量化网络延迟影响

## 🏗️ 模型架构

评测框架而非模型：输入为 13 个场景下录制的用户音频（每系统 221 条），经各被测系统（GPT-Live、GPT-Realtime、Gemini Live、Moshi、PersonaPlex、Freeze-Omni 及级联基线）实时推理后，采集客户端侧输出音频与文本。评分模块分四路：时序按地板控制动作与响应时刻计算；口述任务按预定义规则比对期望动作与脚本答案；耳语/音量从输出音频信号提取；接地性用多轮（>20 轮）探针问答判定。共 1,519 次评分运行。

## 📚 数据集

- InteractionBench 自建集（13 场景 × 221 条/系统，评测）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 口述任务得分 | InteractionBench | 六个全双工系统（未给单值） | **级联基线 38/50** | 级联最高 |
| 时序与任务准确率秩相关 ρ | InteractionBench | — | **0.83** | 六个全双工系统间 |
| 耳语成功率 | InteractionBench | 其他系统多数不耳语 | **Gemini Live 8/10** | 唯一多数通过 |
| 接地探针通过率 | InteractionBench | 开源全双工模型 14-35% | **托管系统 67-88%** | +30~50% |
| 时序得分（GPT-Live） | InteractionBench | 含约 1.5 s 网络延迟 86% | **去延迟后 56%** | -30% |

1,519 次评分运行显示：六个全双工系统上时序与口述任务准确率秩相关 ρ=0.83；级联基线口述任务最高（38/50）但时序倒数第二；无系统能在要求窗口内纠正用户语法；仅 Gemini Live 多数请求下耳语（8/10）；托管系统接地通过率 67-88%，开源全双工模型仅 14-35%。GPT-Live 去 1.5 s 延迟后时序分从 86% 降至 56%，说明客户端侧时序测量混入网络因素。

## 🎯 结论与影响

最强结论是：现有实时语音系统在副语言控制与长对话接地上的差距远大于口述任务，且时序分数高度依赖测量点。该基准为后续系统提供统一四维评测口径，对工业落地意味着选型不能只看任务准确率，需分别评估延迟与接地能力。

## ⚠️ 局限与未解决问题

每系统仅 221 条、13 场景，统计功效有限；耳语仅 10 次请求即下结论；时序含网络延迟使跨系统比较不完全公平，作者虽做去延迟分析但未统一测量口径；未报推理延迟与算力开销；口述任务期望动作由规则固定，可能偏向特定交互范式。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-11-03/">← 返回 2026-11-03 速递</a></div>
