import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Set up logging to standard output
logging.basicConfig(level=logging.INFO, format=logging_str)

logger = logging.getLogger("BOC_Exchangerates_Scrapper_Logger")