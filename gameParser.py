import string

#Define a list of words not to remove from input
important_words = ["",""] # TODO



def filter_words(words):
	#This function removes the unimportant words from a string
	for item in words:
		if item not in important_words:
			words.remove(item)
			continue
		else:
			pass
	return words