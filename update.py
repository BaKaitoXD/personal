import mysql.connector
import os
import time


def update_to_active(stud_id):
    try:
        con = mysql.connector.connect(
            host="localhost", user="root", password="", database="avila")
        cur = con.cursor()

        type = input("What needs to be active? ")

        # defining the Query
        sql = "UPDATE todo SET status = %s WHERE student_id = %s and todo = %s"
        val = ("active", stud_id, type)
        # executing the query
        cur.execute(sql, val)

        # f# final step is to commit to indicaet the database
        # that we have changed the table data
        try:
            con.commit()
        except:
            con.rollback()
    except mysql.connector.Error as e:
        print("Error reading data from Mysql table", e)
    finally:
        print(cur.rowcount, "records updated")
        con.close()
        cur.close()


def update_to_complete(stud_id):
    try:
        con = mysql.connector.connect(
            host="localhost", user="root", password="", database="avila")
        cur = con.cursor()

        type = input("What needs to be complete? ")

        # defining the Query
        sql = "UPDATE todo SET status = %s WHERE student_id = %s and todo = %s"
        val = ("complete", stud_id, type)
        # executing the query
        cur.execute(sql, val)

        # f# final step is to commit to indicaet the database
        # that we have changed the table data
        try:
            con.commit()
        except:
            con.rollback()
    except mysql.connector.Error as e:
        print("Error reading data from Mysql table", e)
    finally:
        print(cur.rowcount, "records updated")
        con.close()
        cur.close()


def update_information(stud_id):
    menu = 0
    while menu != "0":
        os.system('cls')
        print("///////////////////////////////////////")
        print("           Select To Update Information")
        print("///////////////////////////////////////\n")
        print("[0] Back")
        print("[1] Update First Name")
        print("[2] Update Last Name")
        print("[3] Update Middle Name")
        print("[4] Change Gender")
        print("[5] Change Password")
        menu = input("\nMenu: ")
        if menu == "1":
            try:
                con = mysql.connector.connect(
                    host="localhost", user="root", password="", database="avila")
                cur = con.cursor()

                new_fn = input("Updated First Name: ")
                # defining the Query
                sql = "UPDATE account SET first_name = %s WHERE id = %s"
                val = (new_fn, stud_id, )
                # executing the query
                cur.execute(sql, val)

                # f# final step is to commit to indicaet the database
                # that we have changed the table data
                try:
                    con.commit()
                except:
                    con.rollback()
            except mysql.connector.Error as e:
                print("Error reading data from Mysql table", e)
            finally:
                print(cur.rowcount, "records updated")
                con.close()
                cur.close()
        elif menu == "2":
            try:
                con = mysql.connector.connect(
                    host="localhost", user="root", password="", database="avila")
                cur = con.cursor()

                new_ln = input("Updated Last Name: ")
                # defining the Query
                sql = "UPDATE account SET last_name = %s WHERE id = %s"
                val = (new_ln, stud_id, )
                # executing the query
                cur.execute(sql, val)

                # f# final step is to commit to indicaet the database
                # that we have changed the table data
                try:
                    con.commit()
                except:
                    con.rollback()
            except mysql.connector.Error as e:
                print("Error reading data from Mysql table", e)
            finally:
                print(cur.rowcount, "records updated")
                con.close()
                cur.close()
        elif menu == "3":
            try:
                con = mysql.connector.connect(
                    host="localhost", user="root", password="", database="avila")
                cur = con.cursor()

                new_mn = input("Updated Middle Name: ")
                # defining the Query
                sql = "UPDATE account SET middle_name = %s WHERE id = %s"
                val = (new_mn, stud_id, )
                # executing the query
                cur.execute(sql, val)

                # f# final step is to commit to indicaet the database
                # that we have changed the table data
                try:
                    con.commit()
                except:
                    con.rollback()
            except mysql.connector.Error as e:
                print("Error reading data from Mysql table", e)
            finally:
                print(cur.rowcount, "records updated")
                con.close()
                cur.close()
        elif menu == "4":
            try:
                con = mysql.connector.connect(
                    host="localhost", user="root", password="", database="avila")
                cur = con.cursor()

                new_sex = input("Change gender[male][female]: ")
                # defining the Query
                sql = "UPDATE account SET sex = %s WHERE id = %s"
                val = (new_sex, stud_id, )
                # executing the query
                cur.execute(sql, val)

                # f# final step is to commit to indicaet the database
                # that we have changed the table data
                try:
                    con.commit()
                except:
                    con.rollback()
            except mysql.connector.Error as e:
                print("Error reading data from Mysql table", e)
            finally:
                print(cur.rowcount, "records updated")
                con.close()
                cur.close()
        elif menu == "5":
            try:
                con = mysql.connector.connect(
                    host="localhost", user="root", password="", database="avila")
                cur = con.cursor()

                new_password = input("Change Password: ")
                # defining the Query
                sql = "UPDATE account SET password = %s WHERE id = %s"
                val = (new_password, stud_id, )
                # executing the query
                cur.execute(sql, val)

                # f# final step is to commit to indicaet the database
                # that we have changed the table data
                try:
                    con.commit()
                except:
                    con.rollback()
            except mysql.connector.Error as e:
                print("Error reading data from Mysql table", e)
            finally:
                print(cur.rowcount, "records updated")
                con.close()
                cur.close()
        elif menu != "0":
            print("!!! Invalid input !!!")
        time.sleep(2)
