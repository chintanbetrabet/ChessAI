def connect_all(seq):
	edges=[]
	for i in range(len(seq)):
		for j in range(i+1, len(seq)):
			edges.append((seq[i],seq[j]))
	return edges

rows=[list(range(9*i, 9*(i+1))) for i in range(9)]

boxes=[[0,1,2,9,10,11,18,19,20],[3,4,5,12,13,14,21,22,23],[6,7,8,15,16,17,24,25,26],\
		[27,28,29,36,37,38,45,46,47],[30,31,32,39,40,41,48,49,50],[33,34,35,42,43,44,51,52,53],\
		[54,55,56,63,64,65,72,73,74],[57,58,59,66,67,68,75,76,77],[60,61,62,69,70,71,78,79,80]]

E=[]
for each_row in rows:
	E+=connect_all(each_row)
for each_col in map(list, zip(*rows)):
	E+=connect_all(each_col)
for each_box in boxes:
	E+=connect_all(each_box)
	
	
print 81, len(E)
for e in E:
	print ' '.join(map(str,list(e)))