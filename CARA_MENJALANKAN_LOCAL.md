# Panduan Menjalankan Website Secara Lokal

Ikuti langkah-langkah di bawah ini untuk menjalankan project Django ini di komputer lokal (Windows).

## 1. Persiapan Awal
Pastikan Anda sudah menginstal Python di komputer Anda. Anda bisa mengeceknya dengan membuka Command Prompt (Terminal) dan mengetik:
```bash
python --version
```

## 2. Mengaktifkan Virtual Environment
Project ini sudah memiliki folder virtual environment (`venv`). Untuk mengaktifkannya, buka Command Prompt (cmd) atau PowerShell di dalam folder project ini (`d:\website_desa`), kemudian jalankan perintah:


**Command Prompt (cmd):**
```bash
venv\Scripts\activate.bat
```

**PowerShell:**
```powershell
venv\Scripts\Activate.ps1
```
*(Jika berhasil, akan ada tulisan `(venv)` di sebelah kiri terminal Anda)*

## 3. Instalasi Dependensi (Package)
Setelah virtual environment aktif, instal semua package yang dibutuhkan (jika belum terinstal) dengan perintah:
```bash
pip install -r requirements.txt
```

## 4. Pengaturan File Environment (Variabel .env)
Project ini menggunakan file `.env` untuk pengaturan rahasia seperti secret key atau konfigurasi database.
1. Cari file bernama `.env.example`
2. Copy atau duplicate file tersebut, lalu ubah namanya menjadi `.env` (tanpa kata example).

## 5. Menjalankan Migrasi Database
Untuk memastikan struktur database (SQLite) sudah up-to-date, jalankan perintah migrasi berikut:
```bash
python manage.py migrate
```

## 6. Menjalankan Server Lokal
Langkah terakhir adalah menyalakan server Django. Jalankan perintah ini:
```bash
python manage.py runserver
```

## 7. Membuka Website
Jika server sudah berjalan tanpa error, buka aplikasi browser (Chrome, Firefox, Edge, dll) dan kunjungi alamat berikut:
[http://127.0.0.1:8000](http://127.0.0.1:8000)

---
**Catatan untuk menghentikan server:**
Untuk mematikan server lokal, tekan tombol `Ctrl + C` pada terminal Anda.
