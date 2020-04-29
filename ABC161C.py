import sys
f = open("input.txt", "r")
sys.stdin = f

n, k = map(int, input().split())
n = n%k

while abs(n-k)<=n:
    n = abs(n-k)

print(n)