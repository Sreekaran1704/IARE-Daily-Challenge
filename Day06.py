#You are given a integer n. You are required to print the number of 0-bits in n. The binary representation of 2 is ‘10’. So, the number of 0-bits in 2 is 1. So, you have to print 1 as the output.
'''
Input:

You are given an integer n.

Output:

You are required to print an integer denoting the number of 0-bits in n.



Sample Input 1:
2

Sample Output 1:
1
'''
a=int(input())
b=bin(a)
count=0
for i in b:
  if i=='0':
    count+=1
print(count-1)
