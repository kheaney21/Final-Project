# Final-Project
Simple voting program using homomorphic encryption

Voter class:
  vote(): collects user input for 3 binary choices
  encrypt(p1, p2, p3): encrypts voting choices
  genPrime(): generates a prime number for key generation
  verifyPrimes(p, q): check if the greatest common denominator between p*q and (p-1)(q-1) is 1
  isPrime(n, k): probabilistically check if a number n is prime, with a maximum of k interations
  genKeys(): generate public and private key pair
  lcm(n1, n2): get least common multiple of n1 and n2
  mmi(g, mlambda): generate mu for private key
  
Driver class:
  poll(): command line prompt for new vote, tally, or quit
  tally(): adds encrypted votes, decrypts totals, and displays results


References
- http://www.cs.tau.ac.il/~fiat/crypt07/papers/Pai99pai.pdf
- https://eprint.iacr.org/2014/202.pdf

