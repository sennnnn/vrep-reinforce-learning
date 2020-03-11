

from python import vrep

def get_image(clientID, handle):
    _,resolution,image = vrep.simxGetVisionSensorImage(clientID, handle, 0, vrep.simx_opmode_buffer)
    
    return resolution,image
