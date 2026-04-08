---
layout: post
title: Fixing Node.js 20 GitHub Actions Errors
date: 2026-04-08 22:29 +0800
description: Github action出错 强制更新node
categories: [Technology, Github]
tags: [Github,Action,Node.js]
pin: false 
---

## Recommended

The Fix (Update to Node 24): Update your workflow to use the latest version of standard actions.

'''

    steps:
    - uses: actions/checkout@v4  # Ensure you are on v4+[[5](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQHijpuGWVfSwPzSs_fRLhEWk7JAMzmUCNEX8Fw1ZM_qvEl-3DjGFnh58B6_RFJjvRGcJnL2M9Oph87UDFMmHCu-LJbMx0TrYHnSGtge4jr82o3ULefLB4TsjFvLJsFgxMKYZnE6kF8Qcyg4vZwdfA%3D%3D)]
    - name: Setup Node
        uses: actions/setup-node@v4
        with:
        node-version: '24' # Change from '20' to '24'
'''

## 先找到工作流文件

一般目录是 .github/workflows ，然后其中会有yml文件 一个或者多个都属正常 然后修改


'''

    name: "Build and Deploy"
    on:
    push:
        branches:
        - main
        - master
        paths-ignore:
        - .gitignore
        - README.md
        - LICENSE

    workflow_dispatch:

    permissions:
    contents: read
    pages: write
    id-token: write

    concurrency:
    group: "pages"
    cancel-in-progress: true

    # 在全局范围添加环境变量，强制所有 JS Action 使用 Node 24 运行
    env:
    FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true

    jobs:
    build:
        runs-on: ubuntu-latest

        steps:
        - name: Checkout
            uses: actions/checkout@v4
            with:
            fetch-depth: 0

        - name: Setup Pages
            id: pages
            uses: actions/configure-pages@v5 # 升级到 v5

        - name: Setup Ruby
            uses: ruby/setup-ruby@v1
            with:
            ruby-version: 3.3
            bundler-cache: true

        - name: Build site
            run: bundle exec jekyll b -d "_site${{ steps.pages.outputs.base_path }}"
            env:
            JEKYLL_ENV: "production"

        - name: Test site
            run: |
            bundle exec htmlproofer _site \
                --disable-external \
                --ignore-urls "/^http:\/\/127.0.0.1/,/^http:\/\/0.0.0.0/,/^http:\/\/localhost/"

        - name: Upload site artifact
            uses: actions/upload-pages-artifact@v3 # 确保是 v3，如果报 node 错误，上述 env 会处理
            with:
            path: "_site${{ steps.pages.outputs.base_path }}"

    deploy:
        environment:
        name: github-pages
        url: ${{ steps.deployment.outputs.page_url }}
        runs-on: ubuntu-latest
        needs: build
        steps:
        - name: Deploy to GitHub Pages
            id: deployment
            uses: actions/deploy-pages@v4 # 确保是 v4
'''




> **如果你的报错是 Unsupported engine（引擎不支持），你需要修改你项目根目录下的 package.json 文件。**
{: .prompt-tip }

'''

    {
    "name": "your-project",
    "version": "1.0.0",
    "engines": {
        "node": ">=24" 
    }
    }

'''