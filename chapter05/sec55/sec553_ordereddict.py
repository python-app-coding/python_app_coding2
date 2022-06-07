# coding = utf8
import collections as cll

od = cll.OrderedDict()
od['1'] = 'a'
od['2'] = 'b'
od['3'] = 'c'

print(od)

# travers OrderedDict
print("--- traverse OrderedDict ---")
for k, v in od.items():
    print((k, v))

# pop items as LIFO, default last=True
print("--- popitem OrderedDict ---")
od1 = od.copy()
while od1:
    print(od1.popitem())

# pop items as FIFO, if last=False
print("--- popitem(last=False) OrderedDict ---")
od1 = od.copy()
while od1:
    print(od1.popitem(last=False))
