import os
import time

def cpu_task(duration):
    end = time.time() + duration
    while time.time() < end:
        pass  # Busy work

def create_priority_processes():
    for nice_value in [0, 5, 10]:
        pid = os.fork()
        if pid == 0:
            os.nice(nice_value)
            print(f"Child PID={os.getpid()} running with nice={nice_value}")
            start = time.time()
            cpu_task(3)
            print(f"Child PID={os.getpid()} finished in {time.time() - start:.2f}s")
            os._exit(0)
    for _ in range(3):
        os.wait()

if __name__ == "__main__":
    create_priority_processes()
