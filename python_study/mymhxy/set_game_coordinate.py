
import logging
import win32api,win32con,win32gui
import time
import numpy as np



# 设置日志输出配置
logging.basicConfig(filename="mhxy.log", filemode="w", format="%(asctime)s %(levelname)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S", level=logging.DEBUG)
global_temp_str = ''



# 获得屏幕分辨率X轴
screen_width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
# 获得屏幕分辨率Y轴
screen_height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

screen_resolution_infor = '获得屏幕分辨率: %d * %d' % (screen_width, screen_height)
print(screen_resolution_infor)
# logging.info(screen_resolution_infor)
global_temp_str = screen_resolution_infor
logging.info(global_temp_str)



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

# 获取窗口的坐标尺寸信息
l, t, r, b = win32gui.GetWindowRect(handle)
print((l, t, r, b))
# 计算窗口宽、高
wind_width = r - l
wind_height = b - t

find_window_rect_infor = "[%s]窗口坐标信息：(left, top) =  (%d, %d)，(right, bottom) =  (%d, %d)，宽：%d，高：%d" % (wdname, l, t, r, b, wind_width, wind_height)
print(find_window_rect_infor)
logging.info(find_window_rect_infor)

## 指定显示的起始左上角坐标
#wind_left = 1 #200
#wind_top = 0
# 期望的窗口显示位置尺寸
set_wind_left = 200
set_wind_top = 0
set_wind_width = 800
set_wind_height = 600

# # 设置窗口按指定尺寸显示 （失败，无效）
# wind_width = 800
# wind_height = 600
# # 设置窗口位置
# win32gui.SetWindowPos(handle, win32con.HWND_TOP, wind_left, wind_top, wind_width, wind_height, win32con.SWP_SHOWWINDOW)
# # 再次获取重设位置后窗口的坐标尺寸信息
# l, t, r, b = win32gui.GetWindowRect(handle)
#  # 计算窗口宽、高
# wind_width = r - l
# wind_height = b - t
# find_window_rect_infor = "[%s]窗口坐标信息：(left, top) =  (%d, %d)，(right, bottom) =  (%d, %d)，宽：%d，高：%d" % (wdname, l, t, r, b, wind_width, wind_height)
# print(find_window_rect_infor)
# logging.info(find_window_rect_infor)

# 设置窗口位置，方便拉伸
win32gui.SetWindowPos(handle, win32con.HWND_TOP, set_wind_left, set_wind_top, set_wind_width, set_wind_height, win32con.SWP_SHOWWINDOW)

# 再次获取重设位置后窗口的坐标尺寸信息
l, t, r, b = win32gui.GetWindowRect(handle)
 # 计算窗口宽、高
wind_width = r - l
wind_height = b - t
find_window_rect_infor = "设置[%s]窗口位置后的坐标信息：(left, top) =  (%d, %d)，(right, bottom) =  (%d, %d)，宽：%d，高：%d" % (wdname, l, t, r, b, wind_width, wind_height)
print(find_window_rect_infor)
logging.info(find_window_rect_infor)


## 设置鼠标位置到左上角
## win32api.SetCursorPos((wind_left, wind_top))  
## drag_start_point = (wind_left+2, wind_top+2)
## win32api.SetCursorPos(drag_start_point) 
#drag_start_point_x = wind_left+2
#drag_start_point_y = wind_top+2
#win32api.SetCursorPos((drag_start_point_x, drag_start_point_y)) 
## 鼠标进行拖动缩放
#drag_span_x = 200
#drag_span_y = 200
## 计算鼠标拖放结束位置
#drag_end_point_x = drag_start_point_x + drag_span_x
#drag_end_point_y = drag_start_point_y + drag_span_y
#
#drag_point_infor = "起始位置(%d, %d)，结束位置(%d, %d)" % (drag_start_point_x, drag_start_point_y, drag_end_point_x, drag_end_point_y)
#print(drag_point_infor)
#logging.info(drag_point_infor)
#
### 按下鼠标左键
##win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, drag_start_point_x, drag_start_point_y,0,0)
##time.sleep(0.1)
##win32api.mouse_event(win32con.MOUSEEVENTF_MOVE|win32con.MOUSEEVENTF_ABSOLUTE, drag_start_point_x, drag_start_point_y,0,0)
##time.sleep(0.1)
##win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, drag_end_point_x, drag_end_point_y,0,0)
#
#win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, drag_start_point_x, drag_start_point_y,0,0)
#time.sleep(0.1)
#win32api.mouse_event(win32con.MOUSEEVENTF_MOVE|win32con.MOUSEEVENTF_ABSOLUTE, drag_span_x*65535//screen_width, drag_span_y*65535//screen_height,0,0)
#time.sleep(0.1)
#win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, drag_end_point_x, drag_end_point_y,0,0)

cnt = 0
while True:
    # 设置窗口位置，方便拉伸
    win32gui.SetWindowPos(handle, win32con.HWND_TOP, set_wind_left, set_wind_top, set_wind_width, set_wind_height, win32con.SWP_SHOWWINDOW)
    
    # 统计拖放次数
    cnt += 1
    drag_y_infor = '高度拖放中，第 %d 次' % cnt
    print(drag_y_infor)
    logging.info(drag_y_infor)
    
    # 调测时用于退出程序
    if cnt > 200:
        break
    
    # 再次获取重设位置后窗口的坐标尺寸信息
    l, t, r, b = win32gui.GetWindowRect(handle)
     # 计算窗口宽、高
    wind_width = r - l
    wind_height = b - t
    find_window_rect_infor = "设置[%s]窗口位置后的坐标信息：(left, top) =  (%d, %d)，(right, bottom) =  (%d, %d)，宽：%d，高：%d" % (wdname, l, t, r, b, wind_width, wind_height)
    print(find_window_rect_infor)
    logging.info(find_window_rect_infor)

    # 高度拖放合适退出
    if wind_height == set_wind_height:
        break

    # 设置鼠标位置到上下边缘
    temp_x = set_wind_left + 20
    if wind_height > set_wind_height:
        win32api.SetCursorPos((temp_x, set_wind_top)) 
    if wind_height < set_wind_height:
        diff = -3 # 偏差纠正
        win32api.SetCursorPos((temp_x, set_wind_top+wind_height+diff)) 
    
    # 按下鼠标左键
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0,0,0)
    time.sleep(0.01)
    # 可根据实现环境调节的拖放距离
    y_span = 4
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, y_span,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0,0,0)
    #time.sleep(0.01)

    ## 再次获取拖放后窗口的坐标尺寸信息
    #l, t, r, b = win32gui.GetWindowRect(handle)
    # # 计算窗口宽、高
    #wind_width = r - l
    #wind_height = b - t
    #find_window_rect_infor = "[%s]窗口坐标信息：(left, top) =  (%d, %d)，(right, bottom) =  (%d, %d)，宽：%d，高：%d" % (wdname, l, t, r, b, wind_width, wind_height)
    #print(find_window_rect_infor)
    #logging.info(find_window_rect_infor)


###
#

