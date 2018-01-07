# Udacity-ML-Basic-P1-Statistics-Project

## 背景信息

在一个 Stroop（斯特鲁普）任务中，参与者得到了一列文字，每个文字都用一种油墨颜色展示。参与者的任务是将文字的打印颜色大声说出来。这项任务有两个条件：一致文字条件，和不一致文字条件。在一致文字条件中，显示的文字是与它们的打印颜色匹配的颜色词，如：红色（打印颜色红色）、蓝色（打印颜色红色）。在不一致文字条件中，显示的文字是与它们的打印颜色不匹配的颜色词，如：紫色（打印颜色红色）、橙色（打印颜色紫色）。在每个情况中，我们将计量说出同等大小的列表中的墨色名称的时间。每位参与者必须全部完成并记录每种条件下使用的时间。

## 调查问题

作为一般说明，请确保记录你在创建项目时使用或参考的任何资源。作为项目提交的一部分，你将需要报告信息来源。

### Q1: 确认试验中的变量

> 符合要求：问题回复正确确认了试验中的自变量和因变量

- 自变量：文字打印颜色与发音颜色是否匹配
- 因变量：说出打印颜色花费的时间

### Q2a: 建立假设

> 符合要求：零假设和对立假设均以文字和数学方式进行了明确说明。数学陈述中的符号也进行了定义

零假设（H0）：针对一致文字条件和不一致文字条件的列表，说出墨色花费的时间相同。
    
