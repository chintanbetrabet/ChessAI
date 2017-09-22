import networkx as nx
import matplotlib.pyplot as plt
import cPickle as pickle
import sys


args=sys.argv[1:]
fname=args[0]
state=map(int,args[1].split())
timeout=float(args[2])
save=int(args[3])

nxG=pickle.load(open('pickle_data/nxG_%s'%fname,'r'))
nxPos=pickle.load(open('pickle_data/nxPos_%s'%fname,'r'))

plt.clf()
nx.draw(nxG, nxPos, node_color=state)

if save:
	plt.savefig('result.png')
plt.pause(timeout)

