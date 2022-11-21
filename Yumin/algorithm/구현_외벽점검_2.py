# https://sujeng97.tistory.com/42
# 완전탐색 - 순열

from itertools import permutations
from bisect import bisect_right

def solution(n, weak, dist):
    l = len(weak)
    weak_line = weak + [w+n for w in weak]
    answer = []
    for friends in permutations(dist):
        for i in range(l):
            cnt = 0
            position = weak[i]
            for friend in friends:
                cnt += 1
                position += friend
                if position < weak_line[i+l-1]:
                    position = weak_line[bisect_right(weak_line,position)]
                else:
                    answer.append(cnt)
                    break
                    
    return min(answer) if answer else -1
