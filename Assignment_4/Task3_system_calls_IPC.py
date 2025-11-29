import os
import sys

def main():
    # Create pipe
    r, w = os.pipe()
    
    pid = os.fork()  # Fork process

    if pid > 0:
        # Parent process
        os.close(r)
        message = "Hello from Parent Process"
        os.write(w, message.encode())
        os.close(w)
        os.wait()  # Wait for child to finish

    else:
        # Child process
        os.close(w)
        msg = os.read(r, 1024)
        print("Child received message:", msg.decode())
        os.close(r)

if __name__ == "__main__":
    main()
