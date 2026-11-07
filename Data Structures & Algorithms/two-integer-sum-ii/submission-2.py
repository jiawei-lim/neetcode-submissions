class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer_left = 0
        pointer_right = len(numbers)-1
        
        while pointer_left != pointer_right and pointer_right > pointer_left:
            if numbers[pointer_left] + numbers[pointer_right] == target:
                return [pointer_left+1,pointer_right+1]
            
            if numbers[pointer_left] + numbers[pointer_right] > target:
                pointer_right -= 1
            else:
                pointer_left += 1