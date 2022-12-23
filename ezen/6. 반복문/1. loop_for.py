'''
        for 변수 in 시퀀스 자료:
            명령문 
        예 ) for o in [1, 2, 3, 4]
             print(o)
             
        * 순서가 있는 자료형
            - 리스트, 문자열, range 객체, 튜플, 딕셔너리
            
        * range(10) : 0~9까지 포함하는 range 객체를 생성해줌
'''

champions = ["티모", "이즈리얼", "리신"]

for champion in champions:
    print("선택한 챔피언은", champion, "입니다.")

# 문자열 사용
message = "나는 할 수 있어! 다 할 수 있어!"
for word in message:
    print(word)

# range 객체 사용
x = range(10)
for i in x:
    print(i)

print()


# range(시작, 끝+1, 단계)
for i in range(1, 10, 2):
    print(i)
