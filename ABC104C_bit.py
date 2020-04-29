import sys
f = open("input.txt", "r")
sys.stdin = f

d, g = map(int, input().split())

P = [0] * d
C = [0] * d
num = 0
for i in range(d):
    a, b = map(int, input().split())
    P[i] += a
    C[i] += b
    num += a

print(P, C)

for i in range(1, num+1):#i問解く
    score = [0] * d
    for i in range(d):
        if i == P[i-1]:
            score[i-1] += 100*i*P[i-1] + C[i-1]
        else:
            score[i-1] += 100*i*P[i-1]
    if max(score) > g:
        print(i)
        break
    else:
        print("no")
