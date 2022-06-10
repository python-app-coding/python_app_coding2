# coding = utf8

import pandas as pd


df1 = pd.DataFrame(
    data={'sno': ['1001', '1002', '1003'],
          'name': ['李明', '张力', '韩中'],
          'score': [95, 88, 98]
          }
    )
df2 = pd.DataFrame(
    data={'sno': ['1001', '1002', '1003'],
          'name': ['李明', '张力', '韩中'],
          'score': [95, 88, 98]
          },
    index=list('abc')
    )

print(df1)
print(df2)
