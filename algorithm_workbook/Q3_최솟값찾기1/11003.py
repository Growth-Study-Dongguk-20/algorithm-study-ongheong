import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())
mydeque = deque()
now = list(map(int, input().split()))

for i in range(N):
    # 아이디어1. 나보다 큰 데이터 삭제하기
    while mydeque and mydeque[-1][0] > now[i]: #제일 끝에 있는 값이 현재 값보다 크면
        mydeque.pop()
    mydeque.append((now[i], i)) #값, 인덱스
    # 아이디어2. 슬라이딩 윈도우 크기를 벗어난 데이터 삭제하기
    if mydeque[0][1] <= i-L: #윈도우 범위를 벗어나면
        mydeque.popleft()
    print(mydeque[0][0], end=' ')