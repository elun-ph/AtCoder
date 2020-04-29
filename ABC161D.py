import sys
f = open("input.txt", "r")
sys.stdin = f

from collections import deque
k = int(input())

lunlun = deque([1,2,3,4,5,6,7,8,9])

p = 0

def generate_lunlun(p):
    last = p%10
    if last-1>=0:
        yield p*10+last-1
    yield p*10+last
    if last < 9:
        yield p*10+last+1

cnt = 1

while cnt < k:
    for i in generate_lunlun(lunlun.popleft()):
        lunlun.append(i)
    cnt += 1

print(lunlun[0])
