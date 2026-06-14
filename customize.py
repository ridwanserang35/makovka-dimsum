#!/usr/bin/env python3
"""Customize index-temp.html with Makovka real data"""

# Product data
products = [
    {
        "name": "Nashville Fire Cheese",
        "image": "nashville-fire-cheese.jpg",
        "price": "28.000",
        "desc": "Dimsum dengan saus Nashville Fire yang pedas dan topping keju melimpah. Kombinasi sempurna antara pedas dan gurih yang bikin nagih! Cocok untuk pecinta sensasi pedas maksimal."
    },
    {
        "name": "Nashville Fire",
        "image": "nashville-fire.jpg",
        "price": "27.000",
        "desc": "Dimsum dengan saus Nashville Fire glossy dan pedas menggigit. Rasa pedas autentik yang menantang lidah Anda. Wajib coba untuk pecinta makanan pedas ekstrem!"
    },
    {
        "name": "Cheese Mayo",
        "image": "cheese-Mayo.jpg",
        "price": "26.000",
        "desc": "Dimsum lembut dengan saus mayo keju yang creamy dan topping keju kotak. Rasa gurih yang meleleh di mulut dengan tekstur lembut sempurna. Favorit untuk semua umur!"
    },
    {
        "name": "Garlic Mayo",
        "image": "Garlci-Mayo.jpg",
        "price": "25.000",
        "desc": "Dimsum dengan saus garlic mayo kaya rasa bawang putih dan herbs. Aroma harum menggugah selera dengan cita rasa gurih yang memanjakan. Pilihan sempurna untuk pecinta garlic!"
    },
    {
        "name": "Hot Mentai",
        "image": "Hot-Mentai.jpg",
        "price": "30.000",
        "desc": "Dimsum dengan saus mentai pedas khas Jepang dan taburan chili seasoning. Perpaduan unik creamy, gurih, dan pedas yang eksotis. Menu premium yang wajib dicoba!"
    }
]

