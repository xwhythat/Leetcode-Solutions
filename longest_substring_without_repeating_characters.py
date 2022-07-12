# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        l = 0
        r = 1
        longest = 0
        length = len(s[l:r])
        while r < len(s):
            if s[r] not in s[l:r]:
                r += 1
            else:
                l += 1
            longest = max(len(s[l:r]), longest)

        return longest


# test
s = "abcabcbb"
s_1 = "bbbbb"
s_2 = "pwwkew"
s_3 = ""
s_4 = " "

Ex = Solution()
print(Ex.lengthOfLongestSubstring(s_3))
