import os

def fifo_simulation():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'reference_string.txt')

    try:
        with open(file_path, 'r') as f:
            # Pastikan data dibaca sebagai string yang bersih
            content = f.read().replace(',', ' ')
            reference_string = content.split()
            
        frames_count = 3
        memory = []
        faults = 0

        print(f"\nDataset Loaded: {reference_string}")
        print(f"Jumlah Frame  : {frames_count}")
        print("\n" + "="*55)
        print(f"{'| No':<5} | {'Page':<6} | {'Status':<10} | {'Isi Frame (Memori)':<20}")
        print("-" * 55)

        for i, page in enumerate(reference_string, 1):
            status = "HIT"
            if page not in memory:
                if len(memory) < frames_count:
                    memory.append(page)
                else:
                    memory.pop(0)  
                    memory.append(page)
                faults += 1
                status = "MISS"
            
            # Perbaikan error: memastikan semua elemen memory dikonversi ke string sebelum join
            display_list = [str(x) for x in memory]
            mem_display = "[" + "  ".join(display_list) + "]"
            
            print(f"| {i:<3} | {page:<6} | {status:<10} | {mem_display:<20}")

        print("-" * 55)
        print(f"Total Page Fault FIFO: {faults}")
        print("="*55)

    except FileNotFoundError:
        print(f"Error: File 'reference_string.txt' tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    fifo_simulation()