while(1):
    a, b, c = map(int,input().split());
    if (a == 0 or b == 0 or c == 0):
        break;
    aa = a;
    bb = b;
    cc = c;
    a = min(aa,bb,cc);
    c = max(aa,bb,cc);
    b = aa + bb + cc - a - c;
    if (a**2 + b **2 == c ** 2):
        print("right");
    else:
        print("wrong");