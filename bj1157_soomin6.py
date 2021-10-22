def check(value, banArr, depth):
    for i in range (0, len(banArr)):
        for j in range (0, depth):
            if (value[j] == banArr[i]):
                return 1
    return 0


def btrkUp(value, banArr, depth, goal):
    if (len(str(goal)) == depth):
        upside = value

    for i in range (0, 9):
        value[depth] = str(int(value[depth]) + 1)
        if (int("".join(value)) > goal or check(value, banArr, depth)):
            continue
        btrkUp(value, banArr, depth + 1, goal)

def btrkDn(value, banArr, depth, goal):
    if (len(str(goal)) == depth):
        downside = value
    for i in range (9, 0, -1):
        value[depth] = str(int(value[depth]) - 1)
        if (int("".join(value)) or check(value, banArr, depth)):
            continue
        btrkDn(value, banArr, depth + 1, goal)

        


goal = int(input());
banNum = int(input());
banArr = list(map(int, input().split()))


temp = [0 for i in range(len(str(goal)))]
upside = 0
btrkUp(temp, banArr, 0, goal);


temp = [9 for i in range(len(str(goal)))]
downside = 0
btrkUp(temp, banArr, 0, goal);

if (abs(goal - 100) <= abs(goal - upside) or abs(goal - 100) <= abs(goal - downside)):
    print(int(abs(goal - 100)))
elif (abs(goal - upside) >= abs(goal - downside)):
    print(int(abs(goal - downside)) + len(str(int(downside))))
else:
    print(int(abs(goal - upside)) + len(str(int(upside))))