#!/usr/bin/env python
#coding:utf-8
#.decode('gbk')
import lda
from sklearn.feature_extraction.text import CountVectorizer

doc=open('D:\\XX.txt','r').read().decode('gbk').split('\n')#.decode('gbk')
corpus=CountVectorizer().fit_transform(doc)
for i in range(1):
    ss=300
    model = lda.LDA(n_topics=ss, n_iter=2000, random_state=1)
    model.fit(corpus)
    matrix=[] 
    f=open('D:\\XX_lda%s.vec'%ss,'w')#这里改
    for i,term in enumerate(model.doc_topic_):
        print i
        vec=[str(terms) for terms in term]
        matrix.append(' '.join(vec))
    f.write('\n'.join(matrix))
    f.close()
'''
filelist=['enall']
for files in filelist:
    doc=open('E:\\deal\\asist2017\\'+files+'\\'+files+'.txt','r').read().split('\n')#.decode('gbk').split('\n')
    corpus=CountVectorizer().fit_transform(doc)
    for i in range(20):
        ss=10*(i+1)
        model = lda.LDA(n_topics=ss, n_iter=2000, random_state=1)
        model.fit(corpus)
        matrix=[] 
        f=open('E:\\deal\\asist2017\\'+files+'\\lda\\'+files+'_lda%s.vec'%ss,'w')
        for i,term in enumerate(model.doc_topic_):
            print i
            vec=[str(terms) for terms in term]
            matrix.append(' '.join(vec))
        f.write('\n'.join(matrix))
        f.close()
 '''
