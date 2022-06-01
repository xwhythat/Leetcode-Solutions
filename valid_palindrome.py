class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted = ""
        for char in s:
            if char.isalpha() or char.isdigit():
                formatted += char.lower()

        return formatted == formatted[::-1]


# test
s = "0A man, a plan, a canal: Panama0"  # True
s1 = "race a car"  # False
s2 = " "

Ex = Solution()
print(Ex.isPalindrome(s))