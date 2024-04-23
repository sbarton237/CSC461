"""
A DNA sequence encodes each amino acid making a protein as a three-nucleotide sequence called a codon. Given a String representation 
of a DNA segment, print whether the last codon is the start codon ATG or one of the stop codons TAA, TAG, or TGA; or none of the above.
"""

print("Enter the DNA segment: ", end="")
seg = input().upper()

if seg[-3:] == "ATG":
    print("The last codon is the start codon ATG.")
elif seg[-3:] == "TAA" or seg[-3:] == "TAG" or seg[-3:] == "TGA":
    print("The last codon is one of the stop codons.")
else:
    print("The last codon is not the start or a stop codon.")
