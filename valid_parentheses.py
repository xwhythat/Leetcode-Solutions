from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            if c == ")" or c == "]" or c == "}":
                if stack:
                    curr = stack.pop()
                else:
                    return False

                if curr == "(" and c != ")":
                    return False
                if curr == "[" and c != "]":
                    return False
                if curr == "{" and c != "}":
                    return False

        if stack:
            return False

        return True


# test
s = "()"
s_1 = "()[]{}"
s_2 = "(]"
s_3 = ")"

Ex = Solution()
print(Ex.isValid(s))