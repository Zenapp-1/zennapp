# Cara Mengubah Materi dan Thumbnail Modul

## 📝 Struktur Data di `modules.json`

Setiap modul sekarang mendukung 2 field tambahan:
- **`thumbnail`**: URL atau path ke gambar thumbnail
- **`materials`**: Array berisi daftar materi pembelajaran

## 🖼️ Cara Mengubah Thumbnail

### Opsi 1: Menggunakan Gambar dari Folder `image/`
```json
{
  "id": 1,
  "title": "Investasi Dasar",
  "category": "Investasi",
  "level": 0,
  "description": "Pengenalan investasi dan prinsip dasar.",
  "thumbnail": "image/nama-gambar.jpg",
  "materials": [...]
}
```

### Opsi 2: Menggunakan URL Gambar Online
```json
{
  "id": 1,
  "title": "Investasi Dasar",
  "category": "Investasi",
  "level": 0,
  "description": "Pengenalan investasi dan prinsip dasar.",
  "thumbnail": "https://example.com/gambar.jpg",
  "materials": [...]
}
```

### Opsi 3: Menggunakan Gradient Default (Kosongkan)
```json
{
  "id": 1,
  "title": "Investasi Dasar",
  "category": "Investasi",
  "level": 0,
  "description": "Pengenalan investasi dan prinsip dasar.",
  "thumbnail": "",
  "materials": [...]
}
```

## 📚 Cara Mengubah Materi

Tambahkan array `materials` dengan struktur berikut:

```json
{
  "id": 1,
  "title": "Investasi Dasar",
  "category": "Investasi",
  "level": 0,
  "description": "Pengenalan investasi dan prinsip dasar.",
  "thumbnail": "image/crypto.jpeg",
  "materials": [
    {
      "name": "Pengenalan Investasi - Part 1",
      "url": "https://www.youtube.com/watch?v=xxxxx"
    },
    {
      "name": "Prinsip Dasar Investasi - Part 2",
      "url": "https://www.youtube.com/watch?v=yyyyy"
    },
    {
      "name": "Strategi Investasi Jangka Panjang",
      "url": "https://www.youtube.com/watch?v=zzzzz"
    }
  ]
}
```

### Field pada Materials:
- **`name`**: Nama/judul materi (wajib)
- **`url`**: Link YouTube atau URL materi (wajib)

## 📋 Contoh Lengkap

```json
{
  "modules": [
    {
      "id": 1,
      "title": "Investasi Dasar",
      "category": "Investasi",
      "level": 0,
      "description": "Pengenalan investasi dan prinsip dasar.",
      "thumbnail": "image/crypto.jpeg",
      "materials": [
        {
          "name": "Pengenalan Investasi - Part 1",
          "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        },
        {
          "name": "Prinsip Dasar Investasi - Part 2",
          "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        },
        {
          "name": "Tips Investasi untuk Pemula",
          "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        }
      ]
    },
    {
      "id": 2,
      "title": "Strategi Alokasi Aset",
      "category": "Investasi",
      "level": 2,
      "description": "Cara membagi portofolio sesuai tujuan.",
      "thumbnail": "image/ternak uang.jpeg",
      "materials": [
        {
          "name": "Strategi Alokasi Aset - Part 1",
          "url": "https://www.youtube.com/watch?v=xxxxx"
        }
      ]
    }
  ]
}
```

## ⚠️ Catatan Penting

1. **Jika `thumbnail` kosong atau tidak ada**: Sistem akan menggunakan gradient default sesuai tema halaman
2. **Jika `materials` kosong atau tidak ada**: Sistem akan menampilkan materi default "Part 1" dan "Part 2"
3. **Format JSON harus valid**: Pastikan menggunakan koma (`,`) yang benar dan tanda kurung yang seimbang
4. **Path gambar relatif**: Gunakan path relatif dari root folder (misal: `image/nama-gambar.jpg`)
5. **URL materi**: Bisa berupa link YouTube, Google Drive, atau URL lainnya

## 🔄 Setelah Mengubah `modules.json`

1. Simpan file `modules.json`
2. Refresh halaman modul di browser
3. Klik modul untuk melihat perubahan thumbnail dan materi

