print('Đây là chương trình tính BMI')
A=float(input('Hãy nhập chiều cao (mét) của bạn '))
B=float(input('Hãy nhập cân nặng (kí) của bạn '))
C=B/(A*A)
print('chỉ số BMI của bạn là : ', C)
if C < 18.5:
    print('cơ thể của bạn gầy')
elif C >= 25.0:
    print('cơ thể bạn đang thừa cân')
elif 18.5 <= C <= 24.9:
    print('cơ thể bạn đang bình thường')
