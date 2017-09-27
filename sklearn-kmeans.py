#vsm_kmeans

from __future__ import division
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn import metrics
import pickle
import numpy as np
import datetime
import time
import timeit
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


result=open(r'D:\\result\\iconference_vsm_kmeans.txt','a')
#vsm
filelist=['en9808','ch9808']#,'en4904','ch4904'
for files in filelist:
    doc=open('D:\\deal\\'+files+'\\'+files+'.txt','r').read().split('\n')
    corpus_tfidf=TfidfVectorizer().fit_transform(doc)
    for m in range(10):
        kms = KMeans(init='k-means++', n_clusters=20).fit(corpus_tfidf)
        labels = kms.labels_
        true_labels=open('D:\\deal\\catergory1.txt').read().split('\n')
                #ss=metrics.silhouette_score(corpus_tfidf.todense(), labels, metric='sqeuclidean')
                #homogeneity_score=metrics.homogeneity_score(true_labels,labels)
                #completeness_score=metrics.completeness_score(true_labels,labels)
        v_measure_score=metrics.v_measure_score(true_labels,labels)
        result.write(str(files)+'  '+str(v_measure_score)+'\n')
        #str(ss)+tr(homogeneity_score)+' '+str(completeness_score)+' '+
        print m,' ',files,' is done' 
result.close()

'''
# lsi
result=open(r'E:\\result\\asist2017\\lsi_kmeans.txt','a')
filelist=['chall','enall']
clusterlist=[25]#10,20,30,40,50
for files in filelist:
    dictionary = corpora.Dictionary.load('E:\\deal\\asist2017\\'+files+'\\'+files+'.dict')
    corpus = corpora.MmCorpus('E:\\deal\\asist2017\\'+files+'\\'+files+'.mm')
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    for i in range(20):
        s=10*(i+1)
        #LSI模型
        lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=s)
        lsi_vec=lsi[corpus_tfidf]   
        features=[]
        for term in lsi_vec:
            features.append([terms[1] for terms in term])
        for clusters in clusterlist:
            for m in range(10):
                kms = KMeans(init='k-means++', n_clusters=clusters).fit(np.array(features)) 
                labels = kms.labels_
                true_labels=open('E:\\deal\\asist2017\\label.txt').read().split('\n')   
                #ss=metrics.silhouette_score(np.array(features), labels, metric='sqeuclidean')
                #homogeneity_score=metrics.homogeneity_score(true_labels,labels)
                #completeness_score=metrics.completeness_score(true_labels,labels)
                v_measure_score=metrics.v_measure_score(true_labels,labels)
                result.write(str(files)+' '+str(s)+' '+str(v_measure_score)+'\n')
                             #str(ss)+' '+
                             #str(homogeneity_score)+' '+str(completeness_score)+' '+
                print files,' lsi dimension',s,' is done'
result.close()
'''

'''
#lda
result=open(r'E:\\result\\asist2017\\lda_kmeans.txt','a')
filelist=['chall','enall']
clusterlist=[25]
for files in filelist:
    for i in range(20):
        s=10*(i+1)
        lda_vec=open('E:\\deal\\asist2017\\'+files+'\\lda\\'+files+'_lda%s.vec'%s,'r').read().split('\n')
        features=[]
        for term in lda_vec:
            features.append([string.atof(num) for num in term.split(' ')])
        for clusters in clusterlist:
            for m in range(10):
                kms = KMeans(init='k-means++', n_clusters=clusters).fit(np.array(features)) 
                labels = kms.labels_
                true_labels=open('E:\\deal\\asist2017\\label.txt').read().split('\n')   
                #ss=metrics.silhouette_score(np.array(features), labels, metric='sqeuclidean')
                #homogeneity_score=metrics.homogeneity_score(true_labels,labels)
                #completeness_score=metrics.completeness_score(true_labels,labels)
                v_measure_score=metrics.v_measure_score(true_labels,labels)
                result.write(str(files)+' '+str(s)+' '+str(v_measure_score)+'\n')
                             #str(ss)+' '+
                             #str(homogeneity_score)+' '+str(completeness_score)+' '+                           
                print files,' lda dimension',s,' is done'
result.close()
'''
'''
#d2v
result=open(r'E:\\result\\asist2017\\d2v_kmeans.txt','a')
filelist=['chall','enall']
clusterlist=[25]#10,20,30,40,50
for files in filelist:
    for i in range(20):
        s=10*(i+1)
        #Doc2Vec initialize
        div_texts = []
        f = open('E:\\deal\\asist2017\\'+files+'\\'+files+'.txt')
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
        for clusters in clusterlist:
            for m in range(10):
                kms = KMeans(init='k-means++',n_clusters=clusters).fit(np.array(features))
                labels = kms.labels_
                true_labels=open('D:\\deal\\catergory.txt').read().split('\n')
                #ss=metrics.silhouette_score(np.array(features), labels, metric='sqeuclidean')
                #homogeneity_score=metrics.homogeneity_score(true_labels,labels)
                #completeness_score=metrics.completeness_score(true_labels,labels)
                v_measure_score=metrics.v_measure_score(true_labels,labels)
                result.write(str(files)+' '+str(s)+' '+str(v_measure_score)+'\n')
                print files,' d2v dimension',s,' is done'
result.close()
'''
        
