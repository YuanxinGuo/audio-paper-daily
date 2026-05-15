---
title: "The Spheres Dataset: Multitrack Orchestral Recordings for Music Source Separation and Information Retrieval"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#乐器分离"]
summary: "发布了一个包含多轨管弦乐录音的数据集，用于音乐源分离和MIR任务，并提供基线评估。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#乐器分离</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音乐信息检索</span> <span class="tag-pill tag-pill-soft">#多轨录音</span> <span class="tag-pill tag-pill-soft">#房间冲激响应</span> <span class="tag-pill tag-pill-soft">#管弦乐</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2511.21247</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2511.21247" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2511.21247" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>发布了一个包含多轨管弦乐录音的数据集，用于音乐源分离和MIR任务，并提供基线评估。
</div>

## 👥 作者与机构

**Jaime Garcia-Martinez** ¹ · David Diaz-Guerra · John Anderson · Ricardo Falcon-Perez · Pablo Caba\~nas-Molero · Tuomas Virtanen · Julio J. Carabias-Orti · Pedro Vera-Candeas

**机构**：不详

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事音乐源分离、MIR的研究者阅读。建议重点看数据集结构（§3）和基线实验（§5），了解数据集的构建细节和挑战。

## 🌍 研究背景

音乐源分离在流行音乐中已有较多研究，但古典管弦乐场景因乐器众多、混响复杂、串音严重而更具挑战。现有数据集如MUSDB18主要针对流行音乐，缺乏高质量的多轨管弦乐录音。本文旨在填补这一空白，提供一个包含真实录音、多麦克风设置、孤立音轨和房间冲激响应的数据集，以推动管弦乐场景下的源分离、定位、去混响等研究。

## 💡 核心创新

1. 发布首个多轨管弦乐录音数据集（1小时以上）
2. 23通道麦克风阵列，包含近场、主麦克风和环境麦克风
3. 提供孤立音轨和可控串音的立体声混音
4. 估计每个乐器位置的房间冲激响应
5. 基于X-UMX的管弦乐家族分离和麦克风去串音基线

## 🏗️ 模型架构

数据集构建：在专业录音棚中由Colibrì Ensemble演奏柴可夫斯基《罗密欧与朱丽叶》和莫扎特《第40交响曲》等作品，使用23个麦克风（包括近场、主麦克风和环境麦克风）录制。提供孤立音轨（每个乐器单独录制）和混合音轨（模拟真实串音）。同时测量每个乐器位置的房间冲激响应。基线模型采用X-UMX架构，输入为立体声混音，输出为乐器家族（弦乐、木管、铜管、打击乐）的分离结果。

## 📚 数据集

- The Spheres dataset（训练/评估，1小时以上多轨管弦乐录音）
- MUSDB18（用于对比，但本文未直接使用）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SDR (dB) | The Spheres (orchestral family separation) | X-UMX (未提供具体值) | **X-UMX (未提供具体值)** | 未提供具体数值 |

摘要中未给出具体数值，仅提及使用X-UMX模型进行基线评估，结果显示管弦乐场景下源分离的潜力和挑战。具体指标如SDR等未报告。

## 🎯 结论与影响

本文发布了一个高质量的多轨管弦乐录音数据集，为古典音乐源分离和MIR研究提供了宝贵资源。基线实验表明，现有模型在复杂管弦乐场景中面临挑战，该数据集有望推动新方法的发展，并促进分离、定位、去混响和沉浸式渲染等方向的研究。

## ⚠️ 局限与未解决问题

数据集规模有限（1小时），且仅包含两个作品，可能不足以覆盖管弦乐的多样性。基线仅使用X-UMX，未与更多先进模型对比。未提供具体分离指标数值，评估不够充分。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
