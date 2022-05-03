class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def toLetters(s):
            ss = []
            for letter in s:
                ss.append(letter)
            return ss

        ss = toLetters(s)
        st = toLetters(t)

        ss.sort()
        st.sort()
        if ss == st:
            return True
        return False


# test
s1 = "anagram"
t1 = "nagaram"
s2 = "rat"
t2 = "car"

A = Solution()
print(A.isAnagram(s2, t2))
print(sorted(s1))