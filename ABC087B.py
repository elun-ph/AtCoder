import sys
f = open("input.txt", "r")
sys.stdin = f

a = int(input())
b = int(input())
c = int(input())
x = int(input())
cnt = 0

for i in range(c+1):
    for j in range(b+1):
        if (x-50*i-100*j)%500==0 and ((x-50*i-100*j)/500)<=a and ((x-50*i-100*j)/500)>=0:
            cnt += 1

print(cnt)
