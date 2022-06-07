#A number is said to be bad if the number of ‘1’s in its binary representation is an odd number. Find if the given number is bad or not

'''Input:

The first line contains an integer T, the number of test cases. Then the test cases follow.
Each testcase contains an integer n


Output:

Print Yes if the given number is bad or Print No

Sample Input 1:
3
1
2
3

Sample Output 1:
Yes
Yes
No

Explanation:
Binary representation of 1 is 1.
Number of ones is odd so the answer is Yes'''

for i in range(int(input()):
  n=int(input())
  a=bin(n)
  b=a[2:]
  c=b.count('1')
  if c%2!=0:
    print('Yes')
  else:
    print('No')
