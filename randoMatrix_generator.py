# This script produces random matrices by repeatedly subsampling from a larger dataset

import os
from random import seed
from random import randint

matrix  = open("conserved_paralogs.txt", "r").readlines()
m = []
for line in matrix : m.append(line.strip())

replicates = 100
size = 61
outPath = "./sampleMatrices/"

if not os.path.exists(outPath):
	os.system("mkdir " + outPath)
else:
	print "This path exists: " + outPath
	quit()

for x in range(1,replicates + 1):
	new_m = open(outPath + str(x) + ".csv", "a")
	nm = []
	for n in m: nm.append(n)
	
	process = 0
	for process in range(1, size):		
		print "process " + str(process)
#		seed(1)
		index = randint(0,(len(nm) - 1))
		print "index: %s" % index
		print "len(nm): %s" % len(nm)
		print "len(m): %s" % len(m)
		chosen = nm.pop(index)
		new_m.write("%s\n" % chosen)
		
	new_m.close()