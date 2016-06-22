"""This is a user controlled program that analyzes the syntax of a regular SOV-Latin sentence including regular words from the first and second declension (only m. and f.), and verbs in presence tense (conj 1, 2, 4)."""

from ProjectHB_dictionaries import *

def sentence():
	"""Splits sentence word by word"""

	user_sentence = raw_input("Please type the sentence you want to analyze.")
	splitted_sentence = user_sentence.split()
	return splitted_sentence

#DEF VERB
def find_verb(splitted_sentence):
	"""Checks if there is a verb of any conj"""
	if find_verb_1st_conj_ind_pres(splitted_sentence) != True and find_verb_2nd_conj_ind_pres(splitted_sentence) != True and find_verb_4_conj_ind_pres(splitted_sentence) != True:
		print "There is no verb."
		return False

def find_verb_1st_conj_ind_pres(splitted_sentence):
	"""Checks if there is a verb of 1st conj"""
	global des_ind_pres_1_conj
	for word in splitted_sentence:
		if word[-1] in des_ind_pres_1_conj.values() and word[-2:] != "eo" and word[-2:] != "io":
			ending_definition = des_ind_pres_1_conj.keys()[des_ind_pres_1_conj.values().index(word[-1])] 
			print "The verb is %s. It is a %s, 1st conj." % (word, ending_definition)
			return True
		elif word[-2:] in des_ind_pres_1_conj.values():
			ending_definition = des_ind_pres_1_conj.keys()[des_ind_pres_1_conj.values().index(word[-2:])] 
			print "The verb is %s. It is a %s, 1st conj." % (word, ending_definition)
			return True
		elif word[-3:] in des_ind_pres_1_conj.values():
			ending_definition = des_ind_pres_1_conj.keys()[des_ind_pres_1_conj.values().index(word[-3:])] 
			print "The verb is %s. It is a %s, 1st conj." % (word, ending_definition)
			return True
		elif word[-4:] in des_ind_pres_1_conj.values():
			ending_definition = des_ind_pres_1_conj.keys()[des_ind_pres_1_conj.values().index(word[-4:])] 
			print "The verb is %s. It is a %s, 1st conj." % (word, ending_definition)
			return True

def find_verb_2nd_conj_ind_pres(splitted_sentence):
	"""Checks if there is a verb of 2st conj"""
	global des_ind_pres_2_conj
	for word in splitted_sentence:
		if 	word[-2:] in des_ind_pres_2_conj.values():
			ending_definition = des_ind_pres_2_conj.keys()[des_ind_pres_2_conj.values().index(word[-2:])] 
			print "The verb is %s. It is a %s." % (word, ending_definition)
			return True
		elif word[-3:] in des_ind_pres_2_conj.values():
			ending_definition = des_ind_pres_2_conj.keys()[des_ind_pres_2_conj.values().index(word[-3:])] 
			print "The verb is %s. It is a %s." % (word, ending_definition)
			return True
		elif word[-4:] in des_ind_pres_2_conj.values():
			ending_definition = des_ind_pres_2_conj.keys()[des_ind_pres_2_conj.values().index(word[-4:])] 
			print "The verb is %s. It is a %s." % (word, ending_definition)
			return True

def find_verb_4_conj_ind_pres(splitted_sentence):
	"""Checks if there is a verb of 4st conj"""
	global des_ind_pres_4_conj
	for word in splitted_sentence:
		if 	word[-2:] in des_ind_pres_4_conj.values():
			ending_definition = des_ind_pres_4_conj.keys()[des_ind_pres_4_conj.values().index(word[-2:])] 
			print "The verb is %s. It is a %s, 4th conj" % (word, ending_definition)
			return True
		elif word[-3:] in des_ind_pres_4_conj.values():
			ending_definition = des_ind_pres_4th_conj.keys()[des_ind_pres_4_conj.values().index(word[-3:])] 
			print "The verb is %s. It is a %s." % (word, ending_definition)
			return True
		elif word[-4:] in des_ind_pres_4_conj.values():
			ending_definition = des_ind_pres_4th_conj.keys()[des_ind_pres_4_conj.values().index(word[-4:])] 
			print "The verb is %s. It is a %s." % (word, ending_definition)
			return True	

