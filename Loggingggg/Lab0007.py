# import logging
# from imaplib import Debug
#
# logging.basicConfig(filename="newfile.log",
#                     format="%(asctime)s %(message)s",
#                     filemode="w")
#
# logger=logging.getLogger()
# logger.setLevel(logging.DEBUG)
#
# logger.debug("Harmless debug messages")
# logger.info("It's just a information")
# logger.warning("It's a warning")
# logger.error("Did you try to divide by zero?")
# logger.critical("Internet is down")

import logging

logging.basicConfig(filename="newfile2.log",
                    format="%(asctime)s %(message)s",
                    filemode="w")

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

x=3
y=0

logging.info(f"The values of x and y are {x} and {y}")
try:
    x/y
    logging.info(f"x/y is sucessfull with result {x/y}")
except ZeroDivisionError as e:
    logging.error("ZeroDivisionError"+str(e))

logger.debug("Harmless debug message")
logger.info("It's just a information")
logger.warning("It's a warning message")
logger.error("Did you try to divide by zero?")
logger.critical("Internet is down")