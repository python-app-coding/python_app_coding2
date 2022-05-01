# xlwings 使用指南

------
##1. 第三方包xlwings简介

xlwings是一款开源免费的Python第三方库，使用xlwings能够轻松读写Excel文件中的数据，支持按照Excel单元格进行访问修改，可以与pandas等类库集成使用。

在较新的Anaconda和WinPython中，已经预装了xlwings，可以在Windows和MacOs环境中使用。

直接使用Python脚本或在Jupyter单元中，都可以使用xlwings处理Excel文件，也可以在Excel中通过宏调用Python脚本。

在Windows中，还可以编写用户自定义函数。

有关xlwings项目详情，可访问网址：https://www.xlwings.org/

费利克斯•朱姆斯坦（Felix Zumstein）是xlwings的创始人。费利克斯在工作中接触了大量Excel用户，他对Excel在各行各业中的使用瓶颈和解决思路拥有深刻的见解。

他的书《Python for Excel》值得一读：

![xlwings_img_python_for_excel.png](xlwings_img_python_for_excel.png)


##2. 使用xlwings读写EXCEL文件示例
### 导入

`>>> import xlwings as xw`

### 创建新的工作簿

```
>>> wb = xw.Book()  # this will create a new workbook
```

### 打开一个已存在的工作簿

`>>> wb = xw.Book('FileName.xlsx')`

### 在Windows中，使用原字符串表示文件名，避免与转义符反斜杠冲突

`>>> wb = xw.Book(r'C:\path\to\file.xlsx')`

### 创建工作表实例

`>>> sheet = wb.sheets['Sheet1']`

### 操作工作表中数据

```
>>> sheet.range('A1').value = 'Foo 1'

>>> sheet.range('A1').value

>>> sheet.range('A1').value = [['Foo 1', 'Foo 2', 'Foo 3'], [10.0, 20.0, 30.0]]

>>> sheet.range('A1').expand().value

[['Foo 1', 'Foo 2', 'Foo 3'], [10.0, 20.0, 30.0]]
```



### 使用多种类型数据
```
>>> import pandas as pd

>>> df = pd.DataFrame([[1,2], [3,4]], columns=['a', 'b'])

>>> sheet.range('A1').value = df

.>>> sheet.range('A1').options(pd.DataFrame, expand='table').value

a    b

0.0  1.0  2.0

1.0  3.0  4.0
```

### 在EXCEL中绘制Matplotlib图形
```
>>> import matplotlib.pyplot as plt

>>> fig = plt.figure()

>>> plt.plot([1, 2, 3, 4, 5])

[<matplotlib.lines.Line2D at 0x1071706a0>]

>>> sheet.pictures.add(fig, name='MyPlot', update=True)

<Picture 'MyPlot' in <Sheet [Workbook4]Sheet1>>
```

