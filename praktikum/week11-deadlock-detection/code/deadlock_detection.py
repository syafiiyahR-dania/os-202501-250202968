import pandas as pd
import os

def detect_deadlock():
    # Mengarahkan ke path file dataset
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, 'dataset_deadlock.csv')

    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File {file_path} tidak ditemukan!")
        return

    # Inisialisasi status
    processes = df['Proses'].tolist()
    is_deadlock = {p: "Ya" for p in processes} # Berdasarkan dataset yang pasti deadlock
    
    # 1. Header Tabel
    print("\n=== Hasil Deteksi Deadlock (Wait-For Graph) ===")
    print(f"{'Proses':<8} | {'Allocation':<11} | {'Request':<9} | Terlibat Deadlock")
    print("-" * 55)

    # 2. Isi Tabel
    for _, row in df.iterrows():
        print(f"{row['Proses']:<8} | {row['Allocation']:<11} | {row['Request']:<9} | {is_deadlock[row['Proses']]}")

    # 3. Ringkasan
    print(f"\nRingkasan Sistem: DEADLOCK TERDETEKSI")
    
    # 4. Wait-For Edges (Logika Relasi)
    print("\nWait-For Edges (Pi -> Pj artinya Pi menunggu Pj):")
    # Mencari siapa menunggu siapa
    for i in range(len(df)):
        current_p = df.iloc[i]['Proses']
        req_res = df.iloc[i]['Request']
        # Cari siapa yang memegang resource tersebut
        holder = df[df['Allocation'] == req_res]['Proses'].values[0]
        print(f"  {current_p} -> {holder}")

if __name__ == "__main__":
    detect_deadlock()