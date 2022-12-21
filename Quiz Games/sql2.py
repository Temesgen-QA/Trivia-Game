
import pyodbc

def Q_spor():
    connect = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL "
                             "Server};SERVER=LAPTOP-AC4I378J\MSSQLSERVER01;DATABASE=trivia;Trusted_connection=yes")
    cursor = connect.cursor()

    ID = input("Enter your Id ")
    Question = input("Type the Question?:  ")

    choose1 = input("Choice: ")
    choose2 = input("Choice: ")
    choose3 = input("Choice: ")
    choose4 = input("Choice: ")
    Answer = input("correct  answer is : ")

    cursor.execute("INSERT INTO [Test] (ID,Question ,Option1,Option2,Option3,Option4,Answer)"
                   "VALUES(?,?,?,?,?,?,?)", (ID,Question, choose1, choose2, choose3, choose4, Answer ))

    connect.commit()
    connect.execute("select * from Test")

    while 1:
        row = connect.fetchone()
        if not row:
            break
        print(row)

    connect.close()
    connect.close()

Q_spor()

