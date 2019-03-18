import time
import random
import numpy as np
import matplotlib.pyplot as plt

class quickSort():
    
    def __init__(self,x):
        print("Hello!")
        lo = 0
        hi = len(x)-1
        self.sort(x,lo,hi)

    def sort(self,x,lo,hi):
        if lo < hi:
            piv_ind = self.partition(x,lo,hi)
            self.sort(x,lo,piv_ind-1)
            self.sort(x,piv_ind+1,hi)

    def partition(self,x,lo,hi):
        piv = x[hi] 
        i = lo
        for j in range(lo,hi,1):
            if x[j] < piv:
                x[i], x[j] = x[j], x[i]
                i = i + 1
        
        x[i], x[hi] = x[hi], x[i]
        return i


    def median3(self,x,inds):
        if x[inds[0]] <= x[inds[1]] <= x[inds[2]] or x[inds[0]] > x[inds[1]] > x[inds[2]]:
            return inds[1]
        
        if x[inds[1]] <= x[inds[0]] <= x[inds[2]] or x[inds[1]] > x[inds[0]] > x[inds[2]]:
            return inds[0]
        
        return inds[2]


def main():
    len_list = [2**i for i in range(6,20,1)]
    t_list = []
    for l in len_list:
        x = [random.random() for j in range(l)]
        t = time.time()
        qs = quickSort(x)
        delta_t = time.time() - t
        print("Time taken: " + str(delta_t))
        t_list.append(delta_t)
    plt.loglog(len_list,t_list)
    plt.xlabel('List size')
    plt.ylabel('Time (s)')
    plt.title('Quicksort Time Complexity')
    plt.show()

if __name__ == "__main__":
    main()
