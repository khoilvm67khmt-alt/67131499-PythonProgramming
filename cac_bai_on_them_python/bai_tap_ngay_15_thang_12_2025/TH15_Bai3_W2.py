while True:
    c = int(input("Nhập n (0 < n < 10): "))
    if 0 < c < 10:
        break
    else:
        print("Giá trị không hợp lệ, vui lòng nhập lại!")
print("Giá trị n vừa nhập là:", c)