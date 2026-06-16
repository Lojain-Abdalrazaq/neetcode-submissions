class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_map = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                # )]}
                if not stack:
                    return False
                pop = stack.pop()
                if pop != hash_map[char]:
                    return False
        
        return len(stack) == 0
        

        