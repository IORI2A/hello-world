

import logging
import win32api
import win32con
import time
import random
import sys



# 移动鼠标并点击左键
def mouse_move_click(screen_x, screen_y, sleep_time = 0):
    # 
    func_infor = sys._getframe().f_code.co_name
    
    #
    #mouse_move_click_infor = 'mouse_move_click(%d, %d)' % (screen_x, screen_y)
    ##print(mouse_move_click_infor)
    #logging.info(mouse_move_click_infor)
    
    # 设置鼠标位置(x, y)
    win32api.SetCursorPos((screen_x, screen_y))
    time.sleep(0.1+random.random())
    
    # 点击鼠标左键
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, screen_x, screen_y, 0, 0)  

    # random() 方法返回随机生成的一个实数，它在[0,1)范围内。
    if sleep_time == 0:
        sleep_multiple = 1
        t = 0.2
        sleep_time = random.random()*sleep_multiple+t
    sleep_infor = "%s, 鼠标点击(%d, %d)，睡眠时长: %f" % (func_infor, screen_x, screen_y, sleep_time)
    #print(sleep_infor)
    logging.info(sleep_infor)
    time.sleep(sleep_time)
#