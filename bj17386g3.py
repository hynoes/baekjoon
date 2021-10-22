# x정방향으로 선분 성분 정렬
# 1차방정식구하기 4번인덱스에 기울기, 5번인덱스에 y절편
# 구간계산하기 (x1 or x2) ~ (x3 or x4)
# 두 방정식의 차의 해의 값이 구간안에 있는지 확인하기

l1 = input().split();
l2 = input().split();
l1 = list(map(int, l1));
l2 = list(map(int, l2));

if l1[0] > l1[2]:
    temp = l1[0];
    l1[0] = l1[2];
    l1[2] = temp;
    temp = l1[1];
    l1[1] = l1[3];
    l1[3] = temp;

if l2[0] > l2[2]:
    temp = l2[0];
    l2[0] = l2[2];
    l2[2] = temp;
    temp = l1[1];
    l1[1] = l1[3];
    l1[3] = temp;

if (l1[0] - l1[2] != 0):
    l1.append((l1[1] - l1[3])/(l1[0] - l1[2]))
    l1.append(l1[1]-l1[0]*l1[4]);
    l1.append(0);
else:
    l1.extend([0, 0, 1]);


if (l2[0] - l2[2] != 0):
    l2.append((l2[1] - l2[3])/(l2[0] - l2[2]))
    l2.append(l2[1]-l2[0]*l2[4]);
    l2.append(0);
else:
    l2.extend([0, 0, 1]);   

if (l1[4] == l2[4] or (l1[6]*l2[6] == 1)):
    print(0);
    quit();
ans = -(l1[5] - l2[5])/(l1[4] - l2[4]);
if (l1[0] <= ans and ans <= l1[2] and l2[0] <= ans and ans <= l2[2]):
    print(1);
