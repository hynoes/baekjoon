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

i = 1;
prime = [];
while (i <= 10000):
    if isprime(i):
        prime.append(i);
    i+= 1;

t = int(input());
case = [];
for i in range(0,t):
    case.append(int(input()));
    
for i in range(0,t):
    minprime = 0;
    maxprime = 10000;
    for j in range(0,len(prime)):
        if (case[i]/2 < prime[j]):
            break;
        for k in range(j,len(prime)):
            if (prime[j] + prime[k] == case[i] and prime[k] - prime[j] < maxprime - minprime):
                minprime = prime[j];
                maxprime = prime[k];
    print(minprime,maxprime);