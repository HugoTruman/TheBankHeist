import string

#Define a list of words not to remove from input
important_words = ["go","take","buy", "use"
				"north","east","south","west",
				"rpg","id","password","money","tape","pistol","shotgun","grenade","smoke bomb", "smg",
				"kirill mask", "clown mask", "boiler suit", "ghost buster suit", "back pack", "sports bag",
				"fake gun", "twizzler", "C4", "cartoon bomb", "sparkler", "drill", "white overalls", "axe", "stethoscopes"
				]

def filter_words(words):
	#This function removes the unimportant words from a string

	useful_words = []
	for item in words:
		if item in important_words:
			useful_words.append(item)
	return useful_words


def remove_punct(text):
	#This function removes punctuation from a given string
	no_punct = ""

	for char in text:
		if not (char in string.punctuation):
			no_punct += char
	return no_punct

def normalise_input(user_input):
	#Returns a list of strings which are suitable to be understood by the game
	no_punct = remove_punct(user_input).lower()
	split_input = no_punct.split()

	filtered = filter_words(split_input)
	return filtered

#print(normalise_input("I want to GO towards the south Exit!!!!")) TEST for normalise input func
#test means other functions work also
