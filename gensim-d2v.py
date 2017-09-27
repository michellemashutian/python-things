#d2v_ap

from __future__ import division
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import AffinityPropagation
from sklearn import metrics
from gensim import corpora, models, similarities
from scipy.sparse import csr_matrix, coo_matrix
import pickle
import numpy as np
import logging
#import time
#import timeit
#import datetime
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
  
for i in range(6):
    s=100*(i+1)
    #Doc2Vec initialize
    div_texts = []
    f = open('D:\\XX.txt')
    result = open('D:\\XX_d2v%s.txt'%s,'w')
    lines = f.readlines()
    f.close()
    for line in lines:
        div_texts.append(line.strip().split(" "))
    sentences = []
    for i in range(len(div_texts)):
        string = "DOC_" + str(i)
        sentence = models.doc2vec.LabeledSentence(div_texts[i], labels = [string])
        sentences.append(sentence)
    d2v = models.Doc2Vec(sentences, size = s, window = 5, min_count = 0, dm = 1)
    #Doc2Vec train
    for i in range(10):
        d2v.train(sentences)
    features=[]
    for i,term in enumerate(sentences):
        feature=[]
        string = "DOC_" + str(i)
        for term in d2v[string]:
            feature.append(term)
        features.append(feature)
    for i in features:
        result.write(str(i)+'\n')
result.close()

       
