import logging
from logging.handlers import RotatingFileHandler

# Configure logging
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_file = 'logfile.log'
# Create a rotating file handler
rotating_handler = RotatingFileHandler(log_file, maxBytes=1024 * 1024, backupCount=5)
rotating_handler.setFormatter(log_formatter)
# Configure the root logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(rotating_handler)

def logIt(result):

    # Log the result
    logging.info(result)



