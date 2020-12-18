import HateSpeech as ht
import Spamdetector as sp
import Readefficiency as rd
from textclass import _MLmodel 
import ml 

class LearningApi:
		__data=''
		def __init__(self,__data):
				self.__data=__data
			    

		def modelTopicDifferncerML(self):
				return ml._PredictML(LearningApi.__data)


		def modelTopicDifferncerNN(self):
				return _MLmodel._PredictNN(LearningApi.__data)
		

		def modelHatedetector(self):
				return  ht.predictHate(LearningApi.__data)
		
		def ReadablityTester(self):
				return rd.Readtesting(LearningApi.__data)

		def modelSpamdetector(self):
				return sp.predictSpam(LearningApi.__data)

		#def output(self):
		#	return str(LearningApi.modelTopicDifferncerML())+" : "+str(LearningApi.modelSpamdetector())+" : "+str(LearningApi.ReadablityTester())+" : "+str(LearningApi.modelHatedetector())
