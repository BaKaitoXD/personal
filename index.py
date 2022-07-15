import os
import time
from insert import *
from search import *

menu = 0
while menu != "0":
    os.system('cls')
    print("///////////////////////////////////////")
    print("                        ◯  Todo python")
    print("///////////////////////////////////////\n")
    print("[1] Login")
    print("[2] Register")
    print("[0] Quit")
    menu = input("Menu: ")

    if menu == "1":
        log_in()
    elif menu == "2":
        register()
    elif menu != "0":
        print("!!! Invalid input !!!")
    time.sleep(2)
