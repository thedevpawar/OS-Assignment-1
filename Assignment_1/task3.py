import os
import time

def zombie_process():
    pid = os.fork()
    if pid == 0:
        print(f"Child (Zombie) PID: {os.getpid()}")
        os._exit(0)
    else:
        print(f"Parent PID: {os.getpid()} (not waiting for child)")
        time.sleep(10)
        print("Check using: ps -el | grep defunct")

def orphan_process():
    pid = os.fork()
    if pid == 0:
        time.sleep(5)
        print(f"Orphan Child PID: {os.getpid()}, New Parent PID: {os.getppid()}")
    else:
        print(f"Parent PID: {os.getpid()} exiting early...")
        os._exit(0)

if __name__ == "__main__":
    choice = input("Enter 1 for Zombie or 2 for Orphan: ")
    if choice == "1":
        zombie_process()
    else:
        orphan_process()
