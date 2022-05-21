#Kohli gave you a number which consists of digits 1 and 8. (Because his jersey number is 18). So, he wants to find the maximum number he can get by changing at most one digit(1 becomes 8 or 8 becomes 1). For example, you are given a number 1811, then the answer is 8811 since 1881 and 1818 are smaller number compared to 8811. So, the answer is 8811. Since he is going to the nets practice, he wants you to find out the maximum number. Can you help Kohli?

'''Input:

You are given an integer n.

Output:

You are required to find out the maximum number by changing at most 1
digit(either 1 or 8).


Sample Input 1:
1811

Sample Output 1:
8811

Explanation:
The answer is 8811 since 1881 and 1818 are smaller number compared to 8811. So, the answer is 8811.'''

n=int(input())
a=str(n)
b=[]
for i in a:
  b.append(i)
for i in range(len(b)):
  if b[i]=="1":
    b[i]="8"
    break
c="".join(b)
print(int(c))
