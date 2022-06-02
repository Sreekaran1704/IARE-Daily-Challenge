#John is back with again with an interesting problem. He gives you a number N and wants you to find two distinct positive numbers such that their bitwise XOR is N and bitwise AND is 0. If such numbers exist, print True, else print False.
'''For example, if he gives the number N as 6, then the possible numbers that satisfy the above conditions are 2 and 4 because 2&4==0 and 2^4==6.

Input:

You will be given T in the first line, the number of test cases.
In the second line, you will be given an integer N.


Output:

You have to print the True if there exists a pair that satisfies the conditions in the question, else print False.

Sample Input 1:
2
7
11

Sample Output 1:
True 
True

Explanation:
For the first test-case, the two positive integers that satisfy given conditions are 1 and 6 because 1^6=7 and 1&6=0.
For the second test-case, the two positive integers that satisfy given conditions are 3 and 8 because 3^8=11 and 3&8=0.
'''

import math

def Log2(x):
  if x==0:
    return False
  else:
    return (math.log10(x)/math.log10(2))

for i in range(int(input()):
  n=int(input())
  if (math.ceil(Log2(n))==math.floor(Log2(n))):
    print(False)
  else:
    print(True)
