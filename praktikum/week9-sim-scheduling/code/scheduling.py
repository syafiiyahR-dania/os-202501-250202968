import csv

dataset_content = [
    ["Process", "ArrivalTime", "BurstTime"],
    ["P1", 0, 6],
    ["P2", 1, 8],
    ["P3", 2, 7],
    ["P4", 3, 3]
]

with open('dataset.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(dataset_content)

process_list = []
with open('dataset.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        process_list.append({
            "name": row["Process"],
            "at": int(row["ArrivalTime"]),
            "bt": int(row["BurstTime"])
        })

current_time = 0
results = []

print("\nLog Eksekusi - FCFS")

for p in process_list:
    if current_time < p["at"]:
        current_time = p["at"]
    
    start_time = current_time
    print(f"Waktu {start_time}: {p['name']} Mulai dieksekusi")

    finish_time = start_time + p["bt"]
    print(f"Waktu {finish_time}: {p['name']} Selesai dieksekusi")
    
    waiting_time = start_time - p["at"]
    turnaround_time = finish_time - p["at"]
    
    results.append({
        "Process": p["name"],
        "AT": p["at"],
        "BT": p["bt"],
        "Start": start_time,
        "Finish": finish_time,
        "WT": waiting_time,
        "TAT": turnaround_time
    })
    
    current_time = finish_time

    print("\nProses | AT   | BT   | Mulai | Selesai | TAT  | WT")
    print("-" * 50)

total_wt = 0
total_tat = 0
for r in results:
    print(f"{r['Process']:<6} | {r['AT']:<4} | {r['BT']:<4} | {r['Start']:<5} | {r['Finish']:<7} | {r['WT']:<4} | {r['TAT']:<4}")
    total_wt += r['WT']
    total_tat += r['TAT']

print("-" * 50)
print(f"Rata-rata Waiting Time    : {total_wt/len(results):.2f}ms")
print(f"\nRata-rata Turnaround Time : {total_tat/len(results):.2f}ms")