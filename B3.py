"""
Given a DNA strand, its transcribed RNA strand is formed by replacing each nucleotide with its complement nucleotide: 
G -> C, C -> G, T -> A, A -> U.  Given a String representation of a DNA strand, print out its transcribed RNA strand.
"""

print("Enter a DNA strand: ", end="")
strand = input().lower()

strand = strand.replace("g", "C")
strand = strand.replace("c", "G")
strand = strand.replace("t", "A")
strand = strand.replace("a", "U")

print(strand)