#coding=utf-8
import urllib
import re
import sys
import time
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

MAINHTML = 'http://www.jdlingyu.net/page/'

#获取网页源码
def getmainHTmlCode(htmlurl):
    page = urllib.urlopen(htmlurl)
    html = page.read()
    return html
#正则分析标签页源码找出子页码
def getmainHTmlChildPage(htmlCode):
    reg = r'<a href=\'http://www.jdlingyu.net/[0-9]*/\' class=\'imageLink image loading\' target=\'_blank\'>'
    pattern = re.compile(reg)
    urls = re.findall(pattern,htmlCode)
    return urls

def getPagedivHTmlChildPage(htmlCode):
    reg = r'<div[^>]*class="main-body"[^>]*>.*?</div>'
    pattern = re.compile(reg)
    divs = re.findall(pattern,htmlCode)
    return divs
def getImgsrcHTmlChildPage(htmlCode):
    reg = r'<a.*?href=[\'"]([^<>]*?)[\'"]'
    pattern = re.compile(reg)
    img_urls = re.findall(pattern, htmlCode)
    return img_urls


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

for i in range(1,320):
    html_code = getmainHTmlCode(MAINHTML+str(i))
    urls = getmainHTmlChildPage(html_code)
    strPath = 'D:/JDLY/' + str(i)
    mkdir(strPath)
    for url in urls:
        #splits[1]为地址
        splits = url.split('\'')
        albums_code = getmainHTmlCode(splits[1])
        path = splits[1].split('/')
        strPath1 = strPath + '/' + path[3] + '/'
        mkdir(strPath1)
        divs = getPagedivHTmlChildPage(albums_code)
        imgUrls = getImgsrcHTmlChildPage(divs[0])
        n = 1
        for imgurl in imgUrls:
            print imgurl
            urllib.urlretrieve(imgurl, strPath1 + str(n) + '.jpg')
            n = n+1



