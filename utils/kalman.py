import numpy as np
class Kalman(object):
	def __init__(self,kalman_config,debug=False):
		self.A = kalman_config['system']
		self.H = kalman_config['input']
		self.Q = kalman_config['system conv']
		self.R = kalman_config['sensor conv']
		self.P = np.eye(self.A.shape[0])
		self.x = np.empty((0,0))
		self.start = False
		if debug:
			print("="*20)
			print("KALMAN FILTER INFOMATION")
			print("-"*20)
			print("system matritx  \n {} \n".format(self.A))
			print("input matritx \n {} \n".format(self.H))
			print("system conv matritx \n {} \n".format(self.Q))
			print("sensor conv \n {} \n".format(self.R))
			print("init input matritx \n {} \n".format(self.x))
			print("conv matritx \n {} \n".format(self.P))
			print("="*20+ "\n\n")

	def calculate(self,z):
		if self.start == False:
			self.x = self.H.T@z
			self.start = True
		xp = self.A@self.x
		Pp = self.A@self.P@self.A.T + self.Q
		K = Pp@self.H.T@np.linalg.inv(self.H@Pp@self.H.T + self.R)
		self.x = xp + K@(z - self.H@xp)
		self.P = Pp - K@self.H@Pp
		return self.x

class ExtendedKalman(object):
	def __init__(self,kalman_config):
		self.A_function = kalman_config['system function']
		self.H_function = kalman_config['input function']
		self.A = np.empty((0,0))
		self.H = np.empty((0,0))
		self.Q = kalman_config['system conv']
		self.R = kalman_config['sensor conv']
		self.P = np.eye(self.A.shape[0])
		self.x = np.empty((0,0))
		self.start = False

	def calculate(self,z):
		self.A = self.A_function(z)
		self.H = self.H_function(z)
		if self.start == False:
			self.x = self.H.T@z
			self.start = True
		xp = self.A@self.x
		Pp = self.A@self.P@self.A.T + self.Q
		K = Pp@self.H.T@np.linalg.inv(self.H@Pp@self.H.T + self.R)
		self.x = xp + K@(z - self.H@xp)
		self.P = Pp - K@self.H@Pp
		return self.x