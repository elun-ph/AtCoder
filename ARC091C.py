import sys
f = open("input.txt", "r")
sys.stdin = f

n, m = map(int, input().split())

if n > 1 and m > 1:
    print((n-2)*(m-2))
elif max(n,m) > 2:
    print(max(n,m)-2)
elif max(n,m) == 2:
    print(0)
else:
    print(1)
