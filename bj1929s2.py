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

m , n = map(int,input().split());

while (m <= n):
    if isprime(m):
        print(m);
    m += 1;