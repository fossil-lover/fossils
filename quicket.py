import random


bowling_deliveries = {'normal_delivery':6, 'caught1':1, 'caught2':1, 'caught3':1, 'run_out1':1, 'run_out2':1,
					  'run_out3':1, 'spin1':1, 'spin2':1, 'bye1':1, 'bye2':1, 'clean_bowled':1, 'no_ball':1}


# bowling_deliveries = {'normal delivery', 'normal delivery', 'normal delivery', 'normal delivery', 'normal delivery', 'normal delivery', 'caught', 'caught','caught',  'run out',  'run out',
# 					  'run out', 'spin', 'spin', 'bye1', 'bye2', 'clean bold','no ball'}

batting_deliveries = {'0':2,'1':4, '2':4, '3':4, '4':2, '6':2}

# batting_deliveries = {'0 run', '0 run', '1 run', '1 run', '1 run', '1 run', '2 run', '2 run', '2 run', '2 run', '3 runs', '3 runs',
# 					  '3 runs', '3 runs', '4 runs', '4 runs', '6 runs' '6 runs'}
players_score = 0

comp_score = 0

sides = ['batting', 'bowling']

coin_flip_chances = ["heads", "tails"]

players_choice = (input("Choose the side of the coin.")).strip()

coin_flip = random.choice(coin_flip_chances)

print(f"The coin landed on: {coin_flip}")

if coin_flip == players_choice:
	side_chosen_by_player = (input("you win the coin toss! Pick batting or bowling."))

else:
	comp_side_choice = random.choice(sides)
	print(f"you lost the toss. I pick: {comp_side_choice}")
	sides.remove(comp_side_choice)
	side_chosen_by_player = sides[0]
if side_chosen_by_player == 'batting':
	print("choose 6 options from this:")
	print(batting_deliveries)

	print("You will also need the bowling deliveries for the next innings. It is in this:")
	print(bowling_deliveries)

if side_chosen_by_player == 'bowling':
	print("choose 6 random options from this:")
	print(bowling_deliveries)

	print("You will also need the batting deliveries for the next innings. It is in this:")
	print(batting_deliveries)

total_score = 0

