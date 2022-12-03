import logging
import threading

# Play on this variable
#lock = threading.Lock()
lock = threading.RLock()

def do_something():
    with lock:
        print("doing something here...")
    print("do_something end by releasing the lock")
    return "Done doing something"


def do_something_else():
    with lock:
        print("doing something else here...")
    print("do_something_else end by releasing the lock")
    return "Done doing something else"

def main():
    with lock:
        res_1 = do_something()
        res_2 = do_something_else()
    print(res_1)
    print(res_2)

if __name__ == "__main__":
    for i in range(5):
        my_thread = threading.Thread(target=main)
        my_thread.start()



    
