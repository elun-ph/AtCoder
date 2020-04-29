import sys
f = open("input.txt", "r")
sys.stdin = f

s = list(input())
n = len(s)

for i in range(2**(n-1)):
    ans = int(s[0])
    formura = s[0]
    for j in range(1,n):
        if (i >> j-1) & 1 == 1:
            ans += int(s[j])
            formura += "+" + s[j]
        else:
            ans -= int(s[j])
            formura += "-" + s[j]
    if ans == 7:
        print(formura + "=7")
        break