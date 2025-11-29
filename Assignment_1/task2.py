import os

def execute_commands(commands):
    for cmd in commands:
        pid = os.fork()
        if pid == 0:
            print(f"\nExecuting '{cmd}' in Child PID: {os.getpid()}")
            os.execvp(cmd, [cmd])
        else:
            os.wait()

if __name__ == "__main__":
    cmds = ["ls", "date", "whoami"]
    execute_commands(cmds)
