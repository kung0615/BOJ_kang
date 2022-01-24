#+,-만 존재하는 식에서 ()를 통해서 최소값을 구하라
#식을 문자열로 입력받아 연산자와 숫자를 분류하여 따로 저장
#숫자를 정수형채로 저장 숫자 저장할때 앞에 0제거
#그러면 마이너스도 같이 포함하여 저장해도 될까? 이렇게 하면 괄호를 넣기 힘들다
#더하기들만 먼저 괄호를 친다..즉 먼저 계산 한다...나중에 그 합앞에 -가 있으면 가장 작은 값이 나올 것이다..
#즉 -가 중요한 역할을 한다..
#-앞의 숫자를 구분 먼저 하여 다 더하는것이 좋을 듯 하다..
#-를 기준으로 그합끼리 빼면 최솟값이 나올 것이다..숫자와 연산자들을 이동할 수 없으니 ()만 신경쓴다 즉 무엇을 먼저 계산할 지가 중요하다.

from random import randrange
from sqlite3 import IntegrityError


sic = input()
interger=list()
interger = sic.split("-")#+끼리 합이 먼저 이뤄지는 짝끼리 나누어 진다...이를 계산하고 -를 나중에 해주면 되는디... 

for i in range(len(interger)):
    if "+" in interger[i]:#안에 +를 모두 합으로 정수형으로 바꾸어 저장한다.
        sum = 0
        s=str(interger[i])
        s=s.split("+")
        for j in range(len(s)):
            sum+=int(s[j].lstrip('0'))  
        interger[i]=sum

    else:
        interger[i]=int(interger[i].lstrip('0'))
result = interger[0]

for i in range(1,len(interger)):
    result -=interger[i]
print(result)








