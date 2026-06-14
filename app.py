import random
import os
from flask import Flask, render_template

app = Flask(__name__)

# Ground-truth Database matching your structural folders
BRANDS = [
    {"id": "nike", "name": "Nike", "logo_ext": ".webp"},
    {"id": "puma", "name": "Puma", "logo_ext": ".jpg"},
    {"id": "adidas", "name": "Adidas", "logo_ext": ".jpg"},
    {"id": "under-armour", "name": "Under Armour", "logo_ext": ".png"},
    {"id": "reebok", "name": "Reebok", "logo_ext": ".png"},
    {"id": "new-balance", "name": "New Balance", "logo_ext": ".png"},
    {"id": "fila", "name": "Fila", "logo_ext": ".png"},
    {"id": "asics", "name": "ASICS", "logo_ext": ".png"}  # <-- ASICS fully configured
]

@app.route('/')
def home():
    # Loop over your structured BRANDS list to calculate the logo file paths cleanly
    for brand in BRANDS:
        # Generates exact path tracking: /static/logos/nike.webp, /static/logos/asics.png, etc.
        brand["logo_url"] = f"/static/logos/{brand['id']}{brand['logo_ext']}"
        
    banners = [f"banner{i}.png" for i in range(1, 10)]
    return render_template('index.html', brands=BRANDS, banners=banners)

@app.route('/brand/<brand_id>')
def brand_page(brand_id):
    brand_info = next((b for b in BRANDS if b['id'] == brand_id), None)
    if not brand_info:
        brand_info = {"id": brand_id, "name": brand_id.replace('-', ' ').title(), "logo_ext": ".png"}
        
    shoes = []
    # Generates 8 beautiful product cards for your grid layout
    for i in range(1, 9):
        local_img_path = f"static/images/{brand_id}{i}.webp"
        
        # FAIL-SAFE: If you haven't added the individual shoe image yet, 
        # it uses a beautiful real shoe placeholder so your page layout stays gorgeous!
        if os.path.exists(local_img_path):
            img_url = f"/{local_img_path}"
        else:
            img_url = "https://unsplash.com"

        shoes.append({
            "name": f"{brand_info['name']} Pro Edition-0{i}",
            "price": f"{random.randint(3499, 14999):,}",
            "img": img_url
        })
        
    return render_template('products.html', brand=brand_info, shoes=shoes)

if __name__ == '__main__':
    # Essential for Docker environments
    app.run(debug=True, host='0.0.0.0', port=5000)
