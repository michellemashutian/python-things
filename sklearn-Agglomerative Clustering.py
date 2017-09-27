#lda_birch
import math
import pickle
import string
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import Birch
from sklearn import metrics
from sklearn.cluster import AgglomerativeClustering


doc=open('D:\\XX.txt','r').read().split('\n')
corpus_tfidf=TfidfVectorizer().fit_transform(doc)
clusternumber=[18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2]
for c in clusternumber:
    '''
    brch = Birch(n_clusters=c)
    brch.fit(corpus_tfidf)
    labels = brch.labels_ 
    print c,' brch ',brch.fit_predict(corpus_tfidf.todense())
    '''
    agg = AgglomerativeClustering(n_clusters=c, affinity='cosine',linkage='complete')
    agg.fit(corpus_tfidf.todense())
    labels = agg.labels_ 
    print c,' agg ',agg.fit_predict(corpus_tfidf.todense())






