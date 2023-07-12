---
title: Quickstart
date: 2023-07-11T07:00:00-04:00
draft: false
showToc: false
summary: Information about the webpage summarizer
disableShare: true
ShowReadingTime: false
ShowWordCount: false
showAuthor: false
tags:
    - getting-started
    - quickstart
relative: true
---

![](images/quickstart.jpg)

## Quick deploy

Deploying Web-sum ChatGPT Plugin is simple and straightforward, the method being from this current webpage:

1. Go to `chat.openai.com`
2. Click `New chat` > `GPT-4` > `Plugins (Beta)` > `Plugin store` > `Install an unverified plugin`
3. Enter `web-sum.sunnyson.dev`

Et voilà! you are ready to browse the web using ChatGPT.

Enter the webpage you would like to read (in the form of an `URL`) or the link to a PDF hosted by a website (through an `URL` ending with `.pdf`).

**Note**: The current iteration of the plugin does not handle text over the token size of `4096` as set for both GPT-3.5 (ChatGPT) and GPT-4. Every `1000` "tokens" is roughly `750` words, meaning for approximately `3072` words in the webpage or URL document. Future iterations will handle this issue, potentially including multiple post/get requests to process all tokens of a document.