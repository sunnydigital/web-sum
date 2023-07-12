---
title: About
date: 2023-07-11T07:00:00-04:00
draft: false
showToc: false
summary: Information about the webpage summarizer
relativePath: false
---

## About Web-sum ChatGPT Plugin

<figure>
    <img style="border-radius:75%;margin-left:auto;margin-right:auto;" width="75%" src="/static/logo.jpg" alt="Logo">
</figure>

The web-sum ChatGPT plugin is a tool designed to assist you in summarizing webpages efficiently and effectively. Utilizing the capabilities of OpenAI's GPT-4, this plugin allows users to enter a webpage URL and receive a brief, coherent summary of the webpage content.

### Key Features

- **Text Summarization:** Summarize any webpage or PDF by simply inputting the URL.
- **Compatibility:** Seamlessly integrates with ChatGPT.
- **Efficiency:** Leveraging AI technology for fast and accurate summarizations.

**Note**: This plugin will only work if you currently *have access* to plugins in the ChatGPT webpage

## Quick Deployment

Deploying Web-sum ChatGPT Plugin is simple and straightforward, the fastest way being from this current webpage:

1. Go to `chat.openai.com`
2. Click `New chat` > `GPT-4` > `Plugins (Beta)` > `Plugin store` > `Install an unverified plugin`
3. Enter `web-sum.sunnyson.dev`

Et voilà! you are ready to browse the web.

**Note**: The current iteration of the plugin does not handle text over the token size of `4096` as set for both GPT-3.5 (ChatGPT) and GPT-4. Every `1000` "tokens" is roughly `750` words, meaning for approximately `3072` words in the webpage or URL document. Future iterations will handle this issue, potentially including multiple post/get requests to process all tokens of a document.