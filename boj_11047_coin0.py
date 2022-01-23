#coin n종류,각각 종류의 동전 개수 제한없다,그 가치의 합k,동전 개수의 최솟값을 구하자
#동전가치가 ai=a(i-1) * x
#배수는 구할 필요없을거 같다
#주어진 k값을 가장 큰 가치부터 나눌때 몫이 존재할때까지 반복후
#몫이 처음 존재할때 그때 그값으로 최대한 나누후 나머지를 또 다시 같은 방식으로 나눈다
#그때 몫을 최솟값에 계속 더하면 구할 값이 나온다

n,k=map(int,input().split())
a=[]
cnt =0
for i in range(n):
    coin=int(input())
    a.append(coin)
a.sort(reverse=True)

for i in range(n):
    if k//a[i] > 0:
        cnt += k//a[i]
        k = k%a[i] 
print(cnt)