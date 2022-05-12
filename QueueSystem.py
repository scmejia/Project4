import multiprocessing as multi
import threading as th
from random import randint
from time import sleep

def PrintText(index, process):
    print("START %d%s: Call: %d ; Process %s " % (index, process, index, process))
    sleep(randint(1,10))
    print("END %d%s: Call: %d ; Process %s " % (index, process, index, process))

def BuildQueue(queue,process):
    index = queue.get()
    PrintText(index,process);

if __name__ == '__main__':
    queue1 = multi.Queue()
    queue2 = multi.Queue()

    #Queue System
    p1 = multi.Process(target=BuildQueue, args=(queue1,1))
    p1.start()
    p1 = multi.Process(target=BuildQueue, args=(queue1,1))
    p1.start()
    p1 = multi.Process(target=BuildQueue, args=(queue1,1))
    p1.start()
    p2 = multi.Process(target=BuildQueue, args=(queue2,2))
    p2.start()
    p2 = multi.Process(target=BuildQueue, args=(queue2,2))
    p2.start()
    p2 = multi.Process(target=BuildQueue, args=(queue2,2))
    p2.start()
    
    queue1.put(0)
    queue1.put(1)
    queue1.put(2)
    queue2.put(0)
    queue2.put(1)
    queue2.put(2)
    
    p1.join()
    p2.join()
