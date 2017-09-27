#lsi_ap

from __future__ import division
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import AffinityPropagation
from sklearn import metrics
from gensim import corpora, models, similarities
import pickle
import numpy as np
import logging
import time
import timeit
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)



dictionary = corpora.Dictionary.load('E:\\XX.dict')
corpus = corpora.MmCorpus('E:\\XX.mm')
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
for i in range(1):   
    s=150
    result=open(r'E:\\XX_final_'+str(s)+'.txt','a')
    #LSI model 
    lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=s)
    lsi_vec=lsi[corpus_tfidf]   
    features=[]
    for term in lsi_vec:
        features.append([terms[1] for terms in term])
    for i in features:
        result.write(str(i)+'\n')
result.close()




        
