# 导入枚举类
from enum import Enum
 
# 继承枚举类
class DECIDE_STATUS(Enum):
    FALSE = 0
    TRUE = 1
    FAIL   = 0
    SUCCESS = 1
    UNKNOWN = 2
    COMPARE_NO_BASE_OBJECT = 3 # 无检测基准对象
    COMPARE_NOT_MATCH = 4 # 检测不匹配
    COMPARE_MATCH = 5 # 检测匹配

 
#
#from base_status_infor import *
#

# 自动执行游戏操作
# 停止自动执行
# 检测当前是否在自动执行状态中
# 人物是否在移动中
# 是否在NPC问答中
