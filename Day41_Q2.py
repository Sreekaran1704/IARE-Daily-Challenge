#You are given the lengths of sides of a square A, B, C, D. You have to tell if it is possible to construct a square or not with the given lengths

'''Input:

The first line of input consists of a single integer T, denoting the number of test-cases.
The next line consists of four integers denoting the lengths of sides of a square


Output:

Output T lines. Each of these contain “YES” if it is possible to construct a square, else “NO”.

Sample Input 1:
5
1 1 1 1
4 6 21 1
6 4 3 4
6 6 6 6
10 101 1 1

Sample Output 1:
YES
NO
NO
YES
NO

Explanation:
A square has all its sides of equal length. So, the testcases 1 and 4 are YES and the others are NO.'''

for i in range(int(input()):
  a=list(map(int,input().split()))
  b=set(a)
  c=list(b)
  if len(c)==1:
    print("YES")
  else:
    print("NO")
         
