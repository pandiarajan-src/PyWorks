import logging
import threading

def get_logger():
    logger = logging.getLogger("threading logger")
    logger.setLevel(logging.DEBUG)
    logger_file_handler = logging.FileHandler("threading.log")
    formatter = logging.Formatter("%(asctime)s - %(threadName)s - %(levelname)s - %(message)s")
    logger_file_handler.setFormatter(formatter)
    logger.addHandler(logger_file_handler)
    return logger

def doubler(number, logger):
    """
    function that will be called inside the thread
    """
    logger.debug("doubler thread starting now...")
    result = number*2
    #logger.debug("doubler thread function eneded with {}".format(result))
    logger.debug(f"doubler thread function ended with {result}")

class MyCustomThread(threading.Thread):
    def __init__(self, number, logger):
        threading.Thread.__init__(self)
        self.number = number
        self.logger = logger

    def run(self):
        self.logger.debug("Calling doubler in thread")
        doubler(self.number, self.logger)


if __name__ == "__main__":
    logger = get_logger()
    thread_names = ["A", "B", "C", "D", "E", "F"]
    #
    # Normal thread call
    #
    # for i in range(5):
    #     my_thread = threading.Thread(target=doubler, name=thread_names[i], args=(i, logger))
    #     my_thread.start()

    #
    # Calling custom thread class
    #
    for i in range(5):
        my_thread = MyCustomThread(i, logger)
        my_thread.setName(thread_names[i])
        my_thread.start()


        

