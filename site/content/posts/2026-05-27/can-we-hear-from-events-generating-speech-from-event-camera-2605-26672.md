---
title: "Can We Hear from Events? Generating Speech from Event Camera"
date: 2026-05-27T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音生成"]
summary: "提出EventSpeech框架，首次利用事件相机数据生成富有表现力的语音，解决RGB视频时间粒度不匹配问题。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#事件相机</span> <span class="tag-pill tag-pill-soft">#多模态</span> <span class="tag-pill tag-pill-soft">#语音生成</span> <span class="tag-pill tag-pill-soft">#情感语音</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.26672</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-27</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://xrfang-0102.github.io/EventSpeechWeb/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">xrfang-0102.github.io/EventSpeechWeb/</span></span></a><a class="oc-chip oc-chip-demo" href="https://xrfang-0102.github.io/EventSpeechWeb/" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">xrfang-0102.github.io/EventSpeechWeb/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.26672" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.26672" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://xrfang-0102.github.io/EventSpeechWeb/" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://xrfang-0102.github.io/EventSpeechWeb/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出EventSpeech框架，首次利用事件相机数据生成富有表现力的语音，解决RGB视频时间粒度不匹配问题。
</div>

## 👥 作者与机构

**Jingping Fang** ¹ · Lin Chen · Chenyang Xu · Tong Zhao · Weidong Cai · Xiaoming Chen

**机构**：悉尼大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音生成、多模态学习方向的研究者。建议重点阅读§3模型架构和§4实验部分，特别是Event Encoder和HWC模块的设计。可先看表1和表2了解性能提升。

## 🌍 研究背景

传统RGB视频语音生成受限于固定曝光时间，无法捕捉高频发音瞬态，导致情感表达模糊。现有方法多基于RGB视频或音频特征，缺乏对微秒级运动信息的利用。事件相机以微秒精度记录像素变化，天然匹配声学波形动态，但尚未被用于语音生成。本文旨在利用事件流解决时间粒度不匹配问题，实现高质量情感语音生成。

## 💡 核心创新

1. 首次将事件相机数据用于语音生成
2. 提出Event Encoder建模稀疏事件流
3. 设计Hierarchical Wavelet Contextualizer多尺度音频编码
4. 构建EVT-SPK基准数据集含合成和真实数据

## 🏗️ 模型架构

输入为文本和事件流。事件流经Event Encoder（基于稀疏卷积和Transformer）提取视觉特征；文本经文本编码器；音频分支采用多尺度Audio Encoder，内含Hierarchical Wavelet Contextualizer (HWC)进行小波分解和上下文建模。通过双向对齐机制同步文本、事件与音频特征，最终由声码器生成波形。

## 📚 数据集

- EVT-SPK（训练/评估，含大规模合成数据和真实事件相机录制数据）

## 📊 实验结果

摘要未提供具体数值指标，但声称EventSpeech在情感保留和运动模糊抵抗上显著优于现有RGB基线，并建立了多模态语音生成的新范式。

## 🎯 结论与影响

EventSpeech首次证明事件相机数据可有效用于语音生成，通过微秒级事件流解决RGB视频的时间模糊问题，在情感表达上取得突破。该工作开辟了事件相机与语音生成交叉的新方向，有望推动多模态人机交互和情感计算的发展。

## ⚠️ 局限与未解决问题

摘要未提及推理速度、模型参数量等效率指标；仅与RGB基线对比，缺乏与纯音频方法（如Tacotron、FastSpeech）的比较；EVT-SPK数据集的真实数据规模可能有限，泛化性待验证；未讨论事件相机硬件普及性对实际应用的限制。

## 🔗 开源资源

- **项目主页**：<https://xrfang-0102.github.io/EventSpeechWeb/>
- **Demo / 试听**：<https://xrfang-0102.github.io/EventSpeechWeb/>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-05-27/">← 返回 2026-05-27 速递</a></div>
