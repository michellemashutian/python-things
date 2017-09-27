#save thingss

from __future__ import division
from gensim import corpora, models, similarities
import pickle
import numpy as np
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

'''
# for several documents
fn=['XX']
for f in fn: 
    doc=open('E:\\'+f+'.txt','r').read().strip().decode('gbk').split('\n')#.decode('gbk').split('\n')
    texts = [[word for word in document.lower().split(' ')] for document in doc]
    dictionary = corpora.Dictionary(texts)
    dictionary.save('E:\\'+f+'.dict')
    corpus = [dictionary.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize('E:\\'+f+'.mm',corpus)

print 'hello'
'''


doc=open('E:\\XX.txt','r').read().strip().split('\n')#.strip()
texts = [[word for word in document.lower().split(' ')] for document in doc]
dictionary = corpora.Dictionary(texts)
dictionary.save('E:\\XX.dict')
corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('E:\\XX.mm',corpus)
