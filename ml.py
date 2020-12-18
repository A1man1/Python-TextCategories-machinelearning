
import re
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_20newsgroups
import _pickle as Pickle

categories=[
'alt.atheism', 
'comp.os.ms-windows.misc',
'comp.sys.ibm.pc.hardware', 
'comp.sys.mac.hardware', 
'comp.windows.x', 
'misc.forsale', 
'rec.autos', 
'rec.motorcycles', 
'rec.sport.baseball', 
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
'rec.motorcycles':3, 
'rec.sport.baseball':4, 
'rec.sport.hockey':4, 
'sci.crypt':9, 
'sci.electronics':5, 
'sci.med':7, 
'sci.space':8, 
'talk.politics.guns':6, 
'talk.politics.mideast':6, 
'talk.politics.misc':6, 
'talk.religion.misc':6
}

maplib={7:'health and fitness',0:'atheism',1:'technology',2:'sales',3:'transport',4:'sports',5:'electroic science',8:'space',6:'social political',9:'cyber security'}



news_train=fetch_20newsgroups(subset='train',categories=categories,shuffle=True)
news_test=fetch_20newsgroups(subset='test',categories=categories,shuffle=True)


from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

text_clf = Pipeline([('vect', TfidfVectorizer()), ('clf', MultinomialNB()) ])

# train the model
def  _PredictML(data):
		text_clf.fit(news_train.data, news_train.target)
		ata=[data]
		vect = text_clf.predict(ata)
		return maplib.get(lib.get(categories[vect[0]]))



