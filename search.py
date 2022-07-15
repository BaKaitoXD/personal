import mysql.connector
import os
import time
from update import *
from insert import *
from search_all import *


def log_in():
    os.system('cls')
    print("///////////////////////////////////////")
    print("                ◯  Login               ")
    print("                   Dreams Don't work   ")
    print("                   unless you do!      ")
    print("///////////////////////////////////////\n")

    stud_id = input("Student ID: ")
    password = input("Password: ")

    try:
        con = mysql.connector.connect(
            host="localhost", user="root", password="", database="avila")
        cur = con.cursor()

        sql = "SELECT id FROM account WHERE student_id = %s"
        val = (stud_id, )
        cur.execute(sql, val)
        # get all records
        record = cur.fetchall()

        id = 0
        for row in record:
            id = row[0]

        if id > 0:
            id = 0
            sql = "SELECT id FROM account WHERE student_id = %s AND password = %s"
            val = (stud_id, password, )

            cur.execute(sql, val)
            # get all records
            record = cur.fetchall()
            for row in record:
                id = row[0]
            if id > 0:
                dashboard(id)
            else:
                print("!!! Wrong Password !!!")
        else:
            print("!!! Wrong Student ID !!!")
        try:
            con.commit()
        except:
            con.rollback()
    except mysql.connector.Error as e:
        print("Error reading data from Mysql table", e)
    finally:
        con.close()
        cur.close()


def dashboard(stud_id):
    id = stud_id
    student_id = 0
    fn = 0
    ln = 0
    mn = 0
    sex = 0
    gain_access = False
    menu = 0
    while menu != "0":
        os.system('cls')
        try:
            con = mysql.connector.connect(
                host="localhost", user="root", password="", database="avila")
            cur = con.cursor()

            sql = "SELECT * FROM account WHERE id = %s"
            val = (stud_id, )

            cur.execute(sql, val)
            # get all records
            record = cur.fetchall()
            gain_access = True
            for row in record:
                student_id = row[1]
                fn = row[2]
                ln = row[3]
                mn = row[4]
                sex = row[5]
        except mysql.connector.Error as e:
            print("Error reading data from Mysql table", e)
        finally:
            con.close()
            cur.close()

        if gain_access == True:
            if sex == "male":
                sex = "Mr."
            elif sex == "female":
                sex = "Ms."
            else:
                sex = "Mx"
            cappital_mn = mn.upper()
            print("///////////////////////////////////////")
            print("             Hi,", sex, fn.capitalize(),
                  cappital_mn[0] + ".", ln.capitalize())
            print("///////////////////////////////////////\n")
            print("[0] Logout")
            print("[1] Update Info")
            print("[2] Show all Todo")

            menu = input("\nMenu: ")
            if menu == "1":
                update_information(id)
            elif menu == "2":
                read_all_todo(student_id)
            elif menu != "0":
                print("!!! Invalid input !!!")
        time.sleep(2)
