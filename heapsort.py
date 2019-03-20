import time
import random
import numpy as np
import matplotlib.pyplot as plt

class heapSort():
    
    def __init__(self,x):
        print("heapSort initialised")
        self.sort(x)

    def sort(self,x):
        unsorted_len = len(x)
        self.heapify(x,unsorted_len)
        while unsorted_len > 0:
            x[0],x[unsorted_len-1] = x[unsorted_len-1],x[0]
            unsorted_len = unsorted_len -1
            self.sift_down(x,0,unsorted_len-1)

    def heapify(self,x,unsorted_len):
        start = self.parentIndex(unsorted_len-1)
        while start >= 0:
            self.sift_down(x,start,unsorted_len-1)
            start = start - 1
            
    def sift_down(self,x,start,end):
        root = start
        while self.leftChildIndex(root) <= end:
            child = self.leftChildIndex(root)
            swap = root
            if x[swap] < x[child]:
                swap = child

            if child+1 <= end and x[swap] < x[child+1]:
                swap = child + 1

            if swap == root:
                return
            else:
                x[root],x[swap] = x[swap],x[root]
                root = swap

    def print_heap(self,x):
        n_levels = int(np.floor(np.log2(len(x))))
        level = 0
        ind = 0
        for level in range(n_levels):
            n_nodes = 2**level
            for i in range(ind, ind + n_nodes):
                print(str(x[i]) + " ", end = "")
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
        x = [np.round(random.random(),3) for j in range(l)]
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
