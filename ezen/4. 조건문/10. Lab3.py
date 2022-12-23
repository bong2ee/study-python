# 비만도 계산기를 만들어 보시오.

'''
예시 )
        BMI계산기 입니다.
        신장 : 입력
        몸무게 : 입력
        BMI :
'''
print("BMI 계산기 입니다.")
h = int(input("신장 : "))
w = int(input("몸무게 : "))

BMI = w / (h*h) * 10000

print("BMI : ",BMI)
