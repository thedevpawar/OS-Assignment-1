import os

def inspect_process(pid):
    try:
        with open(f"/proc/{pid}/status") as f:
            lines = f.readlines()
        print("=== /proc/[pid]/status ===")
        for line in lines[:10]:
            print(line.strip())

        exe_path = os.readlink(f"/proc/{pid}/exe")
        print("\nExecutable Path:", exe_path)

        print("\nOpen File Descriptors:")
        for fd in os.listdir(f"/proc/{pid}/fd"):
            print(f"FD {fd} ->", os.readlink(f"/proc/{pid}/fd/{fd}"))
    except FileNotFoundError:
        print("Invalid PID or process not found.")

if __name__ == "__main__":
    pid = input("Enter PID to inspect: ")
    inspect_process(pid)
