# MFT (Fixed partition) and MVT (Variable partition) memory allocation

def mft(partitions, processes):
    allocation = {}
    for p in processes:
        allocated = False
        for i in range(len(partitions)):
            if partitions[i] >= p:
                allocation[p] = f"Partition {i+1}"
                partitions[i] -= p
                allocated = True
                break
        if not allocated:
            allocation[p] = "Not Allocated"
    return allocation


def mvt(memory, processes):
    allocation = {}
    used = 0
    for p in processes:
        if used + p <= memory:
            allocation[p] = f"Allocated, remaining {memory - (used+p)}"
            used += p
        else:
            allocation[p] = "Not enough memory"
    return allocation


partitions = [100, 300, 200, 400]
processes = [212, 417, 112, 426]

print("MFT Allocation:", mft(partitions.copy(), processes))
print("MVT Allocation:", mvt(1000, processes))  # memory=1000
