# 시간 초과 문제 발생 --> deepcopy는 신중히 사용할 것
# break와 continue를 잘못 사용해서 시간이 오래 걸린 문제 --> 주의 필요


# book sol
# 현재 설치된 구조물이 '가능한' 구조물인지 확인하는 함수
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:  # 설치된 것이 '기둥'인 경우
            # '바닥 위' 혹은 '보의 한쪽 끝부분 위' 혹은 '다른 기둥 위'라면 정상
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1]


def solution(n, build_frame):
    answer = []
    for frame in build_frame:   # 작업(frame)의 개수는 최대 1,000개
        x, y, stuff, operate = frame
        if operate == 0:    # 삭제하는 경우
            answer.remove([x, y, stuff])    # 일단 삭제를 해본 뒤에
            if not possible(answer):    # 가능한 구조물인지 확인
                answer.append([x, y, stuff])    # 가능한 구조물이 아니라면 다시 설치
        if operate == 1:    # 설치하는 경우
            answer.append([x, y, stuff])    # 일단 설치를 해본 뒤에
            if not possible(answer):    # 가능한 구조물인지 확인
                answer.remove([x, y, stuff])    # 가능한 구조물이 아니라면 다시 제거
    return sorted(answer)   # 정렬된 결과를 반환





# my sol
import copy

# 기둥 설치 확인
def check_vertical(x, y, matrix):
    if y == 0:  # 바닥인지
        return True
    for x_, y_, a_ in matrix:
        if a_ == 0:  # 기존 데이터 중 하나가 기둥이라면
            if x_ == x and y_ + 1 == y: # 다른 기둥 위에 있다면
                return True
        elif a_ == 1:    # 기존 데이터 중 하나가 보라면
            if (x_ == x and y_ == y) or (x_ + 1 == x and y_ == y):   # 보의 한쪽 끝부분 위에 있다면
                return True
    return False

# 보 설치 확인
def check_horizontal(x, y, matrix):
    left_check, right_check = False, False
    for x_, y_, a_ in matrix:
        if a_ == 0: # 기존 데이터 중 하나가 기둥이라면
            if (x_ == x and y_ + 1 == y) or (x_ == x + 1 and y_ + 1 == y):  # 한쪽 끝부분이 기둥 위에 있다면
                return True
        elif a_ == 1: # 기존 데이터 중 하나가 보라면
            if x_ - 1 == x and y_ == y: # 왼쪽 끝부분이 다른 보와 연결되어 있으면
                left_check = True
            elif x_ + 1 == x and y_ == y:  # 오른쪽 끝부분이 다른 보와 연결되어 있으면
                right_check = True
        if left_check and right_check:  # 양쪽 끝부분이 다른 보와 연결되어 있으면
            return True
    return False

def solution(n, build_frame):
    result = []
    for x, y, a, b in build_frame:
        if b == 1:  # 설치
            if a == 0:  # 기둥
                if check_vertical(x, y, result): # 설치 조건에 만족한다면
                    result.append([x, y, a])
            elif a == 1:  # 보
                if check_horizontal(x, y, result):    # 설치 조건에 만족한다면
                    result.append([x, y, a])
        elif b == 0:  # 삭제
            result.remove([x, y, a])   # 삭제 가정
            available = True
            for x_, y_, a_ in result:
                if a_ == 0: # 기둥
                    if not check_vertical(x_, y_, result):   # 제거 조건에 만족하지 않으면
                        available = False
                elif a_ == 1: # 보
                    if not check_horizontal(x_, y_, result): # 제거 조건에 만족하지 않으면
                        available = False
            if available == False:  # 제거 조건에 만족하지 않은 것을 확인하면
                result.append([x, y, a])
                continue

    # 정렬 작업
    # result.sort(key = lambda x: (x[0], x[1], x[2]))
    result = sorted(result, key= lambda x: (x[0], x[1], x[2]))

    return result

# test 1
# print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))

# test 2
# print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))