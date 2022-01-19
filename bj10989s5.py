# 계수 정렬 (counting sort) 공부하기
# 세는거까지는 이해가 되는데 왜 역순으로 풀어야 하는지? 그냥 배열을 직접 만들면 안되나????

import sys

N = int(input());

countarr = [0 for i in range(10001)];
for i in range(0, N):
    countarr[int(sys.stdin.readline())] += 1;

for i in range(0, len(countarr)):
    for j in range(0, countarr[i]):
        sys.stdout.write(str(i) + '\n');