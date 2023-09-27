#!/usr/bin/env python3

#open file of interest
file = open("aligned.fna")

#read every other line in the fna file starting after the first header
sequences = repr(file.readlines()[1::2])


#close file to clear memory
file.close()

#print contents as a string to view whitespace
# print(repr(contents.split("\n")))
# sequences = contents.readlines()[1::2]
print(sequences)


#create a string variable for each sequence
#
#create an empty variable
#iterate across the sequences, when there's a nucletide match, print | to the empty seq, when there's no match print " "
#print 1 seq, then match string, then other seq



#asldkjlkj
x = 6
print(x)