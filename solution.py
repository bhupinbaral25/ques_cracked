
def get_phwords():
	return {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}


class Solution(object):

   def get_result(self, digits):
      if len(digits) == 0:
         return []
      alphabets = get_phwords()
      result = []
      self.solve(digits,alphabets,result)
      return result

   def solve(self, digits, alphabets, result, current_string="", current_level = 0):
      
      if current_level == len(digits):
         result.append(current_string)
         return None

      for index in alphabets[int(digits[current_level])]:
         self.solve(digits, alphabets, result, current_string+index, current_level+1)
	


print(get_phwords())