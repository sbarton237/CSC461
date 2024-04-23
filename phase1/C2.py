"""
Write a program that can take in any of the following molecular formulas as a string and print out whether the compound is an acidic, 
basic, or neutral compound when dissolved in water. The script should not contain pre-sorted lists of compound but rather determine the 
class of molecule base on the formula.

HCl, H2SO4, HNO3, HCO2H - acid
NaOH, Ca(OH)2, KOH, Mg(OH)2 - base
KCl, Na2SO4, KNO3, NaBr - neutral
"""

print("Enter chemical: ")
chem = input()

if "OH" in chem:
    print("Basic")
elif "H" in chem:
    print("Acidic")
else:
    print("Neutral")
