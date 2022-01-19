import math

a, b = map(int, input().split())
i = 0
while(1):
    if (math.ceil(i / a) == b):
        print(i)
        break;
    i += 1