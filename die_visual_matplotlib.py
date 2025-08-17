#!/usr/bin/python3
# -*- coding=utf-8 -*-

# ===================================
# @Filename: die_visual_matplotlib.py
# @Author: Longwei Zhang
# @Create Time: 8/17/25 11:52
# @Email: longwei2@illinois.edu
# ===================================


import matplotlib.pyplot as plt
from die import Die

die = Die(20)
results = [die.roll() for i in range(10000)]
numbers = [i for i in range(1,die.num_faces+1)]
frequencies = [results.count(j) for j in numbers]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.bar(numbers, frequencies)

## Colors
colors = plt.cm.tab20.colors
ax.bar(numbers, frequencies, color=colors, edgecolor="black", alpha=0.85)

## Titles
ax.set_title("Results of rolling one D20*10000")
ax.set_xlabel("Results")
ax.set_ylabel("Frequency of Results")
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xticks(numbers)
plt.show()