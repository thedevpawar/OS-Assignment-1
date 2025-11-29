import logging
import time

logging.basicConfig(
    filename='process_log.txt',
    filemode='w',
    level=logging.INFO,
    format='%(asctime)s -%(processName)s -%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def system_process(task_name):
    logging. info(f"{task_name} started")
    time.sleep(2)
    logging.info(f"{task_name} ended")

if __name__ == "__main__":
    print("Running system_process() once ... ")
    system_process("Test-Process")
    print("Task completed. Check process_log.txt.")
