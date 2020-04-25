

import logging
from mouse_action import *
import sys 
from file_operation_02 import *
from string_operation_02 import *
from image_operation_02 import *
from base_status_infor import *
from compare_object_02 import *



# 根据解析首个匹配文件，直接点击对应位置
def click_object(bmp_path, object_name):
    # 
    func_infor = sys._getframe().f_code.co_name
    
    infor = '>>>> %s, 点击基准对象 [%s]' % (func_infor, object_name)
    #print(infor)
    logging.info(infor)
    
    # 根据 name
    file_name = search_bmp_file(bmp_path, object_name)
    
    # 未找到BMP文件直接返回
    if file_name is None:
        infor = '%s, 无有效的点击对象 [%s]' % (func_infor, object_name)
        #print(infor)
        logging.info(infor)
        return None
    # 
    
    # 解析文件名获取左上、右下坐标值 Coordinate
    l, t, r, b = get_coordinate_by_file_name(file_name)
    # 截图保存
    grab_and_save_img(l, t, r, b, bmp_path + '\\click\\', file_name)
    # 计算随机的点击位置
    x = (l+r)//2 + int(random.random()*((r-l)//2))
    y = (t+b)//2 + int(random.random()*((b-t)//2))
    infor = '%s, 点击 [%s]' % (func_infor, file_name)
    #print(infor)
    logging.info(infor)
    mouse_move_click(x, y)
#



# 根据指定路径上的基准图片，比较相同位置的截图
def click_object_with_path(bmp_path, object_name, match_value = 20):
    # 
    func_infor = sys._getframe().f_code.co_name
    
    infor = '>>>> %s, 点击基准对象 [%s]' % (func_infor, object_name)
    #print(infor)
    logging.info(infor)
    
    # 根据 name_* 获取相应文件 如 '第一栏任务坐标_795_144_945_207.bmp'
    pre_name = object_name + '_'
    file_name = search_bmp_file(bmp_path, pre_name)
    
    # 未找到BMP文件直接返回
    if file_name is None:
        infor = '%s, 无有效的点击对象 [%s]' % (func_infor, object_name)
        #print(infor)
        logging.info(infor)
        return None
    # 
    
    # 解析文件名获取左上、右下坐标值 Coordinate
    l, t, r, b = get_coordinate_by_file_name(file_name)
    # 截图保存
    if match_value == 100:
        grab_and_save_img(l, t, r, b, bmp_path, file_name)
    else:
        # 截图比较相似度 
        ret, l, t, r, b = is_grab_match(bmp_path, file_name, match_value)
        if not ret:
            #
            infor = '%s, 点击对象 [%s] 相似度检测失败' % (func_infor, object_name)
            #print(infor)
            logging.info(infor)

            return None
    
    # 计算随机的点击位置
    x = (l+r)//2 + int(random.random()*((r-l)//2))
    y = (t+b)//2 + int(random.random()*((b-t)//2))
    infor = '%s, 点击 [%s]' % (func_infor, file_name)
    #print(infor)
    logging.info(infor)
    mouse_move_click(x, y)
#


# 通过多个图片文件来对比操作
# 根据指定路径上的基准图片，比较相同位置的截图
# 根据多个匹配文件，逐个解析坐标，并截取对应位置图片与基准对比，图片相似才点击对应位置
def click_object_with_path_by_multi_auto_value(bmp_path, object_name):
    # 
    func_infor = sys._getframe().f_code.co_name
    
    infor = '>>>> %s, 点击基准对象 [%s]' % (func_infor, object_name)
    #print(infor)
    logging.info(infor)
    
    # 根据 name 获取相应文件 如 '001.object.756_419_908_439.20.bmp'
    pre_name = object_name # + '_'
    list_file_name = search_bmp_file_list(bmp_path, pre_name)
    ##print(list_file_name)
    click_success = False
    if list_file_name:
        for file_name in list_file_name:          
            # 比较相似才进行点击
            ret, l, t, r, b = is_grab_match_auto_value(bmp_path, file_name)
            if ret:
                x = (l+r)//2 + int(random.random()*((r-l)//2))
                y = (t+b)//2 + int(random.random()*((b-t)//2))
                infor = '%s, 点击 [%s]' % (func_infor, file_name)
                #print(infor)
                logging.info(infor)
                grab_and_save_img(l, t, r, b, bmp_path + '\\click\\', file_name)
                mouse_move_click(x, y)
                click_success = True
                
                if DECIDE_STATUS.TRUE == is_moving(bmp_path + '\\move\\'):
                    while DECIDE_STATUS.TRUE == is_moving(bmp_path + '\\move\\'):
                        continue
                else:
                    return click_success
            #else:    
            #    click_object_infor = '%s, 不点击 [%s]' % (func_infor, name)
            #    #print(click_object_infor)
            #    logging.info(click_object_infor)
    else:
        # 未找到BMP文件直接返回
        infor = '%s, 无有效的点击对象 [%s]' % (func_infor, object_name)
        #print(infor)
        logging.info(infor)  
        click_success = False

    #print(click_success)
    return click_success        
#


# 人物是否在移动中
def is_moving(bmp_path):
    #
    func_infor = sys._getframe().f_code.co_name
    object_name = '人物坐标'
    
    #infor = '>>>> %s, 判定 [%s] 是否变动' % (func_infor, object_name)
    ##print(infor)
    #logging.info(infor)
    
    #检测对比截图
    sleep_time = 1
    status = compare_two_dynamic_object_change(bmp_path, object_name, sleep_time)
    if DECIDE_STATUS.COMPARE_MATCH == status:
        #infor = '%s, [%s] 未移动, status = %s' % (func_infor, object_name, status)
        ##print(infor)
        #logging.info(infor)
        return DECIDE_STATUS.FALSE
        
    if DECIDE_STATUS.COMPARE_NOT_MATCH == status:
        #infor = '%s, [%s] 移动中......, status = %s' % (func_infor, object_name, status)
        ##print(infor)
        #logging.info(infor)
        return DECIDE_STATUS.TRUE

    #infor = '%s, [%s] ???, status = %s' % (func_infor, object_name, status)
    ##print(infor)
    #logging.info(infor)        
    return DECIDE_STATUS.UNKNOWN
#



