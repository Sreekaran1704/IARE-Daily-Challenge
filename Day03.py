#Phani gave you an integer n, he asked you tell the number of composite numbers that are strictly less than the value of n. For example if the value of n is 10, then the composite numbers strictly less than 10 are 4, 6, 8, 9. So the answer is 4.
'''Input:
You are given an integer n.

Output:
You have to print the number of composite numbers which are strictly less than the value of n.
'''


MAX_SIZE = 1000001
isprime = [True] * MAX_SIZE
prime = []
SPF = [None] * (MAX_SIZE)
count=0

def manipulated_seive(N):

	isprime[0] = isprime[1] = False

	for i in range(2, N):
	
		
		if isprime[i] == True:
			prime.append(i)
			SPF[i] = i
		j = 0
		while (j < len(prime) and
			i * prime[j] < N and
				prime[j] <= SPF[i]):
		
			isprime[i * prime[j]] = False
			SPF[i * prime[j]] = prime[j]
			
			j += 1
		
N=int(input())
manipulated_seive(N)
i=0
while i<len(prime) and prime[i]<=N:
  count+=1
  i+=1
 print(N-count-2)
