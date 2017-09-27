#random choose lines
import random

def rct(filename,num):
    doc=open('D:\\deal\\'+filename+'\\'+filename+'.txt','r').read().strip().split('\n')
    randomt=open('D:\\deal\\'+filename+'_'+str(num)+'.txt','w')
    randomtext=random.sample(doc,num)
    for text in randomtext:
        randomt.write(text+'\n')
    randomt.close()

def main():
    fn=['en4904_cater','ch4904_cater']#'en4904_cater','ch4904_cater',
    ln=[2452]#1226,2452,3678
    for f in fn:
        for l in ln:
            rct(f,l)

if __name__ =='__main__':
    main()
