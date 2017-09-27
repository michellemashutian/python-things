import numpy as np
import matplotlib.pyplot as plt
import xlrd

#open excel file and get sheet
myBook = xlrd.open_workbook(r'D:\xx.xlsx')

fontsizes = [8, 16, 24, 32]

fig=plt.figure()
ax0=fig.add_subplot(221)
ax1=fig.add_subplot(222)
ax2=fig.add_subplot(223)
ax3=fig.add_subplot(224)



mySheet0 = myBook.sheet_by_index(9)

dimension0 = mySheet0.col(0)
dimension0 = [x.value for x in dimension0]
km0 = mySheet0.col_values(1)
db0 = mySheet0.col_values(2)
ap0 = mySheet0.col_values(3)
#bi0 = mySheet0.col_values(4)
dimension0.pop(0)
km0.pop(0)
db0.pop(0)
ap0.pop(0)
#bi0.pop(0)
'''
db0=np.array([0.595235086,0.384555585,0.393931283,0.255923129,
              0.125761804,0.117657631,-0.033606735,
              None,0.015254252,0.015254252])

km0=np.array([0.689536741,0.523599475,0.517648499,0.346313395,
              0.245282299,None,None,
              None,None,None])
'''
ax0.plot(dimension0,km0,color='blue',marker='s',markerfacecolor='blue',markersize=4,label='KM')
ax0.plot(dimension0,db0,color='red',marker='^',markerfacecolor='red',markersize=4,label='DB')
ax0.plot(dimension0,ap0,color='green',marker='*',markerfacecolor='green',markersize=4,label='AP')
#ax0.plot(dimension0,bi0,color='black',marker='o',markerfacecolor='black',markersize=4,label='BI')
ax0.set_xlabel('a', fontsize=20)#

'''
mySheet1 = myBook.sheet_by_index(6)
dimension1 = mySheet1.col(0)
dimension1 = [x.value for x in dimension1]
#km1 = mySheet1.col_values(1)
db1 = mySheet1.col_values(2)
ap1 = mySheet1.col_values(3)
#bi1 = mySheet1.col_values(4)
dimension1.pop(0)
#km1.pop(0)
db1.pop(0)
ap1.pop(0)
#bi1.pop(0)

km1=np.array([0.689536741,0.523599475,0.517648499,0.346313395,
               0.245282299,None,None,None,None,None])

ax1.plot(dimension1,km1,color='blue',marker='s',markerfacecolor='blue',markersize=4,label='KM')
ax1.plot(dimension1,db1,color='red',marker='^',markerfacecolor='red',markersize=4,label='DB')
ax1.plot(dimension1,ap1,color='green',marker='*',markerfacecolor='green',markersize=4,label='AP')
#ax1.plot(dimension1,bi1,color='black',marker='o',markerfacecolor='black',markersize=4,label='BI')
ax1.set_xlabel('b', fontsize=20)


mySheet2 = myBook.sheet_by_index(7)
dimension2 = mySheet2.col(0)
dimension2 = [x.value for x in dimension2]
km2 = mySheet2.col_values(1)
db2 = mySheet2.col_values(2)
ap2 = mySheet2.col_values(3)
#bi2 = mySheet2.col_values(4)
dimension2.pop(0)
km2.pop(0)
db2.pop(0)
ap2.pop(0)
#bi2.pop(0)

'''
#lsi2=np.array([0.689536741,0.523599475,0.517648499,0.346313395,
               #0.245282299,None,None,None,None,None])
'''
ax2.plot(dimension2,km2,color='blue',marker='s',markerfacecolor='blue',markersize=4,label='KM')
ax2.plot(dimension2,db2,color='red',marker='^',markerfacecolor='red',markersize=4,label='DB')
ax2.plot(dimension2,ap2,color='green',marker='*',markerfacecolor='green',markersize=4,label='AP')
#ax2.plot(dimension2,bi2,color='black',marker='o',markerfacecolor='black',markersize=4,label='BI')
ax2.set_xlabel('c', fontsize=20)#



mySheet3 = myBook.sheet_by_index(8)
dimension3 = mySheet3.col(0)
dimension3 = [x.value for x in dimension3]
km3 = mySheet3.col_values(1)
db3 = mySheet3.col_values(2)
ap3 = mySheet3.col_values(3)
#bi3 = mySheet3.col_values(4)
dimension3.pop(0)
km3.pop(0)
db3.pop(0)
ap3.pop(0)
#bi3.pop(0)
'''
#db3=np.array([None,None,None,0.227870938,
              #0.175513077,0.153445294,0.089810881,0.13771758,0.074191676,0.102922177])
'''

ax3.plot(dimension3,km3,color='blue',marker='s',markerfacecolor='blue',markersize=4,label='LSI')
ax3.plot(dimension3,db3,color='red',marker='^',markerfacecolor='red',markersize=4,label='LDA')
ax3.plot(dimension3,ap3,color='green',marker='*',markerfacecolor='green',markersize=4,label='D2V')
#ax3.plot(dimension3,bi3,color='black',marker='o',markerfacecolor='black',markersize=4,label='BI')
ax3.set_xlabel('d', fontsize=20)


#handles, labels = ax3.get_legend_handles_labels()
ax3.legend(loc=8,ncol=3,bbox_to_anchor=(0, 0.02), borderaxespad=30)#,handles,labels,bbox_to_anchor=(1.02, 0.6), borderaxespad=0.1.05
'''
plt.show()
