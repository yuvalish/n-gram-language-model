import random
import math

class Permutation():
    def __init__(self,d):
        self.map = d

    def get_neighbor(self):
        d = self.map.copy()
        lst = [alpha for alpha in d]
        if(len(lst)>1):
            r1 = random.choice(lst)
            r2 = random.choice(lst)
            while(r2==r1):
                r2 = random.choice(lst)
            tmp = d[r1]
            d[r1]=d[r2]
            d[r2]=tmp
        p = Permutation(d)
        return p

    def translate(self, string):
        d = self.map
        new_str=""
        for i in range(len(string)):
            new_str+=d[string[i]]
        return new_str

    def get_energy(self,model,msg):
        new_msg = Permutation.translate(self,msg)
        if(len(new_msg)==0):
            return None
        energy = (-1)*math.log(model.unigram[new_msg[0]],2)
        d = model.bigram
        for i in range(1,len(new_msg)):
            w2 = new_msg[i]
            w1 = new_msg[i-1]
            energy += (-1)*math.log(d[(w2,w1)],2)
        return energy
