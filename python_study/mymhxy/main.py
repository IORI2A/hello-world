
import win32api
import win32gui
import win32con
from PIL import ImageGrab
import numpy as np
import cv2
import time
import random
import logging
import tkinter as tk
import threading
from PIL import Image



# logging.basicConfig()
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')


#logging.basicConfig(filename="test.log", filemode="w", format="%(asctime)s %(name)s:%(levelname)s:%(message)s", datefmt="%d-%M-%Y %H:%M:%S", level=logging.DEBUG)
logging.basicConfig(filename="test.log", filemode="w", format="%(asctime)s %(levelname)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S", level=logging.DEBUG)
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')


# 获取屏幕分辨率
def resolution():  
    # int GetSystemMetrics(int nIndex);
    # SM_CXSCREEN 0
    # SM_CYSCREEN 1
    return win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
    

# 获取梦幻西游窗口信息，返回一个矩形窗口四个坐标
def get_window_info():
    wdname = u'《梦幻西游》手游'
    handle = win32gui.FindWindow(0, wdname)  # 获取窗口句柄
    if handle == 0:
        # text.insert('end', '提示：请打开梦幻西游\n')
        # text.see('end')  # 自动显示底部
        print("提示：请打开梦幻西游")
        return None
    else:
        #
        print(win32gui.GetWindowRect(handle))
        # win32gui.SetWindowPos(handle, 0, 167, 3, 800, 800, 0x0040) 
        # 设置窗口位置
        win32gui.SetWindowPos(handle, win32con.HWND_TOPMOST, 167, 3, 600, 600, win32con.SWP_SHOWWINDOW)
        win32gui.MoveWindow(handle, 167, 3, 600, 600, True)
        return win32gui.GetWindowRect(handle)


# 设置窗口位置
def set_window_pos(handle, x, y, cx, cy):
    win32gui.SetWindowPos(handle, 0, x, y, cx, cy, SWP_SHOWWINDOW)  
    return None



# 截屏
def capture(left, top, right, bottom):
    img = ImageGrab.grab(bbox=(left, top, right, bottom))
    img = np.array(img.getdata(), np.uint8).reshape(img.size[1], img.size[0], 3)
    r, g, b = cv2.split(img)
    cv2.merge([b, g, r], img)
    return img


# 录屏
def capture_video(left, top, right, bottom):
    fps = 20

    # 获取屏幕指定区域的屏幕内容对象
    img = ImageGrab.grab(bbox=(left, top, right, bottom))
    height, width = img.size
    video = cv2.VideoWriter('video02.avi', cv2.VideoWriter_fourcc(*'XVID'), fps, (height, width))
 
    while True: 
        # 抓取内容
        captureImage = ImageGrab.grab(bbox=(left, top, right, bottom))  
        frame = cv2.cvtColor(np.array(captureImage), cv2.COLOR_RGB2BGR)
     
        # 显示无图像的窗口
        cv2.imshow('capturing', np.zeros((1, 255), np.uint8))
       
        # 控制窗口显示位置，方便通过按键方式退出
        cv2.moveWindow('capturing', height - 100, width - 100)  
        video.write(frame)
        # 退出条件    
        if cv2.waitKey(50) == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


# 移动鼠标并点击左键
def move_click(x, y, t=0):  
    win32api.SetCursorPos((x, y))  # 设置鼠标位置(x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
                         win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)  # 点击鼠标左键
    
    logging.info('move_click(x = %d, y = %d, t= %d)' % (x, y, t))
    
    if t == 0:
        time.sleep(random.random()*2+1)  # sleep一下
    else:
        time.sleep(t)
    return 0


