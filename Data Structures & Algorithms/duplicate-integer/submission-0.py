class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        input_set = set(nums)
        return len(input_set) != len(nums)
        