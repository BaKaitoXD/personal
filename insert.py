import mysql.connector
import os
import time


def register():
    os.system('cls')
    print("///////////////////////////////////////")
    print("               ◯  Sign Up             ")
    print("                   It’s quick and easy.")
    print("///////////////////////////////////////\n")
    no_account = False

    stud_id = input("Student ID: ")
    try:
        con = mysql.connector.connect(
            host="localhost", user="root", password="", database="avila")
        cur = con.cursor()

        sql = "SELECT id FROM account WHERE student_id = %s"
        val = (stud_id, )
        cur.execute(sql, val)
        records = cur.fetchall()
        rec = records[0]
        no_account = False
    except:
        no_account = True
        con.close()
        cur.close()

    if no_account == True:
        con = mysql.connector.connect(
            host="localhost", user="root", password="", database="avila")
        cur = con.cursor()

        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        middle_name = input("Middle Name: ")
        sex = input("Gender[male][female]: ")
        password = input("Password: ")

        sql = "INSERT INTO account(student_id, first_name, last_name, middle_name, sex, password) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (stud_id, first_name, last_name, middle_name, sex, password)

        try:
            cur.execute(sql, val)
            con.commit()
        except:
            con.rollback()
        print("\n", cur.rowcount, "Record inserted!")
    else:
        print("!!! You Have already an Account !!!")

    con.close()
    time.sleep(2)


def add_todo(stud_id):
    os.system('cls')
    print("///////////////////////////////////////")
    print("         Work hard in silence.         ")
    print("            Let success make the noise.")
    print("///////////////////////////////////////\n")
    print("[0] Back")
    todo = input("\nWhat needs to be done? ")

    if todo != "0":
        con = mysql.connector.connect(
            host="localhost", user="root", password="", database="avila")
        cur = con.cursor()
        sql = "INSERT INTO todo(student_id, todo, status) VALUES (%s, %s, %s)"
        val = (stud_id, todo, "active",)
        try:
            cur.execute(sql, val)
            con.commit()
        except:
            con.rollback()

        print("\n", cur.rowcount, "Record inserted!")
        con.close()
