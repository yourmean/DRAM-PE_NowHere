# https://sujeng97.tistory.com/42
# dist 내림차순 정렬 후 모든 취약점 검사 - 시간효율 Good

def solution(n, weak, dist):
    l = len(weak)
    weak_line = weak + [w + n for w in weak]
    dist.sort(reverse=True)
    repaired_list = [()]
    cnt = 0

    for d in dist:
        repairs = []
        cnt += 1

        for i in range(l):
            start = weak[i]
            repairs.append(set([w % n for w in weak_line[i:i + l] if start + d >= w]))

        can = set()
        for r in repairs:
            for x in repaired_list:
                new = r | set(x)
                if len(new) == l:
                    return cnt
                can.add(tuple(new))
        repaired_list = can
    return -1
