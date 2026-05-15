---
title: "关于"
url: "/about/"
summary: "关于本站"
hidemeta: true
---

## 这是什么

**语音/音频论文速递** 每天自动从 arxiv (eess.AS / cs.SD) 与 HuggingFace Daily Papers 抓取最新论文，
通过 DeepSeek 大模型自动分析、打分、生成中文摘要，并按主题与评分聚合发布。

整套系统完全开源、零人工维护：

- 数据源：[arxiv](https://arxiv.org/) · [HuggingFace Daily Papers](https://huggingface.co/papers)
- 分析模型：DeepSeek `deepseek-chat`
- 静态站点：Hugo (PaperMod 主题)
- 自动化：GitHub Actions（每天 09:00 北京时间）
- 全文搜索：[Pagefind](https://pagefind.app/)

## 评分含义

| 分档 | 分数 | 含义 |
| --- | --- | --- |
| 前10% | ≥ 8.0 | 方法新颖且效果显著，可能成为里程碑 |
| 前25% | ≥ 7.0 | 扎实工作、明确改进、值得关注 |
| 前50% | ≥ 6.0 | 增量贡献或工程优化 |
| 中等 | ≥ 5.0 | 一般 |
| 后50% | < 5.0 | 复现性弱或贡献有限 |

## 关于评分的免责声明

所有评分由大语言模型基于摘要自动生成，**仅供快速筛选参考**，不能代替人工评审。
低分不等于工作不好；高分也未必方法上真的有突破。请始终回到原文判断。

## 订阅

- [RSS](index.xml)

## 源码

[github.com/YuanxinGuo/audio-paper-daily](https://github.com/YuanxinGuo/audio-paper-daily)
