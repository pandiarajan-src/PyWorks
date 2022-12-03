from multiprocessing import Process, current_process
import os

def doubler(number):
    result = number * 2
    pid = os.getpid()
    pname = current_process().name
    print(f"{number} is doubled to {result} by the process id: {pid}, process name: {pname}")


if __name__=="__main__":
    data = [10, 5, 3, -5, 4, 6]
    procs = []
    for item in data:
        proc_name = "PandiProc" + str(item)
        proc = Process(target=doubler, args=(item,), name=proc_name)
        proc.start()
        procs.append(proc)
    
    for p in procs:
        p.join()

