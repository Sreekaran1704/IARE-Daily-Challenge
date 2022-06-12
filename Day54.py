#Sakura found a box of precious ancient coins. She loves to build triangles with coins and wants you to help her find the maxium height of the triangle that can be constructed using the given N number of coins. The 1st layer of the triangle consists of 1 coin, the 2nd layer has 2 coins, 3rd layer has 3 coins and so on.

'''Input:

The first line denotes T number of test cases. The following T lines represent N number of coins.

Output:

Single integer denoting the maxium height of the triangle than can be formed.

Sample Input 1:
1
15

Sample Output 1:
5'''

import math
for i in range(int(input()):
  n=int(input())
  a=1+8*n
  h=(-1+math.sqrt(a))/2
  print(int(h))
