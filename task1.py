n = int(input())
nums = list(map(float, input().split()))

tmp = 0
set_ = set()
flag = True

while nums[tmp] != -1:
    if nums[tmp] in set_:
        flag = False
        break
    set_.add(nums[tmp])
    tmp = nums[tmp] - 1
print("Yes") if flag else print('No')
