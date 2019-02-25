#!/usr/bin/env python
# -*- coding: utf-8 -*-
from maker import __version__

import click
import PIL.Image as Image


class QrPostMaker(object):
    def __init__(self, bgimg, qrsizex, qrsizey, qrboxx, qrboxy):
        self.backImg = bgimg
        self.post = None
        self.qrsizex = qrsizex
        self.qrsizey = qrsizey
        self.qrboxx = qrboxx
        self.qrboxy = qrboxy

    def create(self, qrimg):
        """
        @qrImg: 用户二维码图片地址
        """
        try:
            bgimg = Image.open(self.backImg)

            qrimg = Image.open(qrimg)
            qrimg.thumbnail((self.qrsizex, self.qrsizey))
            bgimg.paste(qrimg, (self.qrboxx, self.qrboxy))

            self.post = bgimg
            bgimg.save("qrPost.jpg", "jpeg")
        except Exception as e:
            print(repr(e))


def output_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo("qr-poster-maker version:")
    click.echo("version: 1.0.1")
    ctx.exit()


@click.command()
@click.option('-b', '--bgimg', type=str, help='Background image')
@click.option('-q', '--qrimg', type=str, help='QR Code image')
@click.option('-sx', '--qrsizex', type=str, default='142', help='QR Code size x')
@click.option('-sy', '--qrsizey', type=str, default='142', help='QR Code size y')
@click.option('-bx', '--qrboxx', type=str, default='860', help='QR Code position x')
@click.option('-by', '--qrboxy', type=str, default='1250', help='QR Code position y')
@click.option(
    '-v',
    '--version',
    is_flag=True,
    is_eager=True,
    callback=output_version,
    expose_value=False,
    help="show the version of this tool")
def qrmaker(bgimg, qrimg, qrsizex, qrsizey, qrboxx, qrboxy):
    qr_poster_maker = QrPostMaker(bgimg=bgimg, qrsizex=int(qrsizex), qrsizey=int(qrsizey), qrboxx=int(qrboxx),
                                  qrboxy=int(qrboxy))
    qr_poster_maker.create(qrimg=qrimg)


if __name__ == '__main__':
    qrmaker()
