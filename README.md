# qr-poster-maker

自动生成带微信二维码的海报。

最近在做的微信小程序：离岛日签，在正式上线后收到了一些用户的反馈，有说希望可以将每日的图文信息保存下来的，也有希望可以将图文信息分享到朋友圈的，那么基于这些需求，我给小程序增加了长按保存图文卡片的功能。

由于没有现成的轮子，于是打算自己造一个，这个Python小工具可以根据具体海报指定二维码生成的位置和大小。

# 原理

一般用于推广的海报样式都差不多，需要改变的就是用户的二维码，所以只需要准备好海报的背景图，然后根据用户提供的二维码，将其贴在海报指定的位置上即可。

# 参数说明

- 1、bgimg——海报背景图片
- 2、qrimg——用户二维码图片
- 3、qrsizex——二维码图片的长
- 4、qrsizey——二维码图片的宽
- 5、qrboxx——二维码在海报背景图上的x坐标
- 6、qrboxy——二维码在海报背景图上的y坐标

# 用法

VOL6.jpeg是海报背景图，qr.png是用户二维码图片。

```
pip install qrmaker
maker -b VOL1.jpeg -q qr.png
```

# 效果图

![](https://raw.githubusercontent.com/logan62334/qr-poster-maker/master/maker/qrVOL1.jpg)