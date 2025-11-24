so_luong = [15, 8, 22, 5, 12, 3]
ten_san_pham = ["Áo", "Quần", "Giày", "Túi", "Mũ", "Ví"]

for so in range(len(so_luong)):
    if so_luong[so] < 10:
        print(f"Sản phẩm '{ten_san_pham[so]}' cần nhập thêm (đang có {so_luong[so]})")