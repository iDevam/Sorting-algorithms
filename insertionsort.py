import time
import random
import numpy as np
import matplotlib.pyplot as plt

class insertionSort():
    
    def __init__(self,x):
        print("insertionSort initialised")
        self.x = x
        self.sort()

    def sort(self):
        sorted_len = 0
        while sorted_len < len(self.x):
            self.insert(sorted_len)
            sorted_len = sorted_len + 1

    def insert(self,sorted_len):
        i = sorted_len #index of element to put in correct place
        for j in range(sorted_len-1,-1,-1):
            if self.x[j] > self.x[i]:
                self.x[j], self.x[i] = self.x[i], self.x[j]
                i = i-1
            else:
                return
        return


def main():
    len_list = [2**i for i in range(6,14,1)]
    t_list = []
    for l in len_list:
        x = [random.random() for j in range(l)]
        t = time.time()
        iS = insertionSort(x)
        delta_t = time.time() - t
        print("Time taken: " + str(np.round(delta_t,7)) + " s.")
        print("-"*10)
        t_list.append(delta_t)

    plt.loglog(len_list,t_list)
    plt.xlabel('List size')
    plt.ylabel('Time (s)')
    plt.title('Insertion Sort Time Complexity')
    plt.show()

if __name__ == "__main__":
    main()
