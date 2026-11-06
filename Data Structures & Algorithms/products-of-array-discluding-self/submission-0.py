class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [1]
        suffix_product = deque([1])
        result = []
        
        # calculate prefix array
        for i in range(len(nums)-1):
            prefix_product += [nums[i] * prefix_product[i]]
        
        #calculate suffix array
        for i in range(len(nums)-1,0,-1):
            suffix_product.appendleft(suffix_product[0] * nums[i])
        
        for i in range(len(nums)):
            result += [prefix_product[i] * suffix_product[i]]

        return result
        

