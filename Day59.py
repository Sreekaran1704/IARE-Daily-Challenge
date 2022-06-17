#Connie has learnt array and sorting at college today. He is very inquisite in knowing what more he could do with thoes learnt concepts. He decides to take a sorted array A of length N along with 3 more constants P, Q and R. Connie wants you to create a sorted array based on the array he took by applying the condition that every ith element of your array should be replace with R+P*A[i]**2+Q*A[i].

'''Input:

First line represents N. The second line has 3 space separated constants P Q and R. the third line represents A[N]

Output:

Single line representing modified array in increasing order

Sample Input 1:
5
2 3 4
-10 -6 0 48 67

Sample Output 1:
4 58 174 4756 9183'''

n=int(input())
p,q,r=map(int,input().split())
l=list(map(int,input().split())
l1=[]
for i in l:
  a=r+p*i**2+q*i:
  l1.append(a)
l1.sort()
for i in l1:
  print(i,end=" " )
