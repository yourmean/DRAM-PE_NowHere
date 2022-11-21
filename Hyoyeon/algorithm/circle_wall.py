from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist)+1 #필요한 사람수를 return, 점검이 불가능한 경우를 가정
    weak_l = len(weak)
    
    for i in range(weak_l):
        weak.append(weak[i]+n) #1. 길이를 2배로 늘려서 선형으로 풀이 가능 #[1, 5, 6, 10, 13, 17, 18, 22]

    dist_comb = list(map(list,permutations(dist,len(dist)))) #[[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], ... #갈수있는 거리 순서 경우의 수
    
    
    for i in range(weak_l):
        start = [weak[j] for j in range(i, i+weak_l)] #시작점 하나씩 바꾸기  
          #[1, 5, 6, 10],[5, 6, 10, 13],[6, 10, 13, 17],[10, 13, 17, 18]

        for dist_p in dist_comb:
            result = 1 # 활용 친구 수
            dist_distance = 0
            check_len = start[0] + dist_p[0]   #첫번째 시작 장소에서 1칸 dist하면 2로 움직인다
        
            for k in range(weak_l):
                if start[k] > check_len: #가야하는 거리가 확인 가능한 최대 거리보다 먼 경우
                    result += 1

                    if result > len(dist_p):
                        break
                    dist_distance += 1 #다음 친구를 투입

                    check_len = start[k] + dist_p[dist_distance] #다음 친구가 확인할 수 있는 거리
                #print(result)
            answer = min(answer, result)
    
    
    
    
    if answer > len(dist):
        return -1
    
    
    return answer
