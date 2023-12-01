print("welcome to the treasure island!!!")
print("begin your journey!!!")

direction= input("Choose your way, left or right?\n")
if direction == "left":
    swim_wait= input("Swim or wait?\n")
    if swim_wait == "wait":
        door = input("choose a door, red, blue, yellow\n")
    else:print("you lose")

    if door == "yellow":
            print("you win!!!")
    else:print("you lose")

else:
    print("you lose")
