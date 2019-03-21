import time
import random
import numpy as np
import matplotlib.pyplot as plt

class heapSort():
    
    def __init__(self,x):
        print("heapSort initialised")
        self.x = x
        self.sort()

    def sort(self):
        unsorted_len = len(self.x)
        self.heapify(unsorted_len)
        while unsorted_len > 0:
            self.x[0],self.x[unsorted_len-1] = self.x[unsorted_len-1],self.x[0]
            unsorted_len = unsorted_len -1
            self.sift_down(0,unsorted_len-1)

    def heapify(self,unsorted_len):
        start = self.parentIndex(unsorted_len-1)
        while start >= 0:
            self.sift_down(start,unsorted_len-1)
            start = start - 1
            
    def sift_down(self,start,end):
        root = start
        while self.leftChildIndex(root) <= end:
            child = self.leftChildIndex(root)
            swap = root
            if self.x[swap] < self.x[child]:
                swap = child

            if child+1 <= end and self.x[swap] < self.x[child+1]:
                swap = child + 1

            if swap == root:
                return
            else:
                self.x[root],self.x[swap] = self.x[swap],self.x[root]
                root = swap

    def print_heap(self): #For debugging. Visual aid useful on short lists
        n_levels = int(np.floor(np.log2(len(self.x))))
        level = 0
        ind = 0
        for level in range(n_levels):
            n_nodes = 2**level
            for i in range(ind, ind + n_nodes):
                print(str(self.x[i]) + " ", end = "")
            print("\n")
            ind = ind + n_nodes

    def parentIndex(self,i):
        j = int(np.floor((i-1)/2))
        return j

    def leftChildIndex(self,i):
        j = 2*i + 1
        return j

def main():
    len_list = [2**i for i in range(3,20,1)]
    t_list = []
    for l in len_list:
        x = [np.round(random.random(),4) for j in range(l)]
        t = time.time()
        hs = heapSort(x)
        delta_t = time.time() - t
        print("Time taken: " + str(np.round(delta_t,7)) + " s.")
        print("-"*10)
        t_list.append(delta_t)

    plt.loglog(len_list,t_list)
    plt.xlabel('List size')
    plt.ylabel('Time (s)')
    plt.title('Heapsort Time Complexity')
    plt.show()

if __name__ == "__main__":
    main()
