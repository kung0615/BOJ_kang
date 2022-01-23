#회의실은 한개, n개의 회의, (1,3)같이 시작 끝시간 입력, 최대 회의 횟수
#회의끝과 동시에 시작이게 포인트
#그럼 끝시작과 시작시간이 같은 것 아니면 가장 차이가 작은것
#가장 먼저 작은 끝나는 시간부터 시작 즉, 오름차순으로 정렬 key = lambda x : x[1]
#그 후로 첫번째 x[1]을 finish에 저장 후 정렬의 다음값들과 비교 후 그 값의 x[1]을 finish에 저장
#a마지막print(cnt)
import sys
input = sys.stdin.readline
n=int(input())
l=list()
for i in range(n):#회의 시간들 입력 /// time = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x:(x[1], x[0]))
    s, f = map(int,input().split())
    l.append([s,f])
l.sort(key=lambda x : x[0])# 첫 시작 시간 기준으로 정렬
l.sort(key = lambda x : x[1])#첫끝나는 시간 기준으로 정렬
# 만약 2,2 1,2가 나오면 끝나느 시간으로만 정렬 하면 처음 2,2만 계산후 1,2는 계산하지 못하는 경우가 생긴다 
# 따라서 먼저 시작시간 순으로 정렬휴 끝나는 시간을 정렬하면 1,2 2,2로 되므로 놓치지않고 계산한다.
finish = l[0][1]
cnt = 1#첫 시작회의 저장
for i in range(1,n):
    if finish <= l[i][0]:
        finish = l[i][1]
        cnt += 1
print(cnt)
    


