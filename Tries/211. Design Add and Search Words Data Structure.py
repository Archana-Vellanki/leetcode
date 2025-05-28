# 211. Design Add and Search Words Data Structure
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:

# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

# Example:

# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]

# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
 

# Constraints:

# 1 <= word.length <= 25
# word in addWord consists of lowercase English letters.
# word in search consist of '.' or lowercase English letters.
# There will be at most 2 dots in word for search queries.
# At most 104 calls will be made to addWord and search.


# Trie Data Structure 
# Searching for a word (with ot without a .) requires a DFS starting from trie root

# Time Complexity for add: O(n) where n is the length of the string -- Same is the space complexity
# Time Complexity for search: O(n) where n is the length of the string -- Same is the space complexity

# Worst case analysis with dots:
# Let n be the length of the search word, and d be the number of dots (at most 2).
# Time Complexity (search): Worst-case: O(26^d × n) = O(676 × n) = O(n) practically, since 676 is a constant.


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                node.children[ch] = TrieNode()
                node = node.children[ch]
        node.isEnd = True        

    def search(self, word: str) -> bool:
        # q = []
        def dfs(index, node):
            if index == len(word):
                return node.isEnd
            ch = word[index]
            # print(node, ch)
            if ch != '.':
                if ch not in node.children:
                    return False
                return dfs(index + 1, node.children[ch])
            else:
                for key,val in node.children.items():
                    if dfs(index+1, val):
                        return True
            return False


        return dfs(0, self.root)


            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
