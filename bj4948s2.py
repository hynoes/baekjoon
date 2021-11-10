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

    
n = -1;
rtn = [];
while (1):
    n = int(input());
    if n == 0:
        break;
    
    m = 2*n;
    n += 1;
    sumprime = 0;
    while (m >= n):
        if isprime(n):
            sumprime += 1;
        n += 1;
    rtn.append(sumprime);
    
for i in range (0, len(rtn)):
    print(rtn[i]);