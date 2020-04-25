

import logging
import sys 
from string_operation import *
from PIL import ImageGrab
from PIL import Image
from datetime import datetime



# 获得图像的hash值
def get_hash(img):
    img = img.resize((16, 16), Image.ANTIALIAS).convert('L')  # 抗锯齿 灰度
    avg = sum(list(img.getdata())) / 256  # 计算像素平均值
    s = ''.join(map(lambda i: '0' if i < avg else '1', img.getdata()))  # 每个像素进行比对,大于avg为1,反之为0
    return ''.join(map(lambda j: '%x' % int(s[j:j+4], 2), range(0, 256, 4)))


# 计算两个图像的汉明距离
def hamming(hash1, hash2, n=20):
    # 
    func_infor = sys._getframe().f_code.co_name
    
    b = False
    assert len(hash1) == len(hash2)
    sum_value = sum(ch1 != ch2 for ch1, ch2 in zip(hash1, hash2))
    
    hamming_infor = "%s, 汉明距离(true = sum < n): sum = %d, n = %d" % (func_infor, sum_value, n)
    print(hamming_infor)
    logging.info(hamming_infor)

    #if sum(ch1 != ch2 for ch1, ch2 in zip(hash1, hash2)) < n:
    if sum_value < n:
        b = True
    return b
#

# 根据提供的图片截取相应位置的一张图片，两者进行比对
def is_grab_match(file_name, match_value = 20):
    # 
    func_infor = sys._getframe().f_code.co_name
    
    # 解析文件名获取左上、右下坐标值 Coordinate
    l, t, r, b = get_coordinate_by_file_name(file_name)
    # 截取对应坐标图片
    bbox=(l, t, r, b) 
    current_img = ImageGrab.grab(bbox)
    #current_img.show()
    # 保存截图，用于复盘分析
    time_infor = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')[:-3]
    save_name = file_name[0:file_name.find('.')]
    save_name = save_name + '_' + time_infor + '.png'
    # 需要已经存在该路径
    save_path = './bmp/temp_capture/'
    current_img.save(save_path + save_name)
    
    # 截图与基准图片比较
    base_file = ".\\bmp\\" + file_name
    base_img = Image.open(base_file)
    #base_img.show()
    
    # 比较相似
    hamming_infor = '%s, 截图坐标(%d, %d, %d, %d)' % (func_infor, l, t, r, b)
    ret = False
    if hamming(get_hash(current_img), get_hash(base_img), match_value):
        hamming_infor += '，\'%s\' 与 \'%s\' 相似' % (save_name, file_name)
        ret = True
    else:    
        hamming_infor += '，\'%s\' 与 \'%s\' 不相似' % (save_name, file_name)
        ret = False
    print(hamming_infor)
    logging.info(hamming_infor)
    
    return ret, l, t, r, b
#


# 根据提供的图片坐标间隔性截取相应位置的两张图片，比对两张截取的图片是否有变化
import time

def is_grab_two_match(file_name, match_value = 20, grab_sleep = 1):
    # 
    func_infor = sys._getframe().f_code.co_name
    
    # 解析文件名获取左上、右下坐标值 Coordinate
    l, t, r, b = get_coordinate_by_file_name(file_name)
    
    # 截取对应坐标图片 截图1 和 截图2
    bbox=(l, t, r, b) 
    current_img_1 = ImageGrab.grab(bbox)
    time.sleep(grab_sleep)
    current_img_2 = ImageGrab.grab(bbox)
    # 保存截图，用于复盘分析
    time_infor = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')[:-3]
    save_name = file_name[0:file_name.find('.')]
    save_name_1 = save_name + '_' + time_infor + '_1' + '.png'
    save_name_2 = save_name + '_' + time_infor + '_2' + '.png'
    # 需要已经存在该路径
    save_path = './bmp/temp_capture/'
    current_img_1.save(save_path + save_name_1)
    current_img_2.save(save_path + save_name_1)
    
    # 两张截图比较
    hamming_infor = '%s, 截图坐标(%d, %d, %d, %d)' % (func_infor, l, t, r, b)
    ret = False
    if hamming(get_hash(current_img_1), get_hash(current_img_2), match_value):
        hamming_infor += '，\'%s\' 与 \'%s\' 相似' % (save_name_1, save_name_2)
        ret = True
    else:    
        hamming_infor += '，\'%s\' 与 \'%s\' 不相似' % (save_name_1, save_name_2)
        ret = False
    print(hamming_infor)
    logging.info(hamming_infor)
    
    return ret, l, t, r, b
#
#