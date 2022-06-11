#Sasha has started her own little café. She has very less visit of customers and wants to improve her standards to attract more people to visit her café. She has asked her regular customers to fill up a satisfactory feedack form consisting of binary values. The entire feebback is compressed into a single binary string. The feedback is considered to be positive if the binary string contains "010" or "101", else the feedback is negative.

'''Input:

First line represents the number of feedbacks received. The next N lines represent binary string

Output:

Print "Good" if the feedback is positive, else print "Bad"

Sample Input 1:
2
111011110
0000000000000

Sample Output 1:
Good
Bad'''

for i in range(int(input()):
  s=input()
  a=s.find("010")
  b=s.find("101")
  if a!=-1:
    print("Good")
  else:
    if b!=-1:
      print("Good")
    else:
      print("Bad")
