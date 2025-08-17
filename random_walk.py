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
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        direction = choice([-1, 1])
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance


    def fill_walk(self):
        """Calculate random walk"""

        # Keep walking until the number of points
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)