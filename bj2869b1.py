a, b ,v = input().split();
a = int(a);
b = int(b);
v = int(v);

x = (v - a)/(a - b) + 1;
if x % 1 == 0:
    print(int(x));
else:
    print(int(x+1));