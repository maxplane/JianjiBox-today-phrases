# JianjiBox Today Phrases

简记药箱「今日一语」的公开内容库。每种语言有自己的选材文件。

| 语言 | 内容 |
| --- | --- |
| [简体中文](zh-Hans/phrases.json) | 唐诗宋词、古典格言和健康生活短句 |
| [繁體中文](zh-Hant/phrases.json) | 与简体共用选材，按繁体字形校对 |
| [日本語](ja/phrases.json) | 日本語の俳句、ことわざ、暮らしの短い言葉 |
| [English](en/phrases.json) | Original English verse, aphorisms, and short editorial lines |

每条包括显示文案、作者或署名说明、出处、来源链接、权利依据和标签。日语和英语各自选编。健康内容围绕日常生活与感悟。添加可核对的古典原文、传统短句或原创文案，并在手机上检查两行显示效果。

编辑语言目录中的 `phrases.json`，然后运行：

```sh
python3 build-feed.py
```

将语言文件和生成的 [today-phrases.json](today-phrases.json) 一起提交到 `main`。App 只下载合并文件一次并缓存。常用标签为 `health`、`life`、`uplifting`、`general`、`spring`、`summer`、`autumn`、`winter` 和 `mid-autumn`。天气标签供以后使用。

唐诗宋词部分来自 [chinese-poetry](https://github.com/chinese-poetry/chinese-poetry)。上游数据整理的 [MIT 授权声明](chinese-poetry-LICENSE.txt) 随库保留。其他条目的来源与权利依据记录在各自的数据里。
