import sys
f = open("input.txt", "r")
sys.stdin = f


n = int(input())
x = list(map(int, input().split()))

print(x)
ans = 0

for i in range(max(x)):
    a = 0
    for j in range(n):
        a += (x[j]-i-1)**2
    if i == 0:
        ans += a
    else:
        ans = min(a, ans)

print(ans)
