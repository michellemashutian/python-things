import numpy as np
import matplotlib.pyplot as plt
import xlrd
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

#open excel file and get sheet
myBook = xlrd.open_workbook(r'E:\xx.xlsx')

#fontsizes = [8, 16, 24, 32]
 
fig=plt.figure()
ax0=fig.add_subplot(121)
ax1=fig.add_subplot(122)

mySheet0 = myBook.sheet_by_index(11)
#sheet0  get datas
dimension0 = mySheet0.col(0)
dimension0 = [x.value for x in dimension0]
lsi0 = mySheet0.col_values(1)
lda0 = mySheet0.col_values(2)
d2v0 = mySheet0.col_values(3)
d2v00= mySheet0.col_values(4)
#drop the 1st line of the data, which is the name of the data.
dimension0.pop(0)
lsi0.pop(0)
lda0.pop(0)
d2v0.pop(0)
d2v00.pop(0)
#draw
'''
ax0.plot(dimension0,lsi0,color='blue',label='LSI')
ax0.plot(dimension0,lda0,color='red',label='LDA')
ax0.plot(dimension0,d2v0,color='green',label='D2V')

'''
ax0.plot(dimension0,lsi0,color='y',label='kmeans')
ax0.plot(dimension0,lda0,color='c',label='dbscan')
ax0.plot(dimension0,d2v0,color='m',label='ap')
ax0.plot(dimension0,d2v00,color='black',label='birch')

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
'''
handles, labels = ax1.get_legend_handles_labels()
ax1.legend(handles, labels,loc=2,bbox_to_anchor=(1.02, 0.2), borderaxespad=0.)#1.05

'''
#show the figure
plt.show()
