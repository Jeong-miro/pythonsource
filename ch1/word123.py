import time
import random

words = []

with open("./ch1/data/word.txt", "r", encoding="utf-8") as f:
    for word in f:
        words.append(word.strip())
#print(words)
start = time.time()
n,corr_cnt = 1, 0
#n : 반복횟수 카운트 corr_cnt : 정답 개수 카운트 
while n <= 5:
    random.shuffle(words)
    q = random.choice(words)
    print(f"Q{n})")        
    print(q)

    answer = input()
    if answer.strip() == q.strip():
        print("정답!!")
        corr_cnt += 1
    else:
        print("오타!!")

    n += 1

end = time.time()

et = end - start
et = format(et,".3f")
print(f"게임 시간 : {et}초, 정답개수 : {corr_cnt}개")
if  corr_cnt >= 3:
    print("합격")
else:
    print("불합격")