import sys
f = open("input.txt", "r")
sys.stdin = f

n, y = map(int, input().split())
y //= 1000

cnt = 0

if not(y // 10 <= n <= y):
    print(-1, -1, -1)
else:
    for i in range(y+2):
        for j in range(y//5+2):
            if (y-i-5*j)==(n-i-j)*10 and n-i-j>=0:
                print(n-i-j, j, i)
                break
        else:
            continue
        break
    else:
        print(-1, -1, -1)
