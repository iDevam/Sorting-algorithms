import time
import random
import numpy as np
import matplotlib.pyplot as plt

class quickSort():
    def __init__(self,x):
        print("quickSort initialised")
        self.lo = 0
        self.hi = len(x)-1
        self.sort(x,self.lo,self.hi)

    def sort(self,x,lo,hi):
        if lo < hi:
            piv_ind = self.partition(x,lo,hi)
            self.sort(x,lo,piv_ind-1)
            self.sort(x,piv_ind+1,hi)

        return x

    def partition(self,x,lo,hi):
        piv = x[hi] 
        i = lo
        for j in range(lo,hi,1):
            if x[j] < piv:
                x[i], x[j] = x[j], x[i]
                i = i + 1
        
        x[i], x[hi] = x[hi], x[i]
        return i

def main():
    len_list = [2**i for i in range(6,20,1)]
    t_list = []
    for l in len_list:
        x = [random.random() for j in range(l)]
        t = time.time()
        qs = quickSort(x)
        delta_t = time.time() - t
        print("Time taken: " + str(np.round(delta_t,7)) + " s.")
        print("-"*10)
        t_list.append(delta_t)
    
    plt.loglog(len_list,t_list)
    plt.xlabel('List size')
    plt.ylabel('Time (s)')
    plt.title('Quicksort Time Complexity')
    plt.show()

if __name__ == "__main__":
    main()
