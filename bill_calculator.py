total= float(input ("what is the total?"))

tip_percentage= float(input ("Tip %= 12,15,20?"))

splits= int(input("how many people to split?"))

print(f"Your total= {total}, tip percentage= {tip_percentage}, Splitting amongst= {splits}")

result= (total + ((tip_percentage / total) * 100)) / splits

print(f"everyone pays={result}")
