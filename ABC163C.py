import sys
f = open("input.txt", "r")
sys.stdin = f

n = int(input())
A = list(map(int, input().split()))

B = [0] * n
for i in range(n-1):
    B[A[i]-1] += 1

for i in range(n):
    print(B[i])
