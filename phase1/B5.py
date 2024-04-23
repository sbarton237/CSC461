"""
A DNA sequence encodes each amino acid making a protein as a three-nucleotide sequence called a codon. For example, the sequence 
fragment AGTCT-TATATCT contains the codons (AGT, CTT, ATA, TCT) if read from the first position ("frame"). If read in the second 
frame it yields the codons (GTC, TTA, TAT) and in the third (TCT, TAT, ATC).  Write some Python code to extract the codons into a 
list of three-letter strings given a sequence and frame as an integer value (0, 1, or 2).
"""

print("Enter DNA sequence: ", end="")
sequence = input().upper()
print("Enter Frame: ", end="")
frame = int(input())
l = []
for i in range(frame, len(sequence) - 2, 3):
    l.append(sequence[i:i+3])
print(l)
