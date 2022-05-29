#You are given a binary Stringss which consists of only 0’s and 1’s. Print “YES” if the number of 1’s in the Stringss are greater than or equal to the number of 0’s in the Stringss. Otherwise, print “NO”.

'''Input:

The first line of input consists of a single integer T, denoting the number of testcases.
Then, there are T lines, each of them contain a Stringss.


Output:

Output  T lines. Each of these lines contain “YES” if the number of occurrences of character ‘1’ in the Stringss is more than the occurrences of the character ‘0’. Else, output “NO”.

Sample Input 1:
3
100
0111000111100000001101100111000010100110111101011111001011100010011111111100100001111010101000001111
100
1010011100111011001000111001111100000001101100001010100111011001100010001101000001111010101000000101
100
0110000010101011000010000010110011000110000001000100111100111111000010011101110101111000110111101101

Sample Output 1:
YES
NO
NO

Explanation:
In the first test case, the number of occurences of ‘1’(54) >= number of occurences of ‘0’(46). So we print “YES”.
In rest all cases, we print “NO”.'''

for i in range(int(input()):
  n=int(input())
  s=input()
  l=list(s)
  a=l.count("0")
  b=l.count("1")
  if b>=a:
    print("YES")
  else:
    print("NO")
