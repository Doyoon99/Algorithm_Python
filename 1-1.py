# 이코테 구현 예제 1번

# N 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

# 이동 계획 확인
for plan in plans:
    # 이동 후에 좌표 구하기
    for i in range(len(move)):
        if plans == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny


print(x, y)