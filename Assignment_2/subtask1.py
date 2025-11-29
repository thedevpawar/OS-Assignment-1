# subtask1.py
# Subtask 1: Initialize Logging System

import logging

def init_logging():
    logging.basicConfig(
        filename='process_log.txt',
        level=logging.INFO,
        format='%(asctime)s - %(processName)s - %(message)s'
    )
    logging.info("Logging system initialized.")

if __name__ == "__main__":
    init_logging()
    print("Logging system initialized. Check process_log.txt.")
