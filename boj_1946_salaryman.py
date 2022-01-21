# """
# sys.stdin.readline을 하는 이유는
# 안하면 시간 초과로 통과를 못하기 때문에 사용한다.
# sys.stdin.readline > raw_input() > input() 와 같이
# 입력속도가 빠르다.
# """

import sys
input = sys.stdin.readline
t=int(input())

for i in range(t):
    cnt = 1
    num = int(input())
    salaryman = []
    for j in range(num):
        salaryman.append([int(k)for k in input().split()])# paper,interview = map(int,input().split())
        # salaryman.append([paper,interview])
    
    salaryman.sort(key = lambda x : x[0])
    min = salaryman[0][1]
    

    for j in range(1,num):# 첫번째 하나를 기준으로 정렬을 한후 다음 사람의 2번째 성적이 첫번째보다 크다면 다음 사람은 무조건 붙는다.
        if salaryman[j][1] < min:
            min = salaryman[j][1]
            cnt += 1
    print(cnt)
