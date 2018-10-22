from Map import rooms
from player import *
from items import *
from gameparser import *

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



