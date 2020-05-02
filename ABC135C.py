import sys
f = open("input.txt", "r")
sys.stdin = f

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

monsall = 0
monsnext = a[0]

for i in range(n):
    if monsnext >= b[i]:
        monsall += b[i]
        monsnext = a[i+1]
    else:
        if a[i+1] > b[i] - monsnext:
            monsall += b[i]
            monsnext = a[i+1] - b[i] + monsnext
        else:
            monsall += a[i+1] + monsnext
            monsnext = 0

print(monsall)
