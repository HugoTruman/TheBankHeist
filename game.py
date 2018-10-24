from Map import *
from items import *
#from items_entry import *
from player import *
from gameParser import *
from Endings import *
import os
def list_of_items(items):
	#Function to print a list of items as a string from a list
	list_of_items = []
	for x in items:
		list_of_items.append(x['name'])
	return ', '.join(list_of_items)

def print_room_items(room):
	#Function to print all the items in a room using the list_of_items function
	if room['items'] == []:
		return
	else:
		print('There is ' + list_of_items(room['items']) + ' here.')
		print()

def print_inventory_items(items):
	#Function to print all the items the player has in their inventory
	if items == []:
		print('You have nothing, pity really. Go and get some stuff.')
		print()
	else:
		print('You have ' + list_of_items(items) + '.')
		print()

def print_room(room):
	#Function to print the description and items of a room
	print()
	print(room["name"].upper())
	print()
	print(room["description"])
	print()
	print_room_items(room)

def exit_leads_to(exits, direction):
	#This function prints all the exits from one room 
	return rooms[exits[direction]]["name"]

def print_exit(direction, leads_to):
	#This function prints a line for the print_menu function 
	print("GO " + direction.upper() + " to " + leads_to + ".")

def print_menu(exits, room_items, inv_items):
	#This displays a menu of availible things to do in each room
	print("You can:")
	for direction in exits:
		print_exit(direction, exit_leads_to(exits, direction))
	for items in room_items:
		if items['value'] > 0:
			print('BUY ' + items['id'].upper() + ' to purchase ' + items['name'] + ' for $' + str(items['value'])+'.')
		else:
			print('TAKE ' + items['id'].upper() + ' to take ' + items['name'] + '.')
	for items in inv_items:
		print('DROP ' + items['id'].upper() + ' to drop your ' + items['name'] + '.')
	for items in inv_items:
		if items in current_room['uses']:
			print('USE ' + items['id'].upper() + ' to use ' + items['name'] + '.')  
	print("What do you want to do?")

def is_valid_exit(exits, chosen_exit):
	#This function checks if the exit chosen is valid
	return chosen_exit in exits

def sum_carry_items_weight():
	#This function sums up the amount of weight the user is carrying
	total = 0
	for x in inventory:
		total += x['mass']
	return total

def merge_two_dicts(dict1, dict2):
	#This function merges two dictionairys together
    new_dict = dict1.copy()   
    new_dict.update(dict2)    
    return new_dict

def execute_use(item_id):
	#This function executes a use command on an item
	global current_room
	global discrete
	if all_items[item_id] in current_room['uses'] and all_items[item_id] in inventory:
		if all_items[item_id]['type'] == 'entry':
			print (all_items[item_id]['use'])
			discrete += all_items[item_id]['discrete']
			current_room['description'] = current_room['new description']
			current_room['exits'] = merge_two_dicts(current_room['exits'],current_room['locked exits'])
		elif all_items[item_id]['type'] == 'clothes':
			print (all_items[item_id]['use'])
			discrete += all_items[item_id]['discrete']
			inventory.remove(all_items[item_id])




def execute_go(direction):
	#This function executes a move to another room
	global current_room
	if is_valid_exit(current_room['exits'], direction) == True:
		new_room = current_room['exits'][direction]
		current_room = rooms[new_room]
		print(current_room['name'])
	else:
		print('You cannot go there')


def execute_take(item_id):
	#This function executes a take command to pick up an item.
	global current_room
	global discrete
	if item_id not in all_items:
		print("You cannot take that.")
	else:
		cur_item = all_items[item_id]
		if cur_item not in current_room['items']:
			print("You cannot take that.")
		else:
			if cur_item['value'] > 0 :
				print("You have to buy that, criminal!")
			else:
				if sum_carry_items_weight() + cur_item['mass'] > 10:
					print(
						'''You cannot carry more than 10KG by yourself, consider buying a bag or something. If you already have one, ease up on the buying stuff,
						your robbing a bank not going on holiday, Jesus!
						'''
						)
				else:
					inventory.append(cur_item)
					current_room['items'].remove(cur_item)
					print()
					print('You picked up ' + cur_item['name'])
					print()
					print('ITEM DESCRIPTION: ' + cur_item['description'])
					print()
					print('ITEM MASS:  '+ str(cur_item['mass']))
					print()
					discrete += cur_item['discrete']

	

def execute_drop(item_id):
	#This function allows the user to drop items in the room they are in.
	global current_room
	if item_id not in all_items:
		print('You cannot drop that.')
	else:
		cur_item = all_items[item_id]
		if cur_item not in inventory:
			print("You cannot drop that.")
		else:
			current_room['items'].append(cur_item)
			inventory.remove(cur_item)


def execute_buy(item_id):
	#This 
	global current_room
	global money
	if item_id not in all_items:
		print("You cannot buy that.")
	else:
		cur_item = all_items[item_id]
		if cur_item not in current_room["items"]:
			print("You cannot take that")
		else:
			if sum_carry_items_weight() + cur_item['mass'] > 10:
					print(
						'''You cannot carry more than 10KG by yourself, consider buying a bag or something. If you already have one, ease up on the buying stuff,
						your robbing a bank not going on holiday, Jesus!
						'''
						)
			else:
				if cur_item["value"] > money:
					print("You cannot afford that, it costs $" + str(cur_item["value"]))
				else:
					inventory.append(cur_item)
					current_room["items"].remove(cur_item)
					print("\nYou bought " + cur_item["name"] + "for $" + str(cur_item["value"]))
					money = money - cur_item["value"]
					print('ITEM DESCRIPTION: ' + cur_item['description'])
					print()
					print('ITEM MASS:  '+ str(cur_item['mass']))
					print()
					print("You have $" + str(money) + "left.")
					print()


