#!/usr/bin/env python3

#open file of interest
file = open("aligned.fna")

#read every other line in the fna file starting after the first header -> returns a list
fin = file.readlines()[1::2]

#close file to clear memory
file.close()

#create an empty list, populate the list with sequences with newline stripped from the ends
sequences = []
for seq in fin:
    sequences.append(seq.strip())

#create an empty string variable for the matches
#iterate over each position in the sequences, if they match add | to the string, if not, add a space
match = ""
for i in range(len(sequences[0])):
    if sequences[0][i] == sequences[1][i]:
        match += "|"
    else:
        match += " "

#print the first sequence, followed by the match string, followed by the second sequence
#use + instead of , to seperate items to print to avoid adding a space before match and sequences
print(sequences[0] + "\n" + match + "\n" + sequences[1])
