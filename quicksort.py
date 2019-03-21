import time
import random
import numpy as np
import matplotlib.pyplot as plt

class quickSort():
    def __init__(self,x):
        print("quickSort initialised")
        self.lo = 0
        self.hi = len(x)-1
        self.x = x
        self.sort(self.lo,self.hi)

    def sort(self,lo,hi):
        if lo < hi:
            piv_ind = self.partition(lo,hi)
            self.sort(lo,piv_ind-1)
            self.sort(piv_ind+1,hi)

    def partition(self,lo,hi):
        piv = self.x[hi] 
        i = lo
        for j in range(lo,hi,1):
            if self.x[j] < piv:
                self.x[i], self.x[j] = self.x[j], self.x[i]
                i = i + 1
        
        self.x[i], self.x[hi] = self.x[hi], self.x[i]
        return i

def main():
    len_list = [2**i for i in range(3,20,1)]
    t_list = []
    for l in len_list:
        x = [np.round(random.random(),3) for j in range(l)]
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
