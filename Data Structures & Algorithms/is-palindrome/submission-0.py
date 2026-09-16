class Solution:
    def isPalindrome(self, s: str) -> bool:
        # lower case and removing the the alpha
        s_updated = s.lower()
        final_string = ''
        for i in range(len(s_updated)):
            if s_updated[i].isalnum():
                final_string += s_updated[i]
        
        right_ptr = len(final_string) - 1
        left_ptr = 0
        while left_ptr <= right_ptr:
            if final_string[right_ptr]!=final_string[left_ptr]:
                return False
            
            right_ptr -= 1
            left_ptr += 1
        
        return True


    
        