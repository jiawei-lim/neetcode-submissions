class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = {}
        for i in strs:
            key = self.hashAnagrams(i)
            if key in result_dict:
                result_dict[key] += [i]
            else:
                result_dict[key] = [i]
        return list(result_dict.values())

    def hashAnagrams(self,input_str):
        char_array = [0]*26
        for i in input_str:
            char_array[ord(i) - 97] += 1
        return hash(tuple(char_array))