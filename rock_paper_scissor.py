import os
import sys
import random
import time
import platform

operating_sys = platform.system()
os.system("clear")

wins = 0
losses = 0
draws = 0

msg = ("Want to play Rock, Paper, Scissors ? (y/n)")

if operating_sys == ("Darwin"):

	while True:
		print("Wins:")
		print(wins)
		print("")

		print("Losses:")
		print(losses)
		print("")

		print("Draws:")
		print(draws)
		print("")

		print(msg)

		ans = raw_input(">> ")
		if ans == ("y"):
			print("what do u choose")
			print("Rock(r), Paper(p) or Scissors(s)")

			choice = raw_input(">> ")

			opponent = random.randint(1,3)

			# rock
			if opponent == 1:
				op_choice = ("r")

				if choice == ("r"):
					print("Draw....")
					draws = draws + 1
					time.sleep(1)

				
				if choice == ("p"):
					print("You Win...")
					wins = wins + 1
					time.sleep(1)


				
				if choice == ("s"):
					print("You Lose...")
					losses = losses + 1
					time.sleep(1)


			

			# paper

			if opponent == 2:
				op_choice = ("p")

				if choice == ("p"):
					print("You lose....")
					losses = losses + 1
					time.sleep(1)

				
				if choice == ("p"):
					print("Draw...")
					draws = draws + 1
					time.sleep(1)


				
				if choice == ("s"):
					print("You Win...")
					wins = wins + 1
					time.sleep(1)


			
			# scissor



			if opponent == 3:
				op_choice = ("s")

				if choice == ("r"):
					print("You Win....")
					wins = wins + 1
					time.sleep(1)

				
				if choice == ("p"):
					print("You lose...")
					losses = losses + 1
					time.sleep(1)


				
				if choice == ("s"):
					print("Draw...")
					draws = draws + 1
					time.sleep(1)

			

		msg = ("Want to play again ?? (y/n)")			
		
	



	

				





