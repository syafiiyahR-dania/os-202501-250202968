
# Laporan Praktikum Minggu [X]
 Arsitektur Sistem Operasi dan Kernel

---

## Identitas
- **Nama**  : Syafiiyah Rahmadani
- **NIM**   : 250202968
- **Kelas** : 1IKRB

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Fungsi Utama Sistem Operasi
Sistem operasi (OS) berfungsi sebagai penghubung antara pengguna dan perangkat keras, serta pengelola sumber daya komputer.
Dan fungsinya meliputi:
1. Manajemen proses yaitu mengatur jalannya program dan penjadwalan CPU.
2. Manajemen memori untuk mengalokasikan RAM untuk tiap proses.
3. Manajemen file itu untuk mengatur penyimpanan dan akses data.
4. Manajemen perangkat I/O  mengontrol interaksi hardware dan software.
5. Keamanan & proteksi yaitu menjaga data dan akses sistem.
6. Antarmuka pengguna yaitu menyediakan GUI atau CLI.

Semua fungsi tersebut bekerja bersama agar sistem komputer bisa berjalan efesien,stabil, dan aman.

Peran Kernel
Kernel adalah inti sistem operasi yang mengatur semua fungsi dasar.
Perannya :
a.	Menghubungkan aplikasi dengan hardware.
b.	Mengelola proses, memori, dan sistem berkas.
c.	Menangani interupsi serta komunikasi antar-komponen.

Karnel dapat memastikan program pengguna dapat berjalan dengan aman tanpa harus berinteraksi langsung dengan perangkat keras.

System Call

System call adalah jembatan antara program pengguna dan kernel.
Digunakan saat aplikasi butuh layanan kernel seperti membaca file, membuat proses, atau mengakses perangkat keras.
Contoh nya yaitu read, write, fork, exe

---

## Dasar Teori
 Poin  penting ringkasan yang mendasari percobaan
1. Sistem operasi berfungsi sebagai penghubung antara pengguna dan perangkat keras, serta mengatur semua sumber daya komputer.
2. Fungsi utama OS mencakup manajemen proses, memori, file, perangkat I/O, keamanan, dan antarmuka pengguna.
3. Kernel adalah inti OS yang mengatur operasi dasar seperti pengelolaan memori, proses, dan komunikasi dengan perangkat keras.
4. System call menjadi perantara antara program pengguna dan kernel untuk meminta layanan sistem, misalnya  yaitu membuka file atau membuat proses baru.
5. Kernel dan system call bekerja bersama untuk memastikan aplikasi dapat berjalan dengan aman dan efisien tanpa langsung mengakses hardware


---

## Langkah Praktikum

Langkah-langkah yang dilakukan pada praktikum minggu pertama ini adalah sebagai berikut:
1. Melakukan fork.
2. Mengubah nama repositori hasil fork.
3. Melakukan clone repositori tersebut ke komputer lokal.
4. Membuat struktur folder baru di dalam repositori lokal.
5. Di dalam folder tersebut, membuat `laporan.md` dan sebuah folder `screenshot/`.
6. Menulis ringkasan mengenai perbedaan monolithic kernel, microkernel, dan layered architecture,contoh OS yang menerapkan tiap model dan analisis: model mana yang paling relevan untuk sistem modern di dalam file `laporan.md`.
7. Menjawab pertanyaan kuis yang diberikan pada modul.
8. Menambahkan file laporan dan screenshot ke Git, lalu melakukan commit dengan pesan `week1-intro-arsitekur-os` dan push ke GitHub.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
whoami
lsmod | head
dmesg | head
```

```
## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](./screenshots/Linux-%201.png)


---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)? 

	1.	Makna Hasil percobaan menunjukkan bagaimana sistem operasi bekerja dalam mengatur proses, memori, dan perangkat. Dari hasil itu terlihat bahwa program tidak akan berinteraksi langsung dengan hardware, melainkan akan melalui kernel dan system call yang menjadi penghubung antara aplikasi dan perangkat keras.
	2.	Hubungan hasil dengan teori
	•	Kernel berfungsi mengatur sumber daya sistem dan menjalankan proses.
	•	System call menjadi jembatan antara program pengguna dan kernel.
	•	Arsitektur OS memengaruhi cara kerja sistem pada monolithic kernel, semua layanan ada di satu ruang kernel, sedangkan pada microkernel, layanan dipisah (lebih aman dan stabil).
	3.	Perbedaan hasil di OS yang berbeda di antranya Linux vs Windows
	•	Linux menggunakan monolithic kernel, sehingga proses lebih transparan dan perintah terminal bisa langsung melihat aktivitas kernel (misalnya uname -a, lsmod).
	•	Lalu Windows memakai hybrid kernel, yang lebih tertutup dan fokus pada stabilitas serta keamanan.
Jadi, Linux lebih mudah untuk diamati pembelajaran, sedangkan Windows lebih terkontrol untuk penggunaan umum.

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
1.	Setiap arsitektur sistem operasi memiliki karakteristik yang unik.
Monolithic Kernel unggul dalam kinerja karena semua komponen dijalankan di satu ruang kernel, Microkernel lebih stabil dan aman dengan pemisahan fungsi ke ruang pengguna, sedangkan Layered Architecture memberikan struktur yang jelas dan mudah dikembangkan.
2.	Pemilihan model arsitektur bergantung pada kebutuhan sistem.
Monolithic Kernel cocok untuk sistem yang menuntut kecepatan tinggi seperti server, Microkernel sesuai untuk sistem real time dan perangkat tertanam, sedangkan Layered Architecture efektif untuk pembelajaran dan sistem yang menekankan modularitas.
3.	Sistem modern cenderung menggunakan pendekatan hybrid.
Sistem operasi seperti Windows, macOS, dan Android menggabungkan kelebihan monolithic dan microkernel untuk mencapai keseimbangan
---

## Quiz
1.  Sebutukan 3 fungsi utama sistem oprasi.
   Jawaban: a. Antarmuka pengguna (user interfece)
   b. Menejemen sumber budaya (resouree menegemen)
   c. menejemen proses dan program
2. Jelaskan perbedaan antar karnel mode dan user mode. 
   Jawaban: Untuk karnel mode memiliki  akses penuh ke perangkat keras sedangkan user mode memiliki akses terbataas untuk melindungi sistem dari kerusakan. 
3. Sebutukan contoh OS dengan arsitektur monolithic dan microkarnel.  
   Jawaban:a. Arsitektur monolithic : Linux, UNIX,BSD,DOS, dan Windows 9x 
   b. Arsitektur microkarnel : QNX, MINIX, dan MachOS

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
Bagian yang paling menantang bagi saya adalah memahami tentang cara untuk menyelesaikan tugas yang diberikan kepada mahasiswa di karenakan saya belum sepenuhnya paham cara mengerjakan tugasnya.
- Bagaimana cara Anda mengatasinya? 
Saya mengatasinya dengan cara berdiskusi dengan teman sekelas agar lebih memahami  
cara mengerjakan tugas yang di berikan kepada mahasiswa dan meminta tolong kepada kakak tinggkatan untuk menyelesaikan tugas yang diberikan
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_

