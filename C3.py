"""
Straight-chain alkanes are hydrocarbons with the general stoichiometric formula CnH2n+1 in which the carbon atoms form a simple chain: 
for example, butane, C4H10 has the structural formula which may be depicted H3CCH2CH2CH3. Write a program to output the structural 
formula of such an alkane, given its stoichiometry (assume n > 1). For example, given stoich='C8H18', the output should be:  
H3C-CH2-CH2-CH2-CH2-CH2-CH2-CH3 
"""

print("Enter stoichiometry in form CXHY: ")
stoich = input().upper()
h = stoich.find("H")

c_count = int(stoich[1:h])

start = "H3C-"
end = "CH3"
c_count -= 2

for i in range(c_count):
    start += "CH2-"

print(start + end)