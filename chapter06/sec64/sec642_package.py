# coding = utf8

# tests fuzzy import
from .pkm import *

try:
    print(m1)
    print(m2)
    print(m3)       # m1, m2 are in pkm.__init__.__all__, m3 is not!
except NameError as e:
    print(e)
