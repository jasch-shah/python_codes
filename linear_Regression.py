import sys
import random
import math
import numpy as np
from math import sqrt


random.seed(1024*1024)

class LinearRegression:
    def __init__(self):
        self.w = None
        self.c = 0

    def train(self,X,Y,lamb = 0.0001):
        m,n = X.shape

        x0 = np.matrix(np.ones([m,1]))
        X = np.column_stack([X,x0])

        self.X = X
        self.Y = Y
        self.lamb = lamb

        
