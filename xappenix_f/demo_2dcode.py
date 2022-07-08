# coding: utf8

import numpy as np
from PIL import Image
from pyzbar import pyzbar
import qrcode
from MyQR import myqr


def create_2dbar_with_qrcode(
        data='www.bing.com',
        bar_file='temp_2dbar.png',
        back_color='white',
        fill_color='black',
        version=10,
        error_correction=0,
        box_size=10,
        border=4):
    """
    使用qrcode创建二维码

    Args:
        data(str)； 写入二维码的数据
        bar_file(str): 写入文件名称
        back_color(str): 二维码的背景颜色
        fill_color(str): 二维码的填充颜色（码块颜色）
        version(int): 二维码格子大小，可以是1到40。值越大，格子越大，一般不超过10，选择3比较合适
        error_correction(int): 容许的错误率(0-15%, 1-7%, 2-30%)
        box_size: 二维码中每个小格子包含的像素数量
        border: 二维码到图片边框的小格子数，默认值为 4
    """
    # create 2D barcode
    qr = qrcode.QRCode(version=version,
                       error_correction=error_correction,
                       box_size=box_size,
                       border=border)
    qr.add_data(data)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(bar_file)


def create_2dbar_with_myqr(words, picture, colorsize=True, save_name='temp_myqr_2dbar.png'):
    """
    使用MyQR创建二维码

    Args:
        words(str): 二维码文本数据(不能包含中文字符)
        picture(str): 背景图片文件名，作为背景，不然只是一个光秃秃的二维码
        colorsize(bool)：True，是否生成彩图二维码
        save_name(str)：生成二维码图像名称
    """
    myqr.run(words=words,
             picture=picture,
             colorized=colorsize,
             save_name=save_name)

def read_2dbar(bar_file='temp_2dbar.png'):
    """
    读取二维码文件，返回数组

    >>> myim = np.array(Image.open('temp_2dbar.png'))
    >>> pyzbar.decode(myim)    # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    [
     Decoded(data=...,
     type='QRCODE',
     rect=Rect(left=..., top=..., width=..., height=...),
     polygon=[Point(x=..., y=...), Point(x=..., y=...), Point(x=..., y=...), Point(x=..., y=...)],
     quility=...,
     orientation=...)
    ]

    >>> read_2dbar('temp_2dbar.png')
    'http://www.bilibili.com'
    """
    im = np.array(Image.open(bar_file))
    return pyzbar.decode(im)[0].data.decode("utf-8")
