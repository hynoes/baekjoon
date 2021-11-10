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
prime = 2;

while (n > 1):
    if n % prime == 0:
        print(prime);
        n /= prime;
    elif isprime(n):
        print(int(n));
        break;
    else:
        prime += 1;
        while (isprime(prime) == 0):
            prime += 1;