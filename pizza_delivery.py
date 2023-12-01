print("Welcome!")

size= input("What size of pizza would you prefer to have? \n Large \n Medium \n Small \n")

if size == "Large":
    bill=25
    print("Total bill is $25")

if size == "Medium":
    bill=20
    print("Total bill is $20")

if size == "Small":
    bill=15
    print("Total bill is $15")


pepperoni= input("Would you like to add pepperoni? yes or no? \n")

if pepperoni == "yes" and (size == "Large" or size == "Medium"):
    bill += 3
    print(f"Total= ${bill}")
    
if pepperoni == "yes" and size == "Small":
    bill += 2
    print(f"Total= {bill}")

cheese= input("DO you want to add extra cheese? yes or no/\n")
if cheese == "yes":
    bill += 1
    print(f"Total= ${bill}")
    print("Thankyou!")
else:
    print("No extra cheese")
    print("Thankyou!")
    