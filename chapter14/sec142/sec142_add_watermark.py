# coding = utf8

from PyPDF2 import PdfFileReader, PdfFileWriter


def add_watermark(input_pdf, watermark_pdf, out_pdf):
    """
    为PDF文件增加水印
    :param input_pdf:str 输入文件名
    :param watermark_pdf: 水印文件名
    :param out_pdf: str 输出的已增加水印的文件名

    # 添加水印示例
    >>> add_watermark('raw.pdf', 'watermark.pdf', 'raw_with_watermark.pdf')
    """
    # 读取水印和源文档read watermark and input pdf
    wm_reader = PdfFileReader(watermark_pdf, strict=False)
    watermark = wm_reader.getPage(0)
    pdf_reader = PdfFileReader(input_pdf, strict=False)

    # 添加水印到输出文档add watermark to writer
    pdf_writer = PdfFileWriter()
    for page in pdf_reader.pages:
        # page = pdf_reader.getPage(pageno)
        page.mergePage(watermark)
        page.compressContentStreams()
        pdf_writer.addPage(page)

    # 将输出文档写入文件write to pdf file
    pdf_writer.write(open(out_pdf, 'wb'))
