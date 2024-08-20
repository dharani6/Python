C:\Users\Dhara\OneDrive\Desktop\Python
import logging
logging.basicConfig(filename = "C:\Users\Dhara\OneDrive\Desktop\Python")
logger = logging.getLogger()

logger.info("My country is India")
logger.debug("My country is India")
logger.warning("My country is India")
logger.error("My country is India")
logger.critical("My country is India")
print(logger.level)

'''
notset = 0
debug = 10
info = 20
warning = 30
error = 40
critical = 50

'''