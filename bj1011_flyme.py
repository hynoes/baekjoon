caseNum = int(input())
case = [caseNum]

for i in range(0, caseNum - 1):
    A, B = input().split()
    case[i] = int(B) - int(A)




