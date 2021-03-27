from utils.yaml_manager import YamlReader
import numpy as np

def getKalmanParams(root_path='config/',name='Kalman.yaml'):

    YlR = YamlReader()
    YlR.readYaml(root_path + name)

    Kalman_config = {};
    Kalman_config['system'] = np.array(YlR.getParams('system matrix'))
    Kalman_config['input'] = np.array(YlR.getParams('input matrix'))
    Kalman_config['system conv'] = np.array(YlR.getParams('system conv matrix'))
    Kalman_config['sensor conv'] = np.array(YlR.getParams('sensor conv matrix'))

    return Kalman_config
