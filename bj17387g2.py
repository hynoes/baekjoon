# x정방향으로 선분 성분 정렬
# 1차방정식구하기 4번인덱스에 기울기, 5번인덱스에 y절편
# 두개가 모두 점, 하나가 점인경우 예외처리
# 둘다수직 예외처리
# 하나수직 예외처리
# 수직을 제외한 수평 예외처리
# 두 방정식의 차의 해의 값 구하기
# 구간안에 존재하는지 확인하기



class line():
    hor = 0;
    ver = 0;
    x1 = 0;
    y1 = 0;
    x2 = 0;
    y2 = 0;
    k = 0;
    m = 0;
    ver = 0;
    hor = 0;
    dot = 0;



    def setline(self, arr):
        self.x1 = arr[0];
        self.y1 = arr[1];
        self.x2 = arr[2];
        self.y2 = arr[3];

        if (self.x1 > self.x2):
            temp = self.x1;
            self.x1 = self.x2;
            self.x2 = temp;
            temp = self.y1;
            self.y1 = self.y2;
            self.y2 = temp;

        if (self.x1 == self.x2 and self.y1 == self.y2):
            self.dot = 1
        elif (self.x1 == self.x2):
            self.ver = 1;
        elif (self.y1 == self.y2):
            self.hor = 1;
        return;
    
    def getEq(self):
        if (self.dot == 1):
            self.k = self.y1;
        elif (self.ver == 1):
            self.k = self.y1;
        else:
            self.m = (self.y1-self.y2)/(self.x1-self.x2);
            self.k = -self.m*self.x1 + self.y1;

    def sorty(self):
        if(self.y1 > self.y2):
            temp = self.x1;
            self.x1 = self.x2;
            self.x2 = temp;
            temp = self.y1;
            self.y1 = self.y2;
            self.y2 = temp;

def checkRange(a1,a2,ans):
    if a1 <= a2 and a1 <= ans and ans <= a2:
        return(1);
    elif a1 >= a2 and a2 <= ans and ans <= a1:
        return(1);
    return(0);


l1 = input().split();
l2 = input().split();
l1 = list(map(int, l1));
l2 = list(map(int, l2));

l = line();
l.setline(l1);
l.getEq();

r = line();
r.setline(l2);
r.getEq();

# 선분 정렬
if (r.x1 < l.x1):
    temp = l;
    l = r;
    r = temp;

# 점 예외처리
if (r.dot and l.dot): # 점-점
    if (l.x1 == r.x1 and l.x2 == r.x2 and l.y1 == r.y1 and l.y2 == r.y2):
       print(1);
       #print(l.x1, l.y1);
       quit();
    else:
        print(0);
        quit();
if (r.dot ==1):
    temp = l;
    l = r;
    r = temp;
if (l.dot == 1):
    if (r.ver == 1): # 점-수직
        if (l.x1 != r.x1):
            print(0);
            quit();
        elif checkRange(r.y1,r.y2,l.y1):
            print(1);
            #print(l.x1, l.y1);
            quit();
        else:
            print(0);
            quit();
    elif (r.m * l.x1 + r.k == l.y1): #점-일반
        print(1);
        #print(l.x1, l.y1);
        quit();
    else:
        print(0);
        quit();

# 점 제외

#수직 예외처리
if(l.ver and r.ver): # 수직-수직
    if (l.x1 != r.x1):
        print(0);
        quit();
    l.sorty();
    r.sorty();
    if (r.y1 < l.y1):
        temp = l;
        l = r;
        r = temp;
    if l.y2 == r.y1:
        print(1);
        #print(l.x2, l.y2);
        quit();
    elif checkRange(l.y1, l.y2, r.y1):
        print(1);
        quit();
    else:
        print(0);
        quit();
else:               # 수직 - 일반
    if (r.ver ==1):
        temp = l;
        l = r;
        r = temp; 
    if (l.ver == 1):
        l.sorty();
        ans = r.m * l.x1 + r.k;
        if (checkRange(r.x1, r.x2, l.x1) and checkRange(l.y1, l.y2, ans)):
            print(1);
            #print(l.x1, ans);
            quit();
        else :
            print(0);
            quit(0);

# 수직 제외
        


#평행 예외처리
if((l.hor and r.hor) or (l.m == r.m)):
    if l.k != r.k: # 해없음
        print(0);
        quit();
    else:           # 무한해
        if (l.x2 == r.x1): 
            print(1);
            #print(l.x2, l.x2 * l.m + l.k);
            quit();
        elif checkRange(l.x1, l.x2, r.x1):
            print(1);
            quit();
        else:
            print(0);
            quit();

# 수평 제외

#일반 교점
ansX = -(l.k-r.k)/(l.m-r.m);
ans = r.m * ansX + r.k;

if (checkRange(l.x1,l.x2, ansX) and checkRange(r.x1,r.x2, ansX) and checkRange(l.y1,l.y2, ans) and checkRange(r.y1,r.y2, ans)):
    print(1);
    #print(ansX,ans);
    quit();
else:
    print(0);
    quit();