def button_call_back():
    x = 873
    y = 172
    
    while is_start:
        #
        # 检测是否在做任务的移动过程中
        if is_moving():
            continue
        #
        # 检测是否在做任务时, 与 NPC 交互过程中
        if is_npc_ask():
            # 回应NPC的问话
            print(".............")
            
            ## npc回答选项_单选项位置_747_412_911_420.bmp
            #last_response_left = 747
            #last_response_top = 412
            #last_response_right = 911
            #last_response_bottom = 420
            #
            ## npc回答选项_标题位置_747_369_909_377.bmp
            #response_title_span = 412 - 369
            #if is_npc_response(last_response_left, last_response_top, last_response_right, last_response_bottom):
            #    #
            #    #response_title_left = last_response_left
            #    #response_title_top = last_response_top - response_title_span
            #    #response_title_right = last_response_right
            #    #response_title_bottom = last_response_bottom - response_title_span
            #    #is_npc_response_title
            #    
            #    last_response_top = last_response_top - response_title_span
            #    last_response_bottom = last_response_bottom - response_title_span
            #
            ##
            
            # npc回答选项_单选项位置_747_412_911_420.bmp
            # npc回答选项_标题位置_747_369_909_377.bmp
            response_left = 747
            response_top = 412
            response_right = 911
            response_bottom = 420
            response_span = 412 - 369
            
            first_response_left = response_left
            first_response_top = response_top
            first_response_right = response_right
            first_response_bottom = response_bottom
            
            while_cnt = 0
            while is_npc_response(response_left, response_top, response_right, response_bottom):
                # 
                while_cnt += 1
                print("检测 is_npc_response 次数，第 %d 次" % while_cnt)
                print("检测的回答选项位置:")
                print((response_left, response_top, response_right, response_bottom))
                print("上一个检测的回答选项位置:")
                print((first_response_left, first_response_top, first_response_right, first_response_bottom))
                
                #目前遇到最多有6个选项
                if while_cnt > 10:
                    break
                    
                # 检测直到遇到 回答选项_标题位置
                first_response_top = response_top
                first_response_bottom = response_bottom
                response_top = response_top - response_span
                response_bottom = response_bottom - response_span
            
            # 这里认为遇到 回答选项_标题位置 了
            # 默认点击 第一个选项
            x = (first_response_left + first_response_right)//2
            y = first_response_bottom
            print(">>>> 默认点击 第一个选项, 坐标位置(%d, %d)" % (x, y))
            
            win32api.SetCursorPos((x, y))  # 设置鼠标位置(x, y)
            time.sleep(0.1)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
                                 win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)  # 点击鼠标左键
            sleep_multiple = 2
            t = random.random()*sleep_multiple+1
            print(">>>> 睡眠时长: %d" % (t))
            time.sleep(t)
            
            # 继续执行NPC的交互
            continue
        
        #
        # 检测是否在做任务时, NPC 的剧情播放中
        if is_npc_anywhere_click():
            # 默认点击 窗口内部右上角处
            x = 935 + int(random.random()*5)
            y = 70 + int(random.random()*5)
            print(">>>> 默认点击剧情继续, 坐标位置(%d, %d)" % (x, y))
            
            win32api.SetCursorPos((x, y))  # 设置鼠标位置(x, y)
            time.sleep(0.1)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
                                 win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)  # 点击鼠标左键
            sleep_multiple = 1
            t = random.random()*sleep_multiple+1
            print(">>>> 睡眠时长: %d" % (t))
            time.sleep(t)
            
            continue
        
        #
        # 检测是否在做任务时, NPC 的剧情播放中
        if is_use_task_goods():
            x = (796+874)//2 + int(random.random()*10)
            y = (479+518)//2 + int(random.random()*5)
            print(">>>> 使用物品, 坐标位置(%d, %d)" % (x, y))
            
            win32api.SetCursorPos((x, y))  # 设置鼠标位置(x, y)
            time.sleep(0.1)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
                                 win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)  # 点击鼠标左键
            sleep_multiple = 1
            t = random.random()*sleep_multiple+1
            print(">>>> 睡眠时长: %d" % (t))
            time.sleep(t)
            
            continue
        #
        
        #
        # 检测是否在做任务时, NPC 的剧情播放中
        if is_skip_task_story():
            # 默认点击 窗口内部右上角处 任务使用物品_796_479_874_518
            x = 935 + int(random.random()*5)
            y = 55 + int(random.random()*5)
            print(">>>> 默认点击跳过剧情, 坐标位置(%d, %d)" % (x, y))
            
            win32api.SetCursorPos((x, y))  # 设置鼠标位置(x, y)
            time.sleep(0.1)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
                                 win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)  # 点击鼠标左键
            sleep_multiple = 1
            t = random.random()*sleep_multiple+1
            print(">>>> 睡眠时长: %d" % (t))
            time.sleep(t)
            
            continue
        #
        
        
        #
        x = 873
        y = 172
        print(">>>> 默认点击 剧情任务坐标位置(%d, %d)" % (x, y))
        
        win32api.SetCursorPos((x, y))  # 设置鼠标位置(x, y)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
                             win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)  # 点击鼠标左键
        # time.sleep(1)
        # random() 方法返回随机生成的一个实数，它在[0,1)范围内。
        sleep_multiple = 3
        t = random.random()*sleep_multiple+1
        print(">>>> 睡眠时长: %d" % (t))
        time.sleep(t)
   

def button_stop_call_back():
    global  is_start
    is_start = False
    print("停止")


#
# 获得图像的hash值
def get_hash(img):
    img = img.resize((16, 16), Image.ANTIALIAS).convert('L')  # 抗锯齿 灰度
    avg = sum(list(img.getdata())) / 256  # 计算像素平均值
    s = ''.join(map(lambda i: '0' if i < avg else '1', img.getdata()))  # 每个像素进行比对,大于avg为1,反之为0
    return ''.join(map(lambda j: '%x' % int(s[j:j+4], 2), range(0, 256, 4)))


