#vsm_ap

from __future__ import division
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import AffinityPropagation
from sklearn import metrics
import pickle
import numpy as np
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#result=open(r'D:\\XX.txt','a')
pra=open(r'D:\\deal\\XX_pra.txt','a')
doc=open('D:\\XX.txt','r').read().split('\n')
corpus_tfidf=TfidfVectorizer().fit_transform(doc)

af = AffinityPropagation(preference=None).fit(corpus_tfidf)
cluster_centers_indices = af.cluster_centers_indices_
n_clusters_ = len(cluster_centers_indices)
print n_clusters_

maxpre=np.max(af.affinity_matrix_)
minpre=np.min(af.affinity_matrix_)

af = AffinityPropagation(preference=maxpre).fit(corpus_tfidf)
cluster_centers_indices = af.cluster_centers_indices_
n_clusters_ = len(cluster_centers_indices)
print n_clusters_

af = AffinityPropagation(preference=minpre).fit(corpus_tfidf)
cluster_centers_indices = af.cluster_centers_indices_
n_clusters_ = len(cluster_centers_indices)
print n_clusters_       
