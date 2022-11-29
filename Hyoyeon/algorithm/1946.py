import sys

T = int(input())

for _ in range(T):
    N = int(input())
    lst = sorted([list(map(int,sys.stdin.readline().strip().split())) for x in range(N)],
                key = lambda x: x[0])
    result = 1
    top = 0
    
    for i in range(1, N):
        if lst[i][1] < lst[top][1]:
            top = i
            result += 1
    
    print(result)

    
#[서류 성적, 면접 점수] 리스트로 할당한다음, 서류 성적으로 정렬한다.
#서류 성적이 더 높으면 면접 성적은 고려할 필요가 없다.

#i가 선발되려면, 자신보다 서류 성적이 좋은 사람보다 면접 점수가 높아야한다.
#면접 성적중 가장 높은 성적과 비교한다.  
#가장 좋은 성적을 min에 담았기 때문에, i번쨰 지원자의 면접성적이 min 보다만 크면 신입사원으로
#선발될 수 있다.
    
