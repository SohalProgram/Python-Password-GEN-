import random
import time

def password():
    print('')
    time.sleep(0.1)
    print('How Many passwords Should I Generate?')
    print('')
    time.sleep(2)
    amount = int(input("> "))
    print('')
    time.sleep(2.5)
    print('Generating...')
    time.sleep(2.5)
    print('')

    fix = 1
    while fix <= amount:
        upper = "abcdefgijklmnopqrstuvwxyz"
        lower = "ABCDEFGIJKLMNOPQRSTUWXYZ"
        numbers = "0123456789"
        symbols = "!@#$%^&&*()"

        string = lower + upper + numbers + symbols
        length = 16
        genpassword = "".join(random.sample(string, length))
        print("Your new password is: " + genpassword)
        fix += 1

password()

print('')
r = input("Do you want to generate more passwords?: ")
if r == "yes":
    password()
else:
    print('')
    time.sleep(2.5)
    print("Ok,bey!")
    exit()
