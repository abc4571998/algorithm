# 가장 긴 길이를 찾고 똑같이 만드는 데 필요한 휴지양 파악
# 휴지가 남는다면 휴지 개수로 나눈 몫만큼 추가

n, m = map(int, input().split())
tissues = list(map(int, input().split()))

max_tissue = max(tissues)

need_min_tissue = 0

for tissue in tissues:
    need_min_tissue += max_tissue - tissue

if need_min_tissue > m:
    print('No way!')
else: 
    print(max_tissue + (m-need_min_tissue)//n)