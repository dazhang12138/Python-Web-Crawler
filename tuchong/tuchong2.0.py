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
