# nhập điểm 3 môn toán, lí ,hoá
A=float(input("nhập điểm toán của bạn: "))
B=float(input("nhập điểm lí của bạn: "))
C=float(input("nhập điểm hoá của bạn: "))
D= A+B+C # điều kiện 
if D >= 15 and A >4 and B > 4 and C > 4: # điều kiện tổng điểm >= 15 và không có môn nào dưới 4
    print("đậu")
    if A > 5 and B > 5 and C >5:
      print("Học đều các môn")
    else:
       print("Học chưa đều các môn")
else:
    print("Thi hỏng")
       
   
    