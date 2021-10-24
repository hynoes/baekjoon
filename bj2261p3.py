# 입력받은 좌표를 클래스로 저장하고 
# x축으로 정렬한 배열 y축으로 정렬한 배열을 하나씩 만들기
# (sorted, key, **를 배웠다)
# 각각한번검색해서 x최소거리, y최소거리를 찾고
# 해당최소거리의 y거리, x거리를 구하고 그중 작은것을 기준으로 함
# 다시 그보다 작은 x,y거리를 모두 탐색후, 일괄 x^2+y^2 계산, 최소값 탐색

#문제점1
# mini가 0이 될 수 있는데 그러면 사실상 거의 모든 길이를 탐색해야함 (아마 시간초과가 걸릴듯)

import copy

class point:
    def __init__(self, coor):
        self.x = int(coor[0]);
        self.y = int(coor[1]);

n = int(input());
po = [point([0, 0])] * n;
for i in range(0,n):
    po[i] = point(input().split());


poX = sorted(po,key=lambda point: point.x);
poY = sorted(po,key=lambda point: point.y);


"""

xmin = poX[1].x - poX[0].x;
xindex = 0;
for i in range(1, n - 1):
    if (poX[i + 1].x - poX[i].x < xmin):
        xmin = poX[i + 1].x - poX[i].x;
        xindex = i;

ymin = poY[1].y - poY[0].y;
yindex = 0;
for i in range(1, n - 1):
    if (poY[i + 1].y - poY[i].y < ymin):
        ymin = poY[i + 1].y - poY[i].y;
        index = i;      

mini = min(xmin,ymin);

"""


rtn = (poX[1].x - poX[0].x) ** 2 + (poX[1].y - poX[0].y) ** 2;
for i in range(0, n - 1):
    ans = (poX[i + 1].x - poX[i].x) ** 2 + (poX[i + 1].y - poX[i].y) ** 2;
    if ans < rtn:
        rtn = ans;

for i in range(0, n - 1):
    ans = (poY[i + 1].x - poY[i].x) ** 2 + (poY[i + 1].y - poY[i].y) ** 2;
    if ans < rtn:
        rtn = ans;
        
print(rtn);
