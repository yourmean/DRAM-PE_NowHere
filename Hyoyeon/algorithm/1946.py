import sys
imput = sys.stdin.readline

N = int(input())

for _ in range(N):
    n = int(input())
    bank = [list(map(int, input().split())) for _ in range(n)]
    bank_asc = sorted(bank)
    top = 0
    result = 1
    
    for i in range(1, len(bank_asc)):
        if bank_asc[i][1] < bank_asc[top][1]:   #서류 1등의 면접점수는 bank_asc[0][1]=bank_asc[top][1]
            top = i #서류 2등부터 1등보다 면접을 잘본 사람이 나왔을때 합격시키면 된다. 
            result += 1 # 그다음부터는 최근에 합격 처리된 사람보다 면접을 잘봐야 한다. 
    
    print(result)
