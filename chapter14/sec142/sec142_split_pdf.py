# coding = utf8

from PyPDF2 import PdfFileReader, PdfFileWriter


def split(read_pdf, page_group=None):
    """
    将PDF文件拆分为多个文件
    :param read_pdf: str 被拆分的PDF文件名
    :param page_group: tuple[tuple[int]] 指定各个拆分文件的页号
    :return: 创建各个拆分文件 read_pdf_01, read_pdf_02, ...

    # 将输出文档split_pdf_01.pdf, spli_pdf_02.pdf
    >>> split('demo.pdf', ((1, 2), (5, 4)))
    """
    # 读出原文件
    pdf_reader = PdfFileReader(read_pdf)

    # 为每个输出文档建立一个writer
    pdf_writer_list = [PdfFileWriter() for _ in page_group]

    # 按照页号将有关文档页增加到输出文档
    for j, page_list in enumerate(page_group):
        for pno in page_list:
            pdf_writer_list[j].addPage(pdf_reader.getPage(pno))

    # 将每个writer写入到PDF文件
    for fno, writer in enumerate(pdf_writer_list):
        split_file_name = 'split_pdf_{:02d}.pdf'.format(fno+1)
        with open(split_file_name, 'wb') as fp:
            writer.write(fp)
