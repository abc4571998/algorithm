n = int(input())
coins = []
coins.extend(list(map(int, input().split())))

# 1번부터 줍는경우부터 n번부터 줍는 번호를 확인
# 누적합 배열을 통해 max 일때를 반환
max_value = 0
answer = [coins[0]]
for i in range(1, n):
	sum_coin = answer[i-1] + coins[i]
	answer.append(max(sum_coin, coins[i]))

print(max(answer))