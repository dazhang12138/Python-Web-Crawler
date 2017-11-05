#coding=utf-8
import urllib
import re
import sys
import time
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

MAINHTML = 'http://www.mmxyz.net/rosi-'

#获取网页源码
def getmainHTmlCode(htmlurl):
    page = urllib.urlopen(htmlurl)
    html = page.read()
    return html

#正则分析标签页源码找出子页码
def getmainHTmlChildPage(htmlCode):
    reg = r'http://img1.mmxyz.net/[0-9]{4}/[0-9]{2}/rosi-[0-9]{4}-[0-9]{3}.jpg'
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
path = 'D:/ROSI/'
for i in range(1661,2158):
    code = getmainHTmlCode(MAINHTML + str(i))
    urls = getmainHTmlChildPage(code)
    mkdir(path + str(i))
    j = 1;
    for url in urls:
        urllib.urlretrieve(url, path + str(i) + '/' + str(j) + '.jpg')
        j = j + 1
        print url