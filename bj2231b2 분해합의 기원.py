#분해합의 근본 구하기
#문제의 취지와는 맞지 않음

def next(n):
    sum = n;
    while (n >= 1):
        sum += n % 10;
        n /= 10;
        n = int(n);
    return (sum);

def newStart(arr, i):
    while (arr[i] == 1):
        i += 1;
    return (i);

n = int(input());

arr = [0] * 1000001;
i = 1;
temp = 0;
while (1):
    i = newStart(arr, i);
    temp = i;
    while (temp <= n):
        arr[temp] = 1;
        temp = next(temp);
        if (temp == n):
            print(i);
            quit();
