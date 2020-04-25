

import os
import sys
import logging
import win32gui
from click_object_02 import *
from compare_object_02 import *
from base_status_infor import *

# 显示窗口
def display_game(window_title):
    #
    display_game_infor = '>>>> %s, 显示 [%s] 窗口' % (sys._getframe().f_code.co_name, window_title)
    #print(display_game_infor)
    logging.info(display_game_infor)
        
    # 获取窗口句柄
    handle = win32gui.FindWindow(0, window_title)  
    if handle == 0:
        # 未获取到指定窗口
        no_find_window_infor = '未找到[%s]窗口' % window_title
        #print(no_find_window_infor)
        logging.error(no_find_window_infor)
    
    # 窗口置前
    win32gui.SetForegroundWindow(handle)
#


# 设置目标窗口到预设位置、尺寸
# 直接调用一个py运行
def set_game_coordinate():
    #
    object_name = '预设游戏窗口'
    
    infor = '>>>> %s, %s' % (sys._getframe().f_code.co_name, object_name)
    #print(infor)
    logging.info(infor)
    
    # python命令 + *.py 
    str = ('python set_game_coordinate.py')   
    ret =os.system(str)
    
    # 打印执行结果 0表示 success ， 1表示 fail
    #print('执行结果 [0表示 success ， 1表示 fail] : ', end = '')
    #print(ret)    
#


#
def compare_and_click_path_obj(bmp_path, object_name):
    #
    func_infor = sys._getframe().f_code.co_name

    infor = '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> %s, [%s]' % (func_infor, object_name)
    #print(infor)
    logging.info(infor)
    
    #
    status, file_name = compare_object_with_path(bmp_path + '\\0\\', object_name)
    if DECIDE_STATUS.COMPARE_MATCH == status:
        # 001.NPC问答.756_419_908_439_20.bmp
        list = file_name.split('.')
        #print(list)        
        click_object_name = list[1]
        click_success = click_object_with_path_by_multi_auto_value(bmp_path + '\\1\\', click_object_name)
        if not click_success:
            # 点击自身
            #print('>>>> %s, 点击自身' % (func_infor))
            click_object(bmp_path + '\\0\\', click_object_name)
            while DECIDE_STATUS.TRUE == is_moving(bmp_path + '\\0\\move\\'):
                continue
                
    return status
#


def click_path_obj(bmp_path, object_name):
    #
    func_infor = sys._getframe().f_code.co_name
    
    infor = '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> %s, [%s]' % (func_infor, object_name)
    #print(infor)
    logging.info(infor)

    click_object_with_path_by_multi_auto_value(bmp_path, object_name)
#


#
def test_func():
    #
    func_infor = sys._getframe().f_code.co_name
    
    infor = '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> %s' % (func_infor)
    #print(infor)
    logging.info(infor)
    
    object_name = 'object'
    #compare_and_click(object_name)
    click_object_with_path_by_multi_auto_value('.\\object\\', object_name)
#

#
def click_button_callback():
    #
    func_infor = sys._getframe().f_code.co_name
    
    infor = '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> %s' % (func_infor)
    #print(infor)
    logging.info(infor)
    
    bmp_path = '.\\ob\\'
    object_name = 'ob'
    click_path_obj(bmp_path, object_name)
#


#
def compare_and_click_button_callback():
    #
    func_infor = sys._getframe().f_code.co_name
    
    infor = '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> %s' % (func_infor)
    #print(infor)
    logging.info(infor)
    
    bmp_path = '.\\ob\\'
    object_name = 'ob'
    compare_and_click_path_obj(bmp_path, object_name)
#


# 
def move_check_button_callback():
    #
    func_infor = sys._getframe().f_code.co_name
    
    infor = '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> %s' % (func_infor)
    #print(infor)
    logging.info(infor)
    
    status = is_moving('.\\ob\\0\\move\\')
    if DECIDE_STATUS.TRUE == status:
        infor = '%s, 移动中......' % (func_infor)
    else:
        infor = '%s, 未移动, status = %s' % (func_infor, status)
    
    #print(infor)
    logging.info(infor)
#


#
def auto_compare_and_click_button_callback():
    #
    func_infor = sys._getframe().f_code.co_name
    
    bmp_path = '.\\ob\\'
    object_name = 'ob'
    
    global keep_while
    keep_while = True
    while_count = 0
    while keep_while:
        infor = '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> %s, 连续循环次数 %d' % (func_infor, while_count+1)
        #print(infor)
        logging.info(infor)
    
        status = compare_and_click_path_obj(bmp_path, object_name)
        if DECIDE_STATUS.COMPARE_MATCH == status:
            while_count = 0
        else:
            while_count += 1
            
        if while_count >= 6:
            break
#


#
def stop_button_callback():
    #
    func_infor = sys._getframe().f_code.co_name
    
    global keep_while
    keep_while = False
    
    infor = '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> %s, keep_while = %s' % (func_infor, keep_while)
    #print(infor)
    logging.info(infor)
#
#