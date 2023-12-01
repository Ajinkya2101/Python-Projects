height= float(input("enter your height= "))
weight= float(input("enter your weight= "))

bmi = float( weight / (height**2) )

if bmi <= 18.5:
    print(bmi)
    print("Underweight")

elif bmi > 18.5 and bmi <= 25:
        print(bmi)
        print("normal weight")

elif bmi > 25 and bmi < 30:
        print(bmi)
        print("overweight")

elif bmi > 30 and bmi < 35:
        print(bmi)
        print("obese")
        
else:
        print("clinically obese")

