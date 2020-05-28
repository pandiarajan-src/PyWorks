'''Logging temperature using our own log hanlder'''
import logging
import time
import sys
import random as rand


LOG_FORMAT = '%(name)s : %(levelname)s : %(asctime)s : %(message)s '
#******Use basic config of root handler******
logging.basicConfig(level=logging.DEBUG, filename='log_ex.log', filemode='a', format=LOG_FORMAT)

LOGGER = logging.getLogger(__name__)

#********Defining your own handler and add to logger**********
#F_HANDLER = logging.FileHandler("log_ex.log", "a")
#F_HANDLER.setLevel(logging.DEBUG)
#FORMATTER = logging.Formatter(LOG_FORMAT)
#F_HANDLER.setFormatter(FORMATTER)
#LOGGER.addHandler(F_HANDLER)
#**************************************************************

if __name__ == "__main__":
    INDEX = 0
    while INDEX < 60:
        TEMPERATURE = rand.randint(20, 40)
        if 20 <= TEMPERATURE <= 25:
            LOGGER.info("Current Temperature is %s, enjoy!!!", TEMPERATURE)
        elif 25 <= TEMPERATURE <= 30:
            LOGGER.warning("Current Temperature is %s, stay safe!!!", TEMPERATURE)
        elif 30 <= TEMPERATURE <= 35:
            LOGGER.error("Current Temperature is %s, above the threshold, turn on coller",\
                         TEMPERATURE)
        elif 35 <= TEMPERATURE <= 40:
            LOGGER.critical("Current Temperature is %s, stay home, no outside, turn high cool",\
                            TEMPERATURE)
        else:
            LOGGER.error("This should not happen, pls check the system")
        INDEX += 1
        time.sleep(1)
    sys.exit(1)
