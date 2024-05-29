# Intuition
We need to ensure two things:

1. All characters in `s` are in `t`
2. The order of the characters in `s` is maintained in `t`
The use of both strings `s` and `t` is required to determine if the conditions are true. So we are going to need to iterate over both strings.
Ideally, we could iterate over them simultaneously, regardless of their length. To iterate over two items at the same time, we need to use two pointers.

# Approach
We initialize two pointers, `s_pos` and `t_pos` to `0`. We use these as indices for `s` and `t`, respectively. We initialize an empty string, `sequence`, 
to keep track of the subsequence as we build it from `t`.

We begin iterating over our two strings, continuing until `s_pos` or `t_pos` exceeds the range of `s` or `t`, respectively. In each iteration, we can add 
`1` to `t_pos`, while maintaining `s_pos` until the character at `s[s_pos]` is encountered in `t`. Then, add the current character to `sequence` and adjust `s_pos`
to begin searching for the next character in `s`. Continue until either `s` or `t` have been exhausted. Finally, return the result of `sequence == s`.

This approach ensures that even if all the characters in `s` exist in `t`, we only consider them in the same order they occur in `s`. This satisfies our two 
required conditions.

Complexity
* Time complexity: $$O(n)$$, where nnn is the larger of s.length and t.length
Space complexity: O(1)O(1)O(1)
Code
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
