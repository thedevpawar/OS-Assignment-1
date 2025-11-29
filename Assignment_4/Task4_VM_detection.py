import platform
import subprocess

def detect_vm():
    print("Checking for Virtual Machine environment...\n")

    cpu_info = subprocess.getoutput("lscpu | grep 'Virtualization'")
    print("Virtualization Info:", cpu_info)

    product_name = subprocess.getoutput("cat /sys/class/dmi/id/product_name")
    print("Product Name:", product_name)

    manufacturer = subprocess.getoutput("cat /sys/class/dmi/id/sys_vendor")
    print("Manufacturer:", manufacturer)

    if any(x in product_name.lower() or x in manufacturer.lower() for x in 
           ["vmware", "virtual", "kvm", "qemu", "virtualbox", "hyper-v"]):
        print("\nSystem is likely running inside a Virtual Machine.")
    else:
        print("\nSystem appears to be running on real hardware.")

if __name__ == "__main__":
    detect_vm()
