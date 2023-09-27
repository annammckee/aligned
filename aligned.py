#!/usr/bin/env python3

#open file of interest
file = open("aligned.fna")

#read file contents into a variable
contents = file.read()

#close file to clear memory
file.close()

#print contents as a string to view whitespace
print(repr(contents.splint("\n")))


#create a string variable for each sequence
#
#create an empty variable
#iterate across the sequences, when there's a nucletide match, print | to the empty seq, when there's no match print " "
#print 1 seq, then match string, then other seq



#asldkjlkj
x = 6
print(x)