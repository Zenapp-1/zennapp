# 📚 Panduan Lengkap: Mengubah Modul dengan Mudah

## 🎯 Struktur File

Setiap modul sekarang memiliki file JSON terpisah di folder `data/`:
- **`data/akademi-crypto.json`** - Untuk modul Akademi Crypto
- **`data/trade-with-suli.json`** - Untuk modul Trade with Suli  
- **`data/ternak-uang.json`** - Untuk modul Ternak Uang

## ✏️ Cara Mengubah Modul

### 1️⃣ Buka File JSON yang Ingin Diubah

Buka file JSON sesuai modul yang ingin diubah:
- Untuk **Akademi Crypto** → buka `data/akademi-crypto.json`
- Untuk **Trade with Suli** → buka `data/trade-with-suli.json`
- Untuk **Ternak Uang** → buka `data/ternak-uang.json`

### 2️⃣ Struktur Data Modul

Setiap modul memiliki struktur seperti ini:

```json
{
  "id": 1,
  "title": "Nama Modul",
  "category": "Kategori",
  "level": 0,
  "description": "Deskripsi/isi modul yang akan ditampilkan",
  "thumbnail": "path/gambar.jpg",
  "youtube_url": "https://www.youtube.com",
  "materials": [
    {
      "name": "Nama Materi",
      "url": "https://www.youtube.com"
    }
  ]
}
```

## 📝 Cara Mengubah Setiap Bagian

### 🏷️ Mengubah Nama Modul

Ubah field `"title"`:

```json
{
  "title": "Nama Baru Modul Anda"
}
```

### 🖼️ Mengubah Gambar Thumbnail

Ubah field `"thumbnail"` dengan path ke gambar:

**Opsi 1: Menggunakan gambar dari folder `image/`**
```json
{
  "thumbnail": "image/nama-gambar.jpg"
}
```

**Opsi 2: Menggunakan URL gambar online**
```json
{
  "thumbnail": "https://example.com/gambar.jpg"
}
```

**Opsi 3: Menggunakan gradient default (kosongkan)**
```json
{
  "thumbnail": ""
}
```

### 📄 Mengubah Isi/Deskripsi Modul

Ubah field `"description"`:

```json
{
  "description": "Isi modul yang akan ditampilkan di halaman detail. Bisa berisi penjelasan lengkap tentang modul ini."
}
```

### 📚 Mengubah Daftar Materi

Ubah array `"materials"`. Setiap materi memiliki:
- `"name"`: Nama/judul materi
- `"url"`: Link YouTube atau URL materi

**Contoh:**
```json
{
  "materials": [
    {
      "name": "Pengenalan Investasi - Part 1",
      "url": "https://www.youtube.com/watch?v=xxxxx"
    },
    {
      "name": "Prinsip Dasar - Part 2",
      "url": "https://www.youtube.com/watch?v=yyyyy"
    },
    {
      "name": "Tips Investasi untuk Pemula",
      "url": "https://www.youtube.com/watch?v=zzzzz"
    }
  ]
}
```

**Menambah Materi Baru:**
Tambahkan object baru di dalam array `materials`:

```json
{
  "materials": [
    {
      "name": "Materi 1",
      "url": "https://www.youtube.com"
    },
    {
      "name": "Materi 2 - BARU",
      "url": "https://www.youtube.com/watch?v=baru"
    }
  ]
}
```

**Menghapus Materi:**
Hapus object yang tidak diinginkan dari array `materials`.

## 📋 Contoh Lengkap

Berikut contoh lengkap modul yang sudah diubah:

