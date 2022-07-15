import mysql.connector
import os
import time
from insert import *
from delete import *
from update import *


def read_all_todo(stud_id):
    menu = 0
    while menu != "0":
        os.system('cls')
        print("///////////////////////////////////////")
        print("          Work hard in silence.        ")
        print("             Let success make the noise.")
        print("///////////////////////////////////////")
        print("[0] Back")
        print("[1] Add Todo")
        print("[2] Need to Complete")
        print("[3] Need to Active")
        print("[4] Need to Delete")

        try:
            con = mysql.connector.connect(
                host="localhost", user="root", password="", database="avila")
            cur = con.cursor()

            sql = "SELECT * FROM todo WHERE student_id = %s ORDER BY status ASC;"
            val = (stud_id, )
            cur.execute(sql, val)
            # get all records
            records = cur.fetchall()

            print("\nView All Todo")
            for row in records:
                print("__________________________")
                print("todo:", row[2])
                print("status:", row[3])
        except mysql.connector.Error as e:
            print("Error reading data from Mysql table", e)
        finally:
            if con.is_connected():
                con.close()
                cur.close()

        print("__________________________")
        menu = input("\nMenu: ")

        if menu == "1":
            add_todo(stud_id)
        elif menu == "2":
            update_to_complete(stud_id)
        elif menu == "3":
            update_to_active(stud_id)
        elif menu == "4":
            delete_todo(stud_id)
        elif menu != "0":
            print("!!! Invalid input !!!")
        time.sleep(2)
