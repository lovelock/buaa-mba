---
title: "层次分析法(AHP)详解：如何选择最佳工作offer"
description: 
date: 2024-08-10T23:51:22+08:00
image: 
math: true
license: 
hidden: false
comments: true
categories: ["运筹与决策"]
tags: ["ahp"]
---

在职业生涯中,我们经常需要在多个工作offer之间做出选择。本文将详细介绍如何使用层次分析法(Analytic Hierarchy Process, AHP)来系统地分析和选择最佳工作offer。我们将通过一个具体案例,逐步展示AHP的应用过程。

## 什么是AHP？

AHP是一种多准则决策方法,由Thomas L. Saaty在20世纪70年代开发。它通过将复杂问题分解为层次结构,然后进行两两比较,最终综合各层次的权重得出结论。

## 案例背景

假设你收到了来自A、B、C三家公司的工作offer,需要在它们之间做出选择。你考虑的主要因素包括薪资、发展前景、工作环境和工作内容。

## AHP分析步骤

### 步骤1：建立层次结构

- 目标：选择最佳offer
- 准则：薪资、发展前景、工作环境、工作内容
- 方案：A公司、B公司、C公司

### 步骤2：构建判断矩阵

首先,我们需要构建准则比较矩阵:

|            | 薪资 | 发展前景 | 工作环境 | 工作内容 |
|------------|------|----------|----------|----------|
| 薪资       | 1    | 2        | 3        | 1/2      |
| 发展前景   | 1/2  | 1        | 2        | 1/3      |
| 工作环境   | 1/3  | 1/2      | 1        | 1/4      |
| 工作内容   | 2    | 3        | 4        | 1        |

然后,我们需要为每个准则构建方案比较矩阵。以下是全部四个准则的方案比较矩阵:

1. 薪资比较矩阵:

|        | A公司 | B公司 | C公司 |
|--------|-------|-------|-------|
| A公司  | 1     | 2     | 3     |
| B公司  | 1/2   | 1     | 2     |
| C公司  | 1/3   | 1/2   | 1     |

1. 发展前景比较矩阵:

|        | A公司 | B公司 | C公司 |
|--------|-------|-------|-------|
| A公司  | 1     | 1/2   | 1/3   |
| B公司  | 2     | 1     | 1/2   |
| C公司  | 3     | 2     | 1     |

1. 工作环境比较矩阵:

|        | A公司 | B公司 | C公司 |
|--------|-------|-------|-------|
| A公司  | 1     | 1     | 2     |
| B公司  | 1     | 1     | 2     |
| C公司  | 1/2   | 1/2   | 1     |

1. 工作内容比较矩阵:

|        | A公司 | B公司 | C公司 |
|--------|-------|-------|-------|
| A公司  | 1     | 3     | 2     |
| B公司  | 1/3   | 1     | 1/2   |
| C公司  | 1/2   | 2     | 1     |

### 步骤3：计算权重向量

对每个判断矩阵,我们使用几何平均法计算权重向量。以准则比较矩阵为例:

1. 计算每行的几何平均值:

   薪资: $\sqrt[4]{(1 \times 2 \times 3 \times 1/2)} = 1.316$

   发展前景: $\sqrt[4]{(1/2 \times 1 \times 2 \times 1/3)} = 0.760$

   工作环境: $\sqrt[4]{(1/3 \times 1/2 \times 1 \times 1/4)} = 0.452$

   工作内容: $\sqrt[4]{(2 \times 3 \times 4 \times 1)} = 2.213$


2. 归一化处理:

   $总和 = 1.316 + 0.760 + 0.452 + 2.213 = 4.741$
   
   薪资: $1.316 / 4.741 = 0.278$

   发展前景: $0.760 / 4.741 = 0.160$

   工作环境: $0.452 / 4.741 = 0.095$

   工作内容: $2.213 / 4.741 = 0.467$

准则权重计算结果:

- 薪资: 0.278
- 发展前景: 0.160
- 工作环境: 0.095
- 工作内容: 0.467

对于每个准则下的方案比较矩阵,我们使用相同的方法计算权重。以下是所有方案比较矩阵的权重计算结果:

1. 薪资:
   A公司: 0.540, B公司: 0.297, C公司: 0.163

2. 发展前景:
   A公司: 0.163, B公司: 0.297, C公司: 0.540

3. 工作环境:
   A公司: 0.400, B公司: 0.400, C公司: 0.200

4. 工作内容:
   A公司: 0.540, B公司: 0.163, C公司: 0.297

### 步骤4：一致性检验

