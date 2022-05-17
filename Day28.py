#Bunty is given an Array of integers of n elements. For any ordered triplet (i,j,k) such that i, j, and k are pairwise distinct and 1≤i,j,k≤N, the value of this triplet is (Ai−Aj)⋅Ak. Bunty needs to find the maximum value among all possible ordered triplets.

'''Constraints:
1 ≤ T ≤ 100
3 ≤ N ≤ 3⋅10^5
1 ≤ Ai ≤ 10^6

Input:

The first line contains an integer T, the number of test cases. Then the test cases follow.
The first line of each test case contains an integer N.
The second line of each test case contains N space-separated integers A1,A2,…,AN.

Output:

For each test case, output the maximum value among all different ordered triplets.

Sample Input 1:
1
5
3 4 4 1 2

Sample Output 1:
12

Explanation:
The desired triplet is (2,4,3), which yields the value of (A2−A4)⋅A3=(4−1)⋅4=12'''

for i in range(int(input()):
  n=int(input())
  l=list(map(int,input().split()))
  a=max(l)
  l.remove(a)
  b=max(l)
  c=min(l)
  print((a-c)*b)
