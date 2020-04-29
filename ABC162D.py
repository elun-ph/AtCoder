import sys
f = open("input.txt", "r")
sys.stdin = f

n = int(input())
s = list(input())

max_interval = (n-3)//2+1

exception = 0

for interval in range(1,max_interval+1):
    for i in range(n-interval*2):
        if s[i]!=s[i+interval] and s[i+interval]!=s[i+2*interval] and s[i+2*interval]!=s[i]:
            exception += 1

allc = s.count("R")*s.count("G")*s.count("B")

print(allc-exception)
