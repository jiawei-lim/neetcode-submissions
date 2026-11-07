class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        result = []
        for i,v in enumerate(nums):
            if v > 0:
                return result
            
            if i-1 >= 0 and nums[i] == nums[i-1]:
                continue

            pointer_left = i+1
            pointer_right = len(nums) - 1

            target = -v
            while pointer_left < pointer_right:
                v_left = nums[pointer_left]
                v_right = nums[pointer_right]

                if v_left + v_right == target:
                    result += [[v,v_left,v_right]]
                    pointer_left += 1
                    pointer_right -= 1
                    while nums[pointer_left] == nums[pointer_left-1] and pointer_left < pointer_right:
                        pointer_left += 1
                    
                elif v_left + v_right > target:
                    pointer_right -= 1
                else:
                    pointer_left += 1
        
        return result