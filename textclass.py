
import re
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_20newsgroups
import _pickle as Pickle

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

class _MLmodel:
		categories=[
			'alt.atheism', 
			'comp.os.ms-windows.misc',
			'comp.sys.ibm.pc.hardware', 
			'comp.sys.mac.hardware', 
			'comp.windows.x', 
			'misc.forsale', 
			'rec.autos', 
			'rec.sport.hockey', 
			'sci.crypt', 
			'sci.electronics', 
			'sci.med', 
			'sci.space', 
			'talk.politics.guns', 
			'talk.politics.mideast', 
			'talk.politics.misc', 
			'talk.religion.misc'
		]

		lib={
		'alt.atheism':0, 
		'comp.os.ms-windows.misc':1,
		'comp.sys.ibm.pc.hardware':1, 
		'comp.sys.mac.hardware':1, 
		'comp.windows.x':1, 
		'misc.forsale':2, 
		'rec.autos':3, 
		'rec.sport.hockey':4, 
		'sci.crypt':5, 
		'sci.electronics':5, 
		'sci.med':5, 
		'sci.space':5, 
		'talk.politics.guns':6, 
		'talk.politics.mideast':6, 
		'talk.politics.misc':6, 
		'talk.religion.misc':6
		}

		maplib={0:'atheism',1:'technology',2:'sales',3:'transport',4:'sports',5:'science',6:'social political'}
		_news_train=fetch_20newsgroups(subset='train',categories=categories,shuffle=True)
		_news_test=fetch_20newsgroups(subset='test',categories=categories,shuffle=True)






#text=input("enter your data")
# train the model
		def  _PredictNN(data):
				__text_clf = Pipeline([('vect', TfidfVectorizer()), ('clf',  MLPClassifier(hidden_layer_sizes=(5,2),activation='identity',learning_rate='constant',max_iter=500,verbose=True, random_state=1)) ])  
				__text_clf.fit(_MLmodel._news_train.data,_MLmodel._news_train.target)
				ata=[data]
				vect=__text_clf.predict(ata)
				return _MLmodel.maplib.get(_MLmodel.lib.get(_MLmodel.categories[vect[0]]))

		def  _PredictML(data):
				__text_clf = Pipeline([('vect', TfidfVectorizer()), ('clf', MultinomialNB()) ])  
				__text_clf.fit(_MLmodel._news_train.data,_MLmodel._news_train.target)
				ata=[data]
				vect=__text_clf.predict(ata)
				return _MLmodel.maplib.get(_MLmodel.lib.get(_MLmodel.categories[vect[0]]))      
#with open('Nlclassifier.pkl', 'rb') as fid:
#						text_clf = Pickle.load(fid)
#ata=[text]
#vect=text_clf.predict(ata)
#ata=[text]
#print(ata)
#data=re.split('[!|.|?]+',text)
#vect2 = text_clf.predict(data)
#vect = text_clf.predict(ata)

#print('result1 ata',vect)
#print(categories[vect[0]])
#print(lib.get(categories[vect[0]]))
#print(maplib.get(lib.get(categories[vect[0]])))


#print('result2 data',vect2)
#print(categories[vect2[0]])
#print(lib.get(categories[vect2[0]]))
#print(maplib.get(lib.get(categories[vect2[0]])))
