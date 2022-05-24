#Ajay placed a magical box in front of you. He places two 1 rupee coins in the box on the first day (in this manner -> 1 and 1). When you both go and see the box tomorrow(this is considered as Day 1), you are surprised to see that the second coin has got the value which is the equal to the sum of the two coins placed. For every subsequent day, the first coin is replaced by the second coin. You are required to find out the value of second coin on the nth day.

'''Input:

The first line consists of N denoting the Nth day.

Output:

A single integer consists of the value of the coin on the Nth day. As the value of the coin could be large, print the answer modulo 1000000000+7.

Sample Input 1:
2

Sample Output 1:
3

Explanation:
Initially, the value of coins are 1 and 1. On the first day, the value of coins become 1 and 2. On second day, the value of coins become 2 and 3. So the answer is 3.'''

n=int(input())
a=1
b=1
c=a
for i in range(n):
  b=c+b%(1000000007)
  c=a%(1000000007)
  a=b%(1000000007)
print(b)
