import time

print("--- PROGRAM UJI RESOURCE DOCKER DIMULAI ---")

# 1. Simulasi Beban CPU (Menghitung angka besar)
print("Sedang memproses perhitungan berat (CPU Load)...")
start_time = time.time()
for i in range(10**7):
    _ = i * i
end_time = time.time()
print(f"Selesai dalam: {end_time - start_time:.2f} detik")

# 2. Simulasi Beban Memori (Alokasi RAM bertahap)
print("\nSedang mengalokasikan memori (Memory Load)...")
keranjang_data = []
try:
    for i in range(1, 11):
        # Menambah beban sekitar 50MB setiap putaran
        data_baru = ' ' * (50 * 1024 * 1024) 
        keranjang_data.append(data_baru)
        print(f"Berhasil menggunakan total RAM: {i * 50} MB")
        time.sleep(1)
except MemoryError:
    print("\n[STOP] Memori tidak cukup! Program dihentikan oleh sistem.")

print("\n--- SEMUA PROSES SELESAI ---")