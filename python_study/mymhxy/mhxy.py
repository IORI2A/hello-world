

import tkinter as tk
import logging
# import my_thread # 使用其中类时的方式 my_thread.MyThread
from my_thread import MyThread # 使用其中类时的方式 MyThread
from call_back_operation import *


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
    
    button = tk.Button(root,text='**自动执行**', command=lambda: MyThread(auto_play_game))
    button.pack()
    
    button = tk.Button(root,text='**停止自动执行**', command=lambda: MyThread(stop_play_game))
    button.pack()
    
    button = tk.Button(root,text='**是否自动执行中**', command=lambda: MyThread(is_auto_play_game))
    button.pack()
    
    #button = tk.Button(root,text=u"第一个任务", command=lambda: my_thread.MyThread(button_call_back))
    #button = tk.Button(root,text=u"第一个任务", command=lambda: MyThread(button_click_first_task, 100, 100))
    #button = tk.Button(root,text=u"第一个任务", command=lambda: MyThread(click_first_task, 100, 100))
    button = tk.Button(root,text='第一栏任务', command=lambda: MyThread(click_first_row_task))
    button.pack()
    #button_text = '第一栏任务'
    #button = tk.Button(root,text = button_text, command=lambda: MyThread(click_object, button_text))
    #button.pack()
    
    button = tk.Button(root,text='技能按钮', command=lambda: MyThread(click_skill_button))
    button.pack()
    
    button = tk.Button(root,text='一键升级按钮', command=lambda: MyThread(click_one_key_to_upgrade_button))
    button.pack()
    
    button = tk.Button(root,text='人物技能窗口关闭按钮', command=lambda: MyThread(click_skill_window_close_button))
    button.pack()
    
    button = tk.Button(root,text='点击继续', command=lambda: MyThread(click_anywhere_continue))
    button.pack()
    
    button = tk.Button(root,text='点击一个NPC选项的首项', command=lambda: MyThread(click_first_of_one_npc_response))
    button.pack()
    
    button = tk.Button(root,text='使用任务道具', command=lambda: MyThread(click_use_task_goods))
    button.pack()
    
    button = tk.Button(root,text='是否咕噜味叽哩对话', command=lambda: MyThread(is_gulu_jili_ask))
    button.pack()
    
    # 窗口显示运行
    root.mainloop()



