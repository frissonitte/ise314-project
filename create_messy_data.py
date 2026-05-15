import random
import csv
from datetime import datetime, timedelta

random.seed(42)

# ── helpers ──────────────────────────────────────────────────────────────────
def rand_date():
    base = datetime(2023, 1, 1)
    d = base + timedelta(days=random.randint(0, 730))
    # Mix 3 date formats intentionally
    fmt = random.choice(["dd/mm/yyyy", "mm-dd-yyyy", "iso"])
    if fmt == "dd/mm/yyyy":  return d.strftime("%d/%m/%Y")
    if fmt == "mm-dd-yyyy":  return d.strftime("%m-%d-%Y")
    return d.strftime("%Y-%m-%d")

def rand_price():
    p = round(random.uniform(5, 500), 2)
    # Mix formats: plain, $, €, comma-decimal
    style = random.choice(["plain", "dollar", "euro", "comma"])
    if style == "plain":   return str(p)
    if style == "dollar":  return f"${p}"
    if style == "euro":    return f"€{p}"
    # comma decimal (Turkish locale style)
    return str(p).replace(".", ",")

def rand_customer():
    names  = ["Ahmet Yılmaz","Zeynep Kaya","Emre Demir","Fatma Şahin",
              "Can Arslan","Elif Çelik","Burak Aydın","Selin Koç",
              "Mert Öztürk","Gül Yıldız","Hakan Doğan","Ayşe Polat",
              "Tarık Güneş","Merve Aksoy","Barış Erdoğan","Deniz Kurt"]
    phones = [f"05{random.randint(10,59)}{random.randint(1000000,9999999)}" for _ in range(16)]
    domains= ["gmail.com","yahoo.com","hotmail.com","outlook.com"]
    n = random.choice(names)
    e = n.split()[0].lower() + str(random.randint(1,99)) + "@" + random.choice(domains)
    p = random.choice(phones)
    # Issue: all three in one column
    return f"{n}|{e}|{p}"

def rand_address():
    streets = ["Atatürk Cad. No:12","Bağdat Cad. No:45","İstiklal Cad. No:7",
               "Cumhuriyet Blv. No:3","Gazi Cad. No:88","Millet Cad. No:22"]
    cities  = ["Istanbul","Ankara","Izmir","Bursa","Antalya","Adana","Sakarya"]
    country = random.choice(["Turkey","TR","Türkiye","TURKEY"])  # inconsistent
    # Issue: multi-info in one column
    return f"{random.choice(streets)}, {random.choice(cities)}, {country}"

# ── product reference table (2nd file) ────────────────────────────────────────
product_ids = list(range(1001, 1021))
categories_clean = ["Electronics","Clothing","Books","Home & Garden",
                    "Sports","Toys","Food & Beverage","Automotive"]

products = []
for pid in product_ids:
    products.append({
        "product_id": pid,
        "product_name": random.choice([
            "Wireless Headphones","Smart Watch","Running Shoes","Yoga Mat",
            "Python Cookbook","LED Desk Lamp","Portable Charger","Backpack",
            "Coffee Maker","Bluetooth Speaker","Phone Case","Notebook Set",
            "Gaming Mouse","Sunglasses","Resistance Bands","Water Bottle"
        ]),
        "category": random.choice(categories_clean),
        "stock": random.randint(0, 500)
    })

with open("outputs/products_ref.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["product_id","product_name","category","stock"])
    w.writeheader()
    w.writerows(products)

# ── main orders table ─────────────────────────────────────────────────────────
statuses_dirty = [
    "Delivered","Delivered","Shipped","Shipped","Processing","Processing",
    "Cancelled","Returned",
    "Deliverd","Deliverd",    # typo
    "Shiped","Shippd",        # typos
    "PROCESSING",             # wrong case
    None,                     # missing
]

discount_styles = [
    "10%","5%","0%","15%","20%","25%","0.10","0.05","0.15",
    None, None,               # missing
    "30%",
]

rows = []
for i in range(105):  # 105 rows, will have ~5 dupes so net ≥100 after dedup
    pid = random.choice(product_ids)
    qty = random.randint(-3, 20)    # some negatives (issue)
    price = rand_price()
    rating = random.choice([1,2,3,4,5,5,5,4,4, None, 6, 0])  # 6 and 0 out-of-range
    row = {
        # No index / ID column (issue)
        "customer_info": rand_customer() if random.random() > 0.05 else None,  # some NULL
        "order_date":    rand_date(),
        "product_id":    pid if random.random() > 0.04 else None,
        "price":         price,
        "quantity":      qty,
        "shipping_address": rand_address() if random.random() > 0.06 else None,
        "status":        random.choice(statuses_dirty),
        "discount":      random.choice(discount_styles),
        "customer_rating": rating,
        # Issue: category stored in ORDERS table too (inconsistently cased, fragmented vs products_ref)
        "category_tag":  random.choice(["electronics","Electronics","ELECTRONICS",
                                         "Clothing","clothing","Books","BOOKS",
                                         "home","Home & Garden",None]),
    }
    rows.append(row)

# Inject ~5 deliberate duplicate rows
for _ in range(5):
    rows.append(random.choice(rows[:80]))

random.shuffle(rows)

fieldnames = ["customer_info","order_date","product_id","price","quantity",
              "shipping_address","status","discount","customer_rating","category_tag"]

with open("outputs/orders_raw.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)

print(f"orders_raw.csv  → {len(rows)} rows")
print(f"products_ref.csv → {len(products)} rows")

# Quick sanity check
nulls = sum(1 for r in rows if r["customer_info"] is None)
typos = sum(1 for r in rows if r["status"] in ["Deliverd","Shiped","Shippd","PROCESSING"])
negs  = sum(1 for r in rows if isinstance(r["quantity"], int) and r["quantity"] < 0)
print(f"NULL customer_info: {nulls}  |  status typos: {typos}  |  negative qty: {negs}")