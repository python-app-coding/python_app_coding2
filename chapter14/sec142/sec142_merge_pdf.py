# coding = utf8

from PyPDF2 import PdfFileReader, PdfFileWriter


def merge(read_pdf_list, mergepdf='merge_00.pdf'):
    """
    将多个PDF文件合并为一个文件
    :param read_pdf_list: tuple[str] 被合并的PDF文件名
    :param merge_pdf: str 合并后的文件名

    # 合并文件示例
    >>> merge(('split_pdf_01.pdf', 'split_pdf_02.pdf'), 'merge.pdf')
    """
    # 创建文档读取、输出对象
    readers = [PdfFileReader(pdf) for pdf in read_pdf_list]
    merge_writer = PdfFileWriter()

    # 将源文档页对象添加到输出对象中
    for reader in readers:
        for i in range(reader.getNumPages()):
            merge_writer.addPage(reader.getPage(i))

    # 将输出对象写入到文件
    with open(mergepdf, 'wb') as fp:
        merge_writer.write(fp)
