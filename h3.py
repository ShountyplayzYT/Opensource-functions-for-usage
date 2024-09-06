import time
n = ""
t = 0
while True:
    n = input("What would you like to do with you car?" + '''
Accelerate to 40km/h
Accelerate to 60km/h
Quit the race
:: ''').lower()

    if n == "accelerate to 40km/h":
        print("The other cars have passed way ahead of you. You are last place")
        n1 = input("Would you like to accelerate to 80km/h, as that is the only way to go ahead, or acceleate to 60km/h and get third place?").lower()
        if n1 == "accelerate to 80km/h":
            print("You engine heats up too much and you engine fails. what do you do?")
            n2 = input('''accelerate to 100km/h
            maintain speed
            deaccelerate to 60km/h''')
            if n2 == "accelerate to 100km/h":
                print("Your car crashes very badly and you die.")
                break
            elif n2 == "maintain speed":
                print("Oh no! you run out of fuel. Game over,")
                break
            else:
                print("You pulled yourself together. Congrats! you got 3rd place!")
                break
        elif n1 == "accelerate to 60km/h":
            print("oh well. You got 3rd place. Congrats!")
            break


    if n == "accelerate to 60km/h":
        r = input("You are neck to neck with first place. Would you like to try to overtake them?")
        if r == "yes":
            print("Your engine burns and you die. Better luck next time!")
            break
        elif r == "no":
           rs =  input("The other car tries to take over but breaks down, and your first place. Will you maintain your pace or accelrate furthur?")
           if rs == "maintain pace":
               print("You maintain pace and win the race. Congrats!")
               break
           elif rs == "accelerate":
               print("Your engine burns and you lose the race.")
               break

    if n == "quit":
        print("You lose the race by forfeit")
        break




