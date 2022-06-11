# coding = utf8

import pandas as pd
import numpy as np
import faker
import random
from openpyxl import load_workbook


def make_faker_dataframe(number=100):
    idno = []; name=[]; phone=[]; addr=[]; yw=[]; sx=[]; wy=[]
    fk = faker.Faker('zh_CN')
    for i in range(number):
        idno.append('010{:03d}'.format(i+1))
        name.append(fk.name())
        phone.append(fk.phone_number())
        addr.append(fk.address())
        yw.append(random.randint(0, 150))
        sx.append(random.randint(0, 150))
        wy.append(random.randint(0, 100))
    df = pd.DataFrame({'sno': idno, 'name': name, 'phone': phone,
                       'addr': addr, 'yw': yw, 'sx': sx, 'wy': wy})
    df.loc[:, 'zf'] = df.yw + df.sx + df.wy
    df1 = df[['sno', 'name', 'phone', 'addr']]
    df2 = df[['sno', 'name', 'yw', 'sx', 'wy', 'zf']]
    return df, df1, df2


def demo_write_data_to_sheets():
    """
    write DataFrame to Excel.Sheet
    :param file: excel file name
    :param number: row number for DataFrame
    :return: DataFrame1 for sheet info, DataFrame2 for sheet score
    """
    df, df1, df2 = make_faker_dataframe(10)
    file = 'temp_demo_write_sheets.xlsx'

    # write DataFrame to Excel with ExcelWriter
    # 生成ExcelWriter对象，使用引擎openpyxl
    with pd.ExcelWriter(file, engine='openpyxl') as writer:
        df1.to_excel(writer, sheet_name='info')  # 将df1写入工作表info
        df2.to_excel(writer, sheet_name='score')  # 将df2写入工作表score

    # read all sheets from Excel by setting sheet_name=None
    dfs = pd.read_excel(file, sheet_name=None, index_col=0, dtype={'sno': str})

    print(
        f"""
        #DataFrame数据集df1, df2
         >>> df1
        {df1}
         >>> df2
        {df2}
        
        #将DataFrame数据集df1, df2写入Excel文件
         >>> with pd.ExcelWriter('demo_excel2.xlsx', engine='openpyxl') as writer:
         ...     df1.to_excel(writer, sheet_name='info')        # 将df1写入工作表info
         ...     df2.to_excel(writer, sheet_name='score')       # 将df2写入工作表score
        
        # 设置sheet_name=None，读取所有Excel文件的工作簿，读取第0列索引
         >>> dfs = pd.read_excel('demo_excel2.xlsx', sheet_name=None, index_col=0, dtype={{'sno': str}})
         >>> dfs['info']
        {dfs['info']}
         >>> dfs['score']
        {dfs['score']}
        """
    )


if __name__ == '__main__':
    demo_write_data_to_sheets()
