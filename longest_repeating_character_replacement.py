# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        longest = 0

        for r in range(len(s)):
            if s[r] not in count:
                count[s[r]] = 0
            count[s[r]] += 1

            if (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest


# test
s = "BBBB"
k = 2
s1 = "AABABBA"
k1 = 1

Ex = Solution()
print(Ex.characterReplacement(s, k))