在实际应用中,应进行一致性检验以确保判断的合理性。

设比较矩阵为$A$，特征向量为$w$，一致性检验的步骤如下：

$$
B_w=MMULT(A, w)
$$

$$
\lambda_{max} = \frac{\sum\limits_{i=1}^n{\frac{(B_w)_i}{w_i}}}{n}
$$

$$
C.I. = \frac{\lambda_{max} - n}{n-1}
$$

$$
C.R. = \frac{C.I.}{R.I.}
$$

![准则比较矩阵](/images/or/ahp-001.png)
![薪资比较矩阵](/images/or/ahp-002.png)
![发展前景比较矩阵](/images/or/ahp-003.png)
![工作环境比较矩阵](/images/or/ahp-004.png)
![工作内容比较矩阵](/images/or/ahp-005.png)

可以看到，每个$C.R.$都是小于0.1的，所以这些比较矩阵是是满足一致性的。

如果一致性检验不通过，这通常代表以下几个方面的问题：

1. 判断不一致：
   这意味着决策者在进行成对比较时，可能存在逻辑矛盾。例如，如果A比B重要，B比C重要，但C却比A重要，这就是一个典型的不一致判断。

2. 数据质量问题：
   可能存在数据输入错误，或者在收集判断数据时出现了误解或偏差。

3. 复杂性过高：
   当比较的因素数量较多时，保持所有判断的一致性变得更加困难。

4. 专家意见分歧：
   如果矩阵是基于多个专家的意见综合而成，不同专家之间的判断差异可能导致整体一致性较差。

5. 决策问题定义不清：
   如果问题本身定义不明确，或者各因素之间的关系复杂，可能导致判断困难，从而影响一致性。

6. 尺度使用不当：
   在使用1-9尺度进行判断时，如果对尺度的理解不准确，可能导致不一致的判断。

当一致性检验不通过时，通常需要采取以下措施：

1. 重新审视判断：检查是否存在明显的逻辑矛盾或输入错误。
1. 调整判断：适当调整一些判断值，使其更加一致。
1. 重新收集数据：如果问题严重，可能需要重新进行调查或咨询。
1. 使用其他方法：考虑使用其他决策方法或模型来补充分析。
1. 分解问题：如果问题过于复杂，考虑将其分解为更小的子问题。
1. 提高一致性比率阈值：在某些情况下，可以适当放宽一致性要求，但这需要谨慎操作。

总之，一致性检验不通过并不意味着整个分析无效，但确实表明需要仔细审视和可能的修正，以确保决策的可靠性和有效性。

### 步骤5：计算总排序

将每个准则下的方案权重与准则权重相乘,然后求和:

| 公司 | 薪资(0.278) | 发展前景(0.160) | 工作环境(0.095) | 工作内容(0.467) | 总分 |
|------|-------------|-----------------|-----------------|-----------------|------|
| A    | $0.540 \times 0.278$ | $0.163 \times 0.160$     | $0.400 \times 0.095$     | $0.540 \times 0.467$     | 0.466|
| B    | $0.297 \times 0.278$ | $0.297 \times 0.160$     | $0.400 \times 0.095$     | $0.163 \times 0.467$     | 0.242|
| C    | $0.163 \times 0.278$ | $0.540 \times 0.160$     | $0.200 \times 0.095$     | $0.297 \times 0.467$     | 0.292|

计算过程示例(A公司):

$0.540 \times 0.278 + 0.163 \times 0.160 + 0.400 \times 0.095 + 0.540 \times 0.467 = 0.466$

## 结果分析

根据AHP分析结果,三家公司的最终排序为:

1. A公司: 0.466
1. C公司: 0.292
1. B公司: 0.242

A公司的综合得分最高,主要得益于其在薪资和工作内容方面的优势。虽然C公司在发展前景方面表现最佳,但在其他方面相对较弱。B公司在各方面表现中等,但没有突出优势。

## 结论

通过AHP分析,我们可以看到A公司是最佳选择。这种方法帮助我们系统地考虑了多个因素,并根据它们的相对重要性进行了权衡。然而,需要注意的是,AHP分析结果应该作为决策的参考,而不是唯一依据。个人偏好、直觉和其他定性因素也应该在最终决策中得到考虑。

AHP方法为复杂的决策问题提供了一个结构化的分析框架,特别适用于需要考虑多个相互冲突的准则的情况。无论是在职业选择、项目评估还是战略规划中,AHP都是一个强大的决策支持工具。

文中使用的[excel文件下载](/xlsx/AHP示例.xlsx)
