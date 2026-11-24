---
title: "SonicRender: Structured and Time-Grounded Rendering of Multi-Event Audio Scene Generation"
date: 2026-11-24T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频生成"]
summary: "提出 SonicRender 统一多事件音频渲染器，用时序音频场景图绑定源身份与时间窗，实现结构化可控的场景混合生成。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多事件音频生成</span> <span class="tag-pill tag-pill-soft">#时序定位</span> <span class="tag-pill tag-pill-soft">#条件流匹配</span> <span class="tag-pill tag-pill-soft">#音频场景图</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.30241</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-23</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://caiyunrui.github.io/SonicRender" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">caiyunrui.github.io/SonicRender</span></span></a><a class="oc-chip oc-chip-demo" href="https://caiyunrui.github.io/SonicRender" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">caiyunrui.github.io/SonicRender</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.30241" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.30241" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://caiyunrui.github.io/SonicRender" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://caiyunrui.github.io/SonicRender" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出 SonicRender 统一多事件音频渲染器，用时序音频场景图绑定源身份与时间窗，实现结构化可控的场景混合生成。
</div>

## 👥 作者与机构

**Yunrui Cai** ¹ · Xu Li · Yan Rong · Dingdong Wang · Yucheng Zhou · Xixin Wu · Chen Zhang · Zhiyong Wu · … 等 1 人

**机构**：香港中文大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做可控音频生成、场景级音频合成与多事件混合的研究者阅读。建议通读，重点看 §3 的 TASG 构建与 AbsTime 绝对帧坐标注入方式，以及 MMAG 时间戳基准与 SceneMix 评估协议；表 2 与主观实验部分值得细看，可复现其时间窗命中率指标。

## 🌍 研究背景

统一音频生成器已能在单模型内合成语音、音乐与音效，但复杂场景请求还要求指定哪些事件发生、由谁产生、何时被听到。现有方法多依赖文本描述或简单条件，难以在单次生成中满足组合性约束，事件身份与时间窗常被混淆或丢失。本文要解决的是如何在统一生成框架内实现结构化、带时间定位的多事件音频场景渲染。

## 💡 核心创新

1. 提出 Temporal Audio Scene Graph（TASG），将持久源身份与带时间戳的语音/音乐/环境/音效事件绑定
2. 引入 AbsTime，为音频隐流提供绝对帧坐标与有效画布时长
3. 结合联合文本-音频注意力与条件流匹配实现结构化定时场景渲染
4. 构建 SceneMix 评估集与多事件负载、时序定位分析协议

## 🏗️ 模型架构

输入为结构化场景描述（TASG 节点：源身份、事件类型、内容、声学角色、关系、时间窗）与文本条件。TASG 经编码后与文本一起通过联合文本-音频注意力注入生成主干；AbsTime 模块将绝对帧坐标与有效画布时长拼接到音频隐流，使模型感知事件在时间轴上的位置。主干采用条件流匹配（conditional flow matching）进行生成，输出为多事件混合音频的隐表示再解码为波形。摘要未给出参数量。

## 📚 数据集

- MMAG timestamp benchmark（评估，时间戳定位）
- SceneMix（评估，多事件场景合成）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Speech F1 | MMAG timestamp benchmark | 对比中最强已报告分数（摘要未给具体值） | **0.79** | 超过对比最强已报告分数 |
| Sound F1 | MMAG timestamp benchmark | 对比中最强已报告分数（摘要未给具体值） | **0.60** | 超过对比最强已报告分数 |
| All-event recall | SceneMix | 五个对比系统（摘要未给具体值） | **85.4%** | 主观研究显著优于全部对比系统 |
| Window-hit rate | SceneMix | 五个对比系统（摘要未给具体值） | **83.9%** | — |
| Speaker accuracy | SceneMix | 五个对比系统（摘要未给具体值） | **95.7%** | — |

在 MMAG 时间戳基准上语音/声音 F1 达 0.79/0.60，超过对比中最强已报告分数；SceneMix 上全事件召回 85.4%、时间窗命中率 83.9%、说话人准确率 95.7%。主观研究在感知音质与场景实现两方面显著优于全部五个对比系统，并给出语音、通用音频、音乐、多事件负载与时序定位的分解分析。摘要未给基线具体数值与效率指标。

## 🎯 结论与影响

最强结论是统一生成器可在单次前向中按结构化场景图精确渲染带时间定位的多事件混合音频。这为可控场景级音频生成提供了图结构条件与绝对时间坐标两条可复用设计，对影视/游戏音效与虚拟场景音频制作有落地潜力。

## ⚠️ 局限与未解决问题

摘要未报告推理延迟、参数量与训练数据规模；对比基线具体数值缺失，难以判断提升幅度；SceneMix 为自建评估集，存在数据偏置风险；缺少对 TASG 与 AbsTime 各模块的消融细节；主观研究样本量与听测协议未说明。

## 🔗 开源资源

- **项目主页**：<https://caiyunrui.github.io/SonicRender>
- **Demo / 试听**：<https://caiyunrui.github.io/SonicRender>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-11-24/">← 返回 2026-11-24 速递</a></div>
