

import logging
import sys



# 解析文件名获取左上、右下坐标值
def get_coordinate_by_file_name(file_name):
    # 
    func_infor = sys._getframe().f_code.co_name
    
    # 001.NPC问答.756_419_908_439_20.bmp
    list = file_name.split('.')
    ##print(list)
    coord_value = list[-2]
    
    coord_value_list = coord_value.split('_')
    l = int(coord_value_list[0])
    t = int(coord_value_list[1])
    r = int(coord_value_list[2])
    b = int(coord_value_list[3])
    
    coordinate_infor = '%s, 解析 \'%s\' 得到坐标信息(%d, %d, %d, %d)' % (func_infor, file_name, l, t, r, b)
    ##print(coordinate_infor)
    logging.info(coordinate_infor)
            
    return l, t, r, b
#


# 
def get_coordinate_value_by_file_name(file_name):
    # 
    func_infor = sys._getframe().f_code.co_name
    
    # 001.NPC问答.756_419_908_439_20.bmp
    list = file_name.split('.')
    ##print(list)
    seqno = list[0]
    name = list[1]
    coord_value = list[-2]
    #
    ##print(seqno)
    ##print(name)
    ##print(coord_value)
    
    coord_value_list = coord_value.split('_')
    ##print(len(coord_value_list))
    l = int(coord_value_list[0])
    t = int(coord_value_list[1])
    r = int(coord_value_list[2])
    b = int(coord_value_list[3])
    if len(coord_value_list) > 4:
        v = int(coord_value_list[4])
    else:
        v = 20
    
    coordinate_infor = '%s, 解析 \'%s\' 得到坐标信息(%d, %d, %d, %d), v = %d' % (func_infor, file_name, l, t, r, b, v)
    #print(coordinate_infor)
    logging.info(coordinate_infor)
            
    return l, t, r, b, v
#




if __name__ == "__main__":
    #get_coordinate_by_file_name('NPC问答.400_558_431_577.bmp')
    get_coordinate_value_by_file_name('001.NPC问答.756_419_908_439_20.bmp')
    get_coordinate_value_by_file_name('001.NPC问答.756_419_908_439.bmp')