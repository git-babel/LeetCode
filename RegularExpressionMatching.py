class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def _isCharMatch(c: str, p: str):
            if len(c) != 1 or len(p) != 1:
                raise ValueError

            return c == p or p == "."

        def _isEmptiablePattern(p: str):
            if p == "":
                return True
            elif len(p) > 1 and p[1] == '*':
                return _isEmptiablePattern(p[2:])
            else:
                return False


        def _isMatch(s: str, p: str):
            if not s or not p:
                return s == "" and _isEmptiablePattern(p)

            curr_pattern = p[0]
            next_pattern = p[1] if len(p) > 1 else None

            if next_pattern and next_pattern == "*":
                if _isCharMatch(s[0], p[0]):
                    return _isMatch(s[1:], p) or _isMatch(s, p[2:])
                else:
                    return _isMatch(s, p[2:])
                elif _isCharMatch(s[0], p[0]):
                    return _isMatch(s[1:], p[1:])
            else:
                return False

        return _isMatch(s, p)
