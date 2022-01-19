def rec(a,b,c,dict):
	if (a <= 0 or b <= 0 or c <= 0):
		return(1);
	elif (a> 20 or b> 20 or c> 20):
		return(rec(20,20,20,dict));
	abc = 1000000 + a * 10000 + b * 100 + c;
	rtn = 0;
	if abc in dict:
		rtn = dict[abc];
	else:
		if (a<b and b< c):
			rtn = rec(a, b, c-1, dict) + rec(a, b-1, c-1, dict) -rec(a, b-1, c, dict);
		else:
			rtn = rec(a-1, b, c, dict) + rec(a-1, b-1, c, dict) + rec(a-1, b, c-1, dict) - rec(a-1, b-1, c-1, dict);
		dict[abc] = rtn;
	return(rtn);

dict = {}

dict[1000000] = 1;

prt = [];

while(1):
	a, b, c = map(int, input().split());
	if (a == -1 and b == -1 and c == -1):
		break;
	prt.append("w(" + str(a) + ", " + str(b) + ", " + str(c)+") = " + str(rec(a,b,c,dict)));

for i in range(0, len(prt)):
	print(prt[i]);
