"""This is a user controled program that analyzes the syntax of a regular SOV-Latin sentence including regular words from the first and second declination (only m. and f.), and verbs in presence tense."""

from dictionaries import *

def sentence():
	user_sentence = raw_input("Please type the sentence you want to analyze.")
	splitted_sentence = user_sentence.split()
	return splitted_sentence

def find_verb(splitted_sentence):
	if find_verb_1st_conj_ind_pres(splitted_sentence) != True and find_verb_2nd_conj_ind_pres(splitted_sentence) != True and find_verb_4_conj_ind_pres(splitted_sentence) != True:
		print "There is no verb."

def find_verb_1st_conj_ind_pres(splitted_sentence):
	global des_ind_pres_1_conj
	for word in splitted_sentence:
		if word[-1] in des_ind_pres_1_conj.values() and word[-2:] != "eo" and word[-2:] != "io":
			ending = des_ind_pres_1_conj.keys()[des_ind_pres_1_conj.values().index(word[-1])] 
			print "The verb is %s. It is a %s, 1st conj." % (word, ending)
			return True
		elif word[-2:] in des_ind_pres_1_conj.values():
			ending = des_ind_pres_1_conj.keys()[des_ind_pres_1_conj.values().index(word[-2:])] 
			print "The verb is %s. It is a %s, 1st conj." % (word, ending)
			return True
		elif word[-3:] in des_ind_pres_1_conj.values():
			ending = des_ind_pres_1_conj.keys()[des_ind_pres_1_conj.values().index(word[-3:])] 
			print "The verb is %s. It is a %s, 1st conj." % (word, ending)
			return True
		elif word[-4:] in des_ind_pres_1_conj.values():
			ending = des_ind_pres_1_conj.keys()[des_ind_pres_1_conj.values().index(word[-4:])] 
			print "The verb is %s. It is a %s, 1st conj." % (word, ending)
			return True

def find_verb_2nd_conj_ind_pres(splitted_sentence):
	global des_ind_pres_2_conj
	for word in splitted_sentence:
		if 	word[-2:] in des_ind_pres_2_conj.values():
			ending = des_ind_pres_2_conj.keys()[des_ind_pres_2_conj.values().index(word[-2:])] 
			print "The verb is %s. It is a %s." % (word, ending)
			return True
		elif word[-3:] in des_ind_pres_2_conj.values():
			ending = des_ind_pres_2_conj.keys()[des_ind_pres_2_conj.values().index(word[-3:])] 
			print "The verb is %s. It is a %s." % (word, ending)
			return True
		elif word[-4:] in des_ind_pres_2_conj.values():
			ending = des_ind_pres_2_conj.keys()[des_ind_pres_2_conj.values().index(word[-4:])] 
			print "The verb is %s. It is a %s." % (word, ending)
			return True

def find_verb_4_conj_ind_pres(splitted_sentence):
	global des_ind_pres_4_conj
	for word in splitted_sentence:
		if 	word[-2:] in des_ind_pres_4_conj.values():
			ending = des_ind_pres_4_conj.keys()[des_ind_pres_4_conj.values().index(word[-2:])] 
			print "The verb is %s. It is a %s, 4th conj" % (word, ending)
			return True
		elif word[-3:] in des_ind_pres_4_conj.values():
			ending = des_ind_pres_4th_conj.keys()[des_ind_pres_4_conj.values().index(word[-3:])] 
			print "The verb is %s. It is a %s." % (word, ending)
			return True
		elif word[-4:] in des_ind_pres_4_conj.values():
			ending = des_ind_pres_4th_conj.keys()[des_ind_pres_4_conj.values().index(word[-4:])] 
			print "The verb is %s. It is a %s." % (word, ending)
			return True	

def find_subject(splitted_sentence):
	global des_subst_first_decl
	global des_subst_second_decl
	for word in splitted_sentence:
		if word[-1] == "a" or word[-1] == "i" or word[-2:] in des_subst_nominat.values():
			print "The subject is %s." % (word)
			return
	print "There is no subject."
	return None

def find_object(splitted_sentence):
	for word in splitted_sentence:
		if word[-2:] in des_subst_accusat.values():
			print "The object is %s." % (word)
			return
	print "There is no object."
	return None

#def analyze_word():
	# if word_to_analyze[-1] == "a" or word_to_analyze[-2:] in des_subst_nominat_sg.values():
	# 	print "%s is a noun. Nom. Sg." % (word_to_analyze)
	# elif word_to_analyze[-2:] in des_subst_accusat_sg.values():
	# 	print "%s is a noun. Acc. Sg." % (word_to_analyze)
	# elif word_to_analyze[-2:] in des_pres_ind_1_conj.values():
	# 	print "%s is a verb. Pres. Ind." % (word_to_analyze)
	# #print more info, then use this to make other functions better, adding details

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