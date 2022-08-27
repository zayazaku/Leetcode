class Solution(object):
    def twoSum(self, nums, target):
        visited = {}
        for index, num in enumerate(nums):
            tmp = target - num
            if tmp in visited:
                return [visited[tmp], index]
            visited[num] = index
        return []
        