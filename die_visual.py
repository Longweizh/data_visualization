#!/usr/bin/python3
# -*- coding=utf-8 -*-

# ===================================
# @Filename: die_visual.py
# @Author: Longwei Zhang
# @Create Time: 8/16/25 18:20
# @Email: longwei2@illinois.edu
# ===================================


from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Create a D6
die_1 = Die(6)
die_2 = Die(6)
#die_3 = Die(6)

# Make some rolls and store them
results = [die_1.roll()*die_2.roll() for _ in range(10000)]

# Analyze the results
frequencies = [results.count(value) for value in range(1,
                                                       die_1.num_faces*die_2.num_faces+1)]

# Visualiza the results
x_values = list(range(1,die_1.num_faces*die_2.num_faces+1))
data = Bar(x=x_values, y=frequencies)

x_axis_config = {'title': 'Result','dtick' : 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling D6*D6 10000 times',
                   xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6*d6.html')