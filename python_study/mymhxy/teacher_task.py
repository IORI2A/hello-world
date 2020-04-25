


import sys
import logging
import time
from click_object_02 import *
from compare_object_02 import *
from base_status_infor import *


def teacher_task():
    #
    func_infor = sys._getframe().f_code.co_name
    
    compare_bmp_path = '.\\师门任务\\0\\'
    click_bmp_path = '.\\师门任务\\1\\'
    
    #infor = '>>>> %s, 检测[%s], 点击[%s]' % (func_infor, compare_object_name, click_object_name)
    #print(infor)
    #logging.info(infor)
    
    # 点击任务栏中的师门任务
    time.sleep(1)
    object_name = '任务栏中的师门任务'
    status, file_name = compare_object_with_path(compare_bmp_path, object_name, 20) 
    if DECIDE_STATUS.COMPARE_MATCH == status:
        click_object_with_path(click_bmp_path, object_name, 100)
        
    # 选择师门任务窗口进行点击选择
    time.sleep(1)
    object_name = '选择师门任务窗口'
    status, file_name = compare_object_with_path(compare_bmp_path, object_name, 20) 
    if DECIDE_STATUS.COMPARE_MATCH == status:
        click_object_with_path(click_bmp_path, object_name, 20)
        
    # 师门任务中NPC问答
    time.sleep(1)
    object_name = 'NPC问答'
    status, file_name = compare_object_with_path(compare_bmp_path, object_name, 20) 
    if DECIDE_STATUS.COMPARE_MATCH == status:
        click_object_with_path(click_bmp_path, object_name, 100)
#
#