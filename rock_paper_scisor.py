import random
print("**Rock⛰️-Paper📃-Scissor✂️**")
print('Developed By Shreyansh Shukla ©2020')
print()
print('Player VS Computer')
print()
comp = random.randint(1,3)

print('Press 1 for Paper📃')
print('Press 2 for Rock⛰️')
print('Press 3 for Scissor ✂️')
print('Computer turn')

man = int(input('Player turn: '))
if(man==1 and comp==2) :
	print('Computer choosed Water')
	print('Computer Wins')
elif(man==2 and comp ==3):
	print('Computer chose Scissors')
	print('You Won')
	
elif(man==3 and comp==1):
	print('Computer chose paper')
	print('You won')
	
elif(man==3 and comp==2):
	print('Computer chose rock')
	print('Computer wins')
	
elif(man==2 and comp==1):
	print('Computer chose paper')
	print('You won')
	
#choice are same
elif(man==1 and comp==1):
	print('Computer chose Paper')
	print('Tie')
	
elif(man==2 and comp==2):
	print('Computer chose Rock')
	print('Tie')
	
elif(man==3 and comp==3):
	print('Computer chose Scissors')
	print('Tie')