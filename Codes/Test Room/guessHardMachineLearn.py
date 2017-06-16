import random
import time

a = random.randint(1,9)
def check_odd(num):
    if num % 2 > 0:
        print("odd")
        print("loading...")
        time.sleep(2)
        print("loading...")
        time.sleep(2)
        print("Possibility found!")
        time.sleep(2)
        if a > 0 and a < 2:
            print("The number is 1")
        elif a > 2 and a < 4:
            print("The number is 3")
        elif a > 4 and a < 6:
            print("The number is 5")
        elif a > 6 and a < 8:
            print("The number is 7")
        elif a > 8 and a < 10:
            print("The number is 9")
    print("The actual number was %a!" %(a))
def check_even(num):
    if a % 2 == 0:
        print("Even")
        print("loading...")
        time.sleep(2)
        print("loading...")
        time.sleep(2)
        print("loading...")
        time.sleep(2)
        print("loading...")
        time.sleep(2)
        print("loading...")
        time.sleep(2)
        if a > 1 and a < 3:
            print("The number is 2")
        elif a > 3 and a < 5:
            print('The number is 4')
        elif a > 5 and a < 7:
            print("The number is 6")
        elif a > 7 and a < 9:
            print("The number is 8")
    else: check_odd(a)
    print("The actual number was %a!" %(a))

check_even(a)
