# 🎨 Contoh HTML untuk Banner Modul

## 📋 Cara Menggunakan

Tambahkan field `banner_html` di JSON modul untuk menampilkan konten HTML custom di banner.

## 🎯 Contoh Struktur Banner

### Contoh 1: Banner dengan Welcome Section dan Level Path

```json
{
  "id": 1,
  "title": "On Boarding",
  "banner_html": "<div style=\"display: flex; justify-content: space-between; align-items: center; padding: 3rem; background: linear-gradient(135deg, rgba(6,182,212,0.2) 0%, rgba(59,130,246,0.15) 50%, rgba(99,102,241,0.1) 100%); border-radius: 1rem;\"><div style=\"flex: 1;\"><h1 style=\"font-size: 3rem; font-weight: bold; color: white; margin-bottom: 1rem;\">Welcome,<br>Start here</h1><button style=\"background: #06b6d4; color: white; padding: 1rem 2rem; border: none; border-radius: 0.5rem; font-size: 1.125rem; font-weight: 600; cursor: pointer; display: flex; align-items: center; gap: 0.5rem;\"><svg width=\"24\" height=\"24\" fill=\"white\" viewBox=\"0 0 24 24\"><path d=\"M8 5v14l11-7z\"/></svg>MULAI SEKARANG</button></div><div style=\"flex: 1; position: relative; height: 200px;\"><div style=\"position: absolute; top: 50%; left: 0; right: 0; height: 4px; background: rgba(255,255,255,0.3); transform: translateY(-50%); border-radius: 2px;\"></div><div style=\"position: absolute; left: 0; top: 50%; transform: translateY(-50%); background: #06b6d4; color: white; padding: 0.5rem 1rem; border-radius: 0.5rem; font-weight: 600;\">Level 0</div><div style=\"position: absolute; left: 25%; top: 50%; transform: translateY(-50%); background: #10b981; color: white; padding: 0.5rem 1rem; border-radius: 0.5rem; font-weight: 600;\">Level 1</div><div style=\"position: absolute; left: 50%; top: 50%; transform: translateY(-50%); background: #f59e0b; color: white; padding: 0.5rem 1rem; border-radius: 0.5rem; font-weight: 600;\">Level 2</div><div style=\"position: absolute; left: 75%; top: 50%; transform: translateY(-50%); background: #f97316; color: white; padding: 0.5rem 1rem; border-radius: 0.5rem; font-weight: 600;\">Level 3</div></div></div>",
  "banner_bg": "linear-gradient(135deg, rgba(6,182,212,0.2) 0%, rgba(59,130,246,0.15) 50%, rgba(99,102,241,0.1) 100%)"
}
```

### Contoh 2: Banner Sederhana dengan Teks

```json
{
  "id": 1,
  "title": "On Boarding",
  "banner_html": "<div style=\"text-align: center; padding: 4rem 2rem;\"><h1 style=\"font-size: 3rem; font-weight: bold; color: white; margin-bottom: 1rem;\">Welcome to On Boarding</h1><p style=\"font-size: 1.25rem; color: rgba(255,255,255,0.8); margin-bottom: 2rem;\">Mulai perjalanan belajar Anda di sini</p><button style=\"background: #06b6d4; color: white; padding: 1rem 2rem; border: none; border-radius: 0.5rem; font-size: 1.125rem; font-weight: 600; cursor: pointer;\">MULAI SEKARANG</button></div>",
  "banner_bg": "linear-gradient(135deg, rgba(6,182,212,0.3) 0%, rgba(59,130,246,0.2) 100%)"
}
```

## 📝 Field yang Tersedia

- **`banner_html`**: HTML content untuk banner (wajib jika ingin menggunakan HTML)
- **`banner_bg`**: Background color/gradient untuk banner (opsional)
- **`banner_image`**: Gambar banner (digunakan jika `banner_html` kosong)

## ⚠️ Catatan

1. Jika `banner_html` diisi, sistem akan menggunakan HTML content
2. Jika `banner_html` kosong, sistem akan menggunakan `banner_image` atau `thumbnail`
3. HTML bisa menggunakan inline styles atau class yang sudah ada
4. Pastikan HTML valid dan aman

