"""1) Create an empty stack and push -1 to it. The first element
   of the stack is used to provide a base for the next valid string.

2) Initialize result as 0.

3) If the character is '(' i.e. str[i] == '('), push index
   'i' to the stack.

2) Else (if the character is ')')
   a) Pop an item from the stack (Most of the time an opening bracket)
   b) If the stack is not empty, then find the length of current valid
      substring by taking the difference between the current index and
      top of the stack. If current length is more than the result,
      then update the result.
   c) If the stack is empty, push the current index as a base for the next
      valid substring.

3) Return result.
"""

class Solution(object):
    def longestValidParentheses(self, string):
        n = len(string)

        # Create a stack and push -1 as initial index to it.
        stk = []
        stk.append(-1)

        # Initialize result
        result = 0

        # Traverse all characters of given string
        for i in xrange(n):

            # If opening bracket, push index of it
            if string[i] == '(':
                stk.append(i)

            else:    # If closing bracket, i.e., str[i] = ')'

                # Pop the previous opening bracket's index
                stk.pop()

                # Check if this length formed with base of
                # current valid substring is more than max
                # so far
                if len(stk) != 0:
                    result = max(result, i - stk[len(stk)-1])

                # If stack is empty. push current index as
                # base for next valid substring (if any)
                else:
                    stk.append(i)

        return result
