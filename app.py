import random
from flask import Flask, render_template

app = Flask(__name__)

# Complete 8-Brand Database
BRANDS = [
    {"id": "nike", "name": "Nike", "logo_ext": ".webp"},
    {"id": "puma", "name": "Puma", "logo_ext": ".jpg"},
    {"id": "adidas", "name": "Adidas", "logo_ext": ".jpg"},
    {"id": "under-armour", "name": "Under Armour", "logo_ext": ".png"},
    {"id": "reebok", "name": "Reebok", "logo_ext": ".png"},
    {"id": "new-balance", "name": "New Balance", "logo_ext": ".png"},
    {"id": "fila", "name": "Fila", "logo_ext": ".png"},
    {"id": "asics", "name": "ASICS", "logo_ext": ".png"}
]

@app.route('/')
def home():
    # All 9 of your designed banners are now active
    banners = [f"banner{i}.png" for i in range(1, 10)]
    return render_template('index.html', brands=BRANDS, banners=banners)

@app.route('/brand/<brand_id>')
def brand_page(brand_id):
    brand_info = next((b for b in BRANDS if b['id'] == brand_id), None)
    shoes = []
    # Generates 9 UNIQUE products with varied prices for the grid
    for i in range(1, 10):
        shoes.append({
            "name": f"{brand_info['name']} Pro Edition {random.randint(100, 999)}",
            "price": f"{random.randint(2499, 18999):,}", # Varied real-world prices
            "img": f"/static/images/{brand_id}{i}.webp"
        })
    return render_template('products.html', brand=brand_info, shoes=shoes)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