# 计算两个图像的汉明距离
def hamming(hash1, hash2, n=20):
    b = False
    assert len(hash1) == len(hash2)
    sum_value = sum(ch1 != ch2 for ch1, ch2 in zip(hash1, hash2))
    print("汉明距离(true = sum < n): n = %d, sum = %d" % (n, sum_value))
    #if sum(ch1 != ch2 for ch1, ch2 in zip(hash1, hash2)) < n:
    if sum_value < n:
        b = True
    return b
    
    
# 地图坐标_293_68_351_84
def is_moving():
    #
    print("is_moving()")
    
    #
    left = 293
    top = 68
    right = 351
    bottom = 84
    bbox=(left, top, right, bottom)
    print(bbox)
    
    # 截取坐标值图形
    sleep_sec = 2
    map_coord_img_1 = ImageGrab.grab(bbox)
    time.sleep(sleep_sec)
    map_coord_img_2 = ImageGrab.grab(bbox)

    #map_coord_img_1.show()
    #map_coord_img_2.show()
    
    #检测对比截图
    value = 20
    if hamming(get_hash(map_coord_img_1), get_hash(map_coord_img_2), value):
        #print("移动中......")
        print(">>>> 未移动")
        return False
        
    #print("未移动")
    print(">>>> 移动中......")
    return True
#


# npc弹窗_374_557_432_571.bmp
# npc弹窗_400_558_431_577.bmp
def is_npc_ask():
    #
    print("is_npc_ask()")
    
    #
    #left = 374
    #top = 557
    #right = 432
    #bottom = 571
    left = 400
    top = 558
    right = 431
    bottom = 577
    bbox=(left, top, right, bottom)
    print(bbox)
    
    # 截取判定NPC问话位置图形
    npc_ask_img = ImageGrab.grab(bbox)
    #npc_ask_img.show()
    
    # 判断的基准图片
    #base_npc_ask_img = Image.open("F:\\lz\\svn_work\\anjian_branch\\npc弹窗_374_557_432_571.bmp")
    base_npc_ask_img = Image.open("F:\\lz\\svn_work\\anjian_branch\\npc弹窗_400_558_431_577.bmp")
    #base_npc_ask_img.show()
    
    #检测对比截图
    value = 20
    if hamming(get_hash(npc_ask_img), get_hash(base_npc_ask_img), value):
        #print("NPC 未问答")
        print(">>>> NPC 问答中......")
        return True
        
    #print("NPC 问答中......")
    print(">>>> NPC 未问答")
    return False
#


# npc回答选项_单选项位置_747_412_911_420.bmp
#def is_npc_response():
def is_npc_response(l, t, r, b):
    #
    print("is_npc_response()")
    
    #
    left = l
    top = t
    right = r
    bottom = b
    bbox=(left, top, right, bottom)
    print(bbox)
    
    # 截取判定NPC问话位置图形
    npc_response_img = ImageGrab.grab(bbox)
    #npc_response_img.show()
    
    # 判断的基准图片
    base_npc_response_img = Image.open("F:\\lz\\svn_work\\anjian_branch\\npc回答选项_单选项位置_747_412_911_420.bmp")
    #base_npc_response_img.show()
    
    #检测对比截图
    value = 20
    if hamming(get_hash(npc_response_img), get_hash(base_npc_response_img), value):
        print(">>>> 是 NPC 回答选项......")
        return True
        
    print(">>>> 不是 NPC 回答选项")
    return False
#


# npc回答选项_标题位置_747_369_909_377.bmp
def is_npc_response_title(l, t, r, b):
    #
    print("is_npc_response_title()")
    
    #
    left = l
    top = t
    right = r
    bottom = b
    bbox=(left, top, right, bottom)
    print(bbox)
    
    # 截取判定NPC问话位置图形
    npc_response_img = ImageGrab.grab(bbox)
    npc_response_img.show()
    
    # 判断的基准图片
    base_npc_response_img = Image.open("F:\\lz\\svn_work\\anjian_branch\\npc回答选项_单选项位置_747_412_911_420.bmp")
    base_npc_response_img.show()
    
    #检测对比截图
    value = 20
    if hamming(get_hash(npc_response_img), get_hash(base_npc_response_img), value):
        print("是 NPC 回答选项标题......")
        return True
        
    print("不是 NPC 回答选项标题")
    return False
#


