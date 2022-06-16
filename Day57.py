#The soldiers returned after their expedition outside the Wall Shina. Unfortunately one soldier went missing during their return. Each soldier has a ID numberd 0 through N. The ID number of the soldier surely lies in the range [0,N]. Find out the ID number of the missing soldier.

'''Input:

Single line denoting thearray of ID numbers

Output:

Print the only ID number in the range that is missing from the array

Sample Input 1:
0 1

Sample Output 1:
2'''

a=list(map(int,input().split())
n=len(a)
a.sort()
for i in range(n+1):
  if i in a:
    continue
  else:
    print(i)
    break
