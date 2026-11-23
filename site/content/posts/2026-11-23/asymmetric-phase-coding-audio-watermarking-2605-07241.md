---
title: "Asymmetric Phase Coding Audio Watermarking"
date: 2026-11-23T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频水印"]
summary: "提出免训练的非对称相位编码音频水印，用Ed25519签名+RS纠错+QIM，盲提取且可离线验证来源。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频水印</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频水印</span> <span class="tag-pill tag-pill-soft">#语音鉴伪</span> <span class="tag-pill tag-pill-soft">#信号处理</span> <span class="tag-pill tag-pill-soft">#语音增强鲁棒性</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.07241</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-23</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.07241" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.07241" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出免训练的非对称相位编码音频水印，用Ed25519签名+RS纠错+QIM，盲提取且可离线验证来源。
</div>

## 👥 作者与机构

**Guang Yang** ¹ · Fengchen Liu · Amir Ghasemian · Zhong Wang · Ninareh Mehrabi · Homa Hosseinmardi

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音频水印、深度伪造检测、语音鉴伪与内容溯源的研究者与工程团队阅读。值得通读，重点看 §3 的相位选点与 QIM 嵌入机制、表 2 的八种攻击配置结果，以及 DNS64/DeepFilterNet3 增强器鲁棒性一节；若关注落地，先看 3.17 ms 单核验证延迟与容量匹配对比。

## 🌍 研究背景

深度伪造语音威胁声纹认证，被动取证检测器对不断演进的生成模型和真实信道失真敏感，泛化差。主动水印（AudioSeal、WavMark、SilentCipher 等神经水印）多依赖学习式编解码，需训练、可解释性弱，且难以提供不可否认的来源证明。本文要解决的是：给出一种免训练、可离线公开验证、能抵抗压缩与重采样等真实信道失真的密码学签名式音频水印原语。

## 💡 核心创新

1. Ed25519 签名 + Reed-Solomon 纠错构成可验证签名层
2. 伪随机 STFT 相位 bin 选择承载冗余 QIM 码
3. 在相邻 bin 对数幅度差上做冗余 QIM 量化
4. 可选解码端搜索抵抗整数时间平移
5. 可与 AudioSeal 等学习式水印叠加使用

## 🏗️ 模型架构

输入为 44.1 kHz 波形，先做 STFT；用伪随机种子在相位 bin 中选点，在相邻 bin 对的对数幅度差上嵌入冗余 QIM 码，码字由 Ed25519 对消息签名后经 Reed-Solomon 纠错编码得到。提取端盲提取码字，校验签名以确认签名者身份与消息完整性；可选解码端搜索处理整数时间平移。全程免训练，签名 64 字节，单核验证 10 s 片段 3.17 ms。

## 📚 数据集

- LibriSpeech test-clean（评估，1905 条 10 s 片段）
- 15 个公开语料共 18 组（评估，2048 条，含音乐、会议、电话、多语种与声码化语音）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 验证通过率 | LibriSpeech test-clean（八种攻击配置） | 神经基线 AudioSeal / WavMark / SilentCipher（复现/已发表） | **98.3%~99.8%** | 各条件下均高通过率 |
| PESQ（identity） | LibriSpeech test-clean | — | **3.82** | — |
| 验证通过率 | 18 组公开语料（2048 条） | — | **97.1%~99.4%** | — |
| 单核验证延迟 | 10 s 签名片段 | — | **3.17 ms** | — |

在 LibriSpeech 八种攻击（裁剪、低通、重采样、FLAC/MP3/OGG 128 kbps）下验证率 98.3%~99.8%，错误密钥与未签名片段零接受；跨 18 组语料 97.1%~99.4%。可抵抗平台处理链、重复 MP3/OGG 编码、有界裁剪与整数时移，并在 DNS64、DeepFilterNet3 增强器下多数片段仍可验证。与 AudioSeal、WavMark、SilentCipher 对比含容量匹配工作点，且可与 AudioSeal 叠加。

## 🎯 结论与影响

最强结论是免训练密码学签名水印在真实信道失真下仍保持近 99% 验证率且零误接受，并提供不可否认来源证明。这为音频溯源提供了可审计、低延迟的原语，可与学习式水印互补；工业上适合内容凭证与鉴伪流水线的轻量前置层。

## ⚠️ 局限与未解决问题

摘要未给出容量（bit/s）与感知质量的完整权衡曲线，PESQ 3.82 相对干净语音仍有下降；对强去同步攻击（大幅裁剪、变速、音高变换）与生成式再合成攻击的鲁棒性未充分覆盖；与神经基线的对比多为复现值，缺少统一攻击集下的公平消融。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-11-23/">← 返回 2026-11-23 速递</a></div>
