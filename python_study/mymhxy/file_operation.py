# [用 Python 实现文件查找](https://www.cnblogs.com/Lclkris/p/8724711.html)

##查找某个目录下的目标文件
#import os       #引入操作系统模块
#import sys      #用于标准输入输出
#    
#def search(path,name):
#
#    for root, dirs, files in os.walk(path):  # path 为根目录
#        if name in dirs or name in files:
#            flag = 1      #判断是否找到文件
#            root = str(root)
#            dirs = str(dirs)
#            return os.path.join(root, dirs)
#    return -1
#
#
##path = input('请输入您要查找哪个盘中的文件（如：D:\\\）')
##print('请输入您要查找的文件名：')
##name = sys.stdin.readline().rstrip()  #标准输入,其中rstrip()函数把字符串结尾的空白和回车删除
#answer = search('.\\bmp\\', '第一栏任务_795_144_945_207.bmp')
#if answer == -1:
#    print("查无此文件")
#else:
#    print(answer)


# [如何用 Python 模糊搜索文件](https://www.cnblogs.com/Lamfai/p/9398358.html)
#import os
## 路径（鼠标右键查看文件属性）
#path = './bmp/'
#files = os.listdir(path)
## 查找文件名字含有fish且以.png后缀的文件
#for f in files:
#    #if 'fish' in f and f.endswith('.png'):
#    print(f)
#    if '第一栏任务_' in f:
#        print('Found it!' + f)


import os
import logging
import sys



# 模糊查找单个文件
def search_bmp_file(pre_name):
    #
    func_infor = sys._getframe().f_code.co_name
    
    # 在子目录BMP中查找带前缀的图片文件
    bmp_path = './bmp/'
    bmp_files = os.listdir(bmp_path)
    for f in bmp_files:
        #print(f)
        if pre_name in f:
            search_bmp_file_infor = '%s, 找到带前缀 \'%s\' 的文件 : %s' % (func_infor, pre_name, f)
            print(search_bmp_file_infor)
            logging.info(search_bmp_file_infor)
            return f
        else:
            no_search_bmp_file_infor = '%s, 未找到带前缀 \'%s\' 的文件 : %s' % (func_infor, pre_name, f)
            print(no_search_bmp_file_infor)
            logging.error(no_search_bmp_file_infor)
            #return None
#


# 模糊查找文件，返回多个匹配结果
def search_bmp_file_list(pre_name):
    #
    func_infor = sys._getframe().f_code.co_name
    
    # 在子目录BMP中查找带前缀的图片文件
    bmp_path = './bmp/'
    bmp_files = os.listdir(bmp_path)
    list_file_name = []
    for f in bmp_files:
        #print(f)
        if pre_name in f:
            # 找到
            search_bmp_file_infor = '%s, 找到带前缀 \'%s\' 的文件 : %s' % (func_infor, pre_name, f)
            print(search_bmp_file_infor)
            logging.info(search_bmp_file_infor)
            # 加入列表
            list_file_name.append(f)
        else:
            no_search_bmp_file_infor = '%s, 未找到带前缀 \'%s\' 的文件 : %s' % (func_infor, pre_name, f)
            print(no_search_bmp_file_infor)
            logging.error(no_search_bmp_file_infor)
    
    # 没有找到时提示
    if not len(list_file_name):
        no_search_bmp_file_infor = '%s, 未找到带前缀 \'%s\' 的文件。最后的文件：%s' % (func_infor, pre_name, f)
        print(no_search_bmp_file_infor)
        logging.error(no_search_bmp_file_infor)
    
    return list_file_name
#

#判断一个 list 是否为空
#
#传统的方式：
#
#if len(mylist):
#    # Do something with my list
#else:
#    # The list is empty
#由于一个空 list 本身等同于 False，所以可以直接：
#
#if mylist:
#    # Do something with my list
#else: