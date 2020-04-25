

import sys
import logging
import win32gui
from click_object import *


# 显示窗口
def display_game(window_title):
    #
    display_game_infor = '>>>> %s, 显示 [%s] 窗口' % (sys._getframe().f_code.co_name, window_title)
    print(display_game_infor)
    logging.info(display_game_infor)
        
    # 获取窗口句柄
    handle = win32gui.FindWindow(0, window_title)  
    if handle == 0:
        # 未获取到指定窗口
        no_find_window_infor = '未找到[%s]窗口' % window_title
        print(no_find_window_infor)
        logging.error(no_find_window_infor)
    
    # 窗口置前
    win32gui.SetForegroundWindow(handle)
#


# 点击首个任务位置
def click_first_row_task():
    #
    object_name = '第一栏任务'
    
    infor = '>>>> %s, 点击 [%s]' % (sys._getframe().f_code.co_name, object_name)
    print(infor)
    logging.info(infor)
    
    click_object(object_name)
#


# 点击技能按钮
def click_skill_button():
    #
    object_name = '技能按钮'
    
    infor = '>>>> %s, 点击 [%s]' % (sys._getframe().f_code.co_name, object_name)
    print(infor)
    logging.info(infor)
    
    click_object_by_multi(object_name)
#


# 点击一键升级按钮
def click_one_key_to_upgrade_button():
    #
    object_name = '一键升级按钮'
    
    infor = '>>>> %s, 点击 [%s]' % (sys._getframe().f_code.co_name, object_name)
    print(infor)
    logging.info(infor)
    
    click_object_by_multi(object_name)
#


# 点击人物技能窗口关闭按钮
def click_skill_window_close_button():
    #
    object_name = '人物技能窗口关闭按钮'
    
    infor = '>>>> %s, 点击 [%s]' % (sys._getframe().f_code.co_name, object_name)
    print(infor)
    logging.info(infor)
    
    click_object_by_multi(object_name)
#


# 点击任意地方继续
def click_anywhere_continue():
    #
    object_name = '点击继续'
    
    infor = '>>>> %s, 点击 [%s]' % (sys._getframe().f_code.co_name, object_name)
    print(infor)
    logging.info(infor)
    
    click_object(object_name)
#


# 设置目标窗口到预设位置、尺寸
# 直接调用一个py运行
import os

def set_game_coordinate():
    #
    object_name = '预设游戏窗口'
    
    infor = '>>>> %s, %s' % (sys._getframe().f_code.co_name, object_name)
    print(infor)
    logging.info(infor)
    
    # python命令 + *.py 
    str = ('python set_game_coordinate.py')   
    ret =os.system(str)
    
    # 打印执行结果 0表示 success ， 1表示 fail
    print('执行结果 [0表示 success ， 1表示 fail] : ', end = '')
    print(ret)    
#


# 自动执行游戏操作
#from auto_play_game_implement import auto_play_game_implement

def auto_play_game():
    # 
    object_name = '自动执行'
    
    global is_start
    is_start = True
    
    infor = '>>>> %s, %s : %s' % (sys._getframe().f_code.co_name, object_name, is_start)
    print(infor)
    logging.info(infor)
    
    auto_play_game_implement()
#


# 停止自动执行
def stop_play_game():
    # 
    object_name = '停止自动执行'
    
    global is_start
    is_start = False
    
    infor = '>>>> %s, %s : %s' % (sys._getframe().f_code.co_name, object_name, is_start)
    print(infor)
    logging.info(infor)
#


# 检测当前是否在自动执行状态中
def is_auto_play_game():
    # 
    object_name = '是否自动执行中'
    
    global is_start
    
    infor = '>>>> %s, %s : %s' % (sys._getframe().f_code.co_name, object_name, is_start)
    print(infor)
    logging.info(infor)
#


# 点击一个NPC选项的首项
def click_first_of_one_npc_response():
    #
    object_name = '一个NPC选项的首项'
    
    infor = '>>>> %s, 点击 [%s]' % (sys._getframe().f_code.co_name, object_name)
    print(infor)
    logging.info(infor)
    
    click_object(object_name)
#


# 点击使用任务道具
def click_use_task_goods():
    #
    object_name = '使用任务道具'
    
    infor = '>>>> %s, 点击 [%s]' % (sys._getframe().f_code.co_name, object_name)
    print(infor)
    logging.info(infor)
    
    click_object(object_name)
#


# 点击星宿手册关闭按钮
def click_popup_xingxiushouce_window_close():
    #
    object_name = '星宿手册关闭'
    
    infor = '>>>> %s, 点击 [%s]' % (sys._getframe().f_code.co_name, object_name)
    print(infor)
    logging.info(infor)
    
    click_object(object_name)
#


# 点击五个NPC选项的首项
def click_first_of_five_npc_response():
    #
    object_name = '五个NPC选项的首项'
    
    infor = '>>>> %s, 点击 [%s]' % (sys._getframe().f_code.co_name, object_name)
    print(infor)
    logging.info(infor)
    
    click_object(object_name)
#


# 点击第二个任务位置
def click_second_row_task():
    #
    object_name = '第二栏任务'
    
    infor = '>>>> %s, 点击 [%s]' % (sys._getframe().f_code.co_name, object_name)
    print(infor)
    logging.info(infor)
    
    click_object(object_name)
#


# 点击自动选择每日任务
def click_auto_select_teacher_task():
    #
    object_name = '自动选择每日任务'
    
    infor = '>>>> %s, 点击 [%s]' % (sys._getframe().f_code.co_name, object_name)
    print(infor)
    logging.info(infor)
    
    click_object(object_name)
#


# 点击师门任务选择
def click_select_teacher_task():
    #
    object_name = '师门任务选择'
    
    infor = '>>>> %s, 点击 [%s]' % (sys._getframe().f_code.co_name, object_name)
    print(infor)
    logging.info(infor)
    
    click_object(object_name)
#
#

#
#
#
################# 自动执行脚本的相关逻辑判定 ############################
from compare_object import *
from base_status_infor import *



# 人物是否在移动中
def is_moving():
    #
    func_infor = sys._getframe().f_code.co_name
    object_name = '人物坐标'
    
    infor = '>>>> %s, 判定 [%s] 是否变动' % (func_infor, object_name)
    print(infor)
    logging.info(infor)
    
    #检测对比截图 #### match_value = 20, sleep_time = 2
    match_value = 20
    sleep_time = 2
    status = compare_two_dynamic_object_change(object_name, match_value, sleep_time)
    if DECIDE_STATUS.COMPARE_MATCH == status:
        infor = '%s, [%s] 未移动, status = %s' % (func_infor, object_name, status)
        print(infor)
        logging.info(infor)
        return DECIDE_STATUS.FALSE
        
    if DECIDE_STATUS.COMPARE_NOT_MATCH == status:
        infor = '%s, [%s] 移动中......, status = %s' % (func_infor, object_name, status)
        print(infor)
        logging.info(infor)
        return DECIDE_STATUS.TRUE

    infor = '%s, [%s] ???, status = %s' % (func_infor, object_name, status)
    print(infor)
    logging.info(infor)        
    return DECIDE_STATUS.UNKNOWN
#


# 是否在NPC问答中
def is_npc_ask():
    #
    func_infor = sys._getframe().f_code.co_name
    object_name = 'NPC问答'
    
    infor = '>>>> %s, 判定 [%s]' % (func_infor, object_name)
    print(infor)
    logging.info(infor)
    
    #检测对比截图
    match_value = 20
    status = compare_object(object_name, match_value)
    if DECIDE_STATUS.COMPARE_MATCH == status:
        infor = '%s, [%s] NPC 问答中......, status = %s' % (func_infor, object_name, status)
        print(infor)
        logging.info(infor)
        return DECIDE_STATUS.TRUE
        
    if DECIDE_STATUS.COMPARE_NOT_MATCH == status:
        infor = '%s, [%s] NPC 未问答, status = %s' % (func_infor, object_name, status)
        print(infor)
        logging.info(infor)
        return DECIDE_STATUS.FALSE
        
    infor = '%s, [%s] ???, status = %s' % (func_infor, object_name, status)
    print(infor)
    logging.info(infor)        
    return DECIDE_STATUS.UNKNOWN
#