# 点击任意地方_771_56_950_86.bmp
def is_npc_anywhere_click():
    #
    print("is_npc_anywhere_click()")
    
    #
    left = 771
    top = 56
    right = 950
    bottom = 86
    bbox=(left, top, right, bottom)
    print(bbox)
    
    # 截取判定NPC问话位置图形
    npc_anywhere_click_img = ImageGrab.grab(bbox)
    #npc_anywhere_click_img.show()
    
    # 判断的基准图片
    base_npc_anywhere_click_img = Image.open("F:\\lz\\svn_work\\anjian_branch\\点击任意地方_771_56_950_86.bmp")
    #base_npc_anywhere_click_img.show()
    
    #检测对比截图
    value = 20
    if hamming(get_hash(npc_anywhere_click_img), get_hash(base_npc_anywhere_click_img), value):
        print(">>>> 是 NPC 点击任何地方界面......")
        return True
        
    print(">>>> 不是 NPC 点击任何地方界面")
    return False
#


# 任务使用物品_796_479_874_518.bmp
def is_use_task_goods():
    #
    print("is_use_task_goods()")
    
    #
    left = 796
    top = 479
    right = 874
    bottom = 518
    bbox=(left, top, right, bottom)
    print(bbox)
    
    # 截取判定NPC问话位置图形
    use_task_goods_img = ImageGrab.grab(bbox)
    #use_task_goods_img.show()
    
    # 判断的基准图片
    base_use_task_goods_img = Image.open("F:\\lz\\svn_work\\anjian_branch\\任务使用物品_796_479_874_518.bmp")
    #base_use_task_goods_img.show()
    
    #检测对比截图
    value = 20
    if hamming(get_hash(use_task_goods_img), get_hash(base_use_task_goods_img), value):
        print(">>>> 是使用任务物品......")
        return True
        
    print(">>>> 不是使用任务物品")
    return False
#


# 跳过剧情_773_44_944_69.bmp
def is_skip_task_story():
    #
    print("is_skip_task_story()")
    
    #
    left = 773
    top = 44
    right = 944
    bottom = 69
    bbox=(left, top, right, bottom)
    print(bbox)
    
    # 截取判定NPC问话位置图形
    skip_task_story_img = ImageGrab.grab(bbox)
    #skip_task_story_img.show()
    
    # 判断的基准图片
    base_skip_task_story_img = Image.open("F:\\lz\\svn_work\\anjian_branch\\跳过剧情_773_44_944_69.bmp")
    #base_skip_task_story_img.show()
    
    #检测对比截图
    value = 20
    if hamming(get_hash(skip_task_story_img), get_hash(base_skip_task_story_img), value):
        print(">>>> 是跳过任务剧情界面......")
        return True
        
    print(">>>> 不是跳过任务剧情界面")
    return False
#
#


class MyThread(threading.Thread):
    def __init__(self, func, *args):
        super().__init__()

        self.func = func
        self.args = args

        self.setDaemon(True)
        self.start()  # 在这里开始

    def run(self):
        self.func(*self.args)



# 启动
if __name__ == "__main__":
    print("start ......")
    
    global is_start
    is_start = True
    
    # screen_resolution = resolution()
    # print(screen_resolution)
    # 
    # # 全屏坐标
    # window_size = get_window_info()
    # print(window_size)
    
    # capture_image = capture(window_size[0], window_size[1], window_size[2], window_size[3])
    # cv2.imshow("screen", capture_image)
    # cv2.waitKey(0)
    
    # capture_video(window_size[0], window_size[1], window_size[2], window_size[3])
    
    # move_click(200, 70)
    
    
    # 获取梦幻西游窗口信息
    wdname = u'《梦幻西游》手游'
    # 获取窗口句柄
    handle = win32gui.FindWindow(0, wdname)  
    if handle == 0:
        # 未获取到指定窗口
        no_find_window_infor = "未找到[%s]窗口" % wdname
        print(no_find_window_infor)
        logging.error(no_find_window_infor)
    
    # 窗口置前
    win32gui.SetForegroundWindow(handle)


    # 创建主窗口
    root = tk.Tk()
    root.title("梦幻西游手游辅助")
    root.minsize(300, 250)
    root.maxsize(300, 250)
    
    button = tk.Button(root, text="任务", command=lambda: MyThread(button_call_back), width = 15,height = 2)
    #button.place(relx=0.2, rely=0.15, width=200)
    button.pack()
    
    button_stop = tk.Button(root,text=u"停止", command=lambda: MyThread(button_stop_call_back), width = 15,height = 2)
    #button_stop.place(relx=0.4, rely=0.85, width=200)
    button_stop.pack()
    
    button_is_move = tk.Button(root,text=u"移动中...", command=lambda: MyThread(is_moving), width = 15,height = 2)
    button_is_move.pack()
    
    button_test = tk.Button(root,text=u"TEST...", command=lambda: MyThread(is_npc_anywhere_click), width = 15,height = 2)
    button_test.pack()
    
    # 窗口显示运行
    root.mainloop()
    
    
    
