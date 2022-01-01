import math


# 검증수 : 각각 5개의 숫자의 제곱의 합 %10
nums = list(map(int, input().split()))
result = 0


# # 첫번째 방법 (인덱스로 접근) range()
# for i in range(len(nums)):
#     result += math.pow(nums[i], 2)

# 두번째 방법 for in
for i in nums:
    result += math.pow(i, 2)

result = (result % 10)

print(int(result))
