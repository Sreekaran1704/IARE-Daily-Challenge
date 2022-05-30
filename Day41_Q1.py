# You are given a number P. You are required to print the base-N representation of the number P.

'''Input:

The first line of input consists of a single integer T, denoting the number of test-cases.
The integer P denotes the number.
The next line consists of the integer N which denotes the base


Output:

Output  T lines. Each of these lines contain base n representation of the number P.

Sample Input 1:
1
10
2

Sample Output 1:
1010

Explanation:
The base-2 representation of number 10 is ‘1010’. Hence, the answer is 1010.'''

dig='0123456789ABCDEF'
def numtobase(n,b):
  digits=[]
while(n>0):
  rem=n%b
  digits.append(rem)
  n=n//b
newdigits=[]
while digits:
  new_digits.appned(dig[digits.pop()])
return ''.join(new_digits)

for i in range(int(input()):
  n=int(input())
  b=int(input())
  print(numtobase(n,b))
