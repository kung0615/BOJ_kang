n = int(input())
tree = list(map(int,input().split()))
time = 1#처음 나무를 심을때 드는 시간
tree.sort(reverse=True)
for i in range(len(tree)):#나무를 심을때마다 먼저 심은 나무가 자라는 남은시간
        tree[i] -= len(tree)-i-1

time += len(tree)+max(tree)#첫번째나무를 심고 나머지 나무를 심는 시간과 아직 가장 많이 남은 나무의기간을 더한다.
print(time)