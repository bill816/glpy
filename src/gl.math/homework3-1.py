#!/usr/bin/python
# -*- coding: utf-8 -*-
#copyRight by heibanke 
#%matplotlib inline

from matplotlib import pyplot as plt
import numpy as np

A=np.array([[3],[1]])
C=np.array([[1],[3]])

x=np.linspace(-2,2,10)

"""
x相当于是一维的点。
xx＝Ax相当于讲解图中的OA这条直线。为了打直线图引入的变量。
3x是这条直线的横坐标范围，x是这条直线的纵坐标范围
这里也可以不引入这么多点，引入两个点就行，不过这样可以和后续代码保持一致。
"""
x.shape=(1,10)
xx=A.dot(x)


B=A.T.dot(C)
AA=np.linalg.inv(A.T.dot(A))

#P=Ax^=A*AA*B
P=A*AA*B
E=C-P

fig = plt.figure() #figsize=(10,6)
ax= fig.add_subplot(111)

ax.plot(xx[0,:],xx[1,:])
ax.plot(A[0],A[1],'ko')
ax.plot([C[0],P[0]],[C[1],P[1]],'r-o')
ax.plot([0,C[0]],[0,C[1]],'m-o')
ax.plot([0,E[0]],[0,E[1]],'k-o')

margin=0.1
ax.text(A[0]+margin, A[1]+margin, r"A",fontsize=20)
ax.text(C[0]+margin, C[1]+margin, r"C",fontsize=20)
ax.text(P[0]+margin, P[1]+margin, r"P",fontsize=20)
ax.text(E[0]+margin, E[1]+margin, r"E",fontsize=20)


ax.axis('equal')
plt.show()