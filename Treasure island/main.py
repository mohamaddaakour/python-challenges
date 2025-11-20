print("Welcome to Treasure Island. Your mission is to find the treasure.")

left_right = input("Choose a Direction l for Left and r for Right\n")

if left_right == "l":
    swim_wait = input("Choose Your Desicion s for Swim and w for Wait\n")

    if swim_wait == "w":
        door = input("Choose a door now b for Blue, r for Red, y for Yellow\n")

        if door == "b":
            print("Eaten bu beasts. Game Over")
        elif door == "r":
            print("Burned by fire. Game Over.")
        elif door == "y":
            print("You Win!")
        else:
            print("Game Over.")
    
    else:
        print("Attacked by trout. Game Over.")

else:
    print("Fall into a hole. Game Over.")