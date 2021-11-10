# map함수의 결과값을 list로 바꿔서 저장하기
# 에라스토테네스의 체

def isprime(n):
    if (n < 2):
        return (0);
    root = n ** 0.5;
    index = 2;
    while (root >= index):
        if (n % index == 0):
            return (0);
        index += 1;
    return (1);
    

n = int(input());
arr = list(map(int,input().split()));

rtn = 0;
for i in range(0,n):
    rtn += isprime(arr[i]);
print(rtn);
        