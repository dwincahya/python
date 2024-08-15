# Daftar Produk
products = {
    "1": {"name": "Kulkas LG 2 Pintu", "price": 2339000, "stock": 20},
    "2": {"name": "Monitor LG 19 inch", "price": 1499000, "stock": 50},
    "3": {"name": "Monitor LG 16 invh", "price": 899000, "stock": 80},
}

def add_to_cart(cart, product_id, quantity):
    if product_id in products and products[product_id]["stock"] >= quantity:
        cart.append({"product_id": product_id, "quantity": quantity})
        products[product_id]["stock"] -= quantity
    else:
        print("Produk tidak tersedia atau stok tidak cukup.")

def checkout(cart):
    total = sum(products[item["product_id"]]["price"] * item["quantity"] for item in cart)
    print(f"Total belanja Anda: Rp{total}")
    payment = int(input("Masukkan jumlah uang yang dibayarkan: "))
    
    if payment >= total:
        change = payment - total
        print(f"Pembayaran berhasil. Kembalian Anda: Rp{change}")
        cart.clear()
    else:
        print("Uang tidak cukup untuk membayar.")

def main():
    cart = []
    print("Selamat datang di CahyaStore!")
    
    while True:
        print("\nDaftar Produk:")
        for pid, pdata in products.items():
            print(f"{pid}: {pdata['name']} - Rp{pdata['price']} (Stok: {pdata['stock']})")
        
        option = input("Pilih produk berdasarkan ID atau ketik 'checkout' untuk membayar: ")
        
        if option == "checkout":
            checkout(cart)
            break
        elif option in products:
            qty = int(input(f"Masukkan jumlah {products[option]['name']} yang ingin dibeli: "))
            add_to_cart(cart, option, qty)
        else:
            print("Produk tidak ditemukan.")

if __name__ == "__main__":
    main()
