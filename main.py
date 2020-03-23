# Matthew Parnham
# 2287511
# parnham@chapman.edu
# References Koby Yoshida
import sqlite3
from Student import Student

conn = sqlite3.connect('db.sqlite')
c = conn.cursor()

cont = True
while(cont):
    print()
    print("1. Display All Students and all their attributes.")
    print("2. Create Student.")
    print("3. Update Student.")
    print("4. Delete Student by StudentId.")
    print("5. Search/Display students by Major, GPA and Advisor.")
    print("6. Exit.")
    sel = input("Select an option: ")
    if sel.isalpha():
        print("Invalid input.")
        continue
    sel = int(sel)
    print()

    if sel == 1: #Print rows
        c.execute("SELECT * FROM Student WHERE isDeleted = 0")
        rows = c.fetchall()
        for row in rows:
            s = Student(row[0],row[1],row[2],row[3],row[4],row[5])
            print(s.getStudent())
    elif sel == 2: #Create Student
        id = int(input("ID: "))
        fN = input("First Name: ")
        lN = input("Last Name: ")
        gpa = float(input("GPA: "))
        m = input("Major: ")
        fA = input("Faculty Advisor: ")

        c.execute(
            "INSERT INTO Student('StudentId', 'FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdvisor', 'isDeleted')"
            "VALUES (?,?,?,?,?,?,?)",(id,fN,lN,gpa,m,fA,False))
        conn.commit()
        studentId = c.lastrowid
        print("record created", studentId)
    elif sel == 3: #Update Student
        id = int(input("ID: "))
        c.execute("SELECT StudentId FROM Student WHERE StudentId = {}".format(id))
        row = c.fetchall()
        if row:
            print("Please input new advisor and major. Leave blank to skip making changes.")
            adv = input("New advisor: ")
            maj = input("New major: ")
            if adv != "":
                c.execute(
                    "UPDATE Student SET FacultyAdvisor = '{}' WHERE StudentId = {}".format(adv,id))
            if maj != "":
                c.execute(
                    "UPDATE Student SET Major = '{}' WHERE StudentId = {}".format(maj, id))
            conn.commit()
        else:
            print("Student not found.")
    elif sel == 4: #Delete Student
        id = int(input("ID: "))
        c.execute("SELECT StudentId FROM Student WHERE StudentId = {}".format(id))
        row = c.fetchall()
        if row:

            c.execute(
                "UPDATE Student SET isDeleted = TRUE WHERE StudentId = {}".format(id))
            conn.commit()
        else:
            print("Student not found.")
    elif sel == 5: #Search/display student
        searchType = int(input("Search by \n1. Major\n2. GPA\n3. Advisor\n> "))
        if searchType == 1:
            query = input("Major: ")
            c.execute("SELECT * FROM Student WHERE Major LIKE '%{}%'".format(query))
            rows = c.fetchall()
            for row in rows:
                s = Student(row[0], row[1], row[2], row[3], row[4], row[5])
                print(s.getStudent())
        elif searchType == 2:
            query = input("GPA: ")
            c.execute("SELECT * FROM Student WHERE GPA = {}".format(query))
            rows = c.fetchall()
            for row in rows:
                s = Student(row[0], row[1], row[2], row[3], row[4], row[5])
                print(s.getStudent())
        else:
            query = input("Advisor: ")
            c.execute("SELECT * FROM Student WHERE FacultyAdvisor LIKE '%{}%'".format(query))
            rows = c.fetchall()
            for row in rows:
                s = Student(row[0], row[1], row[2], row[3], row[4], row[5])
                print(s.getStudent())
    else:
        cont = False
