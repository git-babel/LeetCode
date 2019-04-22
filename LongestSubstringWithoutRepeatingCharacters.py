class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        candidates = [0] * len(s)
        for idx in range(len(s)):
            candidate = self.getCandidate(idx, s)
            candidates[idx] = candidate
        
        return max(candidates) if len(s) > 0 else 0
    
    def getCandidate(self, idx: int, s: str):
        collisions = {}
        collisions[s[idx]] = True
        
        curr = idx + 1
        while curr < len(s):
            char = s[curr]
            if char in collisions:
                break
            
            collisions[char] = True
            curr += 1
        
        return curr - idx
