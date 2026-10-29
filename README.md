# FCFS CPU Scheduling Algorithm

## Introduction
FCFS means **First Come, First Served**. The process that arrives in the ready queue first is scheduled first. FCFS is a simple, non-preemptive CPU scheduling algorithm.

## Features
- Calculates start and completion times
- Calculates waiting time and turnaround time
- Displays average waiting and turnaround times
- Includes a sample Gantt chart image

## Example processes

| Process | Arrival Time | CPU Burst Time |
|---|---:|---:|
| P1 | 0 | 4 |
| P2 | 1 | 3 |
| P3 | 2 | 2 |

## Sample execution
Run the program with Python 3:

```bash
python fcfs.py
```

The sample result is:

```text
Process      Arrival    Burst    Start   Finish   Waiting  Turnaround
P1                 0        4        0        4         0            4
P2                 1        3        4        7         3            6
P3                 2        2        7        9         5            7
Average waiting time: 2.67
Average turnaround time: 5.67
```

## Gantt chart
![FCFS Gantt chart](images/fcfs-gantt.png)

## Formulas
- Waiting Time = Start Time − Arrival Time
- Turnaround Time = Completion Time − Arrival Time

## Notes
This is an educational example. FCFS is non-preemptive, so once a process starts, it runs until its CPU burst is complete. If the CPU is idle before the next process arrives, the program accounts for that idle time.

## Files
- `fcfs.py` — Python implementation
- `images/fcfs-gantt.png` — Gantt chart image
- `report.docx` — Short project report
