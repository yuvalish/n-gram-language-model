from permutation import *
import random
import math

class SimulatedAnnealing():
    def __init__(self, in_temp, threshold, c_rate):
        self.in_temp = in_temp
        self.threshold = threshold
        self.c_rate = c_rate

    def run(self,in_h,msg,model):
        alpha = self.c_rate
        h = in_h
        t = self.in_temp
        while(t>self.threshold):
            h2 = Permutation.get_neighbor(h)
            delta = Permutation.get_energy(h2,model,msg) - Permutation.get_energy(h,model,msg)
            if(delta<0):
                p=1
            else:
                p=math.exp(-delta/t)
            r = random.random()
            if(r<p):
                h=h2
            t = alpha*t
        return(h)
