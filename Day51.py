#Pixis is anxious of certain numbers and calls them SPECIAL. He defines a number is called SPECIAL when it contains the digits in the set {0,1,2,3,4,5}. Pixis wants you to find out the Nth SPECIAl number. Input consists of only one integer denoting N. Output the Nth SPECIAL number

'''Input:

Single integer denoting N

Output:

Single integer denotinh SPECIAL number

Sample Input 1:
8

Sample Output 1:
11

Explanation:
The first 8 SPECIAL numbers are: 0,1,2,3,4,5,10,11'''

def fun(n):
  ans=[]
  for i in range(6):
    ans.append(i)
  for i in range(n//6+1):
    for j in range(6):
      if(ans[i]*10 !=0):
        ans.append(ans[i]*10+ans[j])
  return ans[n-1]
n=int(input())
print(fun(n))
