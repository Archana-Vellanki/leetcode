# 636. Exclusive Time of Functions
# Solved
# Medium
# Topics
# Companies
# On a single-threaded CPU, we execute a program containing n functions. Each function has a unique ID between 0 and n-1.

# Function calls are stored in a call stack: when a function call starts, its ID is pushed onto the stack, and when a function call ends, its ID is popped off the stack. The function whose ID is at the top of the stack is the current function being executed. Each time a function starts or ends, we write a log with the ID, whether it started or ended, and the timestamp.

# You are given a list logs, where logs[i] represents the ith log message formatted as a string "{function_id}:{"start" | "end"}:{timestamp}". For example, "0:start:3" means a function call with function ID 0 started at the beginning of timestamp 3, and "1:end:2" means a function call with function ID 1 ended at the end of timestamp 2. Note that a function can be called multiple times, possibly recursively.

# A function's exclusive time is the sum of execution times for all function calls in the program. For example, if a function is called twice, one call executing for 2 time units and another call executing for 1 time unit, the exclusive time is 2 + 1 = 3.

# Return the exclusive time of each function in an array, where the value at the ith index represents the exclusive time for the function with ID i.

 

# Example 1:


# Input: n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
# Output: [3,4]
# Explanation:
# Function 0 starts at the beginning of time 0, then it executes 2 for units of time and reaches the end of time 1.
# Function 1 starts at the beginning of time 2, executes for 4 units of time, and ends at the end of time 5.
# Function 0 resumes execution at the beginning of time 6 and executes for 1 unit of time.
# So function 0 spends 2 + 1 = 3 units of total time executing, and function 1 spends 4 units of total time executing.
# Example 2:

# Input: n = 1, logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
# Output: [8]
# Explanation:
# Function 0 starts at the beginning of time 0, executes for 2 units of time, and recursively calls itself.
# Function 0 (recursive call) starts at the beginning of time 2 and executes for 4 units of time.
# Function 0 (initial call) resumes execution then immediately calls itself again.
# Function 0 (2nd recursive call) starts at the beginning of time 6 and executes for 1 unit of time.
# Function 0 (initial call) resumes execution at the beginning of time 7 and executes for 1 unit of time.
# So function 0 spends 2 + 4 + 1 + 1 = 8 units of total time executing.
# Example 3:

# Input: n = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
# Output: [7,1]
# Explanation:
# Function 0 starts at the beginning of time 0, executes for 2 units of time, and recursively calls itself.
# Function 0 (recursive call) starts at the beginning of time 2 and executes for 4 units of time.
# Function 0 (initial call) resumes execution then immediately calls function 1.
# Function 1 starts at the beginning of time 6, executes 1 unit of time, and ends at the end of time 6.
# Function 0 resumes execution at the beginning of time 6 and executes for 2 units of time.
# So function 0 spends 2 + 4 + 1 = 7 units of total time executing, and function 1 spends 1 unit of total time executing.
 

# Constraints:

# 1 <= n <= 100
# 1 <= logs.length <= 500
# 0 <= function_id < n
# 0 <= timestamp <= 109
# No two start events will happen at the same timestamp.
# No two end events will happen at the same timestamp.
# Each function has an "end" log for each "start" log

#  Intuition:
# Each function can be interrupted by another function (nested calls).
# To track how long a function runs exclusively (excluding nested calls), we need to:
  # use stack to save the start time of a function.
  # When a new function starts, before adding it to the stack, we should update the active time of the previous function in the answer.
  # When a function ends, pop from stack, calculate its duration and update the answer. If a process still exists in the stack, that is the parent function; update its start time to current_timestamp + 1 
# (because as soon as the nested call ends, the parent function starts to run in the current span.)
# Remember that the previous span was already processed. We only have to take care of the current span of the parent function.


# Example:
# n = 2
# logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]

# Step-by-step:
# "0:start:0" → Function 0 starts at time 0 → stack = [[0, 0]]
# "1:start:2" → Nested function 1 starts at time 2
#              → Function 0 paused → 2 - 0 = 2 units added to ans[0]
#              → stack = [[0, 0], [1, 2]]
# "1:end:5"   → Function 1 ends at time 5
#              → 5 - 2 + 1 = 4 units added to ans[1]
#              → stack = [[0, 0]]
#              → Resume function 0, update its start time to 6
# "0:end:6"   → Function 0 ends at time 6
#              → 6 - 6 + 1 = 1 unit added to ans[0]

# Final answer: [3, 4]
# → Function 0: 2 (before nested) + 1 (after nested) = 3
# → Function 1: ran for 4 units exclusively

# Time complexity: O(m) where m is the size of logs list. 
# Space complexity: O(m + n) m -> stack n -> answer where n is the number of functions

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        func_exec_times = [0]*n
        stack = []
        log_format = lambda log: (int(log[0]), log[1], int(log[2]))

        for each in logs:
            f_id, log_type, timestamp = log_format(each.split(":"))
            if log_type == "start":
                if stack:
                    func_exec_times[stack[-1][0]] += timestamp - stack[-1][1]
                stack.append([f_id, timestamp])
            else:
                func_exec_times[f_id] += timestamp - stack.pop()[1] + 1
                if stack:
                    stack[-1][1] = timestamp + 1
            
        return func_exec_times

