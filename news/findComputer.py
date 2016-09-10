# -*- coding:utf-8 -*-
# ! /usr/bin/python
# pythontab提醒您注意中文编码问题，指定编码为utf-8
# -*- coding: utf-8 -*-
# 支持文件类型
# 用16进制字符串的目的是可以知道文件头是多少字节
# 各种文件头的长度不一样，少则2字符，长则8字符
import os
import struct
from os.path import getsize, join

'''
查看文件类型
文件格式 文件头(十六进制)
JPEG (jpg) FFD8FF
PNG (png) 89504E47
GIF (gif) 47494638
TIFF (tif) 49492A00
Windows Bitmap (bmp) 424D
CAD (dwg) 41433130
Adobe Photoshop (psd) 38425053
Rich Text Format (rtf) 7B5C727466
XML (xml) 3C3F786D6C
HTML (html) 68746D6C3E
Email [thorough only] (eml) 44656C69766572792D646174653A
Outlook Express (dbx) CFAD12FEC5FD746F
Outlook (pst) 2142444E
MS Word/Excel (xls.or.doc) D0CF11E0
MS Access (mdb) 5374616E64617264204A
1A45DFA3 mkv
'''


def __typeList():
    return {
        "FFD8FF": "JPEG(jpg)",
        "89504E47": "PNG(png)",
        "47494638": "GIF(gif)",
        "49492A00": "TIFF(tif)",
        "424D": "Windows Bitmap(bmp)",
        "41433130": "CAD(dwg)",
        "38425053": "Adobe Photoshop(psd)",
        "7B5C727466": "Rich Text Format(rtf)",
        "3C3F786D6C": "XML(xml)",
        "68746D6C3E": "HTML(html)",
        "44656C69766572792D646174653A": "Email[thorough only] (eml)",
        "CFAD12FEC5FD746F": "Outlook Express(dbx)",
        "2142444E": "Outlook(pst)",
        "D0CF11E0": "MS Word / Excel(xls. or.doc)",
        "5374616E64617264204A": "MSAccess(mdb)",
        "1A45DFA3": "mkv",
        "2E524D4600":"RMVB(rmvb,rm)"
    }  # 字节码转16进制字符串

def __bytes2hex(bytes):
    num = len(bytes)
    hexstr = u""
    for i in range(num):
        t = u"%x" % bytes[i]
        if len(t) % 2:
            hexstr += u"0"
        hexstr += t
    return hexstr.upper()

# 获取文件类型
def __filetype(filename):
    ftype = 'unknown'
    try:
        binfile = open(filename, 'rb')  # 必需二制字读取
        tl = __typeList()
        for hcode in tl.keys():
            numOfBytes = int(len(hcode) / 2)  # 需要读多少字节
            binfile.seek(0)  # 每次读取都要回到文件头，不然会一直往后读取
            hbytes = struct.unpack_from("B" * numOfBytes, binfile.read(numOfBytes))  # 一个 "B"表示一个字节
            f_hcode = __bytes2hex(hbytes)
            # print(filename+' header '+f_hcode)
            if f_hcode == hcode:
                ftype = tl[hcode]
                break
        binfile.close()
    except:
        return ftype
    return ftype

'''
查看文件类型
'''

# 保存当前有的磁盘
def __existdisk():
    curdisks = []
    allDisks = ['C:', 'D:', 'E:', 'F:', 'G:', 'H:', 'I:', 'J:', 'K:', \
                'L:', 'M:', 'N:', 'O:', 'P:', 'Q:', 'R:', 'S:', 'T:', \
                'U:', 'V:', 'W:', 'X:', 'Y:', 'Z:', 'A:', 'B:']
    for disk in allDisks:
        if os.path.exists(disk):
            if disk == 'C:':
                continue
            if disk == 'D:':
                curdisks.append(disk)
    print("existdisk -- " + str(curdisks))
    return curdisks

#使用了os.walk函数  获取文件夹个数
def __walkfunc(folder):
    folderscount=0
    filescount = 0
    size=0
    #walk(top,topdown=True,onerror=None)
    #top表示需要遍历的目录树的路径
    #topdown的默认值是"True",表示首先返回目录树下的文件，然后在遍历目录树的子目录
    #参数onerror的默认值是"None",表示忽略文件遍历时产生的错误.如果不为空，则提供一个自定义函数提示错误信息后继续遍历或抛出异常中止遍历
    for root,dirs,files in os.walk(folder): #返回一个三元组:当前遍历的路径名，当前遍历路径下的目录列表，当前遍历路径下的文件列表
        folderscount+=len(dirs)
        filescount+=len(files)
        size+=sum([getsize(join(root,name)) for name in files])
    print(size)
    return folderscount

# 查找文件内容中有要查找的字符
def __SearchFile(listDate ,path, src):
    print("准备对" + str(path) + "进行检测...")
    i = 0
    oldper = 0
    lenth = __walkfunc(path)
    if not os.path.exists(path):
        print("%s 路径不存在" % path)

    for root, dirs, files in os.walk(path, True):
        i += 1
        percent = int(i*100/lenth)
        if percent>oldper:
            oldper = percent
            print('已经检查' + str(path) + str(oldper) + "%")
        for item in files:
            paths = os.path.join(root, item)
            typeid = __filetype(paths)
            try:
                if typeid == 'unknown':
                    pass
                elif typeid.__contains__(src):
                    listDate.setdefault(item,paths)
            except:
                pass


# 查找当前所有磁盘目录文件内容下是否有要找的字符
def SearchALLFile(src):
    print('SearchALLFile -- start')
    listDate = {}
    curdisks = __existdisk()
    for disk in curdisks:
        disk = disk + "\\"
        __SearchFile(listDate ,disk, src)
    print("完成搜索")
    return listDate


    # if __name__ == '__main__':
    # filetype('D:/电影/绝地逃亡.Skiptrace.2016.TC720P.X264.AAC.Mandarin.CHS-ENG.Mp4Ba.mp4')
    # filetype('D:/电影/丛林大反攻4.吓傻了.中英字幕.Open.Season.Scared.Silly.2015.720p.BluRay.x264.深影影视组.mp4')
    # filetype('D:/电影/飘花电影piaohua.com行运一条龙1024高清粤语中字.mkv')
    # filetype('D:/电影/小八戒电影xiaobajie.com九品芝麻官国粤双语中字BD1280.mkv')
    # filetype('D:/电影/千王之王2000粤.rm')
    # filetype('D:/电影/飘花电影piaohua.com龙凤茶楼.rmvb')
     # print(SearchALLFile('rmvb'))
