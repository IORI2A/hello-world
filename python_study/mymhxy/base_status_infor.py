# ����ö����
from enum import Enum
 
# �̳�ö����
class DECIDE_STATUS(Enum):
    FALSE = 0
    TRUE = 1
    FAIL   = 0
    SUCCESS = 1
    UNKNOWN = 2
    COMPARE_NO_BASE_OBJECT = 3 # �޼���׼����
    COMPARE_NOT_MATCH = 4 # ��ⲻƥ��
    COMPARE_MATCH = 5 # ���ƥ��

 
#
#from base_status_infor import *
#

# �Զ�ִ����Ϸ����
# ֹͣ�Զ�ִ��
# ��⵱ǰ�Ƿ����Զ�ִ��״̬��
# �����Ƿ����ƶ���
# �Ƿ���NPC�ʴ���
