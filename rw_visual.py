#!/usr/bin/python3
# -*- coding=utf-8 -*-

# ===================================
# @Filename: rw_visual.py
# @Author: Longwei Zhang
# @Create Time: 8/16/25 16:53
# @Email: longwei2@illinois.edu
# @Description: 
# ===================================

import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    # Make the random walk
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Plot the random walk
    plt.style.use('classic')
    fig,ax = plt.subplots(figsize=(15,9))
    point_numbers = range(rw.num_points)
    ax.scatter(0,0,s=100,c='green')
    #ax.scatter(rw.x_values,rw.y_values,s=1,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none')
    ax.plot(rw.x_values,rw.y_values,linewidth=0.5,c='blue')
    ax.scatter(rw.x_values[-1],rw.y_values[-1],s=100,c='red')

    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Do you want to continue?(y/n)")
    if keep_running.lower() == 'n':
        break