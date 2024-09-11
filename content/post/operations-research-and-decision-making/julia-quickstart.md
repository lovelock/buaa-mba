
---
title: "Julia快速上手：为了实现线性规划"
description: 
date: 2024-08-11T22:34:21+08:00
image: 
math: 
license: 
hidden: false
comments: true
categories: ["运筹学"]
tags: ["Julia", "Windows", "winget", "homebrew"]
---

众所周知，Julia就是为科学计算而生的语言，经过我的检验，它确实是很适合做科学计算，在做线性规划时其语句写出来非常接近自然语言，给人的感觉是用自然语言的方式把问题描述出来，然后就神奇地被Julia给解决了。这篇文章主要介绍Windows下如何安装Julia及做线性规划需要的几个库。

## 安装Julia

推荐使用Winget进行安装，方便后期的管理。Winget是类似于macOS下的Homebrew的包管理工具。

```
winget install julia -s msstore
```

这时候你会发现从CMD/PowerShell是没办法执行`julia`命令的，这又是因为万恶的环境变量，而这也体现出winget相比Homebrew的缺陷：没有一个统一不变的路径，也就是说软件包实际是安装在每次对应的版本号的目录下的，但它会通过符号链接给出一个不带版本号的路径，所有通过Homebrew安装的formula的可执行文件都放在同一个路径下，只要把这个路径放在`PATH`中，通过Homebrew新安装的软件包自然就可以直接执行了。而Windows上的winget并不会这样，所以我们需要把Julia的安装路径手动添加到环境变量`Path`中，在我的环境下是这样（我居然还安装了一个PowerToys来简化这个过程，Windows可真是太好用啦！！！）。这样会有什么问题是显而易见的，等下次升级了Julia，这个路径要么就失效了，要么如果新版本不会覆盖旧版本，那么会发现安装了新版本，使用的还是老版本。

```
C:\Users\frost\AppData\Local\Programs\Julia-1.10.4\bin
```

## 安装所需的包

1. 执行`julia`进入JuliaREPL
2. 按`]`进行pkg管理模式（这一步很重要）
3. 执行`add JuMP GLPK Plots`

![Julia交互界面](/images/julia/julia-installation.png)
有可能会有网络问题，请自行解决，这个需要安装非常多的依赖，很可能是由于安装了`Plots`包的原因，毕竟需要画图，要的依赖就很多了。

## 编辑器支持

这一步就很简单了，最简单的做法就是在VSCode里安装Julia扩展。

![Julia效果示例](/images/julia/julia-example-01.png)

## 总结

本文介绍了在Windows下如何安装Julia以及安装需要的科学计算和画图相关的包，接下来就可以回到介绍线性规划的文章继续阅读了。