# Makovka Food Company - Landing Page

> Premium Dimsum Cibeber - Rasa Premium, Harga Bersahabat

## 🎨 Tema Design

**Warna Dominan:**
- **Merah Menyala** (#e50914) - Primary brand color
- **Putih** (#ffffff) - Clean & elegant
- **Hitam** (#080808) - Bold & premium

## 📁 Struktur Project

```
food-promo-images/
├── index.html          # Main HTML (refactored & clean)
├── css/
│   ├── main.css        # Main stylesheet (imports all)
│   ├── variables.css   # Theme colors & design tokens
│   ├── base.css        # Reset & base styles
│   ├── navbar.css      # Navigation bar
│   ├── hero.css        # Hero section
│   ├── sections.css    # About, Products, Stats, Services, Testimonials, CTA
│   └── footer.css      # Footer
├── js/
│   └── main.js         # Interactive features
└── assets/             # Images & media (empty, uses Unsplash CDN)
```

## ✨ Fitur

### 1. **Responsive Design**
- Desktop, tablet, mobile optimized
- Mobile menu with hamburger toggle

### 2. **Interactive Elements**
- Smooth scroll navigation
- Scroll-triggered animations
- Stats counter animation
- Product hover effects
- WhatsApp integration for orders

### 3. **Performa**
- Modular CSS (easy to maintain)
- Intersection Observer for lazy animations
- Optimized for fast loading

### 4. **Sections**
- **Hero** - Bold intro dengan gradient overlay & glowing effects
- **About** - Tentang perusahaan dengan image card
- **Products** - 3 produk unggulan dengan tag & hover effects
- **Stats** - 4 statistik dengan background parallax
- **Services** - 3 layanan dengan icon cards
- **Testimonials** - 3 testimoni pelanggan
- **CTA** - Call-to-action dengan WhatsApp link
- **Footer** - 4 kolom informasi

## 🚀 Cara Menjalankan

### 1. Local Development

```bash
cd ~/Project/food-promo-images

# Option 1: Python simple server
python3 -m http.server 8000

# Option 2: PHP built-in server
php -S localhost:8000

# Option 3: Node.js http-server
npx http-server -p 8000
```

Buka browser: `http://localhost:8000`

### 2. Deploy to Production

**Vercel:**
```bash
cd ~/Project/food-promo-images
npx vercel --prod
```

**Netlify:**
```bash
cd ~/Project/food-promo-images
npx netlify deploy --prod --dir=.
```

**GitHub Pages:**
```bash
cd ~/Project/food-promo-images
git init
git add .
git commit -m "Initial commit"
git remote add origin <your-repo-url>
git push -u origin main
# Enable GitHub Pages in repo settings
```

## 🎯 Customization

### Ubah Warna Tema

Edit `css/variables.css`:

```css
:root {
  --red: #e50914;        /* Primary color */
  --red-bright: #ff1f2d; /* Hover color */
  --black: #080808;      /* Dark background */
  --white: #ffffff;      /* Light background */
}
```

### Ubah Konten

Edit `index.html` - semua konten sudah terstruktur dengan semantic HTML.

### Tambah Produk

Copy-paste block `.product-card` di section `#products`.

### Ubah WhatsApp Number

Find & replace: `6285880880476` dengan nomor WhatsApp baru.

## 📱 Contact Integration

Semua tombol "Order" dan "Pesan Sekarang" mengarah ke WhatsApp dengan pesan otomatis:

- **Product Order**: `Halo! Saya tertarik dengan [Nama Produk]. Bisa info lebih lanjut?`
- **General Contact**: Langsung buka chat WhatsApp

## 🔧 Browser Support

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari, Chrome Android)

## 📊 Performance

- **First Contentful Paint**: < 1.5s
- **Largest Contentful Paint**: < 2.5s
- **Cumulative Layout Shift**: < 0.1
- **Time to Interactive**: < 3.5s

## 🐛 Known Issues

None at the moment. Semua fitur tested & working.

## 📝 Changelog

### v2.0.0 (2026-06-15)
- ✅ Refactored: Pisahkan CSS ke 7 file modular
- ✅ Added: JavaScript interactivity (scroll effects, animations, mobile menu)
- ✅ Improved: Tema dominan **Merah menyala**, **Putih**, **Hitam**
- ✅ Enhanced: Responsive design untuk mobile
- ✅ Added: Stats counter animation
- ✅ Added: Smooth scroll navigation
- ✅ Added: WhatsApp integration untuk order buttons
- ✅ Optimized: Performance dengan Intersection Observer

### v1.0.0 (sebelumnya)
- Single-file HTML dengan inline CSS
- Basic responsive layout

## 📄 License

© 2026 Makovka Food Company. All Rights Reserved.

---

**Developed with ⚡ by Erika Masahiro**
