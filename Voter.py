import random
import math
import sys
from Crypto.Hash import SHA256

class voter:
	'Class for voter object'
	
	def __init__(self):
		keyPair = genKeys()
		#n, g
		self.pubKey = (keyPair[0], keyPair[1])
		#lambda, mu
		self.privKey = (keyPair[3], keyPair[4])
		
	def getPubKey(self):
		return pubKey	
	
	def vote():
		'Collects votes from user input'
		input1 = ("0 - citrus, 1 - berries")
		while(input1 != 0 AND input1 =! 1):
			input1 = ("Invalid input; 0 - citrus, 1 - berries")
		input2 = ("0 - pancakes, 1 - waffles")
		while(input2 != 0 AND input2 =! 1):
			input2 = ("Invalid input; 0 - pancakes, 1 - waffles")
		input3 = ("0 - syrup, 1 - jam")
		while(input3 != 0 AND input3 =! 1):
			input3 = ("Invalid input; 0 - syrup, 1 - jam")
		return encrypt(input1, input2, input3)
	
	def encrypt(p1, p2, p3):
		'Encrypt ballot answers'
		
		#get n from public key
		n = self.pubKey[0]
		
		#get g from public key
		g = self.pubKey[1]
		
		#generate pseudo random r
		r = random.(1, n)
		
		#hash votes
		m1 = 
		m2 =
		m3 =
		
		#verify gcd(r, n) = 1
		count = 0
		k = 10,000
		while(count <= k):
			if(math.gcd(r, n) == 1):
				print("gcd(r, n) = 1 verified")
				break
			#try new number
			r = random.(1, n)
			#update counter
			count = count + 1
		# new r?
		c1 = g**m * r**n % n**2
		c2 = 
		c3 = 
		
		return[c1, c2, c3]
		
		

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
		
	def verifyPrimes(p, q):
		'Check if p & q are prime via greatest common denominator'
		count = 0
		if(math.gcd(p*q, (p-1)(q-1)) == 1):
			print("gcd test = true")
			return True
		else:
			print("gcd test = false")
			return False
			
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
		while (count < k):
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
	
	def genKeys():
		#max number for prime generation
		max = 100,000
		#max number of iterations
		k = 10,000
		p = genPrime(max, k)
		q = genPrime(max, k)
		
		cont = True
		count = 0
		while (cont = True AND count < k):
			if (verifyPrimes(p, q) == True):
				print("keys generated")
				cont = False
			#update counter
			count = count + 1
		if(cont == False):
			#if count exceeds k, then notify user and return hard coded primes in the interest of time
			print("Hard coded values used")
			p = 102181
			q = 104717
		n = p*q
		#least common multiple
		mlambda = lcm (p-1, q-1)
		#generate random number g
		g = random(1, n**2)
		mu = mmi(g, mlambda, k)
		return (n, g, mlambda, mu)
		
	def lcm(n1, n2):
		'method to get lcm of two numbers'
		gcd = math.gcd(n1, n2)
		lcm = (n1 * n2)/gcd
		return lcm
		
	def mmi(g, mlambda):
		'method to calculate modular multiplicative inverse'
		mu = (n/((g**mlambda % n**2) - 1)) % n
		return mu

		
