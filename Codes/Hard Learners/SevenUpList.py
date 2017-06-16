import random
import time

selection = []
x = 0
while x < 10:
    num = random.randint(1,9)
    selection.append(num)
    x = x + 1
def checker(bNum):
    if selection[0] > 7:
        time.sleep(1)
        print("Seven Up!")
        print("The 1st num was the winner!")
    elif selection[1] > 7:
        time.sleep(2)
        print("Seven Up!")
        print("The 2nd num was the winner!")
    elif selection[2] > 7:
        time.sleep(3)
        print("Seven Up!")
        print("The 3rd num was the winner!")
    elif selection[3] > 7:
        time.sleep(4)
        print("Seven Up!")
        print("The 4th num was the winner!")
    elif selection[4] > 7:
        time.sleep(5)
        print("Seven Up!")
        print("The 5th num was the winner!")
    elif selection[5] > 7:
        time.sleep(6)
        print("Seven Up!")
        print("The 6th num was the winner!")
    elif selection[6] > 7:
        time.sleep(7)
        print("Seven Up!")
        print("The 7th num was the winner!")
    elif selection[7] > 7:
        time.sleep(8)
        print("Seven Up!")
        print("The 8th num was the winner!")
    elif selection[8] > 7:
        time.sleep(9)
        print("Seven Up!")
        print("The 9th num was the winner!")
    elif selection[9] > 7:
        time.sleep(10)
        print("Seven Up!")
        print("The 10th num was the winner!")
    else: print("All numbers are less than 7, begin round 2!")
checker(selection)
print(selection)
