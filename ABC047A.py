import sys
f = open("input.txt", "r")
sys.stdin = f

s = list(map(int, input().split()))
s.sort()

if s[0] + s[1] == s[2]:
    print("Yes")
else:
    print("No")