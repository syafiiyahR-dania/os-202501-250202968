def hitung_fcfs(data_pelanggan):
    n = len(data_pelanggan)
    
    # Inisialisasi list untuk menyimpan hasil
    waktu_selesai = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    
    # Hitung waktu untuk pelanggan pertama
    # Pelanggan pertama selesai pada: waktu kedatangan + waktu pelayanan
    waktu_selesai[0] = data_pelanggan[0]['kedatangan'] + data_pelanggan[0]['pelayanan']
    turnaround_time[0] = waktu_selesai[0] - data_pelanggan[0]['kedatangan']
    waiting_time[0] = turnaround_time[0] - data_pelanggan[0]['pelayanan']
    
    # Hitung untuk pelanggan selanjutnya (P2 sampai P5)
    for i in range(1, n):
        # Kasir mulai melayani saat pelanggan datang ATAU saat pelanggan sebelumnya selesai
        waktu_mulai_layanan = max(data_pelanggan[i]['kedatangan'], waktu_selesai[i-1])
        
        waktu_selesai[i] = waktu_mulai_layanan + data_pelanggan[i]['pelayanan']
        turnaround_time[i] = waktu_selesai[i] - data_pelanggan[i]['kedatangan']
        waiting_time[i] = turnaround_time[i] - data_pelanggan[i]['pelayanan']

    # Tampilkan Hasil
    print(f"{'Pelanggan':<10} | {'Datang':<10} | {'Layanan':<10} | {'Selesai':<10} | {'Waiting':<10} | {'Turnaround':<10}")
    print("-" * 75)
    
    total_wt = 0
    total_tat = 0
    
    for i in range(n):
        total_wt += waiting_time[i]
        total_tat += turnaround_time[i]
        print(f"{data_pelanggan[i]['nama']:<10} | "
              f"{data_pelanggan[i]['kedatangan']:<10} | "
              f"{data_pelanggan[i]['pelayanan']:<10} | "
              f"{waktu_selesai[i]:<10} | "
              f"{waiting_time[i]:<10} | "
              f"{turnaround_time[i]:<10}")
    
    print("-" * 75)
    print(f"Rata-rata Waiting Time    : {total_wt / n:.1f}")
    print(f"Rata-rata Turnaround Time : {total_tat / n:.1f}")

# Data sesuai studi kasus
pelanggan = [
    {'nama': 'P1', 'kedatangan': 0, 'pelayanan': 5},
    {'nama': 'P2', 'kedatangan': 1, 'pelayanan': 3},
    {'nama': 'P3', 'kedatangan': 2, 'pelayanan': 8},
    {'nama': 'P4', 'kedatangan': 3, 'pelayanan': 6},
    {'nama': 'P5', 'kedatangan': 4, 'pelayanan': 2},
]

# Jalankan fungsi
hitung_fcfs(pelanggan)