# """
# build a countdown timer program that counts down from 10 to 1
# """
# print("starting countdown:")
# for i in range(10, 0, -1):
#     print(i)
# print("Countdown finished!")


"""
Count down:
I have a bomb that I want to detonate at Aptech but I don’t want to be caught in the blast 

Help me design and develop a countdown timer that counts down from 10 to 1
"""
import time

"""
Countdown Timer Program
======================

This program creates a simple countdown timer that counts from 10 to 1.
It uses a while loop and the 'time' module for delays.
"""

def functionToCount():
    print("=== COUNTDOWN TIMER ===")
    print("Starting countdown from 10 to 1...\n")

    # Countdown from 10 to 1
    count = 10
    while count >= 0:
        print(f" {count}...")
        # time.sleep(1)  # Pause the program for 1 second
        count = count -1

    print("=== TIMER FINISHED ===")


human = {
    "name": "majesty",
    "gender": "male"
}


def countup():
    isFalse = True
    count = 0
    while isFalse:
        print(count)
        count = count + 1
        if(count >= 10):
            isFalse = False
            break