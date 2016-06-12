"""This is a user controled program that analyzes the syntax of a regular SOV-Latin sentence including regular words from the first and second declination, and verbs in presence tense."""
# Adapt/change docstring

user_sentence = raw_input("Please type the sentence you want to analyze.")

def sentence():
	global user_sentence
	splitted_sentence = user_sentence.split()
	return splitted_sentence

#splitted_sentence = sentence()
#print splitted_sentence

print "Thank you. What would you like to do?"

des_pres_ind_pres_1_conj = {"1st pers. sg. ind. pres.":"o", "2nd pers. sg. ind. pres.":"as", "3rd pers. sg. ind. pres.":"at", "1st pers. pl. ind. pres.":"amus", "2nd pers. pl. ind. pres.":"atis", "3d pers. pl. ind. pres.":"ant"}
des_pres_ind_pres_2_conj = {"1st pers. sg. ind. pres.":"eo", "2nd pers. sg. ind. pres.":"es", "3rd pers. sg. ind. pres.":"et", "1st pers. pl. ind. pres.":"emus", "2nd pers. pl. ind. pres.":"etis", "3d pers. pl. ind. pres.":"ent"}
des_subst_first_decl = {"1st decl. nom. sg.":"a", "1st decl. acc. sg.":"am", "1st decl. nom. pl.":"ae", "1st decl. acc. sg.":"as"}
des_subst_second_decl = {"2nd decl. nom. sg.":"us", "2nd decl. acc. sg.":"um", "2nd decl. nom. pl.":"i", "2nd decl. acc. pl.":"os"}
des_subst_nominat = {"1a decl. nom. sg.":"a", "2a decl. nom. sg.":"us", "2a decl. nom. sg. -er":"er", "1a decl. nom. pl.":"ae", "2a decl. nom. pl.":"i"}
des_subst_genit_sg = {"1a decl":"ae", "2a decl":"i"}
des_subst_accusat_sg = {"1a decl":"am", "2a decl":"um"}

def find_verb():
	find_verb_1st_conj()
	find_verb_2nd_conj()	
print "There is no verb."

def find_verb_1st_conj():
	global des_pres_ind_1_conj
	splitted_sentence = sentence()
	for word in splitted_sentence:
		for ending in des_pres_ind_pres_1_conj.values():
			if word[-1] in des_pres_ind_pres_1_conj.values():
				ending = des_pres_ind_pres_1_conj.keys()[des_pres_ind_pres_1_conj.values().index(word[-1])] 
				print "The verb is %s. It is a %s." % (word, ending)
				return None
			elif word[-2:] in des_pres_ind_pres_1_conj.values():
				ending = des_pres_ind_pres_1_conj.keys()[des_pres_ind_pres_1_conj.values().index(word[-2:])] 
				print "The verb is %s. It is a %s." % (word, ending)
				return None
			elif word[-3:] in des_pres_ind_pres_1_conj.values():
				ending = des_pres_ind_pres_1_conj.keys()[des_pres_ind_pres_1_conj.values().index(word[-3:])] 
				print "The verb is %s. It is a %s." % (word, ending)
				return None
			elif word[-4:] in des_pres_ind_pres_1_conj.values():
				ending = des_pres_ind_pres_1_conj.keys()[des_pres_ind_pres_1_conj.values().index(word[-4:])] 
				print "The verb is %s. It is a %s." % (word, ending)
				return None

def find_verb_2nd_conj():
	global des_pres_ind_pres_2_conj
	splitted_sentence = sentence()
	for word in splitted_sentence:
		for ending in des_pres_ind_pres_2_conj.values():
			if 	word[-2:] in des_pres_ind_pres_2_conj.values():
				ending = des_pres_ind_pres_2_conj.keys()[des_pres_ind_pres_2_conj.values().index(word[-2:])] 
				print "The verb is %s. It is a %s." % (word, ending)
				return None
			elif word[-3:] in des_pres_ind_pres_2_conj.values():
				ending = des_pres_ind_pres_2_conj.keys()[des_pres_ind_pres_2_conj.values().index(word[-3:])] 
				print "The verb is %s. It is a %s." % (word, ending)
				return None
			elif word[-4:] in des_pres_ind_pres_2_conj.values():
				ending = des_pres_ind_pres_2_conj.keys()[des_pres_ind_pres_2_conj.values().index(word[-4:])] 
				print "The verb is %s. It is a %s." % (word, ending)
				return None

def find_subject():
	global des_subst_first_decl
	global des_subst_second_decl
	splitted_sentence = sentence()
	for word in splitted_sentence:
			if word[-1] == "a" or word[-1] == "i" or word[-2:] in des_subst_nominat.values():
				print "The subject is %s." % (word)
				return
			#elif: more subjects or no subject

def find_object():
	splitted_sentence = sentence()
	for word in splitted_sentence:
				if word[-2:] in des_subst_accusat_sg.values():
					print "The object is %s." % (word)
					return
				# else:
				#  	print "There is no object."
				# 	return

def analyze_word():
	word_to_analyze = raw_input("which word would you like to analyze?")
	if word_to_analyze[-1] == "a" or word_to_analyze[-2:] in des_subst_nominat_sg.values():
		print "%s is a noun. Nom. Sg." % (word_to_analyze)
	elif word_to_analyze[-2:] in des_subst_accusat_sg.values():
		print "%s is a noun. Acc. Sg." % (word_to_analyze)
	

def analyze_sentence():
	find_verb_var = find_verb()
	find_subject_var = find_subject()
	find_object_var = find_object()
	

def menu():
	print "1 - Find verb \n 2 - Find Subject \n 3 - Find Object \n 4 - Analyze word \n 5 - Analyze sentence \n 6 - Exit" 
	user_choice = int(raw_input("Please, type the number of your choice."))
	if user_choice == 1:
		find_verb()
	elif user_choice == 2:
		find_subject()
	elif user_choice == 3:
		find_object()
	elif user_choice == 4:
		analyze_word()
	elif user_choice == 5:
		analyze_sentence()
	else:
		 exit_analyzer()

menu()


# #def exit_analyzer():
# 	#pass

if __name__ == '__main__':
	sentence()