即：![](http://latex.codecogs.com/gif.latex?\\mu_1=\mu_2)

对立假设（H1）：针对一致文字条件下说出墨色花费的时间与针对不一致文字条件下说出的墨色花费的时间不相同

即：![](http://latex.codecogs.com/gif.latex?\\mu_1-\mu_2\neq0)

- ![](http://latex.codecogs.com/gif.latex?\\mu_1) 表示文字和墨色一致条件下读出墨色花费的时间的总体均值
- ![](http://latex.codecogs.com/gif.latex?\\mu_2) 表示文字和墨色不一致条件下读出墨色花费的时间的总体均值

假设检验是：先对总体的参数提出某种假设，然后利用样本信息判断假设是否成立

本题先提出 H0 假设，即时间花费相同，然后计算得到现有样本的可能性有多大，若我们预先规定显著性水平 α = 0.05，那么得到现有样本的概率 P < 0.05 的时候，说明小概率事件发生了，一次试验不应该发生，说明我们的假设有问题，所以拒绝 H0

**数据源：**

Google 表格：[stroopdata.csv](https://docs.google.com/spreadsheets/d/1CzUzdRuVc0o6r9jTI1dDdNqfbx-0VVxldx59VbfZ-DM/edit?usp=sharing) （需科学上网）

### Q2b: 建立统计检验

> 符合要求：通过统计检验来辩证提出的假设，并针对统计检验的假设前提进行说明

1. 不知道总体均值、总体标准偏差，样本量小于 30，选择 **t 检验**
2. 两个样本是同一组人在不同条件下获取的，样本属于：**配对样本**/**相依样本**
3. 对立假设时间不同意味着有可能大于也有可能小于，选择**双尾检验**
4. 显著性水平 α 选择 0.05
5. 两组样本的总体基本是正态分布的（通过样本推断：两组样本都是正态分布的），且样本量小于 30
6. 样本数据可以用来估计总体方差，且总体方差应该大概相等（相依样本可以直接假设方差相等）

综上：采用 α = 0.05 的配对 t 检验中的双尾检验

### Q3:报告描述性统计分析

> 符合要求：为数据集组计算了描述性统计分析，包括至少一项中心性测量和一项可变性测量

集中趋势测量：

- 均值 - mean

    ![](http://latex.codecogs.com/gif.latex?\\frac{\sum_{i=1}^{n}x_i}{n})
- 中位数 - median

    处于数据集正中间的数值，如果有两个，那么取这两个的平均数
- 众数 - mode

    出现频率最高的数字

变异测量

- 范围

    最大值和最小值之间的差：![](http://latex.codecogs.com/gif.latex?x_{max}-x_{min})
- IQR

    将数据集四等分后，IQR = Q3 - Q1
- 标准偏差

    ![](http://latex.codecogs.com/gif.latex?\\sqrt{\frac{\sum_{i=1}^{n}(x_i-\overline{x})^2}{n-1}})
- 两组样本值的差异

    difference = x1 - x2
- 差异的均值

    ![](http://latex.codecogs.com/gif.latex?\\frac{\sum_{i=1}^{n}(x_1-x_2)}{n})

#### 本题：

集中趋势 | Congruent	| Incongruent
---|---|---
均值 | 14.051125 | 22.01591667
中位数	| 14.3565 |	21.0175

变异测量 | Congruent	| Incongruent
---|---|---
标准偏差 | 3.559357958 | 4.797057122
差异的均值 | -7.964791667

详见Google 表格：[stroopdata.csv](https://docs.google.com/spreadsheets/d/1CzUzdRuVc0o6r9jTI1dDdNqfbx-0VVxldx59VbfZ-DM/edit?usp=sharing)
### Q4: 绘制数据图

> 符合要求：创建了展示数据的一项或两项可视化，包括用注释说明图中可观察到的信息。

使用直方图，发现两份样本都是呈正态分布的

图见 Google 表格：[stroopdata.csv](https://docs.google.com/spreadsheets/d/1CzUzdRuVc0o6r9jTI1dDdNqfbx-0VVxldx59VbfZ-DM/edit?usp=sharing)
### Q5: 执行统计检验并解读结果

> 符合要求：正确执行并报告了一项统计检验，包括检验统计量、P 值和检验结果。检验结果针对执行的试验任务进行了解释。

计算 t 统计量的过程

1. t 临界值

    使用 Excel 或者 Google Doc 的`TINV`函数，如：α=0.05，df=23的情况下 `=TINV(0.05, 23)`
2. 差异样本标准偏差

    ![](http://latex.codecogs.com/gif.latex?S_d=\sqrt{\frac{\sum_{i=1}^{n}(d_i-\overline{d})}{n-1}})
3. 计算均值标准误差
    
    ![](http://latex.codecogs.com/gif.latex?SEM=\frac{s}{\sqrt{n}})
4. 计算 t 统计量

    ![](http://latex.codecogs.com/gif.latex?t=\frac{\overline{d}-u}{SEM})
5. 计算 P 值

    [在线工具](https://www.graphpad.com/quickcalcs/pValue1/)

#### 本题：

- α = 0.05
- df = 23
- t 临界值	= ±2.06865761
- 差异样本标准偏差 = 4.86482691
- t 统计量	= -8.020706944
- P 值明显小于 0.05（p < 0.0001）

结论：符合预期，结果是具有显著的统计学意义的，我们拒绝零假设。即：加入干预条件后（文字与墨色不一致），会使得读者读出文字墨色的时间与文字墨色一致条件下的时间不一致。

计算P值的网站：https://www.graphpad.com/quickcalcs/pValue1/

r^2 = 73.66%（有73.66%的概率，差异是因为文字和颜色是否一致导致的）

cohen's d = -1.637219949（说明相差1.64个差异标准差）

### Q6: 更深入探索和扩展调查

> 符合要求：对所观察效应的原因做了假设。提供了 所执行的 Stroop 任务的扩展或相关试验，这可能会得到类似的效应。

不太清楚是什么意思


## 附：

### t 检验分类

1. 单样本 t 检验 - dependent t test
    
    使用单样本 t 检验估计总体均值，并将其与目标值或参考值进行比较
2. 双样本 t 检验 - independent t test
    
    需要分析两个独立组的均值是否存在差异或者计算两个总体均值差异范围
3. 配对 t 检验 - paired t test
    
    确定两个配对样本之差的均值不等于 0（或目标值）或者计算可能包含差异总体均值的值的范围

### 一些有用的网站

[网站一](http://www.socscistatistics.com/pvalues/tdistribution.aspx) - 统计学计算1

[网站二](https://www.graphpad.com/quickcalcs/pValue1/) - 统计学计算2

[网站三](http://latex.codecogs.com/) - LaTeX 转图片