# Read template
with open('index-temp.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace title
html = html.replace('Makovka Food Company', 'Makovka - Premium Dimsum Cibeber')

# Replace hero section
html = html.replace(
    'Taste the <strong>Future</strong> of Food',
    'Rasakan <strong>Kelezatan</strong> Dimsum Autentik'
)
html = html.replace(
    'Experience culinary excellence with our carefully crafted dishes.\n            Made with love, served with passion.',
    'Dimsum premium dengan berbagai varian rasa yang menggugah selera. Dibuat dengan bahan pilihan, disajikan dengan cinta untuk kepuasan Anda.'
)
html = html.replace('Premium Quality', 'Premium Dimsum')
html = html.replace('Explore Menu 🍽️', 'Lihat Menu 🥟')
html = html.replace('Learn More', 'Order via WhatsApp')
html = html.replace('href="#about"', 'href="https://wa.me/6285880880476"')
html = html.replace('Order Now', 'Pesan Sekarang')
html = html.replace('href="#"', 'href="https://wa.me/6285880880476"')

# Replace about section
html = html.replace(
    'We craft exceptional culinary experiences',
    'Makovka: Dimsum Premium Pilihan Keluarga'
)
html = html.replace(
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do\n              eiusmod tempor incididunt ut labore et dolore magna aliqua.',
    'Makovka adalah brand dimsum premium yang menghadirkan cita rasa autentik dengan kualitas terbaik. Kami berkomitmen untuk memberikan pengalaman kuliner dimsum yang tak terlupakan.'
)
html = html.replace(
    'Ut enim ad minim veniam, quis nostrud exercitation ullamco\n              laboris nisi ut aliquip ex ea commodo consequat.',
    'Setiap produk kami dibuat dengan bahan pilihan dan resep khas yang telah teruji. Dengan berbagai varian rasa inovatif, Makovka hadir untuk memenuhi selera pecinta dimsum di Indonesia.'
)

# Replace check items
html = html.replace('100% Fresh Ingredients', 'Bahan 100% Fresh & Berkualitas')
html = html.replace('Award Winning Chefs', 'Resep Teruji & Rasa Konsisten')
html = html.replace('Fast Delivery', 'Delivery Cepat & Aman')

# Replace stats
html = html.replace('10K+<', '5K+<')
html = html.replace('Happy Customers', 'Pelanggan Puas')
html = html.replace('200+', '50+')
html = html.replace('Menu Items', 'Varian Menu')
html = html.replace('15+', '3+')
html = html.replace('Awards Won', 'Tahun Berpengalaman')
html = html.replace('4.9★', '4.8★')
html = html.replace('Rating', 'Rating Pelanggan')

# Replace services
html = html.replace('Fast Delivery', 'Delivery Cepat')
html = html.replace(
    'Get your favorite food delivered hot and fresh to your doorstep.',
    'Pesanan Anda dikirim cepat dan aman langsung ke rumah. Dimsum tetap hangat dan fresh saat tiba.'
)
html = html.replace('Premium Quality', 'Kualitas Premium')
html = html.replace(
    'We use only the finest ingredients for the best taste.',
    'Kami hanya gunakan bahan pilihan berkualitas tinggi untuk cita rasa terbaik dan konsisten.'
)
html = html.replace('24/7 Support', 'Order Mudah')
html = html.replace(
    'Our customer service team is always ready to help you.',
    'Pesan langsung via WhatsApp dengan mudah. Respon cepat dan layanan ramah untuk Anda.'
)

# Replace CTA
html = html.replace(
    'Ready to Order?',
    'Siap Menikmati Kelezatan?'
)
html = html.replace(
    "Let's start your culinary journey with us today. Fresh food,\n            great taste, delivered fast!",
    'Mari mulai pengalaman kuliner dimsum premium Anda hari ini. Rasa nikmat, harga terjangkau, delivery cepat!'
)

# Replace footer contact
html = html.replace('123 Food Street, City, Country', 'Pusat Jajanan Bunderan Perumnas Cibeber (PCI)')
html = html.replace('+1 234 567 8900', '+62 858-8088-0476')
html = html.replace('info@makovka.com', 'wa.me/6285880880476')

# Build product HTML
product_html = ''
for i, p in enumerate(products, 1):
    tag = 'BEST SELLER' if i <= 2 else 'POPULER' if i == 3 else 'PREMIUM'
    product_html += f'''
                <div class="product-card">
                  <div
                    class="product-img"
                    style="background-image: url('{p["image"]}')"
                  >
                    <span class="tag">{tag}</span>
                  </div>
                  <div class="product-body">
                    <h3>{p["name"]}</h3>
                    <p>
                      {p["desc"]}
                    </p>
                    <div class="price">
                      Rp {p["price"]}
                      <button onclick="window.open('https://wa.me/6285880880476?text=Halo%20Makovka,%20saya%20mau%20pesan%20{p["name"].replace(" ", "%20")}', '_blank')">Pesan</button>
                    </div>
                  </div>
                </div>
'''

# Find and replace product grid content
import re
grid_pattern = r'(<div class="product-grid">)(.*?)(</div>\s*</div>\s*<!-- STATS -->)'
html = re.sub(grid_pattern, r'\1' + product_html + r'\n          \3', html, flags=re.DOTALL)

# Replace testimonials
testimonials = [
    {
        "name": "Budi Santoso",
        "initial": "B",
        "role": "Pelanggan Setia",
        "text": "Nashville Fire Cheese-nya juara! Pedasnya pas banget dan kejunya melimpah. Jadi langganan keluarga setiap weekend. Recommended!"
    },
    {
        "name": "Siti Nurhaliza",
        "initial": "S",
        "role": "Food Blogger",
        "text": "Cheese Mayo favorit saya! Teksturnya lembut, rasanya creamy, dan harganya sangat terjangkau. Makovka emang dimsum terenak di Cibeber!"
    },
    {
        "name": "Andi Wijaya",
        "initial": "A",
        "role": "Pengusaha",
        "text": "Hot Mentai-nya premium banget! Rasa mentai autentik dengan level pedas yang menantang. Delivery-nya juga cepat dan dimsum tetap hangat."
    }
]

testimonial_html = ''
for t in testimonials:
    testimonial_html += f'''
                <div class="testimonial-card">
                  <div class="stars">★★★★★</div>
                  <p>
                    "{t["text"]}"
                  </p>
                  <div class="customer">
                    <div class="avatar">{t["initial"]}</div>
                    <div>
                      <h4>{t["name"]}</h4>
                      <span>{t["role"]}</span>
                    </div>
                  </div>
                </div>
'''

testi_pattern = r'(<div class="testimonial-grid">)(.*?)(</div>\s*</div>\s*<!-- CTA -->)'
html = re.sub(testi_pattern, r'\1' + testimonial_html + r'\n          \3', html, flags=re.DOTALL)

# Replace section headings
html = html.replace('Our Products', 'Menu Kami')
html = html.replace(
    'Discover our carefully curated menu of delicious dishes.',
    'Temukan berbagai varian dimsum premium kami yang menggugah selera.'
)
html = html.replace('What We Offer', 'Kenapa Pilih Makovka?')
html = html.replace(
    'Exceptional services that make us stand out from the rest.',
    'Layanan terbaik yang membuat kami berbeda dari yang lain.'
)
html = html.replace('What Customers Say', 'Testimoni Pelanggan')
html = html.replace(
    'Hear from our satisfied customers about their experience.',
    'Dengar langsung pengalaman pelanggan kami yang puas.'
)

# Replace emoji
html = html.replace('🍴', '🥟')

# Write output
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ index.html berhasil di-customize dengan data Makovka!")
print("📂 File: ~/Project/food-promo-images/index.html")
print("🥟 5 produk | 3 testimonial | kontak lengkap")
