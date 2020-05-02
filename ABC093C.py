import sys
f = open("input.txt", "r")
sys.stdin = f

a, b, c = map(int, input().split())

diff = max(a,b,c)*3-a-b-c
if diff%2==0:
    print(diff//2)
else:
    print(diff//2+2)