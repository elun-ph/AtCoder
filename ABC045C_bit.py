import sys
f = open("input.txt", "r")
sys.stdin = f

s = input()
n = len(s)

ans = 0
for i in range(2**(n-1)):
    p = []
    trig = 0
    for j in range(n-1):
        if (i >> j) & 1 == 1:
            p.append(int(s[trig:j+1]))
            trig = j+1
    p.append(int(s[trig:]))
    ans += sum(p)

print(ans)
