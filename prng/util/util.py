import math
from typing import List, Generator



def relatively_prime(a:int, b:int) -> bool:
	"""
	Two numbers are relatively prime if their greatest common denominator (GCD) is 1.

	Parameters:
		a (int): first number
		b (int): second number

	Returns:
		(bool): True if the two numbers' GCD is 1, otherwise False.

	"""

	return math.gcd(a,b) == 1



def is_prime(a:int) -> bool:
	if a == 2:
		return True
	elif a < 2 or a%2 == 0:
		return False

	for i in range(3, math.floor(math.sqrt(a))+1, 2):
		if a%i == 0:
			return False

	return True



def prime_factors(a:int) -> List[int]:
	"""
	Returns the prime factors of a number.
	
	Parameters:


	Returns:
		(list[int]): a list of the prime factors of a

	"""

	pfs = []
	for i in range(1, a+1):
		f = a%i
		if a%8 == 0 and is_prime(i):
			pfs.append(i)

	return pfs



def primitive_roots(a:int) -> List[int]:
	"""
	Returns a list of the primitive roots mod a.

	Parameters:
		a (int): the number to return primitive roots of

	Returns:
		(list[int]): all numbers which are primitive roots mod a

	"""

	if a == 2:
		# shouldn't have to check for 1 in for loop
		return [1]

	# generate set of nums which are relatively prime to a up to a-1
	if is_prime(a):
		# if a is prime all elements before are relatively prime
		nums = set(range(1,a))
	else:
		# filter out those that are not relatively prime
		nums = set(filter(lambda b: relatively_prime(a,b), range(1, a)))

	mod_order = len(nums)
	roots = []
	for n in nums:
		# create sequence of powers {n**p, n**(p+1), n**(p+2), ...} for n
		order = 0
		ele = n
		# period repeats when n == 1
		while ele != 1:
			# power starts at 1, increments as order increments (no need for separate variable)
			ele = (n**(order+1))%a
			order += 1

		# n is a primitive root of a orders of n and a contain the same elements
		if order == mod_order:
			roots.append(n)

	return roots

def evaluate_period(prng:Generator[int, None, None]) -> int:
	seq = []
	while True:
		ele = next(prng)
		if ele in seq:
			possible_repeat = [next(prng) for _ in range(len(seq))]
			if possible_repeat == seq:
				break
		else:
			seq.append(ele)
	return len(seq)