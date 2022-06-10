#You are given an array A of length N. The array contains elements in the range [0,N-1]. Find all the elements occurring more than once in A[N].

'''Input:

Input comsists of 2 lines, the first line consists N and the next line consists array A[]

Output:

Output the list of repeated elements in sorted order

Sample Input 1:
5
0 3 1 2 4

Sample Output 1:
-1

Explanation:
There are no repeated elements in A[N], hence output is -1'''

n=int(input())
a=list(map(int,input().split()))
new=[]
for i in a:
  n=a.count()
  if n>1:
    if new.count(i)==0:
      new.append(i)
new.sort()
if len(new)>0:
  print(i,end=" ")
else:
  print(-1)
