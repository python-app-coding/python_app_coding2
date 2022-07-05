# coding = utf8

# tests fuzzy import
from pkm import *

# m3在pkm的子包中，没有在pkm.__init__.__all__中导入
# 所以，模糊导入后，不能引用m3
# m1, m2 are in pkm.__init__.__all__, m3 is not!
try:
    print(m1)
    print(m2)
    print(m3)
except NameError as e:
    print(e)
