n = int(input());
A = list();
B = list();
for i in range(0, n):
    a, b = map(int, input().split());
    A.append(a);
    B.append(b);
    
for i in range(0, n):
	tier = 0;
	for j in range(0, n):
		if(A[i] < A[j] and B[i] < B[j]):
			tier += 1;
	print(tier + 1);
   
        
    