class Solution(object):
    """
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

    """
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]

        To solve this, we will follow these steps −

1. Define an array called solve to solve the problem recursively
2. solve method takes digits, characters, result, current_string and current_level, the function will be like
if current_level = length of digits, then add current string to the result, and return
for all characters i in characters[digits[current_level]]
perform solve(digits, characters, result, current_string + i, current_level + 1)
        """
        if len(digits) == 0:
          return []
        characters = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        result = []
        self.solve(digits, characters, result)
        return result
    def solve(self, digits, characters, result, current_string = "", current_level = 0):
        if current_level == len(digits):
          result.append(current_string)
          return
        for i in characters[int(digits[current_level])]:
          self.solve(digits, characters, result, current_string+i, current_level+1)
ob1 = Solution()
print(ob1.letterCombinations("37"))