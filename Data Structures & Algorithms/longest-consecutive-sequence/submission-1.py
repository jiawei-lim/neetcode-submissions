class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        number_set = set(nums)
        result = 0

        for i in number_set:
            counter = 1
            next_val = i + 1 
            if (i-1) in number_set:
                continue
            while next_val in number_set:
                counter += 1
                next_val += 1
            if counter > result:
                result = counter

        return result
