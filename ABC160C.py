import sys
f = open("input.txt", "r")
sys.stdin = f

k, n = map(int, input().split())
A = list(map(int, input().split()))

D = [0] * n
for i in range(len(A)-1):
    D[i] += A[i+1]-A[i]
D[n-1] += A[0] + k - A[n-1]

D.remove(max(D))
print(sum(D))