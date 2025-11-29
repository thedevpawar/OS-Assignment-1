def mft(partition_size, processes):
    print("\nMFT (Fixed Partition) Allocation:")
    for i in range(len(processes)):
        if processes[i] <= partition_size:
            print(f"P{i+1} -> Allocated ({processes[i]} KB)")
        else:
            print(f"P{i+1} -> Not Allocated (Too Large)")

def mvt(total_memory, processes):
    print("\nMVT (Variable Partition) Allocation:")
    allocated = 0
    for i in range(len(processes)):
        if allocated + processes[i] <= total_memory:
            allocated += processes[i]
            print(f"P{i+1} -> Allocated ({processes[i]} KB)")
        else:
            print(f"P{i+1} -> Not Allocated (Memory Full)")

partition_size = 100
total_memory = 300
processes = [80, 120, 50, 30, 150]

mft(partition_size, processes)
mvt(total_memory, processes)
