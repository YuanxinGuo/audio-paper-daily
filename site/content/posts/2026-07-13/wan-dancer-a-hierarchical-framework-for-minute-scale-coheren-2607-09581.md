---
title: "Wan-Dancer: A Hierarchical Framework for Minute-scale Coherent Music-to-Dance Generation"
date: 2026-07-13T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#舞蹈视频生成"]
summary: "提出层级框架Wan-Dancer，通过全局关键帧规划与局部时间细化，实现分钟级连贯音乐到舞蹈视频生成。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#舞蹈视频生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音乐到舞蹈生成</span> <span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#长视频生成</span> <span class="tag-pill tag-pill-soft">#层级框架</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.09581</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-13</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.09581" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.09581" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出层级框架Wan-Dancer，通过全局关键帧规划与局部时间细化，实现分钟级连贯音乐到舞蹈视频生成。
</div>

## 👥 作者与机构

**Mingyang Huang** ¹ · Peng Zhang · Li Hu · Guangyuan Wang · Bang Zhang

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合舞蹈生成、视频生成、扩散模型研究者。建议通读，重点看§3.2动态帧率适应与§3.3光流损失函数。可复现实验部分。

## 🌍 研究背景

音乐到舞蹈生成旨在从音乐生成同步舞蹈视频，但现有扩散模型受限于20秒内，长视频存在时间漂移、身份不一致和动作重复。先前方法依赖3D骨架或端到端合成，均无法解决长程连贯性。本文提出层级框架，利用全曲音乐上下文规划关键帧，再局部细化，突破时长限制。

## 💡 核心创新

1. 动态帧率适应：时间映射RoPE嵌入实现精确对齐
2. 光流损失函数增强运动连续性
3. 运动速度控制保留快速运动细节
4. 全局关键帧规划与局部时间细化解耦
5. 支持音频与文本双条件控制

## 🏗️ 模型架构

输入音乐音频和文本提示，经编码器提取特征。全局规划模块利用全曲上下文生成稀疏关键帧姿态序列；局部细化模块以关键帧为条件，通过扩散模型逐段生成高帧率舞蹈视频。关键模块包括：时间映射RoPE嵌入用于动态帧率适应，光流损失函数监督运动连续性，运动速度控制模块调整生成速度。输出720p/30fps视频，时长超一分钟。

## 📚 数据集

- AIST++（训练与评估，含多种舞蹈风格）
- 自定义数据集（评估，五种舞蹈风格）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| FID | AIST++ | Bailando 15.2 | **12.8** | -2.4 |
| Diversity | AIST++ | Bailando 9.1 | **10.3** | +1.2 |
| Beat Alignment Score | AIST++ | Bailando 0.82 | **0.89** | +0.07 |

在AIST++上，Wan-Dancer在FID、多样性和节拍对齐上均优于Bailando等基线。生成视频时长超1分钟，720p/30fps，且跨五种舞蹈风格表现稳定。消融实验验证了动态帧率适应和光流损失的有效性。

## 🎯 结论与影响

Wan-Dancer首次实现分钟级连贯舞蹈视频生成，突破扩散模型时长限制。层级框架为长视频生成提供新范式，有望推动舞蹈创作、虚拟人等领域应用。

## ⚠️ 局限与未解决问题

未报告推理速度与计算成本；仅评估AIST++数据集，泛化性待验证；未与最新端到端方法（如MDM）对比；身份一致性仅定性说明，缺乏定量指标。

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-07-13/">← 返回 2026-07-13 速递</a></div>
