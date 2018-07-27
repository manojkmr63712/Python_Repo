from constraint import *
from itertools import product

numbits = 2
numpos = 2

# this generates a list of all binary vectors of numbits bits
vecs = list(product(*(((1,0),)*numbits)))

problem = Problem()
# we will have numpos variables, i.e. one var for each code,
# each var is an index into vecs, has 2^numbits possible vals
problem.addVariables(list(range(numpos)), list(range(len(vecs))))

# vecs holds our binary vectors. 
# we want True if hamming distance between vecs[a] and vecs[b] is 1
# False otherwise. This will be our constraint. 
def hammingDist1(a,b):
    hamming = sum([vecs[a][i]^vecs[b][i] for i in range(numbits)])
    if hamming == 1: return True
    return False

# add the important constraints
for i in range(numpos):
    j = (i+1)%numpos
    problem.addConstraint(hammingDist1,[i,j])

# make sure all the vectors are different    
problem.addConstraint(AllDifferentConstraint())

# print out the first solution we come across
sol = problem.getSolution()
for i,j in enumerate(sol):
    print(vecs[sol[i]])
