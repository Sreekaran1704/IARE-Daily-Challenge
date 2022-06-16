#Microsoft conducted a contest for N freshers at their workplace. The marks of each student is noted in the form of a list. As HR, you need to finalize thoes K students who got highest marks.

'''Input:

The first line has 2 space separated integers representing N and K respectively. The second line denotes list of marks of N students.

Output:

A single line representing the K highest marks in decreasing order.

Sample Input 1:
6 1
647 12 560 87 101 230

Sample Output 1:
647'''

n,k=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
l.reverse()
for i in range(k):
  print(l[i],end=" ")
