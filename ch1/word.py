# 영어타자 프로그램

from random import shuffle, choice
import time
correct = 0
# word.txt 읽어서 
with open("./ch1/data/word.txt", "r", encoding="utf-8") as f:
# 섞기 random.shuffle()
        contents = f.readlines()
        shuffle(contents)
        start = time.time()
# 임의로 하나 추출 random.choice()
# 5문제 출제
        for i in range(1,6):
            eng = contents[i].strip()
            print("출력된 영단어 :",eng)
            usertap = input(f"영타 입력: ")
            print("입력한 값 : ",usertap)
# Q1) then
# #input() 
# input 결과에 따라 정답!! // 오타!!            
            if usertap == eng:
                print("정답!!")
                correct += 1
            else:
                print("오타!!")
# 게임 시간 출력
# time.time()
# 출력문 ==> 게임시간 : 10초, 정답 개수 : 3개
# 3개이상 정답인 경우 합격 or 불합격
end= time.time()

print(f"게임시간 : {end-start}, 정답 개수 : {correct}")
if correct >= 3 :
    print("합격")
else:
    print("불합격")
