#한번에 하나나 두 계단씩 오를 수 있다
#단 연속된 세 개의 계단을 밟아서는 안 된다 이때 시작점은 포함하지 않는다

#마지막 도착 계단은 반드시 밟아야 한다.
#최대값 점수를 구하라

#만약 18,20,15,25,10,20이 주어지면,,,시작점 기준으로 더해나가는데 
#이떄 시적점 기준 index 2 까지는 연속이 가능한점을 염두하고
#다로 위의 점수와 그 위의 점수를 비교하여 더한다.. 그리고 이때 마지막 점수는 무조건 포함해야하므로
#그냥 더해놓고 없다고 치고 계산하는것이 편할거 같다..

n=int(input())#계단 개수
floor = list()
choi_index = list()#이게 앞서 선택된 index를 저장할 곳.
sum = 0
for j in range(n):#계단 입력 받는다
    f=int(input())
    floor.append(f)

if len(floor) > 1:#1보다 작다면 필요 없는 것 이다.
    sum += floor[-1]#끝의 수는 없다고 생각
    floor.pop(-1)

sum +=floor[0]
choi_index.append(0)#시작점은 더해놓고 시작

i=1
while i < len(floor)-1:#끝점을 지웠고 i+1씩 비교를 하므로 -1
    max = 0
    if floor[i]<floor[i+1]:
        max = floor[i+1]
        sum+=max
        choi_index.append(i+1)
        i+=2
    else:
        if (i-1 not in choi_index or i-2 not in choi_index):
            max = floor[i]
            sum += max
            choi_index.append(i)
            i+=1
        else:
            max=floor[i+1]
            sum+=max
            choi_index.append(i)
            i+=2
print(sum) 

