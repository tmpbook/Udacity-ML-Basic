# Udacity-ML-Basic-P1-Statistics-Project

## 背景信息

在一个 Stroop（斯特鲁普）任务中，参与者得到了一列文字，每个文字都用一种油墨颜色展示。参与者的任务是将文字的打印颜色大声说出来。这项任务有两个条件：一致文字条件，和不一致文字条件。在一致文字条件中，显示的文字是与它们的打印颜色匹配的颜色词，
如：
<br>
<div style="color:red">红色</div>
<div style="color:blue">蓝色</div>
<br>
在不一致文字条件中，显示的文字是与它们的打印颜色不匹配的颜色词，如：
<br>
<br>
<div style="color:green">紫色</div>
<div style="color:purple">橙色</div>
<br>

在每个情况中，我们将计量说出同等大小的列表中的墨色名称的时间。每位参与者必须全部完成并记录每种条件下使用的时间。


## 调查问题

作为一般说明，请确保记录你在创建项目时使用或参考的任何资源。作为项目提交的一部分，你将需要报告信息来源。

### Q1: 确认试验中的变量

> 符合要求：问题回复正确确认了试验中的自变量和因变量

自变量：文字打印颜色与发音颜色是否匹配

因变量：说出打印颜色花费的时间

### Q2a: 建立假设

> 符合要求：零假设和对立假设均以文字和数学方式进行了明确说明。数学陈述中的符号也进行了定义

因为不知道总体参数，所以使用 t 检验，样本类型是相依样本，所以使用相依样本 t 检验

研究类型：

我们使用，α=0.05 的双尾 t 检验

假设这 24 个人这代表了总体，那么一致文字条件下花费的时间，均值为 μ1，非一致文字条件下，所花费的时间均值为 μ2


**数据源：**

Google 表格：[stroopdata.csv](https://docs.google.com/spreadsheets/d/1CzUzdRuVc0o6r9jTI1dDdNqfbx-0VVxldx59VbfZ-DM/edit?usp=sharing) （需科学上网）

### Q2b: 建立统计检验

> 通过统计检验来辩证提出的假设，并针对统计检验的假设前提进行说明

零假设：人们在一致文字和不一致文字条件下，所花费的时间一致

![](http://latex.codecogs.com/gif.latex?\\mu_1=\mu_2)

对立假设：人们在一致文字和不一致文字条件下，所花费的时间不同

![](http://latex.codecogs.com/gif.latex?\\mu_1\neq\mu_2)

*思想：小概率事件反证法*

### Q3:报告描述性统计分析

> 为数据集组计算了描述性统计分析，包括至少一项中心性测量和一项可变性测量


详见Google 表格：[stroopdata.csv](https://docs.google.com/spreadsheets/d/1CzUzdRuVc0o6r9jTI1dDdNqfbx-0VVxldx59VbfZ-DM/edit?usp=sharing)
### Q4: 绘制数据图

> 创建了展示数据的一项或两项可视化，包括用注释说明图中可观察到的信息。

这个不是很清楚，只看出一条线在另一条的上方，详见Google 表格：[stroopdata.csv](https://docs.google.com/spreadsheets/d/1CzUzdRuVc0o6r9jTI1dDdNqfbx-0VVxldx59VbfZ-DM/edit?usp=sharing)
### Q5: 执行统计检验并解读结果

> 正确执行并报告了一项统计检验，包括检验统计量、P 值和检验结果。检验结果针对执行的试验任务进行了解释。

- t 统计量：-8.02
- t 临界值：±2.06

t 统计量落在左侧临界区内，说明这种差异具有极其显著的统计学意义，拒绝零假设

因为落在左侧，说明很大概率 μ1 < μ2

p < 0.05（p < 0.0001）

检验结果：拒绝零假设
### Q6: 更深入探索和扩展调查

> 对所观察效应的原因做了假设。提供了 所执行的 Stroop 任务的扩展或相关试验，这可能会得到类似的效应。