```json
{
  "id": 1,
  "title": "Investasi Dasar untuk Pemula",
  "category": "Investasi",
  "level": 0,
  "description": "Pelajari dasar-dasar investasi dari nol. Modul ini akan membahas konsep investasi, jenis-jenis investasi yang tersedia, cara memilih investasi yang tepat, dan tips untuk pemula yang ingin memulai investasi. Cocok untuk yang baru pertama kali belajar tentang investasi.",
  "thumbnail": "image/crypto.jpeg",
  "youtube_url": "https://www.youtube.com/watch?v=xxxxx",
  "materials": [
    {
      "name": "Pengenalan Investasi - Part 1",
      "url": "https://www.youtube.com/watch?v=part1"
    },
    {
      "name": "Jenis-jenis Investasi - Part 2",
      "url": "https://www.youtube.com/watch?v=part2"
    },
    {
      "name": "Tips Investasi untuk Pemula - Part 3",
      "url": "https://www.youtube.com/watch?v=part3"
    },
    {
      "name": "Q&A Session",
      "url": "https://www.youtube.com/watch?v=qa"
    }
  ]
}
```

## ⚙️ Field Lainnya

### Category (Kategori)
Pilih salah satu kategori yang tersedia:
- `"Investasi"`
- `"Live Replay"`
- `"Mindset"`
- `"Trading"`
- `"Tutorials"`
- `"Crypto"` (untuk Akademi Crypto)
- `"Ternak Uang"` (untuk Ternak Uang)

### Level (Tingkat Kesulitan)
- `0` - Pemula
- `1` - Dasar
- `2` - Menengah
- `3` - Lanjutan
- `4` - Expert

### YouTube URL
URL video utama yang akan diputar saat klik tombol play di banner:
```json
{
  "youtube_url": "https://www.youtube.com/watch?v=xxxxx"
}
```

## 🔄 Setelah Mengubah

1. **Simpan file JSON** yang sudah diubah
2. **Refresh halaman modul** di browser (tekan F5 atau Ctrl+R)
3. **Klik modul** untuk melihat perubahan

## ⚠️ Tips Penting

1. **Format JSON harus valid**: Pastikan menggunakan koma (`,`) yang benar dan tanda kurung yang seimbang
2. **Path gambar relatif**: Gunakan path relatif dari root folder (misal: `image/nama-gambar.jpg`)
3. **Jika thumbnail kosong**: Sistem akan menggunakan gradient default sesuai tema
4. **Jika materials kosong**: Sistem akan menampilkan materi default
5. **Gunakan text editor yang baik**: Disarankan menggunakan VS Code, Notepad++, atau editor yang mendukung JSON syntax highlighting

## 🎨 Contoh Perubahan Lengkap

### Sebelum:
```json
{
  "id": 1,
  "title": "Investasi Dasar",
  "description": "Pengenalan investasi dan prinsip dasar.",
  "thumbnail": "",
  "materials": []
}
```

### Sesudah:
```json
{
  "id": 1,
  "title": "Investasi Dasar untuk Pemula 2024",
  "description": "Pelajari investasi dari dasar hingga mahir. Modul lengkap dengan contoh praktis dan studi kasus nyata. Cocok untuk pemula yang ingin memulai investasi dengan benar.",
  "thumbnail": "image/investasi-thumbnail.jpg",
  "materials": [
    {
      "name": "Pengenalan Investasi - Part 1",
      "url": "https://www.youtube.com/watch?v=abc123"
    },
    {
      "name": "Jenis Investasi - Part 2",
      "url": "https://www.youtube.com/watch?v=def456"
    },
    {
      "name": "Praktik Investasi - Part 3",
      "url": "https://www.youtube.com/watch?v=ghi789"
    }
  ]
}
```

## 🆘 Troubleshooting

**Q: Perubahan tidak muncul setelah refresh?**
A: Pastikan file JSON sudah disimpan dan format JSON valid. Cek browser console (F12) untuk melihat error.

**Q: Gambar tidak muncul?**
A: Pastikan path gambar benar dan file gambar ada di folder yang dimaksud.

**Q: Error saat membuka halaman?**
A: Pastikan format JSON valid. Gunakan JSON validator online untuk mengecek.

**Q: Materi tidak muncul?**
A: Pastikan array `materials` memiliki format yang benar dengan field `name` dan `url`.

---

**Selamat mengubah modul! 🎉**