# 一个NPC选项
def is_one_npc_response():  
    #
    func_infor = sys._getframe().f_code.co_name
    object_name = '一个NPC选项'
    
    infor = '>>>> %s, 判定 [%s]' % (func_infor, object_name)
    print(infor)
    logging.info(infor)
    
    #检测对比截图
    match_value = 10
    status = compare_object(object_name, match_value)
    if DECIDE_STATUS.COMPARE_MATCH == status:
        infor = '%s, [%s] 正确' % (func_infor, object_name)
        print(infor)
        logging.info(infor)
        return DECIDE_STATUS.TRUE
    
    if DECIDE_STATUS.COMPARE_NOT_MATCH == status:
        infor = '%s, [%s] 错误, status = %s' % (func_infor, object_name, status)
        print(infor)
        logging.info(infor)
        return DECIDE_STATUS.FALSE
    
    infor = '%s, [%s] ???, status = %s' % (func_infor, object_name, status)
    print(infor)
    logging.info(infor)        
    return DECIDE_STATUS.UNKNOWN
#


# 是否是点击任意地方继续剧情界面
def is_anywhere_click():
    #
    func_infor = sys._getframe().f_code.co_name
    object_name = '点击继续'
    
    infor = '>>>> %s, 判定 [%s]' % (func_infor, object_name)
    print(infor)
    logging.info(infor)
    
    #检测对比截图
    match_value = 20
    status = compare_object(object_name, match_value)
    if DECIDE_STATUS.COMPARE_MATCH == status:
        infor = '%s, [%s] 正确' % (func_infor, object_name)
        print(infor)
        logging.info(infor)
        return DECIDE_STATUS.TRUE
    
    if DECIDE_STATUS.COMPARE_NOT_MATCH == status:
        infor = '%s, [%s] 错误, status = %s' % (func_infor, object_name, status)
        print(infor)
        logging.info(infor)
        return DECIDE_STATUS.FALSE
    
    infor = '%s, [%s] ???, status = %s' % (func_infor, object_name, status)
    print(infor)
    logging.info(infor)        
    return DECIDE_STATUS.UNKNOWN
#


# 是否有任务物品需要使用
def is_use_task_goods():
    #
    func_infor = sys._getframe().f_code.co_name
    object_name = '使用任务道具'
    
    infor = '>>>> %s, 判定 [%s]' % (func_infor, object_name)
    print(infor)
    logging.info(infor)
    
    #检测对比截图
    match_value = 20
    status = compare_object(object_name, match_value)
    if DECIDE_STATUS.COMPARE_MATCH == status:
        infor = '%s, [%s] 正确' % (func_infor, object_name)
        print(infor)
        logging.info(infor)
        return DECIDE_STATUS.TRUE
    
    if DECIDE_STATUS.COMPARE_NOT_MATCH == status:
        infor = '%s, [%s] 错误, status = %s' % (func_infor, object_name, status)
        print(infor)
        logging.info(infor)
        return DECIDE_STATUS.FALSE
    
    infor = '%s, [%s] ???, status = %s' % (func_infor, object_name, status)
    print(infor)
    logging.info(infor)        
    return DECIDE_STATUS.UNKNOWN
#


# 是否咕噜味叽哩对话
def is_gulu_jili_ask():
    #
    func_infor = sys._getframe().f_code.co_name
    object_name = '咕噜咕噜'
    
    infor = '>>>> %s, 判定 [%s]' % (func_infor, object_name)
    print(infor)
    logging.info(infor)
    
    #检测对比截图
    match_value = 20
    status = compare_object(object_name, match_value)
    if DECIDE_STATUS.COMPARE_MATCH == status:
        infor = '%s, [%s] 正确' % (func_infor, object_name)
        print(infor)
        logging.info(infor)
        return DECIDE_STATUS.TRUE
    
    if DECIDE_STATUS.COMPARE_NOT_MATCH == status:
        infor = '%s, [%s] 错误, status = %s' % (func_infor, object_name, status)
        print(infor)
        logging.info(infor)
        return DECIDE_STATUS.FALSE
    
    infor = '%s, [%s] ???, status = %s' % (func_infor, object_name, status)
    print(infor)
    logging.info(infor)        
    return DECIDE_STATUS.UNKNOWN
