import time
import random
import numpy as np
import matplotlib.pyplot as plt

class bubbleSort():
    
    def __init__(self,x):
        print("bubbleSort initialised")
        self.x = x
        self.sort()

    def sort(self):
        n_swaps = 1
        while n_swaps > 0:
            n_swaps = 0
            for i in range(len(self.x)-1):
                if self.x[i] > self.x[i+1]:
                    self.x[i], self.x[i+1] = self.x[i+1], self.x[i]
                    n_swaps = n_swaps + 1
            
def main():
    len_list = [2**i for i in range(6,20,1)]
    t_list = []
    for l in len_list:
        x = [random.random() for j in range(l)]
        t = time.time()
        bs = bubbleSort(x)
        delta_t = time.time() - t
        print("Time taken: " + str(np.round(delta_t,7)) + " s.")
        print("-"*10)
        t_list.append(delta_t)

    plt.loglog(len_list,t_list)
    plt.xlabel('List size')
    plt.ylabel('Time (s)')
    plt.title('Bubblesort Time Complexity')
    plt.show()

if __name__ == "__main__":
    main()
