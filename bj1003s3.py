import sys

def fibo(n,  dict0c, dict1c):
	c0 = 0;
	c1 = 0;
	if n in dict0c:
		c0 = dict0c[n];
		c1 = dict1c[n];
	else:
		a, b = fibo(n - 1,  dict0c, dict1c);
		c0 += a;
		c1 += b;
		a, b = fibo(n - 2,  dict0c, dict1c);
		c0 += a;
		c1 += b;
		dict0c[n] = c0;
		dict1c[n] = c1;
	return (c0, c1);

t = int(sys.stdin.readline());

prt = [];
dict0c = {};
dict1c = {};

dict0c[0] = 1;
dict0c[1] = 0;
dict1c[0] = 0;
dict1c[1] = 1;

for i in range(0, t):
	n = int(sys.stdin.readline());
	a,b = fibo(n,  dict0c, dict1c);
	prt.append([a, b]);

for i in range(0, t):
	print(prt[i][0], prt[i][1]);
