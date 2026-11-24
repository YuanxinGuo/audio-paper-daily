---
title: "Ultrasound Watermark: Real-time Acoustic Watermarking against Voice Scams on Smartphones"
date: 2026-11-24T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频水印"]
summary: "用手机扬声器发超声、麦克风收面部发音运动反射，生成与语音同步的动态声学水印，实时检测电话诈骗中的合成/重放语音。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频水印</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#声学水印</span> <span class="tag-pill tag-pill-soft">#深度伪造检测</span> <span class="tag-pill tag-pill-soft">#超声感知</span> <span class="tag-pill tag-pill-soft">#移动端实时系统</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.30106</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-23</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.30106" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.30106" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用手机扬声器发超声、麦克风收面部发音运动反射，生成与语音同步的动态声学水印，实时检测电话诈骗中的合成/重放语音。
</div>

## 👥 作者与机构

**Renzhi Hao** ¹ · Shirui Cao · Yizhu Wen · Rishav Gupta · Dharani Nadendla · Mehran Kafai · Hanqing Guo · Dong Li

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做语音深伪检测、声学感知、移动端音频系统的研究者与安全工程师阅读。值得通读系统设计与威胁模型部分，重点看 §3 的超声-语音跨模态融合机制与 §5 的对抗攻击评测表；若只关心检测指标，可先看攻击鲁棒性结果表与延迟测量。

## 🌍 研究背景

TTS 与 VC 使电话语音冒充成本极低，现有防御多为离线分析、依赖云端或外部硬件，且在电话信道失真下性能下降，对自适应攻击（重放、合成、模仿发音）鲁棒性不足。已有声学水印方案多绑定于内容或信道特征，缺乏与说话人物理发音过程的耦合，因而难以抵御不依赖真实发音运动的伪造。本文试图用手机自带器件实现实时、免额外硬件的主动防御。

## 💡 核心创新

1. 用手机扬声器发超声、麦克风收面部发音运动反射，提取运动特征
2. 将超声运动特征与出话语音融合生成动态声学水印
3. 同步的生成器-检测器架构强制跨模态语音-运动一致性
4. 纯手机端实时运行，延迟开销低于 200 ms，无需额外硬件

## 🏗️ 模型架构

系统在通话中由手机扬声器持续发射超声信号，内置麦克风采集经面部发音器官运动调制的反射回波；从回波中提取与发音动作相关的运动特征，与出话语音流在特征层融合，经生成器产生动态水印嵌入语音。接收端检测器同步提取水印并与超声运动特征做跨模态一致性校验，判定语音是否由真实发音运动产生。生成器与检测器同步训练，形成对重放、合成与模仿发音攻击的判别。摘要未给出具体网络名与参数量。

## 📚 数据集

- 自采集同步语音-超声数据集（22 名说话人、8 款手机、4 种真实环境，共 2.5 小时以上，用于训练与评估）

## 📊 实验结果

摘要仅定性说明对重放、合成语音、模仿发音及电话信道失真具有鲁棒性，并保持感知音质，未给出 SI-SDR、PESQ、EER 或检测准确率等具体数值，也未报告与基线防御方法的定量对比，因此无法列表比较。

## 🎯 结论与影响

最强结论是：将声学水印与说话人真实发音运动物理耦合，可在纯手机端实时实现难以伪造的语音来源认证。这为语音深伪防御提供了主动式、跨模态的新思路，对通话安全与身份认证类产品有直接落地潜力。

## ⚠️ 局限与未解决问题

摘要未给出检测准确率、EER、误报率等核心安全指标，也缺少与现有水印/深伪检测基线的定量对比；22 人、8 款手机、4 环境的规模对泛化性验证偏小；未讨论强自适应攻击者已知水印机制时的对抗风险，以及超声发射的功耗与隐私影响。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-11-24/">← 返回 2026-11-24 速递</a></div>
