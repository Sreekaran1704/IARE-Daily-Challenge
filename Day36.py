#You are given an Arrays A consisting of N elements. You have to tell if any element repeats at least thrice in the Arrays. For example, if the Arrays is [1,2,3,3,2,1,1], you have to print ‘T' as the answer because the element 1 repeats thrice. If no element repeats more than thrice, you have to print ‘F’.

'''Input:

You will be given N.
You will be given an Arrays A of N elements


Output:

Print T if any element repeats at least thrice. Print, F otherwise.

Sample Input 1:
5
1 2 3 1 2

Sample Output 1:
F'''

n=int(input())
a=list(map(int,input().split()))
b=set(a)
c=list(b)
flag=0
for i in c:
  b=a.count(i)
  if b>=3:
    flag=1
    print("T")
    break
if flag==0:
  print("F")
