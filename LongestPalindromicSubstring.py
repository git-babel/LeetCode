def expandingSearch(s: str, start: int, end: int):
    radius = 0
    left = start
    right = end

    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
        radius += 1

    return radius

class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        max_str = ""

        for i in range(len(s)):
            odd_radius = expandingSearch(s, i, i)
            even_radius = expandingSearch(s, i, i+1)

            odd_length = 2 * odd_radius - 1
            even_length = 2 * even_radius

            if odd_length > even_length and odd_length > max_len:
                max_len = odd_length
                max_str = s[i-(odd_radius-1):i+odd_radius]
            elif even_length > odd_length and even_length > max_len:
                max_len = even_length
                max_str = s[i-(even_radius-1):i+(even_radius+1)]

        return max_str
