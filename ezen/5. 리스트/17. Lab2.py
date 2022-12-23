'''
    턱걸이 평균 측정 프로그램
    먼저, 턱걸이 횟수를 저장할 빈 리스트를 만드시오
    그리고 일주일간의 턱걸이 횟수를 입력받아서 리스트에 저장하시오
    리스트에 저장된 데이터의 평균을 구해 출력하시오

    예시)
    1일차 턱걸이 횟수 >>>
        ...
    7일차 턱걸이 횟수 >>>

'''

list = []

list.append(int(input("1일차 턱걸이 횟수 >>> ")))
list.append(int(input("2일차 턱걸이 횟수 >>> ")))
list.append(int(input("3일차 턱걸이 횟수 >>> ")))
list.append(int(input("4일차 턱걸이 횟수 >>> ")))
list.append(int(input("5일차 턱걸이 횟수 >>> ")))
list.append(int(input("6일차 턱걸이 횟수 >>> ")))
list.append(int(input("7일차 턱걸이 횟수 >>> ")))

print("턱걸이 평균 횟수 >>> ", sum(list) / len(list))