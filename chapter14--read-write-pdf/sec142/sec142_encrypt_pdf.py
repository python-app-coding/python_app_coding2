# coding = utf8

from PyPDF2 import PdfFileReader, PdfFileWriter


def enrypt(input_pdf, out_pdf='temp_enrypt.pdf', password='123456'):
    """
    为PDF文件设置密码
    :param input_pdf: str 输入的原PDF文件名
    :param out_pdf: str 输出的被加密的文件名
    :param password: str 密码字符串

    # 示例
    >>> encrypt('demo.pdf', 'demo_enrypted.pdf', password='private')
    """

    # 创建读写文件对象
    pdf_reader = PdfFileReader(input_pdf)
    pdf_writer = PdfFileWriter()

    # 将页添加到输出文档对象add pages to writer
    for pno in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(pno))

    # 在输出文档中添加密钥加密add password
    pdf_writer.encrypt(user_pwd=password,  owner_pwd=password, use_128bit=True)

    # write to file
    with open(out_pdf, 'wb') as fp:
        pdf_writer.write(fp)


def decrypt(input_pdf, out_pdf, password=None):
    """
    为PDF文件设置密码
    :param input_pdf: str 输入的原PDF文件名
    :param out_pdf: str 输出的被解密的文件名
    :param password: str 密码字符串

    # 示例
    >>> decrypt('demo_encrypted.pdf', 'demo_decrypt.pdf', password='private')
    """

    # 读取并解密原文档read and decrypt pdf
    pdf_reader = PdfFileReader(open(input_pdf, 'rb'))
    pdf_reader.decrypt(password)
    # 添加解密后文档页到输出文档对象add pages to writer
    pdf_writer = PdfFileWriter()
    for page in pdf_reader.pages:
        pdf_writer.addPage(page)
    # 将输出文档对象写入文件write to file
    with open(out_pdf, 'wb') as fp:
        pdf_writer.write(fp)
