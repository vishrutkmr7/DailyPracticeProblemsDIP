# length of the longest substring without repeating characters
# Challenge: Find solution in linear time

NO_OF_CHARS = 256

class Solution:
    def lengthOfLongestSubstring(self, s):
        # Fill this in.
        l = len(s)
        cur_len = 1
        max_len = 1
        prev_index = 0
        i = 0

        visited = [-1] * NO_OF_CHARS
        visited[ord(s[0])] = 0

        for i in range(1, l):
            prev_index = visited[ord(s[i])]

            if prev_index == -1 or (i - cur_len > prev_index):
                cur_len += 1
            else:
                if cur_len > max_len:
                    max_len = cur_len

                cur_len = i - prev_index

            visited[ord(s[i])] = i

        if cur_len > max_len: 
            max_len = cur_len
        
        return max_len


print (Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10