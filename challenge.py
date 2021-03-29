'''Write a python function which accepts three numbers and returns True if
a.	one of the three numbers is "close" to any one of the other numbers (differing from a number by at most 1), and
b.Number that is left out is "far", differing from both other values by 2 or more.
Return false if the above mentioned conditions are not satisfied.
Sample Input	Expected Output
4,1,3	True
5,6,7	False
'''

def number(num1, num2, num3):
   list = [num1, num2, num3]
   list.sort() #sorted from the lowest number to the highest number

   if list[1] + 2 <= list[2] or list[0] + 2 <= list[1]:
      print("True")
   else:
      print("False")

number(5, 6, 7)