class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_dict = {}

        for i in range(len(nums)):
            number_dict[nums[i]] = i
        
        for i in range(len(nums)):
            current_number = nums[i]
            number_needed = (target-current_number)

            if number_needed in number_dict and number_dict[(target-current_number)] != i:
                return [i,number_dict[(target-current_number)]]