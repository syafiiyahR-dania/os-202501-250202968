
# Laporan Praktikum Minggu [13]
Topik: Docker – Resource Limit (CPU & Memori)


---

## Identitas
- **Nama**  : Sayafi'iyah Rahmadani
- **NIM**   : 250202968 
- **Kelas** : 1IKRB

---

## Tujuan
1. Membuat skrip konfigurasi `Dockerfile` yang fungsional untuk aplikasi atau skrip tertentu.

2. Mengelola siklus hidup Docker mulai dari pembuatan image hingga eksekusi kontainer.

3. Mengkonfigurasi parameter batas sumber daya, khususnya penggunaan CPU dan memori, saat menjalankan kontainer.

4. Menganalisis dampak batas sumber daya terhadap kinerja dan perilaku eksekusi aplikasi di dalam kontainer.

5. Mendokumentasikan seluruh proses lab dan hasil pengamatan dalam laporan yang sistematis dan terstruktur.

---

## Dasar Teori
- Mekanisme Control Groups (cgroups), docker menggunakan fitur kernel Linux yang disebut cgroups untuk mengelola dan membatasi distribusi sumber daya fisik (CPU, Memori, I/O) ke setiap kontainer sehingga satu kontainer tidak mengonsumsi semua sumber daya host.

- Isolasi sumber daya batasan ini bertujuan untuk menciptakan stabilitas sistem melalui isolasi. Dengan batasan ini, setiap kontainer hanya bekerja dalam "alokasi" yang ditentukan, mencegah fenomena "Tetangga Berisik" yang dapat memperlambat aplikasi lain di server yang sama.

- Manajemen Memori (RAM), docker dapat menetapkan batas keras pada penggunaan RAM menggunakan parameter `--memory`. Jika penggunaan memori kontainer melebihi batas ini, sistem akan memicu OOM (Out of Memory) Killer, yang dapat secara otomatis menghentikan kontainer untuk melindungi kernel.

- Manajemen CPU diilakukan melalui pembatasan CPU di Docker (menggunakan parameter `--cpus`) bekerja dengan menetapkan jumlah waktu prosesor yang dapat digunakan kontainer. Nilai 0,5 berarti kontainer hanya diberikan akses ke setengah kapasitas satu inti CPU, yang akan memengaruhi kecepatan eksekusi program.

- Pemantauan Waktu Nyata menggunakan perintah `docker stats` berfungsi sebagai alat verifikasi untuk mengamati secara langsung bagaimana batasan ini bekerja, menampilkan metrik penggunaan CPU dan RAM yang tersisa dibandingkan dengan batas yang ditetapkan.
---

## Langkah Praktikum
1. **Persiapan Lingkungan**

   - Pastikan Docker terpasang dan berjalan.
   - Verifikasi:
     ```bash
     docker version
     docker ps
     ```

2. **Membuat Aplikasi/Skrip Uji**

   Buat program sederhana di folder `code/` (bahasa bebas) yang:
   - Melakukan komputasi berulang (untuk mengamati limit CPU), dan/atau
   - Mengalokasikan memori bertahap (untuk mengamati limit memori).

3. **Membuat Dockerfile**

   - Tulis `Dockerfile` untuk menjalankan program uji.
   - Build image:
     ```bash
     docker build -t week13-resource-limit .
     ```

4. **Menjalankan Container Tanpa Limit**

   - Jalankan container normal:
     ```bash
     docker run --rm week13-resource-limit
     ```
   - Catat output/hasil pengamatan.

5. **Menjalankan Container Dengan Limit Resource**

   Jalankan container dengan batasan resource (contoh):
   ```bash
   docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
   ```
   Catat perubahan perilaku program (mis. lebih lambat, error saat memori tidak cukup, dll.).

6. **Monitoring Sederhana**

   - Jalankan container (tanpa `--rm` jika perlu) dan amati penggunaan resource:
     ```bash
     docker stats
     ```
   - Ambil screenshot output eksekusi dan/atau `docker stats`.

7. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 13 - Docker Resource Limit"
   git push origin main
   ```
---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](./screenshots/Hasil_limit1%20(1).png)
![Screenshot hasil](./screenshots/Hasil_limit1%20(2).png)

---

## Analisis
Analisis eksperimental mengungkapkan perbedaan signifikan antara kontainer yang dibatasi dan yang tidak dibatasi. Pada eksekusi yang tidak dibatasi, program dapat mengonsumsi sumber daya sesuai kebutuhan aplikasi (hingga 500 MB). Ini menunjukkan bahwa secara default, kontainer akan mencoba mengambil sumber daya sebanyak mungkin dari host jika tidak dibatasi.

Kegagalan uji eksekusi kedua menunjukkan aksi OOM (Out of Memory) Killer. Karena skrip pengujian dirancang untuk mengalokasikan hingga 500 MB memori, sementara Docker hanya menyediakan batas maksimum 250 MB dengan parameter `--memory="250m"`, kernel Linux, melalui mekanisme cgroups-nya, segera menghentikan proses untuk menjaga integritas dan stabilitas sistem operasi host.

Secara teknis, perbedaan ini memvalidasi bahwa Docker melakukan lebih dari sekadar menjalankan aplikasi; ia juga berfungsi sebagai pengelola sumber daya yang ketat. Pembatasan CPU memperlambat waktu eksekusi (seperti yang terlihat pada perbedaan durasi dalam detik), sementara pembatasan memori bertindak sebagai "interupsi paksa" jika ambang batas terlampaui. 

## Hasil Pengamatan
Berdasarkan pengujian yang dilakukan melalui terminal, terdapat perbedaan perilaku yang signifikan antara kontainer yang berjalan tanpa batasan dan yang berjalan dengan batasan sumber daya.

- Tanpa batasan, saat menjalankan perintah `docker run --rm week13-resource-limit`, program berhasil mengeksekusi semua instruksi. Program mencatat beban CPU sebesar 1,24 detik dan berhasil mengalokasikan memori secara bertahap, mulai dari 50 MB hingga target 500 MB. Hal ini menunjukkan bahwa tanpa batasan, kontainer memiliki fleksibilitas untuk menggunakan sumber daya host sesuai dengan kebutuhan aplikasinya.

- Kondisi batasan sumber daya (`--memory="250m"`) ketika kontainer dijalankan dengan parameter batasan memori tambahan sebesar 250 MB, program gagal total. Terminal tidak menampilkan output jumlah CPU atau log alokasi memori, dan kontainer langsung berhenti setelah eksekusi.

- Analisis penyebab kegagalan pada kondisi kedua disebabkan oleh mekanisme Out of Memory Killer (OOM) yang dipicu melalui cgroups di kernel host. Karena skrip program dirancang untuk mengalokasikan hingga 500 MB memori, tetapi Docker memberlakukan batasan keras hanya 250 MB, sistem operasi mendeteksi pelanggaran sumber daya. Sebagai tindakan pengamanan untuk menjaga stabilitas sistem host, Docker secara otomatis menghentikan proses kontainer sebelum dapat mengonsumsi memori lebih lanjut.

---

## Kesimpulan
- Pentingnya isolasi sumber daya seperti pembatasan sumber daya menggunakan parameter `--memory` dan `--cpus` sangat efektif dalam mencegah satu kontainer mengonsumsi semua sumber daya host ("Tetangga Berisik"), sehingga menjaga stabilitas sistem.

- Validasi mekanisme cgroups memiliki perbedaan hasil eksekusi antara kondisi normal (500 MB) dan kondisi batas (250 MB) membuktikan bahwa fitur cgroups di kernel Linux bekerja dengan tepat untuk memantau dan membatasi alokasi memori fisik.

- Keamanan sistem melalui OOM killer yang meliputi kegagalan eksekusi kontainer ketika batas memori terlampaui menunjukkan bahwa Docker memprioritaskan keamanan sistem host; lebih baik menghentikan satu proses yang melebihi batasnya daripada membiarkan seluruh sistem mengalami crash karena kehabisan RAM.

---

## Quiz
1. Mengapa container perlu dibatasi CPU dan memori?  
   **Jawaban:**  Kontainer perlu dibatasi (throttle) untuk menjaga stabilitas sistem secara keseluruhan. Tanpa pembatasan, satu kontainer yang mengalami kesalahan atau berada di bawah beban kerja berat dapat mengonsumsi seluruh sumber daya fisik host (fenomena "Tetangga Berisik"), yang mengakibatkan perlambatan atau bahkan penghentian aplikasi lain dan sistem operasi host itu sendiri. Batasan memastikan setiap kontainer hanya menggunakan "jatah" yang dialokasikan melalui mekanisme cgroups.
2. Apa perbedaan VM dan container dalam konteks isolasi resource?  
   **Jawaban:**  Perbedaan utama terletak pada tingkat isolasi dan efisiensinya.

- Mesin Virtual (VM) menyediakan isolasi pada tingkat perangkat keras. Setiap VM memiliki kernel dan sistem operasinya sendiri, sehingga isolasi sumber daya sangat ketat tetapi membutuhkan banyak sumber daya (overhead tinggi).

- Kontainer menyediakan isolasi pada tingkat proses menggunakan kernel yang sama dengan OS host. Kontainer jauh lebih ringan tetapi membutuhkan fitur seperti cgroup dan namespace untuk membuat batasan sumber daya logis antar proses.
3. Apa dampak limit memori terhadap aplikasi yang boros memori? 
   **Jawaban:**  Dampaknya sangat parah dan merusak bagi proses yang melanggar batas.

1. Memicu OOM Killer: Jika sebuah aplikasi mencoba mengalokasikan memori melebihi batasnya (seperti percobaan kami yang membatasinya hingga 250 MB untuk kebutuhan 500 MB), kernel akan mengaktifkan Out of Memory (OOM) Killer.

2. Penghentian paksa: Kontainer akan segera dihentikan secara paksa (dibunuh) oleh sistem untuk mencegah kerusakan pada memori host.

3. Kegagalan eksekusi: Aplikasi tidak akan dapat menyelesaikan tugasnya atau bahkan gagal untuk memulai jika batas memori yang dialokasikan kurang dari kebutuhan minimum aplikasi.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
