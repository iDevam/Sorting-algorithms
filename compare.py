import threading
import time
import numpy as np
import random
import quicksort
import bubblesort
import heapsort
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(10000)

class myThread(threading.Thread):
    def __init__(self,threadID,sorting_alg,x):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.sorting_alg = sorting_alg
        self.x = x
        self.dt = 0
        print("Thread implementing " + str(sorting_alg.__name__) +  " started.")
    
    def run(self):
        t = time.time()
        self.sorting_alg(self.x)
        self.dt = time.time() - t
        print("Thread implementing " + str(self.sorting_alg.__name__) + " finished in " + str(np.round(self.dt,7)) + " s.")

def main():
    len_list = [2**i for i in range(11,15,1)]
    qs_t_list = []
    bs_t_list = []
    hs_t_list = []
    
    for l in len_list:
        print("List size: {}".format(l))
        x = [random.random() for j in range(l)]
        thread1 = myThread(1,quicksort.quickSort,x)
        #thread2 = myThread(2,bubblesort.bubbleSort,x)
        thread3 = myThread(3,heapsort.heapSort,x)
        
        thread1.start()
        #thread2.start()
        thread3.start()
        
        thread1.join()
        #thread2.join()
        thread3.join()

        qs_t_list.append(thread1.dt)
        #bs_t_list.append(thread2.dt)
        hs_t_list.append(thread3.dt)
   
        print("-"*15)

    plt.loglog(len_list,qs_t_list,label='quicksort')
    #plt.loglog(len_list,bs_t_list,label='bubblesort')
    plt.loglog(len_list,hs_t_list,label='heapsort')
    plt.legend(loc='upper left')
    plt.xlabel('List size')
    plt.ylabel('Time (s)')
    plt.title('Time Complexity')
    plt.show()
    


if __name__ == "__main__":
    main()
