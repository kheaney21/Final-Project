import sys
from voter import voter

class election:
	'Driver for a simple questionnaire'
	
	def __init__(self):
		#list of voters
		self.electorate = []
	
		#ballot for q1
		self.b0 = []
		#ballot for q2
		self.b1 = []
		#ballot for q3
		self.b2 = []
	
	def poll():
		'Prompt user for new votes or to tally'
		input = ("v - new vote, t - tally, q - quit")
		
		while(input != q):
			#check for valid input
			if(input == v):
				#new vote
				print("new vote \n")
				voter = voter()
				electorate.append(voter)
				#returns encrypted ballot
				temp = voter.vote()
				b0.append(temp[0])
				b1.append(temp[1])
				b2.append(temp[2])
			elif(input == t):
				#tally
				print("tally \n")
				self.tally()
			elif(input == q):
				print("exit \n")
				break

	
	def tally():
		'Count votes cast'
		#b1 is false if empty
		if(not b1):
			print("no votes cast")
		total0 = 0
		for i in b0:
			total0 = total0 + b0[i]
		total1 = 0
		for i in b1:
			total1 = total1 + b1[i]
		total2 = 0
		for i in b2:
			total2 = total2 + b2[i]
		
		#citrus vs berries
		if (total0 > len(b0)):
			print("berries has the most votes")
		elif(total0 < len(b0)):
			print("citrus has the most votes")
		else: #tie
			print("tie")
		print("results: citrus " + string(len(b0) - total0) + " berries " + string(total0))
		
		#pancakes vs waffles
		if (total0 > len(b0)):
			print("waffles has the most votes")
		elif(total0 < len(b0)):
			print("pancakes has the most votes")
		else: #tie
			print("tie")
		print("results: pancakes " + string(len(b1) - total1) + " waffles " + string(total0))
		
		#syrup vs jam
		if (total0 > len(b0)):
			print("jam has the most votes")
		elif(total0 < len(b0)):
			print("syrup has the most votes")
		else: #tie
			print("tie")
		print("results: syrup " + string(len(b2) - total2) + " jam " + string(total2))
		
