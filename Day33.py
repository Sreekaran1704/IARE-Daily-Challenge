#Hardik Pandya gave you a number. He wants you to find the complement of that number. A complement of a number is the number you get if you flip its bits(1 to 0 and 0 to 1) in its binary representation. Since he is on his way to Hyderabad for his IPL Match, he asked you to tell the answer after the match. Suppose if the number if 5, its binary representation is “101”, then its complement would be 2(“010”). So, your answer is 2. Can you help Hardik?

'''Input:

You are given an integer N.

Output:

Return the complement of the given input number

Sample Input 1:
5

Sample Output 1:
2

Explanation:
The number if 5, its binary representation is “101”, then its complement would be 2(“010”).'''

def bn(x):
    return int(x,2)
n=int(input())
a=bin(n)
s=a[2:]
b=list(s)
for i in range(len(b)):
    if b[i]=="0":
        b[i]="1"
    elif b[i]=="1":
        b[i]="0"
c="".join(b)
print(bn(c))
