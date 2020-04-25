
import os
import logging
import sys



# 模糊查找单个文件
def search_bmp_file(bmp_path, pre_name):
    #
    func_infor = sys._getframe().f_code.co_name
    
    # 在子目录BMP中查找带前缀的图片文件
    bmp_files = os.listdir(bmp_path)
    for f in bmp_files:
        if pre_name in f:
            infor = '%s, %s 中带前缀 \'%s\' 的文件 : %s' % (func_infor, bmp_path, pre_name, f)
            #print(infor)
            logging.info(infor)
            return f
        #else:
        #    no_search_bmp_file_infor = '%s, %s 中未找到带前缀 \'%s\' 的文件 : %s' % (func_infor, bmp_path, pre_name)
        #    #print(no_search_bmp_file_infor)
        #    logging.error(no_search_bmp_file_infor)
        #    #return None
        
    #
    infor = '%s, %s 中未找到带前缀 \'%s\' 的文件' % (func_infor, bmp_path, pre_name)
    #print(infor)
    logging.error(infor)
#


# 模糊查找文件前缀匹配，返回多个匹配结果
def search_bmp_file_list(bmp_path, pre_name):
    #
    func_infor = sys._getframe().f_code.co_name
    
    # 查找带前缀的图片文件
    bmp_files = os.listdir(bmp_path)
    list_file_name = []
    for f in bmp_files:
        if pre_name in f:
            # 找到
            infor = '%s, %s 中带前缀 \'%s\' 的文件 : %s' % (func_infor, bmp_path, pre_name, f)
            #print(infor)
            logging.info(infor)
            # 加入列表
            list_file_name.append(f)
        #else:
        #    no_search_bmp_file_infor = '%s, %s 中非带前缀 \'%s\' 的文件 : %s' % (func_infor, bmp_path, pre_name, f)
        #    #print(no_search_bmp_file_infor)
        #    logging.error(no_search_bmp_file_infor)
    
    # 没有找到时提示
    if not len(list_file_name):
        infor = '%s, %s 中未找到带前缀 \'%s\' 的文件。' % (func_infor, bmp_path, pre_name)
        #print(infor)
        logging.error(infor)
    
    return list_file_name
#

