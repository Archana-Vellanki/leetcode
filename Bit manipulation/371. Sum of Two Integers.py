# 371. Sum of Two Integers
# Solved
# Medium
# Topics
# Companies
# Given two integers a and b, return the sum of the two integers without using the operators + and -.

# Example 1:

# Input: a = 1, b = 2
# Output: 3
# Example 2:

# Input: a = 2, b = 3
# Output: 5
 

# Constraints:
# -1000 <= a, b <= 1000


# APPROACH
# 1. Key Insight
    # XOR (^) acts like addition without carrying. For each bit position, XOR gives 1 if that bit is set in exactly one operand, else 0.
        # Example: 1 ^ 1 = 0 (like 1+1=2, with a carry), but 1 ^ 0 = 1.
    # AND (&) identifies where both bits are 1, which is exactly where the carry would come from.
        # Example: 1 & 1 = 1 indicates a carry bit should go into the next higher bit.
    # Left shift (<<) moves that carry up to the next bit position.
    # By combining these ideas:
        # sum = a ^ b (an “incomplete sum,” ignoring carry).
        # carry = (a & b) << 1 (where each carry bit goes to the next position).
        # Then add the carry by repeating the process with new a = sum and b = carry.
        # Eventually, the carry becomes zero, and a holds the final sum.

# 2. Handling Negatives in Two’s Complement
    # In most programming languages/hardware, negative numbers are stored in two’s complement form. 
    # The same bitwise logic (XOR, AND, SHIFT) applies regardless of whether the value is “negative” or “positive” because it’s all just bits. The sign bit is simply the leftmost bit.
    # Thus, no special steps are needed for negatives—the same routine works automatically.

# 3. Why Python Needs an Extra Step
    # Python integers do not have a fixed bit width, so they don’t “wrap around” at 32 or 64 bits. To mimic the behavior of 32-bit arithmetic (like C/C++/Java “int”), we:
    # Mask intermediate results with 0xffffffff to limit ourselves to 32 bits.
    # After the loop, check if the final 32-bit pattern should be treated as negative (if its highest bit is set). If so, convert it to a Python negative integer.
    # That’s just to match “real” 32-bit two’s complement behavior. In actual 32-bit environments, the overflow and negative handling happen automatically in hardware.


class Solution:
    def getSum(self, a: int, b: int) -> int:
        """ 
        get binary representation 
        reverse process it. # stack?
        use a carry bit
         for every bit, do  carry AND a_bit AND b_bit
        if true, add 1 bit to result, carry remains 1
        else:
          if a_bit and b_bit: carry = 1 result.append(0) 
          else
          12 =>   1100
          29 =>  11101
        result =>  100101
        """

        MASK = 0xffffffff
        MAX_INT = 0x7fffffff
        
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & MASK
            b = carry & MASK
        
        return a if a <= MAX_INT else ~(a ^ MASK)

