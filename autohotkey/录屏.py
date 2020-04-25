# coding: utf-8
from PIL import ImageGrab
import  numpy as np
import  cv2
 
fps = 20
start = 3  # ��ʱ¼��
end = 15  # �Զ�����ʱ��
 
curScreen = ImageGrab.grab()  # ��ȡ��Ļ����
height, width = curScreen.size
 
video = cv2.VideoWriter('video02.avi', cv2.VideoWriter_fourcc(*'XVID'), fps, (height, width))
 
imageNum = 0
while True:
    imageNum += 1
    captureImage = ImageGrab.grab()  # ץȡ��Ļ
    frame = cv2.cvtColor(np.array(captureImage), cv2.COLOR_RGB2BGR)
 
    # ��ʾ��ͼ��Ĵ���
    cv2.imshow('capturing', np.zeros((1, 255), np.uint8))
   
    # ���ƴ�����ʾλ�ã�����ͨ��������ʽ�˳�
    cv2.moveWindow('capturing', height - 100, width - 100)  
    if imageNum > fps * start:
        video.write(frame)
    # �˳�����    
    if cv2.waitKey(50) == ord('q') or imageNum > fps * end:
        break
video.release()
cv2.destroyAllWindows()

