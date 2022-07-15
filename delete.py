import mysql.connector


def delete_todo(stud_id):
    try:
        con = mysql.connector.connect(
            host="localhost", user="root", password="", database="avila")
        cur = con.cursor()
        type = input("What needs to be delete? ")
        sql = "DELETE FROM todo WHERE student_id = %s and todo = %s"
        val = (stud_id, type, )
        cur.execute(sql, val)
        try:
            con.commit()
        except:
            con.rollback()
    except mysql.connector.Error as e:
        print("Error reading data from Mysql table", e)
    finally:
        print(cur.rowcount, "record Deleted")
        con.close()
        cur.close()
