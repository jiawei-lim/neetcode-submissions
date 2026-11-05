class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        freq_bucket = [0]*(len(nums) + 1)
        result = []

        for i in nums:
            if i in freq_map:
                freq_map[i] += 1
            else:
                freq_map[i] = 1
        
        for _, (key,v) in enumerate(freq_map.items()):
            if freq_bucket[v] == 0:
                freq_bucket[v] = [key] 
            else:
                freq_bucket[v] += [key] 

        for i in range(len(nums),-1,-1):
            if freq_bucket[i] != 0:
                result += freq_bucket[i]
            if len(result) >= k:
                break 
                
        return result
