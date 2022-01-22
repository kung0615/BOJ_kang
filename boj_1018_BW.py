N, M = map(int, input().split())
board = list()

for i in range(N):#입력 코드
    board.append(input())
repair = list()

for i in range(N-7):#총 행렬을 8*8롤자르기 위해서 i-7,j-7만큼 고정후
    for j in range(M-7):
        first_W = 0#첫번째가 w시작인지 b시작인지를 기준으로
        first_B = 0
        for k in range(i,i+8):#8칸씩으로 나눈것에 
            for l in range(j,j + 8):
                if (k + l) % 2 == 0:#행,열의 인덱스의 합이 짝인경우 일정한 색을 가지고 홀인경우 다른 일정한 색을 가진다.
                    if board[k][l] != 'W':#합이 짝수이면 시작점과 색깔이 같아야한다
                        first_W = first_W+1
                    if board[k][l] != 'B':
                        first_B = first_B + 1
                else:
                    if board[k][l] != 'B':#합이 홀수이면 시작점과 색깔이 달라야한다.
                        first_W = first_W+1
                    if board[k][l] != 'W':
                        first_B = first_B + 1
        repair.append(first_W)
        repair.append(first_B)
print(min(repair))