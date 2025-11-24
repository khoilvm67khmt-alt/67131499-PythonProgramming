import random
so_may_man = random.randint(1, 20)
print("Chào mừng bạn đến với Game Đoán Số!")
print("Mình đã chọn một số từ 1 đến 20. Hãy đoán xem số đó là bao nhiêu")
while True :
    try :
      doan = int(input("hãy nhập số may mắn của bạn "))
    except ValueError :
        print("Vui lòng nhập số nguyên hợp lệ")
        continue
    if doan < so_may_man :
        print("Tăng số lên đi bạn ơi !!!")
    elif doan > so_may_man :
        print("Giảm số xuống đi bạn ơi !!!")
    else :
        print(f"Chúc mừng !!! Bạn đã đoán đúng số {so_may_man}")
               