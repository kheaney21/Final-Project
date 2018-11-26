import random
import sys

class Voter:
	'Class for voter object'

	def __init__(self, p, q):
		n = p * q
		self.privKeyResult = self.genPrivKey(p, q, n)
		self.privKey = [self.privKeyResult[0], self.privKeyResult[1]]
		self.pubKey = self.privKeyREsult
		

	def genPrivKey(self, p, q, n):
		'Generate private key via Paillier'
		lambda = lcm(p - 1, q - 1)
		g = random(1, n**2)
		l = ((g**lambda % n**2) - 1)/n
		mu = 1/l
		return [lambda, mu, g]
		
	
	def genPubKey(self, p, q, n):
		'Generate public key via Paillier'
		return [n , g]


	def genPrime(n, k):
		'Generate a prime number'

		x = random.randrange(51, n, 2)
		count = 0
		print("k " + str(k))
		while (not isPrime(x, k) and count < k):
			x = random.randrange(51, n, 2)
			count = count + 1
			#print(str(count) + " x " + str(x))
		print("final x " + str(x))
		print("count " + str(count))
		return x
			
	#check if prime via miller-rabin test
	def isPrime(n, k):
		'Check if prime via Miller-Rabin test'
		
		#calculate d
		temp = n
		s = 0
		while temp % 2 == 0:
			temp = temp/2
			s = s + 1
			
		d = n/(2**s)
		
		count = 0
		while count < k:
			#update counter
			count = count + 1
			#generate pseudorandom number
			a = random.randint(2, n - 1)
			x = a**d % n
			if (x == 1 or x == n - 1):
				continue
			for i in range (s-1):
				x = (x**2) % n
				if x == 1:
					return False
				if x == n - 1:
					continue
				
			return False
		return True

