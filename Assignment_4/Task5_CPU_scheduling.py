def fcfs(processes):
    print("\n--- FCFS Scheduling ---")
    wt = [0] * len(processes)
    tat = [0] * len(processes)

    for i in range(1, len(processes)):
        wt[i] = wt[i-1] + processes[i-1][1]

    for i in range(len(processes)):
        tat[i] = wt[i] + processes[i][1]

    avg_wt = sum(wt)/len(wt)
    avg_tat = sum(tat)/len(tat)

    print("Waiting Time:", wt)
    print("Turnaround Time:", tat)
    print("Average WT =", avg_wt)
    print("Average TAT =", avg_tat)


def sjf(processes):
    print("\n--- SJF Scheduling ---")
    processes.sort(key=lambda x: x[1])
    fcfs(processes)


def round_robin(processes, quantum):
    print("\n--- Round Robin Scheduling ---")
    burst = [p[1] for p in processes]
    wt = [0]*len(processes)
    t = 0

    while True:
        done = True
        for i in range(len(processes)):
            if burst[i] > 0:
                done = False
                if burst[i] > quantum:
                    t += quantum
                    burst[i] -= quantum
                else:
                    t += burst[i]
                    wt[i] = t - processes[i][1]
                    burst[i] = 0
        if done:
            break

    tat = [processes[i][1] + wt[i] for i in range(len(processes))]
    print("Waiting Time:", wt)
    print("Turnaround Time:", tat)
    print("Average WT =", sum(wt)/len(wt))
    print("Average TAT =", sum(tat)/len(tat))


def priority(processes):
    print("\n--- Priority Scheduling ---")
    processes.sort(key=lambda x: x[2])  # sort by priority
    fcfs(processes)


if __name__ == "__main__":
    # (process_id, burst_time, priority)
    processes = [(1, 5, 2), (2, 3, 1), (3, 8, 4), (4, 6, 3)]
    quantum = 2

    fcfs(processes.copy())
    sjf(processes.copy())
    priority(processes.copy())
    round_robin(processes.copy(), quantum)
