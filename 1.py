from ssl import CHANNEL_BINDING_TYPES
import cv2
import numpy as np

paper = np.zeros([400, 400, 3], dtype=np.uint8)
flag = True
rows, cols, channels = paper.shape

W = paper.shape[0]// 8
H = paper.shape[0]// 8

for i in range(0, paper.shape[0], W):
    for j in range(0, paper.shape[0], H):
        if flag== False:
            paper[i: i+W, j: j+H] = 255
            flag = True
        else:
            paper[i: i+W, j: j+H] = 0
            flag = False
    if flag:
        flag = False
    else:
        flag = True        
        
        
        
cv2.imshow("",paper)
cv2.waitKey()