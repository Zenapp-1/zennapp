# 📄 Cara Menambahkan Tombol PDF / Summary

## 🎯 Fitur Baru

Sekarang setiap modul bisa memiliki tombol **"Download PDF / Summary"** yang akan mengarahkan ke file PDF atau summary.

## ✏️ Cara Menggunakan

### 1️⃣ Buka File JSON Modul

Buka file JSON sesuai modul yang ingin diubah:
- **Akademi Crypto** → `data/akademi-crypto.json`
- **Trade with Suli** → `data/trade-with-suli.json`
- **Ternak Uang** → `data/ternak-uang.json`

### 2️⃣ Tambahkan Field `pdf_url`

Tambahkan atau edit field `"pdf_url"` di setiap modul:

```json
{
  "id": 1,
  "title": "Investasi Dasar",
  "description": "...",
  "thumbnail": "image/crypto.jpeg",
  "youtube_url": "https://www.youtube.com",
  "pdf_url": "path/ke/file.pdf",
  "materials": [...]
}
```

## 📋 Opsi URL PDF/Summary

### Opsi 1: File PDF Lokal

Jika file PDF ada di folder project:

```json
{
  "pdf_url": "pdf/investasi-dasar.pdf"
}
```

### Opsi 2: File PDF di Google Drive

Gunakan link share Google Drive (ubah menjadi direct link):

```json
{
  "pdf_url": "https://drive.google.com/file/d/FILE_ID/view?usp=sharing"
}
```

**Tips:** Untuk membuat link download langsung, ganti `/view?usp=sharing` dengan `/uc?export=download&id=FILE_ID`

### Opsi 3: File PDF di Server/Cloud

```json
{
  "pdf_url": "https://example.com/files/summary.pdf"
}
```

### Opsi 4: File PDF di Dropbox

```json
{
  "pdf_url": "https://www.dropbox.com/s/FILE_ID/file.pdf?dl=1"
}
```

**Catatan:** Tambahkan `?dl=1` di akhir URL Dropbox untuk direct download.

### Opsi 5: Tidak Ada PDF (Kosongkan)

Jika modul tidak memiliki PDF, kosongkan field:

```json
{
  "pdf_url": ""
}
```

**Tombol akan otomatis disembunyikan jika `pdf_url` kosong.**

## 🔄 Alternatif: Menggunakan `summary_url`

Selain `pdf_url`, Anda juga bisa menggunakan `summary_url`:

```json
{
  "summary_url": "https://example.com/summary.pdf"
}
```

Sistem akan otomatis mendeteksi dan menggunakan salah satu yang tersedia.

## 📝 Contoh Lengkap

### Sebelum (Tanpa PDF):
```json
{
  "id": 1,
  "title": "Investasi Dasar",
  "description": "Pengenalan investasi...",
  "thumbnail": "image/crypto.jpeg",
  "youtube_url": "https://www.youtube.com",
  "pdf_url": "",
  "materials": [...]
}
```

### Sesudah (Dengan PDF):
```json
{
  "id": 1,
  "title": "Investasi Dasar",
  "description": "Pengenalan investasi...",
  "thumbnail": "image/crypto.jpeg",
  "youtube_url": "https://www.youtube.com",
  "pdf_url": "pdf/investasi-dasar-summary.pdf",
  "materials": [...]
}
```

## 🎨 Tampilan Tombol

Tombol **"Download PDF / Summary"** akan muncul:
- Di halaman detail modul
- Setelah deskripsi modul
- Sebelum daftar materi
- Dengan ikon PDF yang menarik
- Warna merah yang mencolok

## ⚠️ Tips Penting

1. **Format URL harus valid**: Pastikan URL PDF bisa diakses
2. **File PDF harus ada**: Pastikan file PDF ada di path yang dimaksud
3. **Link Google Drive**: Gunakan direct download link untuk Google Drive
4. **Link Dropbox**: Tambahkan `?dl=1` di akhir URL untuk direct download
5. **Jika kosong**: Tombol akan otomatis disembunyikan

## 🔍 Troubleshooting

**Q: Tombol tidak muncul?**
A: Pastikan field `pdf_url` atau `summary_url` tidak kosong dan berisi URL yang valid.

**Q: PDF tidak bisa didownload?**
A: 
- Pastikan URL bisa diakses
- Untuk Google Drive, gunakan direct download link
- Untuk Dropbox, tambahkan `?dl=1` di akhir URL

**Q: Ingin mengubah teks tombol?**
A: Edit file HTML dan cari teks "Download PDF / Summary" di bagian tombol.

**Q: Ingin menambahkan lebih dari satu PDF?**
A: Saat ini hanya mendukung satu PDF per modul. Untuk multiple PDF, bisa ditambahkan di array `materials` dengan nama yang berbeda.

## 📂 Struktur Folder yang Disarankan

```
web adli/
├── data/
│   ├── akademi-crypto.json
│   ├── trade-with-suli.json
│   └── ternak-uang.json
├── pdf/
│   ├── investasi-dasar.pdf
│   ├── strategi-alokasi.pdf
│   └── ...
└── ...
```

Dengan struktur ini, Anda bisa menggunakan path seperti:
```json
{
  "pdf_url": "pdf/investasi-dasar.pdf"
}
```

---

**Selamat menambahkan PDF/Summary! 📚**