#


# 是星宿手册窗口
def is_popup_xingxiushouce_window():
    #
    func_infor = sys._getframe().f_code.co_name
    object_name = '星宿手册'
    
    infor = '>>>> %s, 判定 [%s]' % (func_infor, object_name)
    print(infor)
    logging.info(infor)
    
    #检测对比截图
    match_value = 20
    status = compare_object(object_name, match_value)
    if DECIDE_STATUS.COMPARE_MATCH == status:
        infor = '%s, [%s] 正确' % (func_infor, object_name)
        print(infor)
        logging.info(infor)
        return DECIDE_STATUS.TRUE
    
    if DECIDE_STATUS.COMPARE_NOT_MATCH == status:
        infor = '%s, [%s] 错误, status = %s' % (func_infor, object_name, status)
        print(infor)
        logging.info(infor)
        return DECIDE_STATUS.FALSE
    
    infor = '%s, [%s] ???, status = %s' % (func_infor, object_name, status)
    print(infor)
    logging.info(infor)        
    return DECIDE_STATUS.UNKNOWN
#


# 五个NPC选项
def is_five_npc_response():  
    #
    func_infor = sys._getframe().f_code.co_name
    object_name = '五个NPC选项'
    
    infor = '>>>> %s, 判定 [%s]' % (func_infor, object_name)
    print(infor)
    logging.info(infor)
    
    #检测对比截图
    match_value = 10
    status = compare_object(object_name, match_value)
    if DECIDE_STATUS.COMPARE_MATCH == status:
        infor = '%s, [%s] 正确' % (func_infor, object_name)
        print(infor)
        logging.info(infor)
        return DECIDE_STATUS.TRUE
    
    if DECIDE_STATUS.COMPARE_NOT_MATCH == status:
        infor = '%s, [%s] 错误, status = %s' % (func_infor, object_name, status)
        print(infor)
        logging.info(infor)
        return DECIDE_STATUS.FALSE
    
    infor = '%s, [%s] ???, status = %s' % (func_infor, object_name, status)
    print(infor)
    logging.info(infor)        
    return DECIDE_STATUS.UNKNOWN
#


# 达到20级开启新剧情
def is_20_new_task():  
    #
    func_infor = sys._getframe().f_code.co_name
    object_name = '达到20级开启新剧情'
    
    infor = '>>>> %s, 判定 [%s]' % (func_infor, object_name)
    print(infor)
    logging.info(infor)
    
    #检测对比截图
    match_value = 20
    status = compare_object(object_name, match_value)
    if DECIDE_STATUS.COMPARE_MATCH == status:
        infor = '%s, [%s] 正确' % (func_infor, object_name)
        print(infor)
        logging.info(infor)
        return DECIDE_STATUS.TRUE
    
    if DECIDE_STATUS.COMPARE_NOT_MATCH == status:
        infor = '%s, [%s] 错误, status = %s' % (func_infor, object_name, status)
        print(infor)
        logging.info(infor)
        return DECIDE_STATUS.FALSE
    
    infor = '%s, [%s] ???, status = %s' % (func_infor, object_name, status)
    print(infor)
    logging.info(infor)        
    return DECIDE_STATUS.UNKNOWN
#


# 是否自动选择每日任务
def is_auto_select_teacher_task():  
    #
    func_infor = sys._getframe().f_code.co_name
    object_name = '自动选择每日任务'
    
    infor = '>>>> %s, 判定 [%s]' % (func_infor, object_name)
    print(infor)
    logging.info(infor)
    
    #检测对比截图
    match_value = 20
    status = compare_object(object_name, match_value)
    if DECIDE_STATUS.COMPARE_MATCH == status:
        infor = '%s, [%s] 正确' % (func_infor, object_name)
        print(infor)
        logging.info(infor)
        return DECIDE_STATUS.TRUE
    
    if DECIDE_STATUS.COMPARE_NOT_MATCH == status:
        infor = '%s, [%s] 错误, status = %s' % (func_infor, object_name, status)
        print(infor)
        logging.info(infor)
        return DECIDE_STATUS.FALSE
    
    infor = '%s, [%s] ???, status = %s' % (func_infor, object_name, status)
    print(infor)
    logging.info(infor)        
    return DECIDE_STATUS.UNKNOWN
