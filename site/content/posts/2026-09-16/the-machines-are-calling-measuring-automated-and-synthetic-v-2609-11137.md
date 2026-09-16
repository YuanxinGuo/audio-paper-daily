---
title: "The Machines Are Calling: Measuring Automated and Synthetic Voices in Unwanted Inbound Calls"
date: 2026-09-16T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成检测"]
summary: "用语音蜜罐在66天内接听10987通来电，结合音频指纹、商用合成语音检测器与盲听标注，量化机器与合成语音在骚扰电话中的占比。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.0</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音合成检测</span> <span class="tag-pill tag-pill-soft">#反欺诈</span> <span class="tag-pill tag-pill-soft">#语音取证</span> <span class="tag-pill tag-pill-soft">#数据采集</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.11137</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-16</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.11137" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.11137" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用语音蜜罐在66天内接听10987通来电，结合音频指纹、商用合成语音检测器与盲听标注，量化机器与合成语音在骚扰电话中的占比。
</div>

## 👥 作者与机构

**Xingyu Shen** ¹ · Tommy Duong · Muduo Xu · Xiaodong An · Jiaqi Gan · Haoyuan Tang · Jamey Z. Liang · Siyu Zhang · … 等 3 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做语音取证、合成语音检测落地、反骚扰电话测量的研究者与工业风控团队阅读。建议重点看 §3 的三件测量工具（指纹/检测器/盲听）与 §4 的占比分解表，以及检测器阈值翻转 13.6% 与盲听确认率 54.4% 这两处可靠性分析；方法学部分可略读。

## 🌍 研究背景

2024 年 2 月 FCC 将 AI 生成语音纳入 TCPA 监管，但此前没有同行评议的测量说明骚扰电话中机器拨打与合成语音各占多少。已有工作多依赖运营商侧信令或小规模人工举报，缺乏对通话音频本身的细粒度标注，也无法区分「播放录音」与「实时合成」。本文要给出一个可披露的测量流程，同时量化机器拨打率、合成语音率及其在诈骗与营销两类来电中的分布。

## 💡 核心创新

1. 交互式语音蜜罐：LLM 人设 + 真实美国号码，主叫单独音轨录制
2. 音频指纹跨通话匹配同一段录音，区分重放与新鲜音频
3. 商用合成检测器 + 盲听复核的双重标注，并报告阈值翻转率

## 🏗️ 模型架构

系统分三层：采集层为交互式语音蜜罐，用语言模型人设接听真实美国号码来电，主叫语音单独成轨；分析层对每通电话的开场做三路并行处理——音频指纹在通话库内检索同一录音的重放，商用合成语音检测器只看主叫前 10 秒输出合成/人类标签，盲听员对检测器命中样本做人工复核；统计层按营销/诈骗、号码投放时长等维度聚合占比。摘要未给模型参数量或具体网络结构。

## 📚 数据集

- 自建语音蜜罐通话集（10987 通、66 天，其中 7233 通被问候、6192 通可评分，用于分析）
- 盲听标注子集（11 名听者对检测器命中样本复核，用于评估检测器精度）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 机器语音开场占比（下限） | 自建蜜罐 7233 通被问候来电 | 无公开基线 | **26.9%** | — |
| 录音重放开场占比 | 自建蜜罐 7233 通 | 无公开基线 | **13.8%** | — |
| 新鲜合成语音开场占比 | 自建蜜罐 7233 通 | 无公开基线 | **13.1%** | — |
| 检测器阈值翻转率 | 同一波形跨两通电话 | 无公开基线 | **13.6%** | — |
| 检测器命中被盲听确认率 | 11 名听者复核 | 无公开基线 | **54.4%** | — |

摘要给出完整占比分解：13.8% 为重放录音、13.1% 为检测器判为合成的新鲜音频、9.9% 为问候后无人说话、54.2% 为检测器判为人类的新鲜音频、9.0% 无法评分。合成开场在 lead-generation 垃圾营销中占 33.8%，高于诈骗的 21.1%；仅 0.44% 主动披露自动化。号码投放时长与机器占比强相关（59% vs 19%），说明是投放历史而非日历时间驱动。未报告推理延迟或检测器具体型号。

## 🎯 结论与影响

最强结论是骚扰电话中机器语音开场至少占 26.9%，且合成语音集中在营销而非诈骗，监管口径与真实分布存在错位。该测量流程为后续语音取证与反骚扰研究提供了可复现的采集—标注范式，也提示商用合成检测器在真实电话信道下可靠性有限。工业上可用于风控策略按号码投放历史而非时间做动态阈值。

## ⚠️ 局限与未解决问题

仅覆盖美国号码与 66 天窗口，样本偏置明显；商用检测器未披露型号与阈值，盲听确认率仅 54.4% 说明标签噪声大；9.0% 无法评分样本被排除可能低估机器占比；未报告检测器在电话窄带信道下的 EER 或推理成本，也无与开源合成检测基线的对比。

---

<div class="paper-footer"><span>评分：6.0</span><span>原始：6.0</span><a href="/audio-paper-daily/posts/2026-09-16/">← 返回 2026-09-16 速递</a></div>
