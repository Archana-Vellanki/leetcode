# 269. Alien Dictionary
# Solved
# Hard
# Topics
# Companies
# There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

# You are given a list of strings words from the alien language's dictionary. Now it is claimed that the strings in words are sorted lexicographically by the rules of this new language.

# If this claim is incorrect, and the given arrangement of string in words cannot correspond to any order of letters, return "".

# Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.

 

# Example 1:

# Input: words = ["wrt","wrf","er","ett","rftt"]
# Output: "wertf"
# Example 2:

# Input: words = ["z","x"]
# Output: "zx"
# Example 3:

# Input: words = ["z","x","z"]
# Output: ""
# Explanation: The order is invalid, so return "".
 

# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of only lowercase English letters.

# Intuition:
# For every consecutive pair of words, determine the first different character, which defines an ordering: ch1 < ch2.
# Use these relations to build a directed graph.
# Perform a topological sort (BFS or DFS based) on the graph to determine the valid order of characters.

# Approach: BFS-based Topological Sort (Kahn's Algorithm)
# Initialize: adj: adjacency list (character → set of characters that follow it) and indegree: count of incoming edges for each character.

# Compare consecutive words to build the graph:
  # For each pair (word1, word2), compare characters one-by-one.
  # First differing characters imply word1[i] < word2[i] → edge from word1[i] → word2[i].
  # If word1 is longer and word1.startswith(word2), return "" (invalid).

# BFS:
# Add characters with 0 indegree to queue.
# Process nodes, reduce indegrees, and add new zero-indegree nodes to the queue.
# If result includes all characters, return the result string.

# Time Complexity: O(N + K) where N is total characters in all words and K is total unique characters.
# Space Complexity: O(K) for adjacency list and indegree map.

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        #Build adjacency list
        # indegree
        # BFS
        i = 0
        j = 1
        length = len(words)
        adj = defaultdict(set)
        indegree = {ch: 0 for word in words for ch in word}
        while j < length:
            word1,word2 = words[i], words[j]
            for ch1,ch2 in zip(word1,word2):
                if ch1 != ch2:
                    if ch2 not in adj[ch1]:
                        adj[ch1].add(ch2)
                        indegree[ch2] += 1
                    break
            else:
                if len(word1) > len(word2):
                    return ""
            j += 1
            i += 1
        # adj list is ready

        q = deque()
        for ch,indeg in indegree.items():
            if indeg == 0:
                q.append(ch)
        result = []
        while q:
            ch = q.popleft()
            result.append(ch)
            for each in adj[ch]:
                indegree[each] -= 1
                if indegree[each] == 0:
                    q.append(each)  
        if len(result) != len(indegree):
            return ""
        return "".join(result)