#

# 是否师门每周任务
def is_select_teacher_task_window():  
    #
    func_infor = sys._getframe().f_code.co_name
    object_name = '师门每周任务'
    
    infor = '>>>> %s, 判定 [%s]' % (func_infor, object_name)
    print(infor)
    logging.info(infor)
    
    #检测对比截图
    match_value = 20
    status = compare_object(object_name, match_value)
    if DECIDE_STATUS.COMPARE_MATCH == status:
        infor = '%s, [%s] 正确' % (func_infor, object_name)
        print(infor)
        logging.info(infor)
        return DECIDE_STATUS.TRUE
    
    if DECIDE_STATUS.COMPARE_NOT_MATCH == status:
        infor = '%s, [%s] 错误, status = %s' % (func_infor, object_name, status)
        print(infor)
        logging.info(infor)
        return DECIDE_STATUS.FALSE
    
    infor = '%s, [%s] ???, status = %s' % (func_infor, object_name, status)
    print(infor)
    logging.info(infor)        
    return DECIDE_STATUS.UNKNOWN
#

#

#
#
#

#



################# 自动执行脚本的具体实际实现  ############################
def auto_play_game_implement():
    # 
    func_infor = sys._getframe().f_code.co_name
    
    continuous_click_first_row_task_count = 0
    global is_start
    while is_start:
        # 标记当前状态
        status = DECIDE_STATUS.FALSE
        ################################################
        # 检测是否在 移动 过程中
        status = is_moving()
        while DECIDE_STATUS.TRUE == status:
            # 
            infor = '%s, 人物在移动中......' % (func_infor)
            print(infor)
            logging.info(infor)
            
            status = is_moving()
            continue
        #
        if DECIDE_STATUS.UNKNOWN == status:
            infor = '%s, 我不知道该做什么了？' % (func_infor)
            print(infor)
            logging.info(infor)
            
            time.sleep(30)
            # 未知状态，触发报警
        ################################################
        # 检测是否在 NPC问答 中
        npc_ask_count = 0
        status = is_npc_ask()
        while DECIDE_STATUS.TRUE == status:
            # 
            infor = '%s, NPC问答中......' % (func_infor)
            print(infor)
            logging.info(infor)
            
            npc_ask_count += 1
            # NPC问答 次数超限，需要退出 NPC问答 循环
            if npc_ask_count > 10:
                infor = '%s, NPC问答 次数超限[%d]，需要退出 NPC问答 循环' % (func_infor, npc_ask_count)
                print(infor)
                logging.info(infor)
                break
            
            # 是否只有一个NPC选项
            status = is_one_npc_response()
            if DECIDE_STATUS.TRUE == status:
                # 点击一个NPC选项的首位置
                click_first_of_one_npc_response()
                # 重置连续点击任务计数
                continuous_click_first_row_task_count = 0   

            # 是否只有五个NPC选项
            status = is_five_npc_response()
            if DECIDE_STATUS.TRUE == status:
                # 点击一个NPC选项的首位置
                click_first_of_five_npc_response()
                # 重置连续点击任务计数
                continuous_click_first_row_task_count = 0                  
            
            status = is_npc_ask()
            continue
        #
        if DECIDE_STATUS.UNKNOWN == status:
            infor = '%s, 我不知道该做什么了？' % (func_infor)
            print(infor)
            logging.info(infor)
            
            time.sleep(30)
            # 未知状态，触发报警
        ################################################
        # 检测是否在 点击任意地方继续 中  该种界面会自动消息,不用进行循环计数.
        status = is_anywhere_click()
        while DECIDE_STATUS.TRUE == status:
            # 
            infor = '%s, 点击任意地方继续中......' % (func_infor)
            print(infor)
            logging.info(infor)
            
            # 点击继续
            click_anywhere_continue()
            # 重置连续点击任务计数
            continuous_click_first_row_task_count = 0
            
            status = is_anywhere_click()
            continue
        #
        if DECIDE_STATUS.UNKNOWN == status:
            infor = '%s, 我不知道该做什么了？' % (func_infor)
            print(infor)
            logging.info(infor)
            
            time.sleep(30)
            # 未知状态，触发报警    
        #
        #
        #
        infor = '%s, ???????????????? ' % (func_infor)
        print(infor)
        logging.info(infor)

        # 连续点击第一任务栏 10 次都无任何动作时
        if continuous_click_first_row_task_count > 10:
            # 
            infor = '%s, 我已经连续点击第一任务栏 10 次都好像无任何推动' % (func_infor)
            print(infor)
            logging.info(infor)
            
            # 较少出现的场景放于此处判断,且使用 IF 条件判定
            ################################################
            # 检测是否 需要使用任务道具 
            status = is_use_task_goods()
            if DECIDE_STATUS.TRUE == status:
                # 
                infor = '%s, 点击使用任务道具中......' % (func_infor)
                print(infor)
                logging.info(infor)
                
                # 点击使用任务道具
                click_use_task_goods()
                # 重置连续点击任务计数
                continuous_click_first_row_task_count = 0
            #
            if DECIDE_STATUS.UNKNOWN == status:
                infor = '%s, 我不知道该做什么了？' % (func_infor)
                print(infor)
                logging.info(infor)
                
                time.sleep(30)
                # 未知状态，触发报警    
            ################################################
            # 检测是否 咕噜味叽哩对话 
            status = is_gulu_jili_ask()
            if DECIDE_STATUS.TRUE == status:
                # 
                infor = '%s, 点击咕噜味叽哩对话中......' % (func_infor)
                print(infor)
                logging.info(infor)
                
                # 使用点击第一栏任务产生点击效果
                click_first_row_task()
                # 重置连续点击任务计数
                continuous_click_first_row_task_count = 0
            #
            if DECIDE_STATUS.UNKNOWN == status:
                infor = '%s, 我不知道该做什么了？' % (func_infor)
                print(infor)
                logging.info(infor)
                
                time.sleep(30)
                # 未知状态，触发报警    
            ################################################
            # 检测是否 达到20级开启新剧情 
            status = is_20_new_task()
            if DECIDE_STATUS.TRUE == status:
                # 
                infor = '%s, 检测达到20级开启新剧情中......' % (func_infor)
                print(infor)
                logging.info(infor)
                
                # 点击第二栏任务
                click_second_row_task()
                # 重置连续点击任务计数
                continuous_click_first_row_task_count = 0
            #
            if DECIDE_STATUS.UNKNOWN == status:
                infor = '%s, 我不知道该做什么了？' % (func_infor)
                print(infor)
                logging.info(infor)
                
                time.sleep(30)
                # 未知状态，触发报警 
            ################################################
            # 检测是否 师门任务选择 
            status = is_select_teacher_task_window()
            if DECIDE_STATUS.TRUE == status:
                # 
                infor = '%s, 点击师门任务选择中......' % (func_infor)
                print(infor)
                logging.info(infor)
                
                # 点击师门任务选择
                click_select_teacher_task()
                # 重置连续点击任务计数
                continuous_click_first_row_task_count = 0
            #
            if DECIDE_STATUS.UNKNOWN == status:
                infor = '%s, 我不知道该做什么了？' % (func_infor)
                print(infor)
                logging.info(infor)
                
                time.sleep(30)
                # 未知状态，触发报警                
            ################################################
            # 检测是否 星宿手册窗口 
            status = is_popup_xingxiushouce_window()
            if DECIDE_STATUS.TRUE == status:
                # 
                infor = '%s, 点击星宿手册窗口关闭按钮中......' % (func_infor)
                print(infor)
                logging.info(infor)
                
                # 点击星宿手册窗口关闭按钮
                click_popup_xingxiushouce_window_close()
                # 重置连续点击任务计数
                continuous_click_first_row_task_count = 0
            #
            if DECIDE_STATUS.UNKNOWN == status:
                infor = '%s, 我不知道该做什么了？' % (func_infor)
                print(infor)
                logging.info(infor)
                
                time.sleep(30)
                # 未知状态，触发报警    
            #
            
            # 停止自动执行 最好再保存一个现场快照
            if continuous_click_first_row_task_count > 10:
                break
        # 
        # 默认动作 点击 第一任务栏
        click_first_row_task()
        continuous_click_first_row_task_count += 1
#