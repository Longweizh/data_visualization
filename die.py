#!/usr/bin/python3
# -*- coding=utf-8 -*-

# ===================================
# @Filename: die.py
# @Author: Longwei Zhang
# @Create Time: 8/16/25 18:13
# @Email: longwei2@illinois.edu
# ===================================


from random import randint

class Die:
    """A class to represent a die"""
    def __init__(self,num_faces=6):
        self.num_faces = num_faces

    def roll(self):
        """Return a random number of the dice"""
        return randint(1,self.num_faces)