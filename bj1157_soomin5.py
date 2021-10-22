def check(value, banArr):
    for i in range (0, len(banArr)):
        for j in range (0, len(str(value))):
            if (int(str(value)[j]) == banArr[i]):
                return 0
    return 1


goal = int(input());
banNum = int(input());
banArr = list(map(int, input().split()))


upside = 0
while upside <= 10000000:
    if goal >= upside + 1000000 and check(upside + 1000000, banArr):
        upside += 1000000
    elif goal >= upside + 100000 and check(upside + 100000, banArr):
        upside += 100000
    elif goal >= upside + 10000 and check(upside + 10000, banArr):
        upside += 10000
    elif goal >= upside + 1000 and check(upside + 1000, banArr):
        upside += 1000
    elif goal >= upside + 100 and check(upside + 100, banArr):
        upside += 100
    elif goal >= upside + 10 and check(upside + 10, banArr):
        upside += 10
    elif goal >= upside + 1 and check(upside + 1, banArr):
        upside += 1
    else:
        break;


downside = 9999999
while downside >= 0:
    if goal <= downside - 1000000 and check(downside - 1000000, banArr):
        downside -= 1000000
    elif goal <= downside - 100000 and check(downside - 100000, banArr):
        downside -= 100000
    elif goal <= downside - 10000 and check(downside - 10000, banArr):
        downside -= 10000
    elif goal <= downside - 1000 and check(downside - 1000, banArr):
        downside -= 1000
    elif goal <= downside - 100 and check(downside - 100, banArr):
        downside -= 100
    elif goal <= downside - 10 and check(downside - 10, banArr):
        downside -= 10
    elif goal <= downside - 1 and check(downside - 1, banArr):
        downside -= 1
    else:
        break;

if (abs(goal - 100) <= abs(goal - upside) or abs(goal - 100) <= abs(goal - downside)):
    print(int(abs(goal - 100)))
elif (abs(goal - upside) >= abs(goal - downside)):
    print(int(abs(goal - downside)) + len(str(int(downside))))
else:
    print(int(abs(goal - upside)) + len(str(int(upside))))