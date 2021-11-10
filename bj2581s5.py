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

m = int(input());
n = int(input());

minprime = - 1;
sumprime = 0;

while (m <= n):
    if isprime(m):
        if minprime == -1:
            minprime = m;
        sumprime += m;
    m += 1;

if minprime == -1:
    print(-1);
else:
    print(sumprime);
    print(minprime);