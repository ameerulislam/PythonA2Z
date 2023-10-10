# my solution less than B(O^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first = -inf
        for ix, i in enumerate(nums):
            if first + i == target:
                return [ix-1, ix]
            else:
                for jx, j in enumerate(nums[ix+1:]):
                    if i+j == target:
                        return [ix, ix+jx+1]
            first = i

# Chatgpt like always has a better solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_indices:
                return [num_indices[complement], i]
            num_indices[num] = i
