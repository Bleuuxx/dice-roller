import random

dice_number = int(input("Enter how many dice you want to roll: "))
total = 0

def roll(times):
    global total
    while times > 0:
        number = random.randint(1, 6)
        times = times - 1
        total = total + number

roll(dice_number)
print("Total:", total)

input()  # Program will wait for user input before exiting
