# Priority Scheduling + Round Robin Scheduling
def priority_scheduling(processes):
    processes.sort(key=lambda x: x[2])
    total_wt, total_tat = 0, 0

    print("\nPriority Scheduling Results:")
    print("Process\tAT\tBT\tPriority\tWT\tTAT")

    for i in range(len(processes)):
        if i == 0:
            wt = 0
        else:
            wt = total_tat - processes[i][1]

        tat = wt + processes[i][3]
        total_wt += wt
        total_tat += processes[i][3]

        print(f"P{processes[i][0]}\t{processes[i][1]}\t{processes[i][3]}\t{processes[i][2]}\t{wt}\t{tat}")

    print(f"\nAverage Waiting Time: {total_wt/len(processes):.2f}")
    print(f"Average Turnaround Time: {total_tat/len(processes):.2f}")


def round_robin(processes, quantum):
    rem_bt = [p[3] for p in processes]
    t = 0
    wt = [0] * len(processes)
    tat = [0] * len(processes)

    print("\nRound Robin Scheduling Results:")
    print("Gantt Chart:")

    while True:
        done = True
        for i in range(len(processes)):
            if rem_bt[i] > 0:
                done = False
                print(f"P{processes[i][0]}", end=" -> ")

                if rem_bt[i] > quantum:
                    t += quantum
                    rem_bt[i] -= quantum
                else:
                    t += rem_bt[i]
                    wt[i] = t - processes[i][3]
                    rem_bt[i] = 0

        if done:
            break

    for i in range(len(processes)):
        tat[i] = processes[i][3] + wt[i]

    print("\n\nProcess\tBurst\tWT\tTAT")
    for i in range(len(processes)):
        print(f"P{processes[i][0]}\t{processes[i][3]}\t{wt[i]}\t{tat[i]}")

    print(f"\nAverage Waiting Time: {sum(wt)/len(processes):.2f}")
    print(f"Average Turnaround Time: {sum(tat)/len(processes):.2f}")


processes = [
    [1, 0, 2, 6],
    [2, 1, 1, 8],
    [3, 2, 3, 7],
    [4, 3, 2, 3]
]

priority_scheduling(processes.copy())
round_robin(processes.copy(), quantum=3)
