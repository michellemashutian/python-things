#save thingss

from __future__ import division
from gensim import corpora, models, similarities
import pickle
import numpy as np
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

'''
# for several documents
fn=['alluser_final']
for f in fn: 
    doc=open('E:\\'+f+'.txt','r').read().strip().decode('gbk').split('\n')#.decode('gbk').split('\n')
    texts = [[word for word in document.lower().split(' ')] for document in doc]
    dictionary = corpora.Dictionary(texts)
    dictionary.save('E:\\'+f+'.dict')
    corpus = [dictionary.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize('E:\\'+f+'.mm',corpus)

print 'hello'
'''


doc=open('E:\\deal\\asist2017\\enall\\enall.txt','r').read().strip().split('\n')#.strip()
texts = [[word for word in document.lower().split(' ')] for document in doc]
dictionary = corpora.Dictionary(texts)
dictionary.save('E:\\deal\\asist2017\\enall\\enall.dict')
corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('E:\\deal\\asist2017\\enall\\enall.mm',corpus)
