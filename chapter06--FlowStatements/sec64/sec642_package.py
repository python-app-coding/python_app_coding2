# coding = utf8

# tests fuzzy import
from pkm import *

# m3��pkm���Ӱ��У�û����pkm.__init__.__all__�е���
# ���ԣ�ģ������󣬲�������m3
# m1, m2 are in pkm.__init__.__all__, m3 is not!
try:
    print(m1)
    print(m2)
    print(m3)
except NameError as e:
    print(e)
