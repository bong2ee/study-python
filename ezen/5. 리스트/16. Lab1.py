'''
    다음은 이젠아카데미 4강의실 1번부터 5번까지의 1분간 팔굽혀펴기 개수입니다.
    데이터는 리스트에 저장되어 있습니다
        result = [33, 40 , 12, 63, 52]
    아래처럼 출력해보시오

        1) 6번의 팔굽혀펴기 갯수는 9 개이다 .
            리스트의 마지막에 추가하시오.
        2) 2번은 재측정하여 50개를 하였다.
            2번의 데이터를 변경하시오
        3) 3번부터 6번까지의 데이터를 슬라이싱하시오
        4) 모든 데이터를 오름차순으로 정렬하시오
'''
result = [33, 40 , 12, 63, 52]
print(result)

result.append(9)
print(result)

result[1] = 50
print(result)


print(result[2:])

result.sort()
print(result)



