# 합의 나머지는 각각의 나머지와 같다?
# 간단한 동적계획법에서 재귀의 깊이를 줄이는 방법

def rec(n, dict):
	if n in dict:
		return(dict[n]);
	rtn = (rec(n-1,dict) % 15746 + rec(n-2, dict) % 15746) % 15746;
	dict[n] = rtn;
	return (rtn);


dict = {}
dict[1] = 1;
dict[2] = 2;

n = int(input())

for i in range(1, n -1):
	rec(i, dict)

print(rec( n, dict))