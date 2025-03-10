# 71. Simplify Path
# Medium
# Topics
# Companies
# You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.

# The rules of a Unix-style file system are as follows:

# A single period '.' represents the current directory.
# A double period '..' represents the previous/parent directory.
# Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
# Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.
# The simplified canonical path should follow these rules:

# The path must start with a single slash '/'.
# Directories within the path must be separated by exactly one slash '/'.
# The path must not end with a slash '/', unless it is the root directory.
# The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
# Return the simplified canonical path.

 

# Example 1:

# Input: path = "/home/"

# Output: "/home"

# Explanation:

# The trailing slash should be removed.

# Example 2:

# Input: path = "/home//foo/"

# Output: "/home/foo"

# Explanation:

# Multiple consecutive slashes are replaced by a single one.

# Example 3:

# Input: path = "/home/user/Documents/../Pictures"

# Output: "/home/user/Pictures"

# Explanation:

# A double period ".." refers to the directory up a level (the parent directory).

# Example 4:

# Input: path = "/../"

# Output: "/"

# Explanation:

# Going one level up from the root directory is not possible.

# Example 5:

# Input: path = "/.../a/../b/c/../d/./"

# Output: "/.../b/d"

# Explanation:

# "..." is a valid name for a directory in this problem.

# Approach: Key point: Split the path on "/" and use stack to process each of the intermediate paths
# if length > 2: it's a valid directory name/file name so add it to the stack
# else, check for "."  - nothing to do 
#       check for ".." - pop the last directory because we have to go to the parent

# Can be done using character-by-character approach also. Scroll down.
# Time Complexity:O(n)
# Space Complexity:O(n)

# Constraints:

# 1 <= path.length <= 3000
# path consists of English letters, digits, period '.', slash '/' or '_'.
# path is a valid absolute Unix path.

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        name = ""
        strings = path.split('/')
        for each in strings:
            if len(each) > 2:
                stack.append(each)
            else:
                if each == "" or each == "." or (each == ".." and not stack):
                    continue
                if each == ".." and stack:
                    stack.pop()
                else:
                    stack.append(each)
        # print(stack)
        # result = 
        return "/" + "/".join(stack)
                 
                    

# Approach 2 using Character by character approach:
# Possible optimizations - temp can be used as a list instead of a string

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        i =  0
        length = len(path)
        temp = ""
        while i < length:
            # print(stack)
            if path[i] == '/':
                if temp:
                    if temp == "." or (temp == ".." and not stack):
                        i+=1
                        temp = ""
                        continue
                    elif temp ==".." and stack:
                        temp = ""
                        stack.pop()
                    else:
                        stack.append(temp)
                        temp = ""
                else:
                    i+=1
                    continue
            else:
                temp = temp + path[i]
            i+=1
        if temp:
            if temp ==".." and stack:
                stack.pop()
            elif temp == "." or (temp ==".." and not stack):
                # we dont have to do anything
                temp = ''
            else:
                stack.append(temp)
        # print(stack)
        return "/" + "/".join(stack)
                 
                    
