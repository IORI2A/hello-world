

import logging
import sys 
from file_operation_02 import *
from image_operation_02 import *
from base_status_infor import *



# 比较同一位置的不同时点的两张截图
# match_value 越小，要求越相似
def compare_two_dynamic_object_change(bmp_path, object_name, sleep_time = 1):
    # 
    #func_infor = sys._getframe().f_code.co_name
    
    # 
    pre_name = object_name #+ '_'
    list_file_name = search_bmp_file_list(bmp_path, pre_name)
    ##print(list_file_name)
    if list_file_name:
        for file_name in list_file_name:          
            # 截图比较相似度  
            ret, l, t, r, b = is_grab_two_match(file_name, sleep_time)
            if ret:
                #click_object_infor = '%s, 比较 [%s] 无变动' % (func_infor, object_name)
                ##print(click_object_infor)
                #logging.info(click_object_infor)
                
                return DECIDE_STATUS.COMPARE_MATCH
            else:    
                #click_object_infor = '%s, 比较 [%s] 在变动中' % (func_infor, object_name)
                ##print(click_object_infor)
                #logging.info(click_object_infor)
                
                return DECIDE_STATUS.COMPARE_NOT_MATCH
    else:
        # 未有BMP文件直接返回
        click_object_error = '%s, 无有效的检测基准对象 [%s]' % (func_infor, object_name)
        #print(click_object_error)
        logging.info(click_object_error)
        
        return DECIDE_STATUS.COMPARE_NO_BASE_OBJECT
    # 
#


# 根据基准图片，比较相同位置的截图
def compare_object(object_name, match_value = 20):
    # 
    func_infor = sys._getframe().f_code.co_name
    
    infor = '>>>> %s, 检测基准对象 [%s]' % (func_infor, object_name)
    #print(infor)
    logging.info(infor)
    
    status = DECIDE_STATUS.UNKNOWN
    file_name = ''
    
    # object_name 可构建路径及对比目标 # 比较匹配图片的路径规则为 \object_name\0\
    bmp_path = '.\\' + object_name + '\\0\\'
    # 根据 name_* 获取相应文件
    pre_name = object_name + '_'
    list_file_name = search_bmp_file_list(bmp_path, pre_name)
    ##print(list_file_name)
    if list_file_name:
        for file_name in list_file_name:          
            # 截图比较相似度 
            ret, l, t, r, b = is_grab_match(bmp_path, file_name, match_value)
            if ret:
                #click_object_infor = '%s, 比较 [%s] 相似通过' % (func_infor, object_name)
                ##print(click_object_infor)
                #logging.info(click_object_infor)
                
                # 比较相似，则认为可以返回了
                status = DECIDE_STATUS.COMPARE_MATCH
                break
            else:    
                #click_object_infor = '%s, 比较 [%s] 不相似未通过' % (func_infor, object_name)
                ##print(click_object_infor)
                #logging.info(click_object_infor)
                
                status = DECIDE_STATUS.COMPARE_NOT_MATCH
    else:
        # 未有BMP文件
        #click_object_error = '%s, 无有效的检测基准对象 [%s]' % (func_infor, object_name)
        ##print(click_object_error)
        #logging.info(click_object_error)
        
        status = DECIDE_STATUS.COMPARE_NO_BASE_OBJECT
    
    #
    infor = '%s, 检测基准对象 [%s],  status = %s' % (func_infor, file_name, status)
    #print(infor)
    logging.info(infor)
    
    return status, file_name
    # 
#



# 根据指定路径上的基准图片，比较相同位置的截图
def compare_object_with_path(bmp_path, object_name):
    # 
    func_infor = sys._getframe().f_code.co_name
    
    infor = '>>>> %s, 检测基准对象 [%s]' % (func_infor, bmp_path+object_name)
    #print(infor)
    logging.info(infor)
    
    status = DECIDE_STATUS.UNKNOWN
    file_name = ''
    
    # 根据 name_* 获取相应文件
    pre_name = object_name #+ '_'
    list_file_name = search_bmp_file_list(bmp_path, pre_name)
    ##print(list_file_name)
    if list_file_name:
        for file_name in list_file_name:          
            # 截图比较相似度 
            ret, l, t, r, b = is_grab_match_auto_value(bmp_path, file_name)
            if ret:
                # 比较相似，则认为可以返回了
                status = DECIDE_STATUS.COMPARE_MATCH
                break
            else:
                status = DECIDE_STATUS.COMPARE_NOT_MATCH
    else:
        status = DECIDE_STATUS.COMPARE_NO_BASE_OBJECT
    
    #
    infor = '%s, 检测基准对象 [%s],  status = %s' % (func_infor, file_name, status)
    #print(infor)
    logging.info(infor)
    
    return status, file_name
    # 
#
