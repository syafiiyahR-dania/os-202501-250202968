import os

def load_data():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'reference_string.txt')
    with open(file_path, 'r') as f:
        return f.read().replace(',', ' ').split()

def simulate_fifo(pages, capacity):
    memory = []
    faults = 0
    print("\n=== SIMULASI FIFO (First-In First-Out) ===")
    print(f"{'| No':<5} | {'Page':<6} | {'Status':<8} | {'Memory':<15}")
    print("-" * 45)
    for i, page in enumerate(pages, 1):
        status = "HIT"
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            faults += 1
            status = "MISS"
        print(f"| {i:<3} | {page:<6} | {status:<8} | {str(memory):<15}")
    return faults

def simulate_lru(pages, capacity):
    memory = []
    faults = 0
    print("\n=== SIMULASI LRU (Least Recently Used) ===")
    print(f"{'| No':<5} | {'Page':<6} | {'Status':<8} | {'Memory':<15}")
    print("-" * 45)
    for i, page in enumerate(pages, 1):
        status = "HIT"
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            faults += 1
            status = "MISS"
        else:
            # Logika LRU: Pindahkan yang baru diakses ke paling belakang (terbaru)
            memory.remove(page)
            memory.append(page)
        print(f"| {i:<3} | {page:<6} | {status:<8} | {str(memory):<15}")
    return faults

if __name__ == "__main__":
    data = load_data()
    f_faults = simulate_fifo(data, 3)
    l_faults = simulate_lru(data, 3)
    
    print("\n=== ANALISIS PERBANDINGAN ===")
    print(f"Total Page Fault FIFO: {f_faults}")
    print(f"Total Page Fault LRU : {l_faults}")
    if l_faults < f_faults:
        print(">> Algoritma LRU lebih efisien pada dataset ini.")