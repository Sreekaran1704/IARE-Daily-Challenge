#You are given an positive integer n. If n is even, you have to divide it by 2. If n is odd, you have to multiply it with 4 and add 4. You have to repeat this process k times. For example, if n is 100 and k is 4, the process goes like 100->50->25->104->52. So, the value of n after k operations is 52, so you have to print 52 as the answer.

'''Input:

You are given the values of n and k on a single line.

Output:

You have to print the value of n after k operations.

Sample Input 1:
100 4

Sample Output 1:
52
'''

n,k=map(int,input().split())
for i in range(k):
  if n%2==0:
    n=n//2
  else:
    n=(n*4)+4
print(n)
