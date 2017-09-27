import numpy as np
import matplotlib.pyplot as plt
import xlrd
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

#open excel file and get sheet
myBook = xlrd.open_workbook(r'E:xx.xlsx')

#fontsizes = [8, 16, 24, 32]
 
fig=plt.figure()
ax0=fig.add_subplot(5,2,1)
ax1=fig.add_subplot(5,2,2)
ax2=fig.add_subplot(5,2,3)
ax3=fig.add_subplot(5,2,4)
ax4=fig.add_subplot(5,2,5)
ax5=fig.add_subplot(5,2,6)
ax6=fig.add_subplot(5,2,7)
ax7=fig.add_subplot(5,2,8)
ax8=fig.add_subplot(5,2,9)
ax9=fig.add_subplot(5,2,10)



def draw3(index):
    mySheet=myBook.sheet_by_index(index)
    dimension=mySheet.col(0)
    dimension = [x.value for x in dimension]
    lsi = mySheet.col_values(1)
    lda = mySheet.col_values(2)
    d2v = mySheet.col_values(3)
    dimension.pop(0)
    lsi.pop(0)
    lda.pop(0)
    d2v.pop(0)

def draw4(index):
    mySheet=myBook.sheet_by_index(index)
    dimension=mySheet.col(0)
    dimension = [x.value for x in dimension]
    kmeans = mySheet.col_values(1)
    dbscan = mySheet.col_values(2)
    ap = mySheet.col_values(3)
    birch = mySheet.col_values(4)
    dimension.pop(0)
    kmeans.pop(0)
    dbscan.pop(0)
    ap.pop(0)
    birch.pop(0)

draw3()    
    ax0.plot(dimension0,lsi0,color='blue',label='LSI')
    ax0.plot(dimension0,lda0,color='red',label='LDA')
    ax0.plot(dimension0,d2v0,color='green',label='D2V')

'''
ax0.plot(dimension0,lsi0,color='y',label='kmeans')
ax0.plot(dimension0,lda0,color='c',label='dbscan')
ax0.plot(dimension0,d2v0,color='m',label='ap')
ax0.plot(dimension0,d2v00,color='black',label='birch')
ax0.plot(dimension0,kmeans0,color='black',marker='*',markerfacecolor='black',markersize=6,label='KM')
ax0.plot(dimension0,dbscan0,color='blue',marker='s',markerfacecolor='blue',markersize=6,label='DBSCAN')
ax0.plot(dimension0,ap0,color='red',marker='^',markerfacecolor='red',markersize=6,label='AP')
ax0.plot(dimension0,birch0,color='green',marker='o',markerfacecolor='green',markersize=6,label='BIRCH')
ax0.set_xlabel('a', fontsize=20)#


mySheet1 = myBook.sheet_by_index(12)
#sheet1  get datas
dimension1 = mySheet1.col(0)
dimension1 = [x.value for x in dimension1]
lsi1 = mySheet1.col_values(1)
lda1 = mySheet1.col_values(2)
d2v1 = mySheet1.col_values(3)
d2v11 = mySheet0.col_values(4)
#drop the 1st line of the data, which is the name of the data.
dimension1.pop(0)
lsi1.pop(0)
lda1.pop(0)
d2v1.pop(0)
d2v11.pop(0)
'''
ax1.plot(dimension1,lsi1,color='blue',label='LSI')
ax1.plot(dimension1,lda1,color='red',label='LDA')
ax1.plot(dimension1,d2v1,color='green',label='D2V')


ax1.plot(dimension1,lsi1,color='blue',marker='s',markerfacecolor='blue',markersize=9,label='LSI')
ax1.plot(dimension1,lda1,color='red',marker='^',markerfacecolor='red',markersize=9,label='LDA')
ax1.plot(dimension1,d2v1,color='green',marker='o',markerfacecolor='green',markersize=9,label='D2V')


'''
ax1.plot(dimension1,lsi1,color='y',label='LSI')
ax1.plot(dimension1,lda1,color='c',label='LDA')
ax1.plot(dimension1,d2v1,color='m',label='D2V')
ax1.plot(dimension1,d2v11,color='black',label='D2V')
#

ax1.set_xlabel('b', fontsize=20)

#show the figure
plt.show()
