class Solution:

    def encode(self, strs: List[str]) -> str:
        # time complexity -> O(n)
        encoded_str = ""
        for i in range(len(strs)):
            
            encoded_str += str(len(strs[i]))
            encoded_str += "%"
            encoded_str +=strs[i]
        
        print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        # in the decoding part, we need two pointers [P1, P2]
        p1, p2 = 0,0
        decoded_str = [] 
        while p1 < len(s):
            if s[p2] != '%':
                p2 += 1
            else:
                # we are pointing on the '%'
                string_len = int(s[p1:p2])
                item = s[(p2+1):(p2+string_len+1)]
                decoded_str.append(item)
                p2 += string_len + 1
                p1 = p2
        
        return decoded_str
    


    
            
        
        