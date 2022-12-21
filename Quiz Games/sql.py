import pyodbc

def server():
    join = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL "
                          "Server};SERVER=LAPTOP-AC4I378J\MSSQLSERVER01;DATABASE=trivia;Trusted_connection=yes")

    curser = join.cursor()
    curser.execute("insert into [game] ([Question], [name],[score])"
                    "values(?,?,?)", ("who is temesgen", "miki", 7))

    curser.commit()
    curser.execute("select * from game")


    while 1:
        row = curser.fetchone()
        if not row:
            break
        print(row)

    curser.close()
    join.close()

server()
