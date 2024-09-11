---
title: "证明样本方差的期望等于总体方差"
description: 
date: 2024-09-11T09:12:17+08:00
image: 
math: true
license: 
hidden: false
comments: true
categories: ["管理统计"]
tags: ["方差", "标准差", "无偏估计", "正态分布"]
---

## 总方差的定义

\(S\)是总方差：

\[
S = \sum_{i=1}^{n} (x_i - \bar{x})^2
\]

根据均值的定义，可以展开

\[
S = \sum_{i=1}^{n} (x_i^2 - 2x_i\bar{x} + \bar{x}^2)
\]
\[
= \sum_{i=1}^{n} x_i^2 - 2\bar{x}\sum_{i=1}^{n} x_i + n\bar{x}^2
\]
\[
= \sum_{i=1}^{n} x_i^2 - 2n\bar{x}^2 + n\bar{x}^2
\]
\[
= \sum_{i=1}^{n} x_i^2 - n\bar{x}^2
\]

## 计算样本方法的期望\(E[S]\)

根据期望的线性性质，可以将期望运算符分开：

\[
E[S] = E\left[\sum_{i=1}^{n} x_i^2 - n\bar{x}^2\right]
\]
\[
= \sum_{i=1}^{n} E[x_i^2] - E[n\bar{x}^2]
\]

- **第一项** \(E\left[\sum_{i=1}^{n} x_i^2\right]\)：

因为 \(x_i\) 是从总体中独立抽取的，所以可以写为：

\[
E\left[\sum_{i=1}^{n} x_i^2\right] = nE[x_i^2]
\]

- **第二项** \(E\left[n\bar{x}^2\right]\)：

\[
Var(X) = E[(X - E[X])^2]
\]

展开得到：

\[
Var(X) = E[X^2 - 2X \cdot E[X] + (E[X])^2]
\]

利用期望的线性性质，这可以分解为：

\[
Var(X) = E[X^2] - 2E[X] \cdot E[X] + (E[X])^2
\]

简化为：

\[
Var(X) = E[X^2] - (E[X])^2
\]

使用样本均值 \(\bar{x}\) 的定义，\(\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i\)，可以推导出：

\[
E[\bar{x}^2] = Var(\bar{x}) + (E[\bar{x}])^2
\]

已知：

- \(E[\bar{x}] = \mu\)
- \(Var(\bar{x}) = \frac{\sigma^2}{n}\)

所以：

\[
E[\bar{x}^2] = \frac{\sigma^2}{n} + \mu^2
\]

将其代入 \(E[n\bar{x}^2]\) 中：

\[
E[n\bar{x}^2] = n\left(\frac{\sigma^2}{n} + \mu^2\right) = \sigma^2 + n\mu^2
\]

## 代入计算

现在将这两个期望值代入 \(E[S]\)：

\[
E[S] = nE[x_i^2] - (\sigma^2 + n\mu^2)
\]

这里的 \(E[x_i^2]\) 可以通过总体方差的定义来计算，具体为：

\[
E[x_i^2] = Var(X) + (E[X])^2 = \sigma^2 + \mu^2
\]

所以

\[
E[S] = n(\sigma^2 + \mu^2) - (\sigma^2 + n\mu^2)
=(n-1)\sigma^2
\]

而公式\(E[S]=(n-1)\sigma^2\)是一个验证无偏性的结果，所以对于\(s^2\)的定义采用\(\frac{1}{n-1}\)是合理的，所以

\[
E[s^2]=E[\frac{S}{n-1}]=\frac{E[S]}{n-1}=\frac{(n-1)\sigma^2}{n-1} = \sigma^2
\]
