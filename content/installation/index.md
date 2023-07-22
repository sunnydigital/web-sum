---
title: Installation
date: 2023-07-11T07:00:00-04:00
draft: false
showToc: false
summary: Information about setting up the webpage summarizer from your own Replit app
disableShare: true
ShowReadingTime: false
ShowWordCount: false
showAuthor: false
tags:
    - getting-started
    - installation
    - replit
relative: true
---

![](images/installation.jpg)

## Fine, you'll do it yourself

Deploying Web-sum ChatGPT Plugin on your own Replit account is simple and straightforward, the method being from this current webpage:

1. Go to `replit.com`
2. Make an account and create a `repl` using `Python`
3. Download the latest release from [https://github.com/sunnydigital/web-sum/releases](https://github.com/sunnydigital/web-sum/releases)
4. Manually drag all associated files into the folder for your `Repl`
5. Click `Run`
6. Go to `chat.openai.com`
7. Click `New chat` > `GPT-4` > `Plugins (Beta)` > `Plugin store` > `Install your own plugin`
8. Enter the URL for your `Repl`, which is different for each person/`Repl` but always in the form `<Repl Name>.<Your Username>.repl.co`

Et voilà! you are ready to browse the web using ChatGPT.

Enter the webpage you would like to read (in the form of an `URL`) or the link to a PDF hosted by a website (through an `URL` ending with `.pdf`).

**Note**: 
1. Installing your own and running your `Repl` is free, but the `Repl` will only be online for as long as your remain on the page, you can however pay money and deploy it.
2. The current iteration of the plugin does not handle text over the token size of `4096` as set for both GPT-3.5 (ChatGPT) and GPT-4. Every `1000` "tokens" is roughly `750` words, meaning for approximately `3072` words in the webpage or URL document. Future iterations will handle this issue, potentially including multiple post/get requests to process all tokens of a document.