


#str = '第一栏任务坐标_795_144_945_207.bmp'
#
#begin = str.find('_')+1
#end = str.rfind('.')
#print((begin, end))
#print(str[begin:end])
#
#print(str.split('_'))
#print(str[begin:end].split('_'))
#
#sub_str = str[begin:end]
#print(sub_str)
#l_str, t_str, r_str, b_str = sub_str.split('_')
#print((l_str, t_str, r_str, b_str))
#l = int(l_str)
#t = int(t_str)
#r = int(r_str)
#b = int(b_str)
#print((l, t, r, b))


import logging
import sys



# 解析文件名获取左上、右下坐标值
def get_coordinate_by_file_name(file_name):
    # 
    func_infor = sys._getframe().f_code.co_name
    
    #'第一栏任务坐标_795_144_945_207.bmp'
    begin = file_name.find('_')+1
    end = file_name.rfind('.')
    sub_str = file_name[begin:end]
    l_str, t_str, r_str, b_str = sub_str.split('_')
    l = int(l_str)
    t = int(t_str)
    r = int(r_str)
    b = int(b_str)
    
    coordinate_infor = '%s, 解析 \'%s\' 得到坐标信息(%d, %d, %d, %d)' % (func_infor, file_name, l, t, r, b)
    print(coordinate_infor)
    logging.info(coordinate_infor)
            
    return l, t, r, b
#