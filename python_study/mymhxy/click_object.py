

import logging
from mouse_action import *
import sys 
from file_operation import *
from string_operation import *
from image_operation import *



# 根据解析首个匹配文件，直接点击对应位置
def click_object(name):
    # 
    func_infor = sys._getframe().f_code.co_name
    
    # 根据 name_* 获取相应文件 如 '第一栏任务坐标_795_144_945_207.bmp'
    pre_name = name + '_'
    file_name = search_bmp_file(pre_name)
    
    # 未找到BMP文件直接返回
    if file_name is None:
        #
        #click_object_error = '%s, 无有效的点击对象 [%s]' % (func_infor, pre_name)
        click_object_error = '%s, 无有效的点击对象 [%s]' % (func_infor, name)
        print(click_object_error)
        logging.info(click_object_error)
        return None
    # 
    
    # 解析文件名获取左上、右下坐标值 Coordinate
    #l = 795
    #t = 144
    #r = 945
    #b = 207
    l, t, r, b = get_coordinate_by_file_name(file_name)
    
    # 计算随机的点击位置
    x = (l+r)//2 + int(random.random()*((r-l)//2))
    y = (t+b)//2 + int(random.random()*((b-t)//2))
    # sys._getframe().f_code.co_name 获取当前函数名
    #click_object_infor = '%s, 点击 [%s]' % (func_infor, file_name)
    click_object_infor = '%s, 点击 [%s]' % (func_infor, name)
    print(click_object_infor)
    logging.info(click_object_infor)
    mouse_move_click(x, y)
#


# 通过多个图片文件来对比操作
# 根据多个匹配文件，逐个解析坐标，并截取对应位置图片与基准对比，图片相似才点击对应位置
def click_object_by_multi(name):
    # 
    func_infor = sys._getframe().f_code.co_name
    
    # 
    pre_name = name + '_'
    list_file_name = search_bmp_file_list(pre_name)
    #print(list_file_name)
    if list_file_name:
        # 遍历直至成功或最后元素
        for file_name in list_file_name:          
            # 比较相似才进行点击
            value = 20
            ret, l, t, r, b = is_grab_match(file_name, value)
            if ret:
                x = (l+r)//2 + int(random.random()*((r-l)//2))
                y = (t+b)//2 + int(random.random()*((b-t)//2))
                click_object_infor = '%s, 点击 [%s]' % (func_infor, name)
                print(click_object_infor)
                logging.info(click_object_infor)
                mouse_move_click(x, y)
                break
            else:    
                click_object_infor = '%s, 不点击 [%s]' % (func_infor, name)
                print(click_object_infor)
                logging.info(click_object_infor)
                
            ## 解析文件名获取左上、右下坐标值 Coordinate
            #l, t, r, b = get_coordinate_by_file_name(file_name)
            ## 截取对应坐标图片
            #bbox=(l, t, r, b)
            #print(bbox)
            #current_img = ImageGrab.grab(bbox)
            ##current_img.show()
            #
            ## 截图与基准图片比较
            #base_file = ".\\bmp\\" + file_name
            #base_img = Image.open(base_file)
            ##base_img.show()
            #
            ## 比较相似才进行点击
            #value = 20
            #if hamming(get_hash(npc_anywhere_click_img), get_hash(base_npc_anywhere_click_img), value):
            #    x = (l+r)//2 + int(random.random()*((r-l)//2))
            #    y = (t+b)//2 + int(random.random()*((b-t)//2))
            #    click_object_infor = '%s, 相似' % (func_infor)
            #    print(click_object_infor)
            #    logging.info(click_object_infor)
            #    #mouse_move_click(x, y)
            #    break
            #else:    
            #    click_object_infor = '%s, 不相似' % (func_infor)
            #    print(click_object_infor)
            #    logging.info(click_object_infor)
    else:
        # 未有BMP文件直接返回
        click_object_error = '%s, 无有效的点击对象 [%s]' % (func_infor, name)
        print(click_object_error)
        logging.info(click_object_error)
    # 
#