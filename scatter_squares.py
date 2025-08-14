#!/usr/bin/python3
# -*- coding=utf-8 -*-

# ===================================
# @Filename: scatter_squares.py
# @Author: Longwei Zhang
# @Create Time: 5/16/25 17:57
# @Email:lz539@georgetown.edu
# @Description: 
# ===================================


import matplotlib.pyplot as plt


plt.style.use('seaborn-v0_8')
fig, ax= plt.subplots()
x = range(1,1001)
y = [i**2 for i in x]
print(y)
ax.scatter(x, y,c=y,cmap=plt.cm.Blues, s=10)

# Set the range of the axis
ax.axis([0,1100,0,1100000])

# Set the title and label the axes
ax.set_title('Square Numbers',fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)
plt.savefig('square_plot.png',bbox_inches='tight')
plt.show()

# Excecise
plt.style.use('seaborn-v0_8')
fig1, ax1 = plt.subplots()
x = range(1,100)
y = [i**3 for i in x]
ax1.scatter(x, y,c=y,cmap=plt.cm.Reds, s=10)

ax.set_title('Cube',fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cube', fontsize=14)
plt.show()
