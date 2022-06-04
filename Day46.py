#You are given an Arrays arr of length n. You have to print the smallest element in the Arrays arr. For example, if the given Arrays is [5,4,9], the smallest element in the Arrays. So, you have to print 4 as the answer.

'''Input:

You are given the length of the Arrays arr.
You are given the Arrays arr.


Output:

You have to print the smallest element in the arr.

Sample Input 1:
6
1 2 3 4 5 6

Sample Output 1:
1

Explanation:
The smallest element in the Arrays arr is 1.'''
n=int(input())
l=list(map(int,input().split()))
l.sort()
print(l[0])
