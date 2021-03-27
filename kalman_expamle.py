from utils.kalman import Kalman,ExtendedKalman
from utils.paramSetting import *
import numpy as np

if __name__ =="__main__":

    param_path = 'config/'
    Debug = True

    print("Kalman Setting ...")
    Kalman_params = getKalmanParams(root_path=param_path,name='kalman.yaml')
    Kal = Kalman(Kalman_params,debug=Debug)
    print("Done\n")

    result = Kal.calculate(np.array([x,y,z]))
