"""
FCFS CPU Scheduling Algorithm
FCFS = First Come, First Served

This program calculates waiting time, turnaround time, and completion time
for processes using non-preemptive FCFS scheduling.
"""

def fcfs_scheduling(processes):
    # Sort processes by arrival time; preserve input order when arrival times match.
    processes = sorted(processes, key=lambda p: p["arrival"])
    current_time = 0
    results = []

    for process in processes:
        start_time = max(current_time, process["arrival"])
        completion_time = start_time + process["burst"]
        waiting_time = start_time - process["arrival"]
        turnaround_time = completion_time - process["arrival"]

        results.append({
            "pid": process["pid"],
            "arrival": process["arrival"],
            "burst": process["burst"],
            "start": start_time,
            "completion": completion_time,
            "waiting": waiting_time,
            "turnaround": turnaround_time,
        })
        current_time = completion_time

    return results


def print_results(results):
    print("\nFCFS CPU Scheduling")
    print("-" * 74)
    print(f'{"Process":<10}{"Arrival":>9}{"Burst":>9}{"Start":>9}{"Finish":>9}{"Waiting":>10}{"Turnaround":>12}')
    print("-" * 74)

    for r in results:
        print(f'{r["pid"]:<10}{r["arrival"]:>9}{r["burst"]:>9}{r["start"]:>9}'
              f'{r["completion"]:>9}{r["waiting"]:>10}{r["turnaround"]:>12}')

    avg_wait = sum(r["waiting"] for r in results) / len(results)
    avg_turnaround = sum(r["turnaround"] for r in results) / len(results)
    print("-" * 74)
    print(f"Average waiting time: {avg_wait:.2f}")
    print(f"Average turnaround time: {avg_turnaround:.2f}")


if __name__ == "__main__":
    # Example input: process ID, arrival time, CPU burst time
    sample_processes = [
        {"pid": "P1", "arrival": 0, "burst": 4},
        {"pid": "P2", "arrival": 1, "burst": 3},
        {"pid": "P3", "arrival": 2, "burst": 2},
    ]

    result = fcfs_scheduling(sample_processes)
    print_results(result)
