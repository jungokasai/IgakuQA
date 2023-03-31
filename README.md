# Evaluating GPT-4 and ChatGPT on Japanese Medical Licensing Examinations 

## Introduction
we evaluate LLMs (GPT-3 and 4 and ChatGPT) on Japanese medical lincensing examinations from the past five years (2018-2022) and release the data as the IGAKU QA (医学 QA) benchmark

## Benchmark Collection
We collect the exam problems and their answers in the past five years (from 2018 through 2022) from the [official website](https://www.mhlw.go.jp/kouseiroudoushou/shikaku_shiken/ishi/) of the Ministry of Health, Labour and Welfare in Japan.
Notice that we do not rely on any translation of sources from other languages (e.g., English) or countries, and the benchmark comes solely from resources that are originally written in Japanese.
See our paper for more detail.


## Baselines
See [our scripts](https://github.com/jungokasai/IgakuQA/tree/main/scripts) that we use for the experiments in our paper. Note that you need an OpenAI API key to run these baselines.


## Citations
### IgakuQA and our evaluations on Japanese medical licensing examinations
```
@misc{jpn-med-exam_gpt4,
  author    = {Jungo Kasai and Yuhei Kasai and Keisuke Sakaguchi and Yutaro Yamada and Dragomir Radev},
  title     = {Evaluating {GPT}-4 and {ChatGPT} on {J}apanese Medical Licensing Examinations},
  year      = {2023},
  url       = {},
}
```
<p align="center">
<a href="https://www.cs.washington.edu/research/nlp">
<img src="https://github.com/jungokasai/THumB/blob/master/figs/uwnlp_logo.png" height="100" alt="UWNLP Logo">
</a>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<a href="">
<img src="https://github.com/realtimeqa/realtimeqa_public/blob/main/figs/tohoku_nlp.svg" height="100" alt="UWNLP Logo">
</a>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<a href="">
<img src="https://raw.githubusercontent.com/Yale-LILY/SummEval/master/assets/logo-lily.png" height="100" alt="Yale LILY logo">
</a>
</p>
