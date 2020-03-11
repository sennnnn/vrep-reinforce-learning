import sys
sys.path.append('./python')
######################################

import os
import cv2
import time
import numpy as np
import matplotlib.pyplot as plt

from python import vrep
from util import get_image

print('Program started')
# 关闭潜在的连接
vrep.simxFinish(-1)
# 每隔0.2s检测一次，直到连接上V-rep
while True:
    clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
    if clientID > -1:
        break
    else:
        time.sleep(0.2)
        print("Failed connecting to remote API server!")
print("Connection success!")
_,handle = vrep.simxGetObjectHandle(clientID, 'Vision_sensor', vrep.simx_opmode_oneshot_wait)
# 第一次获取 vision sensor 的时候推荐使用 simx_opmode_streaming 这个模式, 要先有一次调用之后才能真正获得图像。
# 通过 remote api 只能获得 vision sensor 的图像而不能获得 camera 的图像。
_,_,_ = vrep.simxGetVisionSensorImage(clientID, handle, 0, vrep.simx_opmode_streaming)
time.sleep(0.1)
image = get_image(clientID, handle)
cv2.imshow('Vision_sensor', image)
cv2.waitKey(0)