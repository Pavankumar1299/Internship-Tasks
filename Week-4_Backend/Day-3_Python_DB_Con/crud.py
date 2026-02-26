import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="1299", database="school_db")

cursor = conn.cursor()
print("MySQL connected")

cursor.execute("drop table student")
cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(30),
    usn INT,
    sem INT
)
""")
conn.commit()

print("Table created")

def insert_student(name, department, usn, sem):
    sql = "INSERT INTO student (name, department, usn, sem) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (name, department, usn, sem))
    conn.commit()
    print("Student inserted")

def read_students():
    cursor.execute("SELECT * FROM student")
    result = cursor.fetchall()
    for row in result:
        print(row)

def update_student(student_id, sem):
    sql = "UPDATE student SET sem = %s WHERE id = %s"
    cursor.execute(sql, (sem, student_id))
    conn.commit()
    print("Student updated")

def delete_student(student_id):
    sql = "DELETE FROM student WHERE id = %s"
    cursor.execute(sql, (student_id,))
    conn.commit()
    print("Student deleted")

insert_student("Pavan", "MCA", 56, 3)
insert_student("Kumar", "MCA", 55, 2)
insert_student("Pavankumar", "BCA", 26, 5)
insert_student("Sudeep", "BE", 56, 2)
insert_student("Pavan", "BE", 101, 1)

print("\nAll Students:")
read_students()

update_student(1, 4)
update_student(4, 4)

print("\nAfter Update:")
read_students()

delete_student(2)

print("\nAfter Delete:")
read_students()

cursor.close()
conn.close()
print("\nMySQL connection closed")