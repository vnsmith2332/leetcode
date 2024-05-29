class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pos = 0
        t_pos = 0
        sequence = ""
        while t_pos < len(t) and s_pos < len(s):
            if t[t_pos] == s[s_pos]:
                sequence += t[t_pos]
                s_pos += 1
            t_pos += 1
        return sequence == s 
