from multiprocessing import Event
import threading
from queue import Queue

def Creator(data, q):
    for item in data:
        evt = threading.Event()
        q.put((item, evt))
        print(f"{item} is put in queue to be doubled\n")
        evt.wait()

def Consumer(q):
    while True:
        data, evt = q.get()
        print(f"{data} was processed and doubled result is : {data * 2}")
        evt.set()
        q.task_done()

    pass

if __name__ == "__main__":
    q = Queue()
    data = [10, 5, 3, -5]
    creator_thread = threading.Thread(target=Creator, args=(data,q))
    consumer_thread = threading.Thread(target=Consumer, args=(q,))
    creator_thread.start()
    consumer_thread.start()

    q.join()
