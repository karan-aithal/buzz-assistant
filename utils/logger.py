import logging
from logging.handlers import RotatingFileHandler

def setup_logger():
    logger = logging.getLogger("AI_Assistant")
    logger.setLevel(logging.INFO)

    # Rotating File Handler
    handler = RotatingFileHandler("app.log", maxBytes=5 * 1024 * 1024, backupCount=3)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger

logger = setup_logger()
