from Map import rooms
from player import *
from items import *
from gameParser import *

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
		print('TAKE ' + items['id'].upper() + ' to take ' + items['name'] + '.')
	for items in inv_items:
		print('DROP ' + items['id'].upper() + ' to drop your ' + items['name'] + '.')    
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
	if item_id not in all_items:
		print("You cannot take that.")
	else:
		cur_item = all_items[item_id]
		if cur_item not in current_room['items']:
			print("You cannot take that.")
		else:
			if sum_carry_items_weight() + cur_item['mass'] > 3:
				print('You cannot carry more than 3KG, you are currently carrying ' + str(sum_carry_items_weight()) + 'KG')
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

#def execute_buy(item_id):
	#This 
	

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

	else:
		print("This makes no sense.")


def menu(exits, room_items, inv_items):
	# Display menu
	print_menu(exits, room_items, inv_items)

	# Read player's input
	user_input = input("> ")

	# Normalise the input
	normalised_user_input = normalise_input(user_input)

	return normalised_user_input


def move(exits, direction):
	#Thsi function shows the next room to go to
	return rooms[exits[direction]]


def main(rooms):

	# Main game loop
	print(
"""
THE BANK HEIST
"""
		)
	while True:
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