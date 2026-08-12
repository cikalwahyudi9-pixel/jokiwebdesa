# 🚀 Panduan Lengkap Deploy Django ke Railway & Supabase

Panduan ini akan menuntun Anda memindahkan aplikasi lokal beserta datanya agar bisa online diakses semua orang menggunakan **Railway** (untuk aplikasinya) dan **Supabase** (untuk databasenya).

> [!IMPORTANT]
> Pastikan semua kode Anda yang terbaru sudah di-*commit* dan di-*push* ke **GitHub** sebelum memulai.

---

## Tahap 1: Ekspor (Backup) Data Lokal Anda
Kita akan menyimpan semua data dari SQLite agar nanti bisa dimasukkan ke Supabase.

1. Buka terminal di VS Code (pastikan virtual environment/venv aktif).
2. Jalankan perintah ini:
   ```bash
   python manage.py dumpdata --exclude auth.permission --exclude contenttypes > data_desa.json
   ```
3. Akan muncul file baru bernama `data_desa.json`.
4. Lakukan commit dan push ke GitHub:
   ```bash
   git add .
   git commit -m "Menambahkan file data_desa.json dan update konfigurasi db"
   git push
   ```

---

## Tahap 2: Buat Database di Supabase
1. Buka website [Supabase.com](https://supabase.com/) dan buat akun/login.
2. Klik tombol **New Project** dan isi detailnya (Nama: terserah Anda, Database Password: buat password yang kuat dan **catat password ini**, Region: pilih Singapore agar cepat).
3. Tunggu sekitar 2-3 menit sampai database selesai dibuat.
4. Setelah masuk ke Dashboard proyek, scroll ke bawah atau cari menu **Project Settings** (ikon gerigi) -> **Database**.
5. Cari bagian **Connection String**, lalu pilih tab **URI**.
6. Anda akan melihat teks seperti ini: 
   `postgresql://postgres.namaproject:[YOUR-PASSWORD]@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres`
7. Copy teks tersebut, dan ubah tulisan `[YOUR-PASSWORD]` dengan password database yang Anda buat di langkah 2.
8. **Simpan URI ini (DATABASE_URL)** di Notepad, kita akan segera menggunakannya.

---

## Tahap 3: Deploy Aplikasi ke Railway
1. Buka website [Railway.app](https://railway.app/) dan login menggunakan akun GitHub Anda.
2. Klik **New Project** -> Pilih **Deploy from GitHub repo**.
3. Pilih repository website desa Anda. Railway akan mulai memprosesnya.
4. **Sangat Penting:** Segera klik aplikasi Anda di dashboard Railway, lalu buka tab **Variables**.
5. Tambahkan variabel-variabel (*Environment Variables*) berikut dengan mengklik tombol **New Variable**:

| NAMA VARIABEL | VALUE (NILAI) | Keterangan |
| :--- | :--- | :--- |
| `DATABASE_URL` | *(Masukkan URI Connection String Supabase dari Notepad)* | Penghubung ke Supabase |
| `DEBUG` | `False` | Mode keamanan produksi |
| `ALLOWED_HOSTS` | `*` | Mengizinkan akses dari domain manapun |
| `SECRET_KEY` | *(Tulis sembarang teks acak, misal: `kunci-rahasia-website-desa-12345`)* | Kunci pengaman Django |

> [!TIP]
> Setelah memasukkan semua variabel di atas, Railway biasanya akan merestart aplikasi secara otomatis untuk menerapkan pengaturan baru.

---

## Tahap 4: Menghasilkan Link Website
1. Di dashboard Railway, klik aplikasi Anda, lalu masuk ke tab **Settings**.
2. Scroll ke bagian **Environment** atau **Domains**.
3. Klik tombol **Generate Domain** (Railway akan memberikan link gratis, misalnya `namaproject-production.up.railway.app`).
4. Ini adalah alamat website Anda sekarang!

---

## Tahap 5: Memasukkan Data ke Database Supabase
Sekarang website sudah online, tetapi databasenya masih kosong (belum ada struktur tabel dan isinya). Kita harus memasukkan data dari `data_desa.json`.

1. Masih di dashboard Railway untuk aplikasi Anda, klik tab **Terminal** (atau tekan tombol `>_` untuk membuka Railway CLI jika dari laptop).
2. Di dalam terminal Railway tersebut, jalankan perintah untuk membuat struktur tabel:
   ```bash
   python manage.py migrate
   ```
3. Jika migrasi berhasil, jalankan perintah ini untuk memasukkan (import) data Anda:
   ```bash
   python manage.py loaddata data_desa.json
   ```

> [!NOTE]
> **Selesai!** Coba buka link domain yang didapatkan dari Tahap 4. Website Desa Anda sekarang sudah online sepenuhnya dengan semua data, artikel, dan galeri yang Anda buat sebelumnya di laptop.
