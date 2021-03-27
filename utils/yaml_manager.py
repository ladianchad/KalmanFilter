import yaml
import numpy as np

class YamlReader(object):
	"""docstring for yamlReader"""
	def __init__(self):
		self.conf = None

	def readYaml(self,path):
		with open(path) as f:
			self.conf = yaml.load(f,Loader=yaml.FullLoader)
	def getParams(self,param):
		if self.conf is not None :
			if param in self.conf:
				if isinstance(self.conf[param],list):
					return np.array(self.conf[param])
				else:
					return self.conf[param]
			else:
				return None
		else:
			return None