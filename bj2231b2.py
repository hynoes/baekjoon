def next(n):
    sum = n;
    while (n >= 1):
        sum += n % 10;
        n /= 10;
        n = int(n);
    return (sum);

n = int(input());

i = n - 200;
while (i <= n):
    i += 1;
    if (next(i) == n):
        print(i);2
        quit();
print(0);
