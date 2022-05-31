#You are given the co-ordinates of a chessboard cell. You have to determine the color of that cell. You will be given the input cell as a Stringss s. For example, if the given input cell is ‘a1’, then the color of the chessboard cell is black. So, you output ‘Black’.


'''Input:

You are given the cell of a chessboard as a Stringss s.

Output:

You should output the color of the cell as ‘White’ or ‘Black’.

Sample Input 1:
a1

Sample Output 1:
Black

Explanation:
The cell ‘a1’ in the chessboard is a black cell'''

a=input()
b=ord(a[0])
if ((b+int(a[1:]))%2==0):
  print("Black")
else:
  print("White")
