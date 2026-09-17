class Solution:
    def reverseString(self, s: list[str]) -> None:
        loop_len = len(s) // 2
        j = len(s) - 1
        for i in range(loop_len):
            s[i], s[j] = s[j], s[i]
            j -= 1