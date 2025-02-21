# 767. Reorganize String
# Solved
# Medium
# Topics
# Companies
# Hint
# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

# Return any possible rearrangement of s or return "" if not possible.

 

# Example 1:

# Input: s = "aab"
# Output: "aba"
# Example 2:

# Input: s = "aaab"
# Output: ""
 

# Constraints:

# 1 <= s.length <= 500
# s consists of lowercase English letters.

# At any point characters with max frequency have to be chosen first. Which data structure is the best for accessing each character in the order of their frequencies ????
# Heap - push all the characters with their frequencies.
# Pop a character with max frequency and add it to the string. Since we dont want any repeated characters, pop the next most frequent character and add it to the result. then update their frequencies and push to the pop again 
# if there is only one character left, check if its frequency is greater than 1, if so we cannot satisfy the condition of no repeated adjacent characters.
# else add that single character to the result and return it
class Solution:
    def reorganizeString(self, s: str) -> str:
        length = len(s)
        
        counter = {}

        for each in s:
            counter[each] = counter.get(each, 0) + 1
            if counter[each] > length//2 + 1:
                return ""   
        heap = [(-freq,ch) for ch,freq in counter.items()]
        heapq.heapify(heap)
        result = []
        while heap:
            # print(heap)
            freq1, ch1 = heapq.heappop(heap)
            if -freq1 > length//2 + 1:
                return ""
            if not heap:
                if -freq1 > 1:
                    return ""
                else:
                    result.append(ch1)
                    break
            freq2, ch2 = heapq.heappop(heap)
            if -freq2 > length//2 + 1:
                return ""
            result.append(ch1)
            result.append(ch2)
            if -freq1 -1  > 0:
                heapq.heappush(heap, (freq1+1, ch1))
            if -freq2 -1  > 0:
                heapq.heappush(heap, (freq2+1, ch2))
        return "".join(result)
