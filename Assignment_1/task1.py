import os

def create_processes(n):
    print(f"Parent PID: {os.getpid()}")
    for i in range(n):
        pid = os.fork()
        if pid == 0:
            print(f"Child {i+1}: PID={os.getpid()}, Parent PID={os.getppid()}")
            print(f"Hello from Child {i+1}!")
            os._exit(0)
        else:
            os.wait()

if __name__ == "__main__":
    n = int(input("Enter number of child processes: "))
    create_processes(n)
