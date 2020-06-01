class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

        For example, given n = 3, a solution set is:

        [
          "((()))",
          "(()())",
          "(())()",
          "()(())",
          "()()()"
        ]

        To solve this, we will follow these steps −

        Define method called genParenthesisRec(). This takes left, right, temp string and result array. initially result array is empty
        The function genParenthesisRec, will work like below
        if left = 0 and right := 0, then insert temp into result, and return
        if left > 0
        getParenthesisRec(left – 1, right, temp + “(”, result)
        if right > left
        getParenthesisRec(left, right – 1, temp + “)”, result)
        """
        result = []
        self.generateParenthesisUtil(n, n, "", result)
        return result
    def generateParenthesisUtil(self, left, right, temp, result):
        if left == 0 and right == 0:
          result.append(temp)
          return
        if left > 0:
          self.generateParenthesisUtil(left-1, right, temp+'(', result)
        if right > left:
          self.generateParenthesisUtil(left, right-1, temp+')', result)

ob = Solution()
print(ob.generateParenthesis(8))