t=int(input())
salaryman = []
cnt_list = []
for i in range(t):
    
    num = int(input())
    for j in range(num):
        salaryman.append([int(k) for k in input().split()])
    salaryman.sort(key = lambda x : x[0])
    
    cnt = 1
    for l in range(num-1):# 첫번째 하나를 기준으로 정렬을 한후 다음 사람의 2번째 성적이 첫번쩨보다 크다면 다음 사람은 무조건 붙는다.
        if salaryman[l][1] > salaryman[l+1][1]:
            cnt += 1
    cnt_list.append(cnt)

for m in range(len(cnt_list)):
    print(cnt_list[m]) 
   