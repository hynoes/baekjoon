# 점화식을 for문으로 계산하기 (간단, 손도깔끔)

import sys

def rec(n, dict):
	if n in dict:
		return(dict[n])
	rtn = rec(n-1,dict) + rec(n-5, dict)
	return (rtn)

t = int(sys.stdin.readline())

dict = {}

dict[1] = 1
dict[2] = 1
dict[3] = 1
dict[4] = 2
dict[5] = 2
dict[6] = 3
dict[7] = 4
dict[8] = 5
dict[9] = 7
dict[10] = 9

narr = []
for i in range(0,t):
	narr.append(int(sys.stdin.readline()))

for i in range(11, max(narr) + 1):
	dict[i] = dict[i - 1] + dict[i - 5]

for i in range(0,t):
	print(rec(narr[i],dict))