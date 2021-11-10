def findArithmetic(num):
    rtn = 1;
    while (num >= rtn ** 2):
        rtn += 1;
    return (rtn - 1);

caseNum = int(input())
case = [0] * caseNum;
rtn = [0] * caseNum;

for i in range(0, caseNum):
    A, B = input().split()
    case[i] = int(B) - int(A);
    arith = findArithmetic(case[i]);
    extra = 0;
    tempsum = arith ** 2;
    rtn[i] = arith * 2 - 1;
    while (arith):
        while (case[i] >= tempsum + arith):
            tempsum += arith;
            extra += 1;
        arith -= 1;
        if (case[i] == tempsum):
            break;
    rtn[i] += extra;

for i in range(0, caseNum):
    print(rtn[i]);
            
    





