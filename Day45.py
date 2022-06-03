#Tony Stark started a new company called as Stark Cabs! This company provides cab services for people. Stark’s friend Bruce Banner runs a school. So, Bruce planned a trip for his students!
'''All the students could go in a single cab but everyone wants to travel only with their friends and nobody else. You have been given two integers P, the number students in the class and Q, the number friendship relations in the class.
Remember that friends of friends are also considered as friends. For example, if X has a friend Y and Y has a friend Z. Then, X and Z are also considered to be friends.
Since Bruce is busy with his students. He asks you to calculate the minimum number of cabs needed for the trip!

Input:

The first line contains two integers A and B.
The next B lines contain two integers P and Q denoting that P and Q are friends.


Output:

For each test-case, output in a single line the number of cabs required.

Sample Input 1:
5 3
1 2 
3 4
1 5

Sample Output 1:
2

Explanation:
Since, 1 and 2 are friends and 5 is also a friend of 1. Then, (1, 2, 5) are considered to be friends and they go in a cab. 3 and 4 are considered to be friends, so they go in another cab. So, a total of 2 cabs are required for travelling! So, you print 2.'''

def dfs(v,visited):
  visited[v]=True
  for i in g[v]:
    if not visited[i]:dfs(i,visited)
p,q=map(int,input().split())
visited=[False]*(p)
g=[[] for i in range(p)]

for i in range(q):
  x,y=map(int,input().split())
  x-=1
  y-=1
  g[x].append(y)
  g[y].append(x)
ans=0

for v in range(p):
  if not visited[v]:dfs(v,visited);ans+=1
print(ans)
