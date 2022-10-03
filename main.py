from password_generator import PasswordGenerator
import random
import string

pwo = PasswordGenerator()

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

def switch(v): yield lambda *c: v in c
loop=True

while(loop):

    print("===============================================")
    print("=================    Menu    ==================")
    print("===============================================")
    print("1)         Generate random pass                ")
    print("2)  Enter the length of your random pass       ")
    print("3)                 Exit                        ")
    print("===============================================")

    menu = int(input("Choose from Menu above...\n"))
    for case in switch(menu):
        if case(1):
            print("================================\n")
            print(pwo.generate())
            print("================================\n")
        elif case(2):
            print("================================\n")
            length = int(input('Enter the length of password: \n'))
            # password is<100 characters not working for >100
            temp = random.sample(all, length)
            password = "".join(temp)
            print(password)
            print("================================\n")
        elif case(3):
            exit()
        else:
            print("Choose something from the menu\n")
