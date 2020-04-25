

import logging
import sys 
from file_operation import *
from image_operation import *
from base_status_infor import *



# 比较同一位置的不同时点的两张截图
# match_value 越小，要求越相似
def compare_two_dynamic_object_change(object_name, match_value = 20, sleep_time = 1):
    # 
    func_infor = sys._getframe().f_code.co_name
    
    # 
    pre_name = object_name + '_'
    list_file_name = search_bmp_file_list(pre_name)
    #print(list_file_name)
    if list_file_name:
        # 遍历直至成功或最后元素
        for file_name in list_file_name:          
            # 截图比较相似度  #### 一些参数值暂时固定
            #value = 20
            #sleep_time = 2
            ret, l, t, r, b = is_grab_two_match(file_name, match_value, sleep_time)
            if ret:
                click_object_infor = '%s, 比较 [%s] 无变动' % (func_infor, object_name)
                print(click_object_infor)
                logging.info(click_object_infor)
                
                return DECIDE_STATUS.COMPARE_MATCH
            else:    
                click_object_infor = '%s, 比较 [%s] 在变动中' % (func_infor, object_name)
                print(click_object_infor)
                logging.info(click_object_infor)
                
                return DECIDE_STATUS.COMPARE_NOT_MATCH
    else:
        # 未有BMP文件直接返回
        click_object_error = '%s, 无有效的检测基准对象 [%s]' % (func_infor, object_name)
        print(click_object_error)
        logging.info(click_object_error)
        
        return DECIDE_STATUS.COMPARE_NO_BASE_OBJECT
    # 
#


# 根据基准图片，比较相同位置的截图
def compare_object(object_name, match_value = 20):
    # 
    func_infor = sys._getframe().f_code.co_name
    
    # 
    pre_name = object_name + '_'
    list_file_name = search_bmp_file_list(pre_name)
    #print(list_file_name)
    if list_file_name:
        # 遍历直至成功或最后元素
        for file_name in list_file_name:          
            # 截图比较相似度 
            ret, l, t, r, b = is_grab_match(file_name, match_value)
            if ret:
                click_object_infor = '%s, 比较 [%s] 相似通过' % (func_infor, object_name)
                print(click_object_infor)
                logging.info(click_object_infor)
                
                return DECIDE_STATUS.COMPARE_MATCH
            else:    
                click_object_infor = '%s, 比较 [%s] 不相似未通过' % (func_infor, object_name)
                print(click_object_infor)
                logging.info(click_object_infor)
                
                return DECIDE_STATUS.COMPARE_NOT_MATCH
    else:
        # 未有BMP文件直接返回
        click_object_error = '%s, 无有效的检测基准对象 [%s]' % (func_infor, object_name)
        print(click_object_error)
        logging.info(click_object_error)
        
        return DECIDE_STATUS.COMPARE_NO_BASE_OBJECT
    # 
#
    
#
#
#
#
#