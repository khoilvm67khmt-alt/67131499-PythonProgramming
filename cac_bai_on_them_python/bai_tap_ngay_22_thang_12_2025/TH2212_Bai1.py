while True:
    w = float(input("Nhập chiều rộng (w >= 0): "))
    h = float(input("Nhập chiều dài (h <= 100): "))
    if w >= 0 and h <= 100:
        break
    else:
        print("Sai, nhập lại!")
chu_vi = 2 * (w + h)
dien_tich = w * h
print(f"Chu vi: {chu_vi:.2f}")
print(f"Diện tích: {dien_tich:.2f}")
