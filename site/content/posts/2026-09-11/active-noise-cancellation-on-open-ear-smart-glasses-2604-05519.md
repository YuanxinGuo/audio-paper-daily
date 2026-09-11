---
title: "Active noise cancellation on open-ear smart glasses"
date: 2026-09-11T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "用眼镜框上8麦克风阵列与开放式扬声器，神经网络估计耳旁噪声并实时生成反噪声，实现无入耳误差麦克风的开放式主动降噪。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#主动降噪</span> <span class="tag-pill tag-pill-soft">#麦克风阵列</span> <span class="tag-pill tag-pill-soft">#可穿戴音频</span> <span class="tag-pill tag-pill-soft">#低延迟系统</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2604.05519</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-11</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2604.05519" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2604.05519" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用眼镜框上8麦克风阵列与开放式扬声器，神经网络估计耳旁噪声并实时生成反噪声，实现无入耳误差麦克风的开放式主动降噪。
</div>

## 👥 作者与机构

**Kuang Yuan** ¹ · Freddy Yifei Liu · Tong Xiao · Yiwen Song · Chengyi Shen · Saksham Bhutani · Justin Chan · Swarun Kumar

**机构**：卡内基梅隆大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做可穿戴音频、麦克风阵列、低延迟 DSP 与神经声学的读者。建议通读，重点看 §3 的麦克风阵列到耳旁噪声映射网络设计与 §4 的 11 用户/8 环境评测协议；表 2 的消融与校准对比值得细看。若只关心算法，可先看网络结构与延迟预算部分。

## 🌍 研究背景

传统 ANC 依赖耳道内误差麦克风测量残余噪声，形成闭环反馈，已在头戴与入耳设备成熟。但开放式眼镜、VR 头显不封闭耳道，无法放置误差麦克风，闭环失效，环境噪声直接进入耳道。已有开放式 ANC 多依赖固定滤波器或需先验声学测量，难以泛化到新用户与新环境。本文要解决的是：仅凭框上麦克风与开放式扬声器，在无先验测量条件下估计耳旁噪声并实时生成反噪声。

## 💡 核心创新

1. 用框上8麦克风阵列神经估计耳旁噪声，替代入耳误差麦克风
2. 低延迟实时反噪声生成管线，适配开放式扬声器
3. 无需先验声学测量即可泛化到未见用户与环境
4. 支持眼镜、VR头显、头带等多形态开放式可穿戴

## 🏗️ 模型架构

输入为分布在眼镜框上的8路麦克风信号，经低延迟特征提取后送入神经网络，估计用户耳道处的环境噪声；网络输出驱动框内小型开放式扬声器生成反噪声信号，与直达噪声在耳旁相消。管线强调低延迟以满足 100–1000 Hz 频段实时相消的相位对齐要求。摘要未给出具体主干网络名与参数量，仅说明为神经网络映射且可跨用户、跨环境泛化，无需先验声学测量。

## 📚 数据集

- 自建眼镜原型采集数据（训练/评估，11名未见用户、8个未见环境，100–1000 Hz）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 平均降噪量 | 11用户/8环境移动场景 | 无校准开放式ANC（未给具体基线值） | **9.6 dB** | — |
| 平均降噪量（用户校准后） | 11用户/8环境移动场景 | 无校准 9.6 dB | **11.2 dB** | +1.6 dB |

在 100–1000 Hz 环境噪声集中频段，对 11 名未见用户与 8 个未见环境、含移动条件下评测：无任何校准平均降噪 9.6 dB，经简短用户特定校准后达 11.2 dB。摘要未报告 SI-SDR、PESQ、MOS 等语音质量指标，也未给出推理延迟、功耗与对比基线数值，消融与跨设备泛化细节需看正文。

## 🎯 结论与影响

最强结论是：无需入耳误差麦克风，仅靠框上麦克风阵列与开放式扬声器即可在开放式可穿戴实现约 10 dB 量级降噪，并泛化到未见用户与环境。这为开放式 ANC 提供了新范式，可能推动眼镜、VR 头显的音频前端设计从闭环误差麦克风转向神经前馈估计。工业上对轻量可穿戴降噪有直接参考价值，但需验证功耗与实时性。

## ⚠️ 局限与未解决问题

仅覆盖 100–1000 Hz，对中高频噪声效果未知；未报告推理延迟、功耗与模型参数量，难以判断端侧可行性；缺少与固定滤波器或传统前馈 ANC 的定量对比；评测规模仅 11 用户/8 环境，统计显著性不足；未给出语音质量类指标，降噪对语音可懂度的影响未评估。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-11/">← 返回 2026-09-11 速递</a></div>
