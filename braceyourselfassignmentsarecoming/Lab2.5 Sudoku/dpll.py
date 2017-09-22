#symbols= len(V)*colors --> [1RGBY.., 2RGBY.., 3RGBY....]
def generate_clauses_graph(V, E, colors):
	C=[]
	
	for each in V:
		C.append([colors*each-c for c in reversed(range(colors))])

	for each in E:
		for c in range(colors):
			C.append([-(colors*each[0]-c),-(colors*each[1]-c)])
	return C
	
def update_model(_model, symb):
	model=dict(_model)
	if symb<0:
		model[-symb]=-1
	else:
		model[symb]=1
	return model	

def evaluate(clause, model):
	result=0
	for symb in clause:
		if abs(symb) in model and model[abs(symb)]*symb>0:
			return 1
		elif abs(symb) not in model:
			result=-1
	return result

def find_pure_symbs(C, S, M):
	pure_symbs=[]
	all_symbs=set([item for sublist in C for item in sublist])
	for symb in S:
		pos, neg= abs(symb) in all_symbs, -abs(symb) in all_symbs
		if (pos, neg) == (True, False):
			pure_symbs.append(abs(symb))
		elif (pos, neg) == (False, True):
			pure_symbs.append(-abs(symb))
	return pure_symbs
	
def find_unit_clauses(C, S, M):
	unit_list=[]
	for clause in C:
		in_model=[abs(symb) in M for symb in clause]
		if in_model.count(False)==1 and evaluate(clause, M)!=1:
			symb=clause[in_model.index(False)]
			if symb not in unit_list and -symb not in unit_list:
				unit_list.append(symb)
	return unit_list

hoals=0
	
def DPLL(C, S, M):
	global hoals
	print hoals
	hoals+=1
	
	sat_set=set([evaluate(clause, M) for clause in C])
	if len(sat_set)==1 and 1 in sat_set:
		return M
	elif 0 in sat_set and -1 not in sat_set:
		return None
	
	pure_symbs=find_pure_symbs(C, S, M)
	if len(pure_symbs)>0:
		for symb in pure_symbs:
			M=update_model(M, symb)
			S.remove(abs(symb))
		return DPLL(C, S, M)

	unit_clauses=find_unit_clauses(C, S, M)
	if len(unit_clauses)>0:
		for symb in unit_clauses:
			M=update_model(M, symb)
			S.remove(abs(symb))
		return DPLL(C, list(S), M)
	
	symb=S.pop(0)
	model= DPLL(C, list(S), update_model(M,-symb))
	if model != None:
		return model
	return DPLL(C, list(S), update_model(M, symb))




def parse_G():
	N, E=map(int, raw_input().split())
	nodes=list(range(1,N+1))
	edges=[]
	for line in range(E):
		e=map(int, raw_input().split())
		edges.append((e[0]+1, e[1]+1))
		
	return nodes, edges


nodes, edges= parse_G()

colors=9
C=generate_clauses_graph(nodes, edges, colors)
assignment= DPLL(C, range(1, len(nodes)*colors+1), {})
cmap=['R','B','G','LR','LB','LG','DR','DB','DG','Y','O','Pi','Pu']

for i in range(1,len(nodes)+1):
	
	slice=[assignment[j] for j in range(colors*(i-1)+1,colors*i+1)]
	#col=cmap[slice.index(1)]
	col=slice_index(1)+1
	print i, col

