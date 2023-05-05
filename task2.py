with open('input.txt', 'r') as f:
    nums = list(map(int, f.readline().split()))

n = nums[0]
nums = nums[1:]

max_element_idx, ans = nums.index(max(nums)), int()

tmp_min = nums[max_element_idx]
for left in range(max_element_idx - 1, -1, -1):
    tmp_min = min(tmp_min, nums[left])
    tmp_len = min(nums[max_element_idx], nums[left]) - tmp_min
    ans = max(ans, tmp_len)
tmp_min = nums[max_element_idx]
for right in range(max_element_idx + 1, n):
    tmp_min = min(tmp_min, nums[right])
    tmp_len = min(nums[max_element_idx], nums[right]) - tmp_min
    ans = max(ans, tmp_len)
with open('output.txt', 'w') as f:
    f.write(str(max(ans)))
