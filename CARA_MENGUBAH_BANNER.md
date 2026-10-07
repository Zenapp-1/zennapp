# 🖼️ Cara Mengubah Gambar Banner di Halaman Detail Modul

## 🎯 Fitur

Anda bisa mengatur gambar banner secara terpisah dari thumbnail card. Banner akan muncul di area hitam besar (dengan tombol play) di halaman detail saat modul diklik.

**✅ Fitur ini sudah aktif dan siap digunakan!**

## ✏️ Cara Menggunakan

### 1️⃣ Buka File JSON Modul

Buka file JSON sesuai modul yang ingin diubah:
- **Akademi Crypto** → `data/akademi-crypto.json`
- **Trade with Suli** → `data/trade-with-suli.json`
- **Ternak Uang** → `data/ternak-uang.json`

### 2️⃣ Tambahkan Field `banner_image`

Tambahkan atau edit field `"banner_image"` di setiap modul:

```json
{
  "id": 1,
  "title": "Investasi Dasar",
  "description": "...",
  "thumbnail": "image/crypto.jpeg",
  "banner_image": "image/banner-investasi.jpg",
  "youtube_url": "https://www.youtube.com",
  "pdf_url": "",
  "materials": [...]
}
```

## 📋 Opsi URL Banner

### Opsi 1: File Gambar Lokal

Jika file gambar ada di folder project:

```json
{
  "banner_image": "image/banner-modul.jpg"
}
```

**Contoh:**
```json
{
  "banner_image": "image/Tws/banner-onboarding.png"
}
```

### Opsi 2: URL Gambar Online

```json
{
  "banner_image": "https://example.com/banner.jpg"
}
```

### Opsi 3: Menggunakan Thumbnail (Kosongkan)

Jika `banner_image` kosong, sistem akan otomatis menggunakan `thumbnail`:

```json
{
  "thumbnail": "image/crypto.jpeg",
  "banner_image": "",
  ...
}
```

**Sistem akan menggunakan thumbnail sebagai banner jika `banner_image` kosong.**

## 🔄 Prioritas Banner

Sistem akan menggunakan gambar banner dengan urutan prioritas berikut:

1. **`banner_image`** - Jika diisi, ini yang digunakan
2. **`banner_url`** - Alternatif nama field
3. **`thumbnail`** - Fallback ke thumbnail jika banner_image kosong
4. **Gradient default** - Jika semua kosong

## 📝 Contoh Lengkap

### Sebelum (Menggunakan Thumbnail):
```json
{
  "id": 1,
  "title": "On Boarding",
  "description": "Pengenalan investasi...",
  "thumbnail": "image/Tws/On boarding.png",
  "banner_image": "",
  "youtube_url": "https://www.youtube.com",
  "materials": [...]
}
```

### Sesudah (Dengan Banner Terpisah):
```json
{
  "id": 1,
  "title": "On Boarding",
  "description": "Pengenalan investasi...",
  "thumbnail": "image/Tws/On boarding.png",
  "banner_image": "image/Tws/banner-onboarding-full.jpg",
  "youtube_url": "https://www.youtube.com",
  "materials": [...]
}
```

## 🎨 Tips Banner

### Ukuran Banner yang Disarankan

- **Rasio**: 16:9 atau 21:9 (landscape)
- **Lebar**: Minimal 1920px untuk kualitas terbaik
- **Format**: JPG atau PNG
- **Ukuran file**: Optimalkan untuk web (max 500KB)

### Perbedaan Thumbnail vs Banner

- **Thumbnail**: Gambar kecil di card modul (180px tinggi)
- **Banner**: Gambar besar di halaman detail (400px tinggi)

**Tips:** Gunakan gambar yang lebih detail untuk banner karena ukurannya lebih besar.

## 📂 Struktur Folder yang Disarankan

```
web adli/
├── image/
│   ├── crypto.jpeg (thumbnail)
│   ├── banner-crypto.jpg (banner)
│   ├── Tws/
│   │   ├── On boarding.png (thumbnail)
│   │   └── banner-onboarding.jpg (banner)
│   └── ...
└── ...
```

## ⚠️ Catatan Penting

1. **Jika `banner_image` kosong**: Sistem akan otomatis menggunakan `thumbnail`
2. **Format gambar**: Mendukung JPG, PNG, GIF, WebP
3. **Path relatif**: Gunakan path relatif dari root folder
4. **Gambar full**: Banner akan tampil full tanpa terpotong (menggunakan `contain`)

## 🔍 Troubleshooting

**Q: Banner tidak muncul?**
A: 
- Pastikan path gambar benar
- Pastikan file gambar ada di folder yang dimaksud
- Cek browser console (F12) untuk melihat error

**Q: Banner terpotong?**
A: 
- Sistem sudah menggunakan `contain` agar gambar full
- Pastikan gambar memiliki aspect ratio yang sesuai (16:9 disarankan)

**Q: Ingin menggunakan thumbnail sebagai banner?**
A: 
- Kosongkan field `banner_image` atau set ke `""`
- Sistem akan otomatis menggunakan `thumbnail`

**Q: Banner berbeda dengan thumbnail?**
A: 
- Itu normal! Banner dan thumbnail bisa berbeda
- Gunakan `banner_image` untuk banner khusus
- Gunakan `thumbnail` untuk gambar di card

## 📋 Contoh Penggunaan

### Contoh 1: Banner dan Thumbnail Sama
```json
{
  "thumbnail": "image/modul.jpg",
  "banner_image": ""
}
```
→ Banner akan menggunakan thumbnail yang sama

### Contoh 2: Banner dan Thumbnail Berbeda
```json
{
  "thumbnail": "image/modul-small.jpg",
  "banner_image": "image/modul-banner-large.jpg"
}
```
→ Banner menggunakan gambar khusus yang lebih besar

### Contoh 3: Banner dari URL Online
```json
{
  "thumbnail": "image/modul.jpg",
  "banner_image": "https://cdn.example.com/banner.jpg"
}
```

---

**Selamat mengatur banner! 🎨**

