year= int(input("enter a year \n"))

div_4 = year%4 

if div_4 == 0:
    div_100 = year%100
    if div_100 != 0:
        print(f"{year} is a Leap Year") 
        div_400= year%400

        if div_400 == 0:
            print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
