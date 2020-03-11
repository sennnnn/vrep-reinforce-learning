import sys
sys.path.append('./python')
######################################

import os
import math
import time
import numpy as np

import vrep

RAD2EDG = 180 / math.pi   # 常数，弧度转度数
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