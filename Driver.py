#driver

#to-do: verify primes via gcd(pq, (p-1)(q-1)) = 1

import random

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
	
def encrypt(key, filename):
	'Encrypts a file based on Paillier encryption'
	#read file as string
	plainText = open(filename, "r+")
	r = random(1, n)
	#iv = Random.new().read(AES.block_size)
	#cipher = AES.new(getHash(key), AES.MODE_CBC, iv)
	cipher = g**plainText * r**n mod n**2
	plainText.write(cipher)

def decrypt(key, filename):
	'Decrypts a file based on Paillier encryption'
	cipherText = open(filename, "r+")
	#iv = cipherText[:AES.block_size]
	cipher = AES.new(getHash(key), AES.MODE_CBC, iv)
	plainText = cipher.decrypt(cipherText[AES.block_size:])
	filename.write(plainText)
	
def vote(voter): 
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
	return [input1, input2, input3]
	
#need to add encryption/decryption
def tallyVotes(ballots)
	'Takes a list of ballots and adds encrypted votes to get a total'
	n = #number of ballots
	b1 = 0
	b2 = 0
	b3 = 0
	#iterate through to count 1 votes
	for i in ballots:
		b1 += i[1]
		b2 += i[2]
		b3 += i[3]
	#calculate 0 votes
	a1 = n - total1
	a2 = n - total2
	a3 = n - total3
	
	#print results
	if(a1 > b1):
		print("citrus wins with " + string(a1) + " votes")
	else:
		print("berries wins with " + string(b1) + " votes")
	if(a2 > b2):
		print("pancakes wins with " + string(a2) + " votes")
	else:
		print("waffles wins with " + string(b2) + " votes")
	if(a3 > b3):
		print("syrup wins with " + string(a3) + " votes")
	else:
		print("jam wins with " + string(b3) + " votes")
		
		
	
	
#max times to check if prime
k = 5000
#limit for number range
n = 10000
#generate random prime numbers g and p
p = genPrime(n, k)
g = genPrime(n, k)

#where to generate p, q
voter1 = voter(self, p, q)
voter2 = voter(self,)
voter3 = voter(self, )
