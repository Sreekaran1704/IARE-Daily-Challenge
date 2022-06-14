#Eren and Zeke each have a string. They can swap their personalities to use eachothers powers to fight enemies. They can only swap personalities if the characters in one strings can be replced to get the exact same string as the others. All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself. Find if it is possible for Eren and Zeke to swap personalities.

'''Input:

Single line consisting of 2 space separated strings, one of Eren's and other of Zeke

Output:

Print "TRUE" if swap is possible, else print "FALSE"

Sample Input 1:
Ball Dogg

Sample Output 1:
TRUE'''

a,b=input().split()
c=list(set(a))
d=list(set(b))
l1=[]
l2=[]
for i in c:
  count1=a.count(i)
  l1.append(count1)
for i in d:
  count2=b.count(i)
  l2.append(count2)
l1.sort()
l2.sort()
if l1==l2:
  print("TRUE")
else:
  print("FALSE")