#DEF SUBJECT
def find_verb_plural(splitted_sentence):
	"""Checks if there is any verb in pl"""
	for word in splitted_sentence:
		if word[-3:] == "mus" or word[-3] == "tis" or word[-2:] == "nt":
			pl_verb = word
			return pl_verb

def find_subject(splitted_sentence):
	global des_subst_first_decl
	global des_subst_second_decl
	idx = None

	if find_verb_plural(splitted_sentence) != None:
		for word in splitted_sentence:

			if word[-1] in des_subst_nominat_pl.values() or word[-2:] in des_subst_nominat_pl.values():
				subject1 = word
				idx = splitted_sentence.index(subject1)+1
				for possible_second_subject in splitted_sentence[idx:]:
					if possible_second_subject[-1] in des_subst_nominat_sg.values() or possible_second_subject[-2:] in des_subst_nominat_sg.values() or possible_second_subject[-1] in des_subst_nominat_pl.values() or possible_second_subject[-2:] in des_subst_nominat_pl.values():
						subject2 = possible_second_subject
						print "There are 2 subjects: %s and %s." % (subject1, subject2)
						return
			elif word[-1] in des_subst_nominat_sg.values() or word[-2:] in des_subst_nominat_sg.values():
				subject1 = word
				idx = splitted_sentence.index(subject1)+1
				for possible_second_subject in splitted_sentence[idx:]:
					if possible_second_subject[-1] in des_subst_nominat_sg.values() or possible_second_subject[-2:] in des_subst_nominat_sg.values() or possible_second_subject[-1] in des_subst_nominat_pl.values() or possible_second_subject[-2:] in des_subst_nominat_pl.values():
						subject2 = possible_second_subject
						print "There are 2 subjects: %s and %s." % (subject1, subject2)
						return True
			else: 
				print "Subject is %s" % (subject1)
				return
	
	
	elif find_verb_plural(splitted_sentence) == None:
		for word in splitted_sentence:
			if word[-1] in des_subst_nominat_sg.values() or word[-2:] in des_subst_nominat_sg.values():
				print "The subject is %s" % (word)
				return 
		
	print "There is no subject."
	return False

# Marcus Paulus amant Claudias: Claudias corrisponde alla desinenza di prima coniugazione presente per es amas

#DEF OBJECT
def find_object(splitted_sentence):
	for word in splitted_sentence:
		if word[-2:] in des_subst_accusat.values():
			print "The object is %s." % (word)
			return True
	print "There is no object."
	return False

# def analyze_word(word_to_analyze):
# 	word_to_analyze = raw_input("Please, type the word you want to analyze")
# 	if find_verb(word_to_analyze) != False:
# 		print "%s is a verb" % (word_to_analyze)
# 	elif find_subject(word_to_analyze) != False:
# 		print find_subject(word_to_analyze)
# 	elif find_object(word_to_analyze) != False:
# 		print find_object(word_to_analyze)


def analyze_sentence(splitted_sentence):
	find_verb(splitted_sentence)
	find_subject(splitted_sentence)
	find_object(splitted_sentence)

def exit_analyzer():
	print "Oh. Sorry you're leaving. Thank you for working with me. Come and visit again soon :-)"	

def menu():
	user_sentence = sentence()
	print "Thank you. What would you like to do? \n 1 - Find verb \n 2 - Find Subject \n 3 - Find Object \n 4 - Analyze word \n 5 - Analyze sentence \n 6 - Exit" 
	user_choice = int(raw_input("Please, type the number of your choice."))
	if user_choice == 1:
		find_verb(user_sentence)
	elif user_choice == 2:
		find_subject(user_sentence)
	elif user_choice == 3:
		find_object(user_sentence)
	elif user_choice == 4:
		analyze_word(user_sentence)
	elif user_choice == 5:
		analyze_sentence(user_sentence)
	elif user_choice == 6:
		exit_analyzer(user_sentence)


if __name__ == '__main__':
	menu()