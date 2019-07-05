# Unscrambled these words to find a word...?

# Write a function get_file_lines to create a Set of dictionary words.
def get_file_lines(filename='/usr/share/dict/words'):
    """Return a set from the given text file with
    any leading and trailing whitespace characters removed from each line."""
    with open(filename) as file:
        lines = [line.strip() for line in file]
    dict_set = set(lines)
    return dict_set

def all_perms(word):
	'''Given a string word, return a list of all its permuatations'''	
	if len(word) <=1:
		return word
	else:
		tmp = []
		for perm in all_perms(word[1:]):
			for i in range(len(word)):
				tmp.append(perm[:i] + word[0:1] + perm[i:])
		return tmp

def match_circles(unscramble_words, circles):
	'''Give a list of unscambled word strings, and a list of  _'s and O's,
	Go through each word, and find all the indeces of the O's, then
	store the characters of the word at those indeces in a final list
	which is what we return.'''

	# Set a counter and final_letters list
	_counter = 0
	final_letters = []
	# Go through each word
	for word in unscramble_words:
		# circles[counter] gives me the circle string at the matching index of the word in unscramble_words
		# Go through that string and at any character that is a O
		curr_idx_list = []
		# BROKEN: I don't know why this is breaking. 🥺
		for idx, char in enumerate(circles[_counter]):
			if char == 'O':
				# Store its index in a curr_idx_list of indexes
				curr_idx_list.append(idx)

		# For each index in temp_list
		for idx in curr_idx_list:
			# append word[index] to final_letters
			final_letters.append(word[idx])
		# update the counter and reset curr_idx_list
		_counter += 1
		curr_idx_list = []
	
	return final_letters

def unscramble_words():
	final_perm = ''
	scrambled_words = ['wya', 'helol', 'colo', 'amazngi']
	circles = ['____O', '_OO__', '_O___O', 'O____O']
	# final2 = ['OOOO', 'OOO']
	dict_set = get_file_lines()
	unscramble_words = []
	for word in scrambled_words:
		word = word.lower()
		curr_permutations = all_perms(word)
		for perm in curr_permutations:
			if perm in dict_set:
				unscramble_words.append(perm)

	final_letters = match_circles(unscramble_words, circles)

	final_letters = ''.join(final_letters)
	final_perms = all_perms(final_letters)
	for perm in final_perms:
		word = word.lower()
		if perm in dict_set:
			final_perm = perm
	
	return final_perm

print(unscramble_words())

# Pseudocode:
	# Write a function that takes in a string and iteratese through each permutation
	# and check if the word is in the set, if so, add it to our final words list

	# Then, lets call that function as we iterate through each string in a list so we return back a final list of words we need.

	# Then, compare each string in our final words to itscorrespoding circles string, and concatenate the letter at that position
	# to our final scramble word which we can finally unscramble.  
