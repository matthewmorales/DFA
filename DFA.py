import random

# ">" corresponds to an input state, the following integers correspond to a transition based on 0, 1 input, the final number is just a State Number Used for recombining the table.
# "*" corresponds to a final state
t_table = {'q0' : [">", "q1", "q3", 0], 'q1' : ["i", "q2", "q4", 1], 'q2' : ["i", "q1", "q4", 2], 'q3' : ["i", "q2", "q4", 3], 'q4' : ["*", "q4", "q4", 4]}

def print_table(t_table):
	for item in t_table:
		if t_table.get(item)[0] == ">":
			print("%s %s : %s" % (t_table.get(item)[0], t_table.get(item)[1], t_table.get(item)[2]))
		elif t_table.get(item)[0] == "*":
			print("%s %s : %s" % (t_table.get(item)[0], t_table.get(item)[1], t_table.get(item)[2]))
		else:
			print("  %s : %s" % (t_table.get(item)[1], t_table.get(item)[2]))

print_table(t_table)

final = {}
non_final = {}
dfa_complete = {}

for items in t_table:
	if t_table.get(items)[0] == "*" :
		final[items] = t_table.get(items)
	else:
		non_final[items] = t_table.get(items)


def distinguishable(test_group, final):
	
	while test_group:
		#do while test_group is not empty
		test_a = {}
		sample_state = random.choice(test_group.keys()) #select a random state from the remaining non_final states
		test_a[sample_state] = test_group.pop(sample_state)
		poppable_states = []

		#compare Test Group A to test Group B, if Something in B indistinguishable from A, Pop off B. Remainder need to be Retested against a Random State from B.
		#Repeat until Test Group B is Empty.
		for item in test_a:
			for states in test_group:
				if test_a[item][1] == test_group[states][1] and test_a[item][2] == test_group[states][2]: 
					print "states are indistingquishable:"
					print test_a[item]
					print test_group[states]

					#states are indistingquishable. Replace all references to test_group state just tested. 
					poppable_states.append(states)
					for entry in test_group:
						if test_group.get(entry)[1] == states:
							test_group[entry][1] = item
							
						if test_group.get(entry)[2] == states:
							test_group[entry][2] = item
					
			#remove indistinguishable state from test group.
			for pops in poppable_states:
				print("Popping indistinguishable state: %s" % (pops))
				test_group.pop(pops)
		final[item] = test_a.pop(item)

	return final

dfa_min = distinguishable(non_final, final)







print_table(dfa_min)