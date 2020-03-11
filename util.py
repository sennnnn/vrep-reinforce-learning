
import numpy as np

from python import vrep

def get_image(clientID, handle):
    error_code,resolution,image = vrep.simxGetVisionSensorImage(clientID, handle, 0, vrep.simx_opmode_buffer)
    if(error_code == vrep.simx_return_ok):
        image = np.array(image, dtype=np.uint8)
        image = np.reshape(image, (resolution[1], resolution[0], 3))

        return image
    else:
        return None