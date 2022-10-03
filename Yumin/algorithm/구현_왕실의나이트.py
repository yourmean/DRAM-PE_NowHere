'''
8*8 체스판, 가로 a-h, 세로 1-8
나이트는 1)수평2+수직1 or 2)수직2+수평1 의 형태로만 이동가능
현재 위치가 a1, c2와 같은 형식으로 주어질 때, 나이트가 이동할 수 있는 경우의 수
'''

def solution():
    temp = input()
    x = int(temp[1])
    y = ord(temp[0]) - 96  #아스키코드 기준 -96으로 숫자 변환
    # y = int(ord(intput_data[0])) - int(ord('a')) + 1

    #나이트의 이동경로 (8경우)
    x1 = [2, 2, 1, 1, -2, -2, -1, -1]
    y1 = [1, -1, 2, -2, -1, 1, -2, 2]

    answer = 0
    for i in range(8):
        dx = x + x1[i]
        dy = y + y1[i]
        if dx > 0 and dy > 0 and dx < 9 and dy < 9: #이동 후 나이트가 체스판 안이면
            answer += 1
    return answer

solution()