"""
(a) Given a string representing a base-pair sequence (i.e. containing only the letters A, G, C and T), determine the fraction of G and 
C bases in the sequence.  (b) Using only string methods, devise a way to determine if a nucleotide sequence is a palindrome in the sense 
that it is equal to its own complementary sequence read backward.  For example, the sequence TGGATCCA is palindromic because its 
complement is ACCTAGGT, which is the same as the original sequence backward. The complementary base pairs are (A,T) and (C,G).
"""

print("Enter DNA sequence: ", end="")
sequence = input().upper()

def fraction_gc(sequence):
    total = len(sequence)
    frac = sequence.count('G') + sequence.count('C')
    print(frac / total)

def palindrome(sequence):
    seq = sequence.lower()
    seq = seq.replace('a', "T")
    seq = seq.replace('t', "A")
    seq = seq.replace('c', "G")
    seq = seq.replace('g', "C")
    if seq[::-1] == sequence:
        print("Is a palindrome.")
    else:
        print("Is not a palindrome.")

fraction_gc(sequence)
palindrome(sequence)