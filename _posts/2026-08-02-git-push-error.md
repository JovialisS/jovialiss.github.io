---
layout: post
title: Git Push Error
date: 2026-08-02 22:56 +0800
description: 维护博客时出现的各种问题。
---


## 回退到目标推送版本

-  直接回退 
   
   HEAD~1 表示回退一个提交，HEAD~n 表示回退 n 个提交
    
    > git reset --hard HEAD~1 
     
   强制推送

    > git push origin main --force-with-lease 



- 按指定版本回退
  
  > git log 查看历史 找到 commit ID
  
  > git revert commit ID
  
  此时会提示编辑提交信息 和vim操作一样 报错关闭后 推送远程仓库
  
  > git push origin main


## 证书校验失败

### GitHub  action 报错提示 

> Could not fetch specs from https://gems.ruby-china.com/ due to underlying error
    <SSL_connect returned=1 errno=0 peeraddr=104.26.6.173:443 state=error: sslv3
    alert handshake failure (SSL alert number 40)
    (https://gems.ruby-china.com/specs.4.8.gz)>
    Error: The process '/opt/hostedtoolcache/Ruby/3.3.12/x64/bin/bundle' failed with exit code 17

### 根源所在

> 本地的Gemfile设置国内源 # source "https://gems.ruby-china.com" 
{: .prompt-warning }

然把硬编码的国内源写在 Gemfile 中其实是一种反模式（Anti-pattern），会导致非国内开发者或海外 CI 持续集成环境出现问题。

### 解决方法

- 将 Gemfile 第一行直接改回官方源 source 'https://rubygems.org'

    接着删除Gemfile.lock，

    本地运行bundle install 之后推送

- 启用 Bundler 的镜像映射功能

    本地运行 

    > bundle config set -- global mirror.https://rubygems.org https://gems.ruby-china.com

    此时本地环境会自动用 Ruby-China 镜像下载，而 GitHub Actions 线上环境会继续用官方源，互不干扰。



    