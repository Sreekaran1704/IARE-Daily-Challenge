#somu thinks about watering her lawn. The lawn may be represented as a segment of length k. somu has got n buckets, the i-th bucket permits her to water some non-stop subsegment of lawn of duration precisely ai each hour. somu can't water any components of the lawn that were already watered, also she can not water the ground outside the lawn.somu has to pick one of the buckets so that it will water the lawn as speedy as viable (as mentioned above, each hour she will be able to water some continuous subsegment of length ai if she chooses the i-th bucket). assist her to determine the minimum wide variety of hours she has to spend watering the lawn. it's far assured that somu can constantly choose a bucket so it is possible water the lawn.
'''
Input:

the first line of input contains two integer numbers n and k — the number of buckets and the period of the lawn, respectively.
the second line of enter contains n integer numbers ai — the length of the section that can be watered by the i-th bucket in one hour.
it is guaranteed that there's at the least one bucket such that it is possible to water the lawn in integer number of hours using only this bucket.

Output:

the minimum number of hours required to water the lawn.

Sample Input 1:
3 6
2 3 5

Sample Output 1:
2

Explanation:
First test the best option is to choose the bucket that allows to water the segment of period 3. We can not choose the bucket that permits us to water the segment of period 5 because then we can not water the whole lawn.
'''
n,k=map(int,input().split())
a=list(map(int,input().split()))
l=[]
for i in range(len(a)):
  if k%a[i]==0:
    l.appned(a[i])
l.sort()
b=k/l[-1]
c=int(b)
print(c)
       