def execute_command(command):
	#This function decides what the user wants to do
	if 0 == len(command):
		return
	if command[0] == "go":
		if len(command) > 1:
			execute_go(command[1])
		else:
			print("Go where?")

	elif command[0] == "take":
		if len(command) > 1:
			execute_take(command[1])
		else:
			print("Take what?")

	elif command[0] == "drop":
		if len(command) > 1:
			execute_drop(command[1])
		else:
			print("Drop what?")
	elif command[0] == "buy":
		if len(command) > 1:
			execute_buy(command[1])
		else:
			print("Buy what?")
	elif command[0] == "use":
		if len(command) > 1:
			execute_use(command[1])
		else:
			print("Use what?")

	else:
		print("This makes no sense.")


def menu(exits, room_items, inv_items):
	# Display menu
	print_menu(exits, room_items, inv_items)

	# Read player's input
	user_input = input("> ")

	# Normalise the input
	normalised_user_input = normalise_input(user_input)
	print(normalised_user_input)
	return normalised_user_input


def move(exits, direction):
	#Thsi function shows the next room to go to
	return rooms[exits[direction]]

def workout_winnings():
	global inventory
	total_mass = sum_carry_items_weight()
	total_mass = -total_mass
	total_mass += 10
	grams_converted = total_mass * 1000
	return grams_converted

def main(rooms):
	global discrete
	global inventory
	lethal = [item_pistol, item_shotgun, item_smg, item_rpg]

	# Main game loop
	os.system('cls')
	print("""
					=========================================================================================================================                                                                                                                     
					__________ ___                      ________                     ___             ____    ____                            
					MMMMMMMMMM `MM                      `MMMMMMMb.                   `MM             `MM'    `MM'        68b                 
					    MM      MM                       MM    `Mb                    MM              MM      MM         Y89                
					    MM      MM  __     ____          MM     MM    ___   ___  __   MM   __         MM      MM   ____  ___   ____   M     
					    MM      MM 6MMb   6MMMMb         MM    .M9  6MMMMb  `MM 6MMb  MM   d'         MM      MM  6MMMMb `MM  6MMMMb  MMMMM  
					    MM      MMM9 `Mb 6M'  `Mb        MMMMMMM(  8M'  `Mb  MMM9 `Mb MM  d'          MMMMMMMMMM 6M'  `Mb MM MM'    ` MM     
					    MM      MM'   MM MM    MM        MM    `Mb     ,oMM  MM'   MM MM d'           MM      MM MM    MM MM YM.      MM     
					    MM      MM    MM MMMMMMMM        MM     MM ,6MM9'MM  MM    MM MMdM.           MM      MM MMMMMMMM MM  YMMMMb  MM     
					    MM      MM    MM MM              MM     MM MM'   MM  MM    MM MMPYM.          MM      MM MM       MM      `Mb MM     
					    MM      MM    MM YM    d9        MM    .M9 MM.  ,MM  MM    MM MM  YM.         MM      MM YM    d9 MM L    ,MM YM.  , 
					   _MM_    _MM_  _MM_ YMMMM9        _MMMMMMM9' `YMMM9'Yb_MM_  _MM_MM_  YM._      _MM_    _MM_ YMMMM9 _MM_MYMMMM9   YMMM9 
					                                                                                                                         
					=========================================================================================================================
		""")
	print("""
	    _      ___                  _           _____                 ___ _ 
	   /_\    / __|__ _ _ __  ___  | |__ _  _  |_   _|__ __ _ _ __   |_  ) |
	  / _ \  | (_ / _` | '  \/ -_) | '_ \ || |   | |/ -_) _` | '  \   / /| |
	 /_/ \_\  \___\__,_|_|_|_\___| |_.__/\_, |   |_|\___\__,_|_|_|_| /___|_|
	                                     |__/                                                                                  
		""")
	print("\nYou are a Student that is in debt to your student loan, you are sturrguling to make ends meet.")
	print("\nYou decided to turn to your last resort. To Rob a bank to pay abck your loan.")
	print("\nYour mission, if you choose to accept it, is to rob the East Hollywood Financial Center.")

	while True:
		if discrete > 50:
			for items in inventory:
				if items in lethal:
					print(end_shot['name'].upper())
					print()
					print(end_shot['description'])
					exit()
			print(end_caught['name'].upper())
			print()
			print(end_caught['description'])
			exit()
		elif all_items['money'] in inventory and current_room == rooms['Van']:
			if discrete > 20:
				print(end_arrested['name'].upper())
				print()
				print(end_arrested['description'])
				exit()
			print(end_get_away_cash['name'].upper())
			print()
			print(end_get_away_cash['description'])
			print()
			print('You succesfully got away with $' + str(workout_winnings()) + ', well done!')
			exit()
		else:
			# Display game status (room description, inventory etc.)
			print_room(current_room)
			print_inventory_items(inventory)

			# Show the menu with possible actions and ask the player
			command = menu(current_room["exits"], current_room["items"], inventory)
			execute_command(command)



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
	main(rooms)