for s in range(2):
	bowling_deliveries_copy = bowling_deliveries.copy()
	batting_deliveries_copy = batting_deliveries.copy()
	for y in range(3):
		current_over_batting_deliveries = []
		current_over_bowling_deliveries = []
		if side_chosen_by_player == 'bowling':
			for x in range(6):
				remaining_bowling_deliveries = list(bowling_deliveries.keys())
			# current_ball_pick = random.choice(remaining_bowling_deliveries)
				while True:
					current_ball_pick = input("choose a card from the bowling deck.").strip()
					if current_ball_pick not in bowling_deliveries_copy:
						print("You have chosen the wrong ball. Please choose an available ball.")
						continue
					else:
						print(f"You chose {current_ball_pick}")
						break
				current_over_bowling_deliveries.append(current_ball_pick)
				bowling_deliveries_copy[current_ball_pick] = bowling_deliveries_copy[current_ball_pick] - 1
				if bowling_deliveries_copy[current_ball_pick] == 0:
					del bowling_deliveries_copy[current_ball_pick]
				print("Now the computer will choose a batting card.")
				remaining_batting_deliveries = list(batting_deliveries_copy.keys())
				current_bat_pick = random.choice(remaining_batting_deliveries)

				current_over_batting_deliveries.append(current_bat_pick)
				batting_deliveries_copy[current_bat_pick] = batting_deliveries_copy[current_bat_pick] - 1
				if batting_deliveries_copy[current_bat_pick] == 0:
					del batting_deliveries_copy[current_bat_pick]

		else:
			for x in range(6):
				remaining_batting_deliveries = list(batting_deliveries.keys())
				# current_bat_pick = random.choice(remaining_batting_deliveries)
				while True:
					current_bat_pick = input("choose a card from the batting deck.").strip()
					if current_bat_pick not in batting_deliveries_copy:
						print("You have chosen the wrong batting decision. Please choose an available one.")
						continue
					else:
						print(f"You chose {current_bat_pick}")
						break
				current_over_batting_deliveries.append(current_bat_pick)
				batting_deliveries_copy[current_bat_pick] = batting_deliveries_copy[current_bat_pick] - 1
				if batting_deliveries_copy[current_bat_pick] == 0:
					del batting_deliveries_copy[current_bat_pick]
				print("Now the computer will choose a bowling card.")
				remaining_bowling_deliveries = list(bowling_deliveries_copy.keys())
				current_ball_pick = random.choice(remaining_bowling_deliveries)

				current_over_bowling_deliveries.append(current_ball_pick)
				bowling_deliveries_copy[current_ball_pick] = bowling_deliveries_copy[current_ball_pick] - 1
				if bowling_deliveries_copy[current_ball_pick] == 0:
					del bowling_deliveries_copy[current_ball_pick]

		print(current_over_batting_deliveries)

		print(current_over_bowling_deliveries)

		current_over_score = 0

		for x in range(6):
			if current_over_bowling_deliveries[x] == 'no_ball':
				current_over_score = current_over_score + (int(current_over_batting_deliveries[x]) * 2) + 1

			if current_over_bowling_deliveries[x] == 'spin1':
				if int(current_over_batting_deliveries[x]) == 1 or int(current_over_batting_deliveries[x]) == 2:
					current_over_score = current_over_score
				else:
					current_over_score = current_over_score + int(current_over_batting_deliveries[x])

			if current_over_bowling_deliveries[x] == 'spin2':
				if int(current_over_batting_deliveries[x]) == 2 or int(current_over_batting_deliveries[x]) == 3:
					current_over_score = current_over_score
				else:
					current_over_score = current_over_score + int(current_over_batting_deliveries[x])

			if current_over_bowling_deliveries[x] == 'bye1':
				if int(current_over_batting_deliveries[x]) == 4:
					current_over_score = current_over_score + 4
				else:
					current_over_score = current_over_score

			if current_over_bowling_deliveries[x] == 'bye2':
				if int(current_over_batting_deliveries[x]) == 1:
					current_over_score = current_over_score + 1
				else:
					current_over_score = current_over_score

			if current_over_bowling_deliveries[x] == 'normal_delivery':
				current_over_score = current_over_score + int(current_over_batting_deliveries[x])

			if current_over_bowling_deliveries[x] == 'caught1':
				if int(current_over_batting_deliveries[x]) == 3 or int(current_over_batting_deliveries[x]) == 4:
					current_over_score = current_over_score
				else:
					current_over_score = current_over_score + int(current_over_batting_deliveries[x])

			if current_over_bowling_deliveries[x] == 'caught2':
				if int(current_over_batting_deliveries[x]) == 6 or int(current_over_batting_deliveries[x]) == 4:
					current_over_score = current_over_score
				else:
					current_over_score = current_over_score + int(current_over_batting_deliveries[x])

			if current_over_bowling_deliveries[x] == 'caught3':
				if int(current_over_batting_deliveries[x]) == 6 or int(current_over_batting_deliveries[x]) == 3:
					current_over_score = current_over_score
				else:
					current_over_score = current_over_score + int(current_over_batting_deliveries[x])

			if current_over_bowling_deliveries[x] == 'run_out1':
				if int(current_over_batting_deliveries[x]) == 1:
					current_over_score = current_over_score
				else:
					current_over_score = current_over_score + int(current_over_batting_deliveries[x])

			if current_over_bowling_deliveries[x] == 'run_out2':
				if int(current_over_batting_deliveries[x]) == 2 or int(current_over_batting_deliveries[x]) == 3:
					current_over_score = current_over_score
				else:
					current_over_score = current_over_score + int(current_over_batting_deliveries[x])

			if current_over_bowling_deliveries[x] == 'run_out3':
				if int(current_over_batting_deliveries[x]) == 2 or int(current_over_batting_deliveries[x]) == 1:
					current_over_score = current_over_score
				else:
					current_over_score = current_over_score + int(current_over_batting_deliveries[x])

		total_score = total_score + current_over_score
		if side_chosen_by_player == "batting":
			print(f"Player's score for this over is {current_over_score}.")
		else:
			print(f"My score for this over is {current_over_score}.")

		print(f"this is the end of over #{y + 1}")

	if side_chosen_by_player == "batting":
		players_score = total_score
		print(f"Player's final score for inning no {s+1} is {players_score}")
	else:
		comp_score = total_score
		print(f"My final score for inning no {s+1} is {comp_score}")

	if s != 1:
		print(" Now the second innings will start.")

		if side_chosen_by_player == "batting":
			side_chosen_by_player = 'bowling'
		else:
			side_chosen_by_player = "batting"

		print(side_chosen_by_player)

	total_score = 0
	current_over_score = 0

print(f"final score for the player is {players_score}")

print(f"final score for me is {comp_score}")

if comp_score > players_score:
	print(f"The computer won by {comp_score - players_score} runs.")
else:
	print(f"The player won by {players_score - comp_score} runs.")