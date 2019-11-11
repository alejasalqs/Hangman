import random
import os

lost_chances = 0
found_letters = []
victory = False

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

selected_word = words[random.randrange(len(words))]
print(HANGMANPICS[lost_chances])


def load_screen():
	clear = lambda: os.system('clear')
	print(HANGMANPICS[lost_chances])


def find_word(word):
	matches = 0
	global selected_word
	for letter in selected_word:
		if word == letter:
			selected_word = selected_word.replace(word,'',1)
			found_letters.append(word)
			matches += 1
	return matches


def verify_if_win():
	if 0 == len(selected_word):
		print("You won the game!")
		return True
	else:	
		return False


def verify_if_loose():
	if 6 == lost_chances:
		print("You loose the game, try again later!")
		return True
	else:	
		return False


while lost_chances != 6:
	result = find_word(str(raw_input("Try to guess the word, type a letter: ")))
	if result > 0:
		won_chances = result
		if verify_if_win():
			break
		load_screen()
	else:
		print("You loose a chance")
		lost_chances += 1
		if verify_if_loose():
			break
		load_screen()