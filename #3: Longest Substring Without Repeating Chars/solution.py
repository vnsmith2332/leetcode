class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        seen = set()
        max_len = 0
        while right < len(s):
            # char at right of window is not in the substring. Add it and check for max length
            if s[right] not in seen:
                seen.add(s[right])
                if len(seen) > max_len:
                    max_len = len(seen)
            # char at right of window is in the substring. Shrink window until this char is removed, then add it back in
            else:
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1
                seen.add(s[right])
            right += 1
        return max_len
      
