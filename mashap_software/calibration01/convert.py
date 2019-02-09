import re

def find_definition(variable, text):
	"""Return the equation of the searched variable."""
	pattern = r'^' + variable + r'\b\s*=.+$'
	return re.findall(pattern, text, re.M)[0]

def vars_in_eqn(eqn):
	"""Return variable names in an equation."""
	pattern = r'\b((?<!#)(?!\d+)\w+\b)(?!\()'
	return re.findall(pattern, eqn)

def convert(eqn, text):
	from config_hall_vensim_map import mappings
	eqns = []
	eqn_vars = vars_in_eqn(eqn)
#	import pdb
#	pdb.set_trace()

	for var in eqn_vars[1:]:
		if var not in mappings:
			new_eqn = find_definition(var, text)
			eqns.append(convert(new_eqn, text))
		else:
			eqn = eqn.replace(var, mappings[var],1)
	eqns.append(eqn)
	return flatten(eqns)

def flatten(L):
    if type(L) != type([]): return [L]
    if L == []: return L
    return flatten(L[0]) + flatten(L[1:])

def convert_constraints(constraints_file='in_constraints.txt', hallajp_file='hallajp.txt'):
	constraints = open(constraints_file).readlines()
	hallajp = open(hallajp_file).read()
	out_constraints = []
	for eqn in constraints:
		out_constraints.append(convert(eqn, hallajp))
	c = [x for x in flatten(out_constraints) if x not in locals()['_[1]']]
	open('out_constraints.txt','w').write('\n'.join(c))
	
if __name__ == '__main__':
	convert_constraints()