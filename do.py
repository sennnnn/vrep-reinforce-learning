import sys
sys.path.append('./python')
######################################

import os
import math
import time
import numpy as np

from python import vrep
from util import get_image

RAD2DEG = 180 / math.pi   # 常数，弧度转度数
tstep = 0.005             # 定义仿真步长
# 配置关节信息
jointNum = 6
baseName = 'Jaco'
jointName = 'Jaco_joint'

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
# 第一次获取 vision sensor 的时候要先使用 simx_opmode_streaming 这个模式
# 通过 remote api 只能获得 vision sensor 的图像而不能获得 camera 的图像。
_,resolution,image = vrep.simxGetVisionSensorImage(clientID, handle, 0, vrep.simx_opmode_streaming)
time.sleep(0.1)
print(len(get_image(clientID, handle)[1]))