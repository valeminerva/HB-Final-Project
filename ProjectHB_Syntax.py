"""This is a user controled program that analyzes the syntax of a regular SOV-Latin sentence including regular words from the first and second declination, and verbs in presence tense."""
# Adapt/change docstring

user_sentence = raw_input("Please type the sentence you want to analyze.")

def sentence():
	global user_sentence
	splitted_sentence = user_sentence.split()
	return splitted_sentence

splitted_sentence = sentence()
#print splitted_sentence

print "Thank you. What would you like to do?"

des_pres_ind_1_conj = {"1st pers. sg.":"o", "2nd pers. sg.":"as", "3d pers. sg.":"at", "1st pers. pl.":"amus", "2nd pers. pl.":"atis", "3d pers. pl.":"ant"}
des_subst_first_decl = {"1st decl. nom. sg.":"a", "1st decl. acc. sg.":"am", "1st decl. nom. pl.":"ae", "1st decl. acc. sg.":"as"}
des_subst_second_decl = {"2nd decl. nom. sg.":"us", "2nd decl. acc. sg.":"um", "2nd decl. nom. pl.":"i", "2nd decl. acc. pl.":"os"}

print des_pres_ind_1_conj.values()
print splitted_sentence

def find_verb():
	global des_pres_ind_1_conj
	splitted_sentence = sentence()
	for word in splitted_sentence:
		for ending in des_pres_ind_1_conj.values():
			if word[-2:] in des_pres_ind_1_conj.values():
				print "The verb is %s" % (word)
				return


def menu():
	print "1 - Find verb \n 2 - Find Subject \n 3 - Find Object \n 4 - Analyse word \n 5 - Analyse all \n 6 - Exit" 
	user_choice = int(raw_input("Please, type the number of your choice."))
	if user_choice == 1:
		find_verb()
	elif user_choice == 2:
		subject()
	elif user_choice == 3:
		object()
	elif user_choice == 4:
		word_to_analyse()
	elif user_choice == 5:
		analyse_sentence()
	else:
		 exit_analyzer()

menu()

# des_pres_ind = {"1st pers. sg.":"o", "2nd pers. sg.":"s", "3d pers. sg.":"t", "1st pers. pl.":"mus", "2nd pers. pl.":"tis", "3d pers. pl.":"nt"}
# des_subst_first_decl = {"1st decl. nom. sg.":"a", "1st decl. acc. sg.":"am", "1st decl. nom. pl.":"ae", "1st decl. acc. sg.":"as"}
# des_subst_second_decl = {"2nd decl. nom. sg.":"us", "2nd decl. acc. sg.":"um", "2nd decl. nom. pl.":"i", "2nd decl. acc. pl.":"os"}

# def find_verb():
# 	global des_pres_ind
# 	splitted_sentence = sentence()
# 	for word in splitted_sentence:
# 		for ending in des_pres_ind.values():
# 			if word[-2:] in des_pres_ind.values():
# 				print "The verb is %s", (word)
# 			else:
# 				print "Ohoh. In this sentence there is no verb."


# # #def subject():
# # 	#pass
# # 	# for che analizzi tutte le parole
# # 	# if / elif :
# # 	# se trova una parola che corrisponde
# # 	# se trova soggetto singolare: continua a cercare: forse due soggetti!
# # 	# se no il soggetto e implicito o il verbo e impersonale

# def object():
# 	global splitted_sentence
# 	for word in splitted_sentence:
# 		for ending in des_subst_first_decl:
# 			for ending in des_subst_second_decl:
# 				if word[-2:] in des_subst_first_decl or des_subst_second_decl:
# 					print "Object is %s", (word)
# 				else:
# 					print "Ohoh. In this sentence there is no object."

# object()

# #def word_to_analyze():
# 	#word_to_anayse = raw_input("What word do you want me to analyse for you?")

# #def analyse_sentence():
# 	#verb()
# 	#subject()
# 	#object()

# #def exit_analyzer():
# 	#pass

if __name__ == '__main__':
	sentence()