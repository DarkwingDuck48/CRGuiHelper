import sqlite3 as lite
import os
import os.path


def create_database(databasename):
    con = lite.connect(databasename)
    with con:
        cur = con.cursor()
        # AllProjects
        cur.execute('''CREATE TABLE IF NOT EXISTS "AllProjects" 
                        (
                          "id" INTEGER PRIMARY KEY, 
                          "ProjectName" TEXT,
                          "ProjectPath" TEXT
                          );''')
        # Project
        cur.execute('''CREATE TABLE IF NOT EXISTS "Project" 
                        (
                          "id" INTEGER PRIMARY KEY, 
                          "ProjectName" TEXT,
                          "CreationDate" DATATIME,
                          "LastOpened" DATATIME
                          );''')

if __name__ == "__main__":
    path = os.path.join(os.getcwd(), "resources", "database_test.db")
    create_database(path)
