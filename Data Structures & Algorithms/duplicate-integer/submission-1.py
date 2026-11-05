class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        input_dict = {}
        for i in nums:
            if i in input_dict:
                return True
            else:
                input_dict[i] = True
        return False
        