print('Đây là chương trình tính tổng 2 số')
A = float(input('hãy nhập số A ='))
B = float(input('hãy nhập số B ='))
print('Hãy nhập yêu cầu của bạn để tính tổng hoặc tích')
print('với dấu + và x')
phep_toan=input('hãy nhập yêu cầu ')
if phep_toan == '+':
    print("Kết quả là =", A+B)
if phep_toan == 'x':
    print("Kết quả là =", A*B)