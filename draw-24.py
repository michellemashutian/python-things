import numpy as np
import matplotlib.pyplot as plt
import xlrd

#open excel file and get sheet
myBook = xlrd.open_workbook(r'D:\desktop\book.xlsx')

fontsizes = [8, 16, 24, 32]

fig=plt.figure()
ax0=fig.add_subplot(121)
ax1=fig.add_subplot(122)

mySheet0 = myBook.sheet_by_index(42)
#sheet0  get datas
dimension0 = mySheet0.col(0)
dimension0 = [x.value for x in dimension0]
kmeans0 = mySheet0.col_values(1)
dbscan0 = mySheet0.col_values(2)
ap0 = mySheet0.col_values(3)
birch0 = mySheet0.col_values(4)
#drop the 1st line of the data, which is the name of the data.
dimension0.pop(0)
kmeans0.pop(0)
dbscan0.pop(0)
ap0.pop(0)
birch0.pop(0)

#draw
ax0.plot(dimension0,kmeans0,color='black',marker='*',markerfacecolor='black',markersize=6,label='KM')
ax0.plot(dimension0,dbscan0,color='blue',marker='s',markerfacecolor='blue',markersize=6,label='DBSCAN')
ax0.plot(dimension0,ap0,color='red',marker='^',markerfacecolor='red',markersize=6,label='AP')
ax0.plot(dimension0,birch0,color='green',marker='o',markerfacecolor='green',markersize=6,label='BIRCH')
ax0.set_xlabel('a', fontsize=20)#



mySheet1 = myBook.sheet_by_index(43)
#sheet1  get datas
dimension1 = mySheet1.col(0)
dimension1 = [x.value for x in dimension1]
kmeans1 = mySheet1.col_values(1)
dbscan1 = mySheet1.col_values(2)
ap1 = mySheet1.col_values(3)
birch1 = mySheet1.col_values(4)
#drop the 1st line of the data, which is the name of the data.
dimension1.pop(0)
kmeans1.pop(0)
dbscan1.pop(0)
ap1.pop(0)
birch1.pop(0)

ax1.plot(dimension1,kmeans1,color='black',marker='*',markerfacecolor='black',markersize=6,label='VSM')
ax1.plot(dimension1,dbscan1,color='blue',marker='s',markerfacecolor='blue',markersize=6,label='LSI')
ax1.plot(dimension1,ap1,color='red',marker='^',markerfacecolor='red',markersize=6,label='LDA')
ax1.plot(dimension1,birch1,color='green',marker='o',markerfacecolor='green',markersize=6,label='D2V')

ax1.set_xlabel('b', fontsize=20)#


handles, labels = ax1.get_legend_handles_labels()
ax1.legend(handles, labels,loc=2,bbox_to_anchor=(1.02, 0.3), borderaxespad=0.)#1.05


#show the figure
plt.show()
