#n*m체스판 총 4가지로만 움직,가장 왼쪽 아래에서 출발
#[(2,1),(1,2),(-1,2),(-2,1)] 이게 보면 왼쪽으로 절대 안간다.. 즉 오른쪽으로 6칸보다 작으면 절대 다쓸 수 없다.
#이동횟수가 4번이상이 된다면 모두 한번씩 사용해야한다.
#col, row에 합을 더하면서 경꼐값기준으로 계속 반복한다.
n,m=map(int,input().split())
cnt=0
# steps = [(2,1),(1,2),(-1,2),(-2,1)] 필요없다...
if n>=3 and m>=7:#가장 최소한 모든 방법을 사용하여 움직일 수 있는 최소한의 칸수 즉 기본으로 4회가 있다
    cnt = 1+4+m-7#가로로 커질때마다 1씩 움직일 수있는곳이 생긴다 

elif n<3 or m<7:
    if n>=3:
        if m >= 4:
            cnt = 4
        else:
            cnt = m

    elif n==2:
        if m >= 7:
            cnt = 1+3
        elif m<7 and m>=5:
            cnt = 1+2
        elif m < 5 and m >=3:
            cnt = 1+1
        else:
            cnt = 1

    elif n == 1:
        cnt =1
print(cnt)
    
# n, m = map(int, input().split())
# if n == 1:
#     print(1)
# elif n == 2:
#     print(min(4, (m + 1) // 2)) n==2일때 위로 한칸,밑으로 한칸가는 두 방법밖에 없으므로 4가 최대이므로 그중 작은값을 출력
# else:
#     if m <= 6:
#         print(min(4, m)) n>=3일때부터는 m<=6일때까지는 4가 최대이므로 m,4의 최소를 출력
#     else:
#         print(m - 2) 1+4+m-7 == m-2