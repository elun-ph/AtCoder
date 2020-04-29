import sys
f = open("input.txt", "r")
sys.stdin = f

n, k = map(int, input().split())

cnt = 0
print()
for i in range(k,n+2):
    cnt += i*(n-i+1)+1

print(cnt%(10**9+7))