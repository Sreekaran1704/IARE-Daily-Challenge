#You will be given an integer. You have to repeatedly add all its digits until the result consists of only digit and print it. For example, if you are given 123 , you have to return 6.

'''Input:

You are given an integer N

Output:

You have to return that single digit after you repeatedly add all its digits until a single digit is left.

Sample Input 1:
123

Sample Output 1:
6'''

n=int(input())
if n==0:
  print(0)
elif n%9==0:
  print(9)
else:
  print(n%9)
