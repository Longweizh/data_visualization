#!/usr/bin/python3
# -*- coding=utf-8 -*-

# ===================================
# @Filename: rw_visual_plotly.py
# @Author: Longwei Zhang
# @Create Time: 8/17/25 11:34
# @Email: longwei2@illinois.edu
# ===================================


from random_walk import RandomWalk
from plotly.graph_objs import Scatter,Layout
from plotly import offline

rw = RandomWalk()
rw.fill_walk()

data = Scatter(x=rw.x_values,y=rw.y_values)
layout = Layout(title='Random Walk',
                xaxis=dict(title = "x"),
                yaxis=dict(title = 'y'))

offline.plot({"data":data,"layout":layout}, filename='random_walk.html')