class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for b in s:
            if b in "([{":
                stack.append(b)
            else:
                if len(stack) == 0:
                    return False
                curr = stack.pop()
                if b == ")" and curr != "(":
                    return False
                elif b == "}" and curr != "{":
                    return False
                elif b == "]" and curr != "[":
                    return False
        if len(stack) != 0:
            return False
        return True