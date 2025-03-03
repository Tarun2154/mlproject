import logging
import os
from datetime import datetime

# Define log directory
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)  # Ensure the directory exists

# Define log file path
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Create a logger instance
logger = logging.getLogger("mlproject_logger")
logger.setLevel(logging.INFO)

# Avoid duplicate handlers if script is run multiple times
if not logger.hasHandlers():
    # Create a file handler
    file_handler = logging.FileHandler(LOG_FILE_PATH)
    file_handler.setFormatter(logging.Formatter("[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"))

    # Create a stream handler (console output)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter("[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"))

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

if __name__ == "__main__":
    logger.info("Logging has started")
    print(f"Logging started. Check logs in: {LOG_FILE_PATH}")
