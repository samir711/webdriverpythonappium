# Q3. Find out the pypi module available which can be used to perform the following activity -
#
# a. read and write excel file
# b. generate logs.

# logging  packages - logging
# https://blog.scalyr.com/2018/02/started-quickly-python-logging/


import logging as logger  # logging

logger.basicConfig(filename='.\App_TestLogs\demo.log', level=logger.DEBUG)

logger.warning("I'm a warning!")
logger.info("Hello, Python!")
logger.debug("I'm a debug message!")