# 爬图虫网站图片

> 网站地址：[https://tuchong.com/](https://tuchong.com/)



准备爬取图虫网站的的高质量图片，这里是一个摄影社区，里面有很多高质量的摄影图片，有风景有人物，都很不错。

但是准备一通之后发现这里页面源代码中没有图片地址。

应该是通过js文件进行写入的方法。

正在寻找破解这种方法的破劫之路。

2017/11/28 9:18:33 


图虫网图片路径分析：

https://photo.tuchong.com/①/②/③

1. 为用户编号
2. ‘f’或者‘ft640’，意义不明确，但是基本勘定用户修改个人网址的为ft640.默认的为f
3. 图片编号，此编号应该为图片存储数据库统一的图片编号，与用户无关。与图片分租无关。

在主页-发现-摄影师中，可以看到一些热门摄影师以及累计关注以及潜力新人的部分摄影师（此处数据为js写入，获取网页源码找不到摄影师地址。）

另外其他地方找不到摄影师的存在。

即便是有了摄影师的编号，查到摄影师所在的图片集中，这时获取到的图片数据也是从js中写入，不能再网页源码中获取。


此时最大的问题就是python去运行JavaScript代码才能获取到数据。


2017/12/17 20:05:59 


---

更新一个新的方法，也算是之前思路的一个辅助类，应为之前想的不能找到具体的图片打开信息，因为需要进行js编译，所以在此直接跳过这个步骤去写了这个辅助类，也就是自己找到喜欢的图片，可以直接复制网址然后直接下载这里面的图片。

但是这样的方法过于繁琐，每次只能下载一个网址也就是一张图片。

## 实现


**代码：**

	#coding=utf-8
	import urllib
	import re
	import sys
	import time
	defaultencoding = 'utf-8'
	if sys.getdefaultencoding() != defaultencoding:
	    reload(sys)
	    sys.setdefaultencoding(defaultencoding)
	
	
	#获取网页源码
	def getmainHTmlCode(htmlurl):
	    page = urllib.urlopen(htmlurl)
	    html = page.read()
	    return html
	
	#正则分析标签页源码找出图片
	def getmainHTmlChildPage(htmlCode):
	    reg = r'<img id="image[0-9]*" class="multi-photo-image" src="[^`]*" alt="">'
	    pattern = re.compile(reg)
	    urls = re.findall(pattern,htmlCode)
	    return urls
	
	#创建目录
	def mkdir(path):
	    path = unicode(path)
	    import os
	    # 判断路径是否存在
	    # 存在     True
	    # 不存在   False
	    isExists = os.path.exists(path)
	    # 判断结果
	    if not isExists:
	        # 如果不存在则创建目录
	        # 创建目录操作函数
	        os.makedirs(path)
	        return True
	    else:
	        # 如果目录存在则不创建，并提示目录已存在
	        return False
	
	paths = 'D:/tuchong/'
	mkdir(paths)
	n = 1
	while True:
	    path = raw_input('请输入图虫图片网址')
	    code = getmainHTmlCode(path)
	    urls = getmainHTmlChildPage(code)
	    for url in urls:
	        imgPath = url.split('"')
	        print imgPath[5]
	        imgId = imgPath[5].split('/')
	        urllib.urlretrieve(imgPath[5], paths + imgId[len(imgId)-1])
	        n = n + 1

**使用**

直接运行这个文件就能进行运行，如果想修改保存目录就修改代码的paths变量的存储位置。

代码中的urls的遍历是为了放置查找到多条图片路径，其实是不需要的。

正则表达式匹配的为：<img id="image[0-9]*" class="multi-photo-image" src="[^`]*" alt="">

**能够匹配到的网址：**

例如：[https://tuchong.com/1061472/14814509/](https://tuchong.com/1061472/14814509/)

这类网址是展示图片的地址：

![](https://i.imgur.com/zv5xUoi.jpg)

这样的图片展示的网址是每个图片都会有个不同的ID。

其实这个网址可以直接查看源代码找到图片地址进行保存，但是这个网站是屏蔽了右键的使用权限。

但也不是没有办法：

![](https://i.imgur.com/571rX89.jpg)

网站图片展示区域是不能右键，但是右侧区域能够使用右键。

这样能够通过右键打开网站源代码。

---

## 更新记录

2017/12/27 16:10:30 

	更改正则匹配规则为 : 
    reg = r'<img id="image[0-9]*" class="multi-photo-image" src="[^`]*?" alt="">'