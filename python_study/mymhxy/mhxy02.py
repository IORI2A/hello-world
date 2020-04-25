

import tkinter as tk
import logging
from my_thread import MyThread
from call_back_operation_02 import *
from teacher_task import *


# 配置日志记录
logging.basicConfig(filename="mhxy.log", filemode="w", format="%(asctime)s %(levelname)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S", level=logging.DEBUG)


if __name__ == "__main__":
    # 创建主窗口
    root = tk.Tk()
    root.title("黑鹰坠落")

    button = tk.Button(root,text='显示游戏窗口', command=lambda: MyThread(display_game, '《梦幻西游》手游'))
    button.pack()
    
    button = tk.Button(root,text='预设游戏窗口', command=lambda: MyThread(set_game_coordinate))
    button.pack()

    button = tk.Button(root,text='TEST', command=lambda: MyThread(test_func))
    button.pack()
    
    button = tk.Button(root,text='师门任务', command=lambda: MyThread(teacher_task))
    button.pack()
    
    button = tk.Button(root,text='点击', command=lambda: MyThread(click_button_callback))
    button.pack()
    
    button = tk.Button(root,text='比较点击', command=lambda: MyThread(compare_and_click_button_callback))
    button.pack()
    
    button = tk.Button(root,text='移动中?', command=lambda: MyThread(move_check_button_callback))
    button.pack()
    
    button = tk.Button(root,text='自动比较点击', command=lambda: MyThread(auto_compare_and_click_button_callback))
    button.pack()
    
    button = tk.Button(root,text='停止', command=lambda: MyThread(stop_button_callback))
    button.pack()
    
    # 窗口显示运行
    root.mainloop()



