# coding = utf8

from PyPDF2 import PdfFileReader, PdfFileWriter


def rotation(input_pdf=None, writepdf='temp_rotation.pdf', rotation_dict=None):
    """
    旋转PDF文件
    :param input_pdf: str 输入文件名
    :param writepdf:  str 旋转后输出文件名
    :param rotation_dict: dict[int: int] 各个页号的旋转度数

    指定文档及页号进行旋转：
    >>> rotation('demo.pdf', rotation_dict={0: 90})
    """
    # create reader and writer
    pdf_reader = PdfFileReader(open(input_pdf, 'rb'))
    pdf_writer = PdfFileWriter()

    # rotate page and add page to writer
    for pno, page in enumerate(pdf_reader.pages):
        if pno in rotation_dict:
            pdf_writer.addPage(page.rotateClockwise(rotation_dict[pno]))
        else:
            pdf_writer.addPage(page)

    # write to file
    with open(writepdf, 'wb') as fp:
        pdf_writer.write(fp)
