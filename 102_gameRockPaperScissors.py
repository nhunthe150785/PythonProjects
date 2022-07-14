from random import randint

while True:
	while True:
		player = input("Enter rock/paper/scissors: ")
		if player=='rock' or player=='paper' or player=='scissors':
			break
		print('Invalid input, try again !')
	computer = randint(0,2)

	if computer == 0:
		computer = 'rock'
	elif computer == 1:
		computer = 'paper'
	else:
		computer = 'scissors'

	print('-'*10)
	print('Your choice: ' + player)
	print('Computer chooses: ' + computer)
	print('-'*10)

	if player == computer:
		print("Draw")
	else:
		if player == 'rock':
			if computer == 'paper':
				print('You Lose')
			else:
				print('You Win')
		elif player == 'paper':
			if computer == 'rock':
				print('You Win')
			else:
				print('You Lose')
		else:
			if computer == 'rock':
				print("You Lose")
			else:
				print("You Win")
	ctn = ""
	while ctn not in ['no','yes']:			
		ctn = input("Do you want to continue?(yes/no): ")
		if ctn not in ['no','yes']:
			print("Invalid input, try again !")	
	if ctn == 'no':
		print("===> End game. Thank you so much !!!")
		break
	elif ctn == 'yes':
		continue

#Way 2:
'''
import random
you = ""
while you != "quit":
    you = input("Enter rock/paper/scissors/quit: ")
    pc = random.choice(["scissors", "rock", "paper"])
    
    if you == pc:
        print(f"you:{you}\npc:{pc}")
        print("Draw !")
    elif (you == "scissors" and pc == "rock") or (you == "rock" and pc == "paper") or (you == "paper" and pc == "scissors"):
        print(f"you:{you}\npc:{pc}")
        print("You lose !")
    elif (pc == "scissors" and you == "rock") or (pc == "rock" and you == "paper") or (pc == "paper" and you == "scissors"):
        print(f"you:{you}\npc:{pc}")
        print("You win !")
    elif you == "quit":
        print("===> End game. Thank you so much !!!")
    else:
        print("Invalid input, try again !")
'''
	