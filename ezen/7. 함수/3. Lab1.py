'''
    세 개의 정수를 인자로 받아,
    합계와 평균을 출력해주는 함수를 만드시오

    예) 합계:          평균:
'''


# print("세 개의 정수 입력>>>")
# x = int(input())
# y = int(input())
# z = int(input())
# def sum(a, b, c):
#     print(a + b + c)
#
#
# def avg(a, b, c):
#     print((a + b + c) / 3)
#
#
# sum(x, y, z)
# avg(x, y, z)

# 설명문(docstring)   """
# 문자열 포매팅(f"")
def print_sum_avg(x, y, z):
    """
    세 개의 숫자를 받아 합계와 평균을 출력하는 함수
    :param a:
    :param b:
    :param c:
    :return:
    """
    sum = x + y + z
    avg = sum / 3
    print(f"합계: {sum} 평균: {avg}")


print_sum_avg(10, 20, 30)

