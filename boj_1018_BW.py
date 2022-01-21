import sys
input = sys.stdin.readline
row,col = map(int,input().split())

ChessBoard = list()
cnt = 0
for i in range(row):
    a=input()
    ChessBoard.append(list(a))#문자열은 변경불가이므로 리스트로 바꿔서 넣어줘야 변경 가능하다.


if ChessBoard[0][0] =='B':
    for j in range(row-1):
        if  ChessBoard[j][0] == ChessBoard[j+1][0]:
            ChessBoard[j+1][0]='W'
            cnt+=1

    for j in range(row):    
        for k in range(col-1):
            if ChessBoard[j][k] == ChessBoard[j][k+1]:
                    if ChessBoard[j][k] =='B':
                        ChessBoard[j][k+1] = 'W'
                        cnt+=1
                    else:
                        ChessBoard[j][k+1] ='B'
                        cnt+=1
else:
    for j in range(row-1):
        if  ChessBoard[j][0] == ChessBoard[j+1][0]:
            ChessBoard[j+1][0]='B'
            cnt+=1

    for j in range(row):    
        for k in range(col-1):
            if ChessBoard[j][k] == ChessBoard[j][k+1]:
                    if ChessBoard[j][k] =='B':
                        ChessBoard[j][k+1] = 'W'
                        cnt+=1
                    else:
                        ChessBoard[j][k+1] ='B'
                        cnt+=1

print(cnt)
