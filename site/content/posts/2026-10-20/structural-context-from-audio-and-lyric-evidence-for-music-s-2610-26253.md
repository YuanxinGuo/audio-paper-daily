---
title: "Structural Context from Audio and Lyric Evidence for Music Structure Analysis Using the New SheetSage-MSA Dataset"
date: 2026-10-20T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐结构分析"]
summary: "构建 SheetSage-MSA 数据集并提出 SCALE，用分离的音频通路建模局部与长程结构，融合带时间戳歌词提升副歌识别。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐结构分析</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音乐结构分析</span> <span class="tag-pill tag-pill-soft">#多模态</span> <span class="tag-pill tag-pill-soft">#歌词建模</span> <span class="tag-pill tag-pill-soft">#数据集构建</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.26253</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://multimodal-music-research-lab.github.io/SCALE/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">multimodal-music-research-lab.github.io/SCALE/</span></span></a><a class="oc-chip oc-chip-demo" href="https://multimodal-music-research-lab.github.io/SCALE/" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">multimodal-music-research-lab.github.io/SCALE/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.26253" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.26253" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://multimodal-music-research-lab.github.io/SCALE/" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://multimodal-music-research-lab.github.io/SCALE/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>构建 SheetSage-MSA 数据集并提出 SCALE，用分离的音频通路建模局部与长程结构，融合带时间戳歌词提升副歌识别。
</div>

## 👥 作者与机构

**Hongbing Li** ¹ · Yaolong Ju

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐信息检索（MIR）与多模态音乐分析方向的研究者阅读。值得通读，重点看 §3 数据集构建流程与 §4 SCALE 的双通路设计，以及表 2 在 HarmonixSet 上的 HR.5F/HR3F 对比；若关注歌词-音频对齐，可细看歌词复发模块。

## 🌍 研究背景

音乐结构分析（MSA）需同时定位边界并赋予功能标签（如 chorus/verse）。此前 SOTA 如 SongFormer 采用单一共享编码器同时处理边界检测与功能标注，但两类任务对局部瞬态与长程上下文的信息需求不同；且多数端到端系统仅用音频，忽略歌词中的结构线索。此外细粒度 MSA 标注稀缺，制约监督训练。本文针对标注稀缺、编码器共享不当、歌词信息缺失三个痛点。

## 💡 核心创新

1. 构建 SheetSage-MSA：9,010 首歌、13,880 段标注、约 82.5 小时音频
2. SCALE 采用任务专用双音频通路，分别建模局部过渡与长程结构上下文
3. 引入带时间戳歌词与歌词复发特征精修副歌预测

## 🏗️ 模型架构

输入为音频与带时间戳歌词。音频侧经两个任务专用通路：局部通路建模帧级边界过渡，长程通路捕获段落级结构上下文，主干为音频编码器（摘要未指明具体网络名）。歌词侧提取时间戳与歌词复发（lyrical recurrence）特征，与音频结构表征融合后精修 chorus 预测。输出为功能标签序列及其边界。摘要未给出参数量。

## 📚 数据集

- SheetSage-MSA（训练/评估，9,010 首歌、13,880 段标注、约 82.5 小时）
- HarmonixSet（评估基准）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| HR.5F | HarmonixSet | SongFormer | **SCALE** | +3.5 个百分点 |
| HR3F | HarmonixSet | SongFormer | **SCALE** | +4.2 个百分点 |
| ACC | HarmonixSet | SongFormer | **SCALE** | +0.9 个百分点 |

在 HarmonixSet 基准上，SCALE 相对 SongFormer 在 HR.5F 与 HR3F 上分别提升 3.5 与 4.2 个百分点，ACC 提升 0.9 点，说明双通路与歌词证据对边界与功能标注均有增益。摘要未报告消融实验细节、推理效率及跨数据集泛化结果。

## 🎯 结论与影响

最强结论是分离任务专用音频通路并融合歌词复发可稳定超越 SongFormer。该工作为 MSA 提供了较大规模细粒度数据集与多模态融合范式，可能推动后续歌词-音频联合结构建模；工业上可用于音乐播放器的自动章节切分与副歌定位。

## ⚠️ 局限与未解决问题

摘要未给出消融实验验证双通路与歌词模块各自贡献，也未报告推理延迟与模型规模；数据集源自 SheetSage 自动流程，标注噪声与版权分布偏差未知；仅在 HarmonixSet 单一基准评估，跨风格泛化待验证。

## 🔗 开源资源

- **项目主页**：<https://multimodal-music-research-lab.github.io/SCALE/>
- **Demo / 试听**：<https://multimodal-music-research-lab.github.io/SCALE/>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-10-20/">← 返回 2026-10-20 速递</a></div>
