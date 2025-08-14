#!/usr/bin/python3
# -*- coding=utf-8 -*-

# ===================================
# @Filename: mpl_squares.py
# @Author: Longwei Zhang
# @Create Time: 5/16/25 17:21
# @Email:lz539@georgetown.edu
# @Description: 
# ===================================


import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots() # subplots here is a function that allow python to
# generate a series of plots. fig means the whole plot and ax means the first
# plot here.
ax.plot(input_values, squares, linewidth=3)

# Set chart table and label the axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=14)

plt.show() # open the viewer
