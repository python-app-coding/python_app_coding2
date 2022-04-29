#使用xlwings
============
##1. 示例
### 导入
*>>> import xlwings as xw*

### 创建新的工作簿
**>>> wb = xw.Book()  # this will create a new workbook**

### 打开一个已存在的工作簿

**>>> wb = xw.Book('FileName.xlsx')**

### 在Windows中，使用原字符串表示文件名，避免与转义符反斜杠冲突

**>>> wb = xw.Book(r'C:\path\to\file.xlsx')**

### 创建工作表实例

**>>> sheet = wb.sheets['Sheet1']**

### 操作工作表中数据

.>>> sheet.range('A1').value = 'Foo 1'

.>>> sheet.range('A1').value

.>>> sheet.range('A1').value = [['Foo 1', 'Foo 2', 'Foo 3'], [10.0, 20.0, 30.0]]

.>>> sheet.range('A1').expand().value

[['Foo 1', 'Foo 2', 'Foo 3'], [10.0, 20.0, 30.0]]

### 使用多种类型数据

.>>> import pandas as pd

.>>> df = pd.DataFrame([[1,2], [3,4]], columns=['a', 'b'])

.>>> sheet.range('A1').value = df

.>>> sheet.range('A1').options(pd.DataFrame, expand='table').value


a    b

0.0  1.0  2.0

1.0  3.0  4.0

### 在EXCEL中绘制Matplotlib图形

.>>> import matplotlib.pyplot as plt

.>>> fig = plt.figure()

.>>> plt.plot([1, 2, 3, 4, 5])

[<matplotlib.lines.Line2D at 0x1071706a0>]

.>>> sheet.pictures.add(fig, name='MyPlot', update=True)

<Picture 'MyPlot' in <Sheet [Workbook4]Sheet1>>

