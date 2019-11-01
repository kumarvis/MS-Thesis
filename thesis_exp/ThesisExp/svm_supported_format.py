
import sys
import csv
from collections import defaultdict

def construct_line( label, line ):
	new_line = []
	if float( label ) == 0.0:
		label = "0"
	new_line.append( label )

	for i, item in enumerate( line ):
		if item == '' or float( item ) == 0.0:
			continue
		new_item = "%s:%s" % ( i , item )
		new_line.append( new_item )
	new_line = " ".join( new_line )
	new_line += "\n"
	return new_line

def construct_svm_line(line):
    svm_line = []
    lbl = line[0]
    svm_line.append(lbl)
    for ii in range(1, len(line)):
        print(ii)
        new_item = "%s:%s" % (ii, line[ii])
        svm_line.append(new_item)

    svm_line = " ".join(svm_line)
    svm_line += "\n"
    return svm_line

input_file = 'data_gen_svm.csv'
output_file = 'data_gen_svm.txt'

label_index = 0
i = open( input_file, 'r' )
o = open( output_file, 'w')
reader = csv.reader(i)

for line in reader:
    new_line = construct_svm_line(line)
    o.write(new_line)

print('exit')

