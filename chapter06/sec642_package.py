# coding = utf8

# test import pkm
# import pkm
# print([p for p in dir(pkm) if '__' not in p])

# test fuzzy import
from pkm import *
try:
    print(m1)
    print(m2)
    print(m3)
except NameError as e:
    print(e)
