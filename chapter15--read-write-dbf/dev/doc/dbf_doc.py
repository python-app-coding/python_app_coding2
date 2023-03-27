# coding = utf8


DBF_DOC = \
    """
    DBF ch3file structure description

    DBF表文件由表头区及数据记录区组成。表头定义表结构及表的其他信息。
    DBF表头区从位置0开始。数据记录区紧接在头记录之后（连续的字节）。
    DBF数据记录长度（以字节为单位）等于所有字段定义长度之和。
    DBF表中存储整数时低位字节在前（小端存储）。

    1．DBF表头结构
        字节偏移 说明
        -------------------------------------------------------------------------------------------
        0  文件类型
            0x02    FoxBASE
            0x03    FoxBASE+/dBASE III PLUS，无备注
            0x30    Visual FoxPro
            0x43    dBASE IV SQL 表文件，无备注
            0x63    dBASE IV SQL 系统文件，无备注
            0x83    FoxBASE+/dBASE III PLUS，有备注
            0x8B    dBASE IV 有备注
            0xCB    dBASE IV SQL 表文件，有备注
            0xF5    FoxPro 2.x（或更早版本）有备注
            0xFB    FoxBASE
        1 - 3 最近一次更新的时间（YYMMDD）
        4 - 7 文件中的记录数目
        8 - 9 第一个数据记录的位置（数据区开始位置）
        10 - 11 每个数据记录的长度（包括带有删除标记的记录在内）
        12 - 27 保留
        28 表的标记
            0x01 文件具有.cdx 索引。
            0x02 文件包含备注。
            0x04 文件是数据库（.dbc）
            该字节可以为任何上面值的和： 0x03, 0x05, 0x06, 0x07。
            表示多项同时存在。
            例如，0x03 表明表具有结构化.cdx和一个备注字段。
        29 代码页标记
        30 - 31 保留，包含 0x00
        32 - n 字段子记录
            字段的数目决定了字段子记录的数目。表中每个字段都对应一个字段子记录。
            field_number = (n - 32) // 32
        n+1 头记录终止符（0x0D）
        n+2 到 n+264
            此范围内的 263 个字节包含后链信息（相关数据库 (.dbc) 的相对路径）。
            如果第一个字节为 0x00，则该文件不与数据库关联。因此数据库文件本身总是包含 0x00。
        关于记录的删除记:
            每个记录数据包括：删除标记（1个字节），各字段数据（按照定义中的宽度）
            如果删除标记字节为空格 (0x20)，该记录为未置删除标记，
            如果删除标记字节为星号 (0x2A), 该记录为设置了删除标记。
        -------------------------------------------------------------------------------------------

    2．字段定义结构
        字节偏移 说明
        -------------------------------------------------------------------------------------------
        0 - 10 字段名（最多 10 个字符 -若少于 10 则用空字符 (0x00) 填充）
        11 字段类型
            C-字符型
            Y-货币型
            N-数值型
            F-浮点型
            D-日期型
            T-日期时间型
            B-双精度型
            I-整型
            L-逻辑型
            M-备注型
            G-通用型
            C-字符型（二进制）
            M-备注型（二进制）
            P-图片型
        12 - 15 记录中该字段的偏移量
        16 字段长度（以字节为单位）
        17 小数位数
        18 字段标记
            0x01 系统列（用户不可见）
            0x02 可存储 null 值的列
            0x04 二进制列（只适于字符型和备注型）
        19 - 32 保留
        -------------------------------------------------------------------------------------------

    格式保存的文件标头：
        支持 null 值
        日期时间型、货币型及双精度型数据
        字符字段和备注字段标记为二进制
        在数据库 (.dbc) 文件中添加表

    关于字段数的计算公式:
        Visual Foxpro 版本为表头区增加了263个预留后缀字节
        可以使用下面的公式求出表文件中的字段数：(hlen - 296)/32
        hlen：第一个记录的位置（表头记录的第 8 到第 9 个字节）
        296： 263（表头区后缀信息）+ 1（字段记录终止符）+ 32（文件开始的文件结构记录）
        32：  字段结构记录的长度。
        而对Foxbase或DbaseIII，则可以使用：(hlen-33)//32
        由于各个版本的差异，如无具体测试，仍应使用从33开始的搜索计算字段数
    """