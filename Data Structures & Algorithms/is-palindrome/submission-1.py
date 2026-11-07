class Solution:
    def isPalindrome(self, s: str) -> bool:
        modified_string = ""
        for i in s:
            if i.isalnum():
                modified_string += i.lower()
        
        pointer_a = 0
        pointer_b = len(modified_string)-1 

        while pointer_a != pointer_b and pointer_b > pointer_a:
            if modified_string[pointer_a] != modified_string[pointer_b]:
                return False
            pointer_a += 1
            pointer_b -= 1
        
        return True