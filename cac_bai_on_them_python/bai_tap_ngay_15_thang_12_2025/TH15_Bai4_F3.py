A = int(input("Nhập số của bạn: "))
tong = 0
for a in range(1, A + 1):
    if a % 2 == 0 and a % 3 == 0:
        tong += a
print("Tổng các số chia hết cho 2 và 3 trong khoảng 1-n là:", tong)