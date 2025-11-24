diem_so = [8.5, 7.0, 9.2, 6.8, 5.5, 8.8]
for diem in diem_so :
    if diem >= 8 :
        print(f"{diem} => Điểm Giỏi")
    elif 6.5 < diem < 7.9 :
        print(f"{diem} => Điểm khá")
    elif diem < 6.5 :
        print(f"{diem} => Điểm trung bình")