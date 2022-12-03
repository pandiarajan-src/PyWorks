from multiprocessing import Process, Lock
import multiprocessing
import os
import logging

def print_method(item, lockobj):
    with lockobj:
        print(f"Printing {item} with lock {os.getpid()}")

if __name__ == "__main__":
    print("Starting main")
    lockobj = Lock()
    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.DEBUG)
    items = ['tango', 'lemon', 'orange', 6, 7]
    procs = []
    for item in items:
        proc = Process(target=print_method, args=(item, lockobj))
        proc.start()
        procs.append(proc)

    for p in procs:
        p.join()
        