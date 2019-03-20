import threading
import time
import numpy as np
import random
import quicksort
import bubblesort
import heapsort

class myThread(threading.Thread):
    def __init__(self,threadID,sorting_alg,x):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.sorting_alg = sorting_alg
        self.x = x
        print("Thread " + str(threadID) + " implementing " + str(sorting_alg) +  " started.")
    
    def run(self):
        t = time.time()
        self.sorting_alg(self.x)
        dt = time.time() - t
        print("Thread " + str(self.threadID) + " finished in " + str(np.round(dt,7)) + " s.")

def main():
    print("Hello world")
    x = [random.random() for j in range(10000)]
    
    thread1 = myThread(1,quicksort.quickSort,x)
    thread2 = myThread(2,bubblesort.bubbleSort,x)
    thread3 = myThread(3,heapsort.heapSort,x)
    
    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

if __name__ == "__main__":
    main()
