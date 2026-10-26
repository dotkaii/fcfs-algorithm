# First Come First Serve Scheduling Algorithm
n = int(input("Enter number of processes: "))

processes = []

for i in range(n):
    at = int(input(f"Enter arrival time for process {i+1}: "))
    bt = int(input(f"Enter burst time for process {i+1}: "))
    processes.append([i+1, at, bt])

# Processes is a list of lists where each inner list contains [process_id, arrival_time, burst_time]
# For example, if there are 3 processes with arrival times and burst times as follows:
# processes = [[1, 0, 5], 
#              [2, 1, 3],
#              [3, 2, 1]]

# Sort processes based on arrival time
processes.sort(key=lambda x: x[1])

time = 0
total_wt = 0
total_tat = 0

print("Process\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time")

for pid, at, bt in processes:

    time = max(time, at) # If the CPU is idle, we need to wait until the process arrives

    ct = time + bt
    tat = ct - at
    wt = tat - bt

    time = ct # Update the current time to the completion time of the current process

    total_wt += wt
    total_tat += tat

    print(f"{pid}\t{at}\t\t{bt}\t\t{ct}\t\t{tat}\t\t{wt}")

print(f"\nTotal Waiting Time: {total_wt}")
print(f"Total Turnaround Time: {total_tat}")

print()

print("Average Waiting Time:", total_wt / n)
print("Average Turnaround Time:", total_tat / n)

