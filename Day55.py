#The titans are playing N games among themselves. Each titan has a unique ID that will be written on the leaderboard. Find the titan's ID who has won altest N/2 games. There always exists 1 titant to win atleast N/2 games.

'''Input:

Single line denoting the leaderboard

Output:

Single integer denoting the titan's ID

Sample Input 1:
5 5 3 5

Sample Output 1:
5'''

a=list(map(int,input().split()))
b=len(a)
d=list(set(a))
for i in d:
  c=a.count(i)
  if c>(b//2):
    print(i)
