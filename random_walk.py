#!/usr/bin/python3
# -*- coding=utf-8 -*-

# ===================================
# @Filename: random_walk.py
# @Author: Longwei Zhang
# @Create Time: 8/14/25 08:20
# @Email:lz539@georgetown.edu
# @Description: 
# ===================================


from random import choice

class RandomWalk:
    """A class to generate random walks"""
    def __init__(self, num_points = 1000):
        """Initialize the random walk"""
        self.num_points = num_points

        """All walks starts from 0"""
        self.x_value = 0
        self.y_value = 0

    def fill_walk(self):
        """Calculate random walk"""

        # Keep walking until the number of points
        while len(self.x_value) < self.num_points:
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)



