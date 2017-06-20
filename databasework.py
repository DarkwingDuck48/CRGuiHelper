import sqlite3 as lite
import os
import os.path


class Database:
    def __init__(self, databasename):
        self.databasename = databasename
        self.con = lite.connect(self.databasename)

    def create_database(self):
        with self.con:
            cur = self.con.cursor()
            # AllProjects
            cur.execute('''CREATE TABLE IF NOT EXISTS "AllProjects" 
                            (
                              "id" INTEGER, 
                              "ProjectName" TEXT,
                              "ProjectPath" TEXT
                              );''')
            # Project
            cur.execute('''CREATE TABLE IF NOT EXISTS "Project" 
                            (
                              "id" INTEGER, 
                              "ProjectName" TEXT,
                              "CreationDate" TEXT,
                              "LastOpened" TEXT,
                              "ImpactedApp" TEXT,
                              "JiraLink" TEXT
                              );''')

    def checkDatabase(self):
        with self.con:
            cur = self.con.cursor()
            tables = [i[0] for i in list(cur.execute('''Select name from sqlite_master'''))]
            if "AllProjects" in tables:
                print(tables)
                return cur
            else:
                os.remove(self.databasename)
                return False

    def insert_values(self, row):
        with self.con:
            cur = self.con.cursor()
            cur.executemany('''INSERT OR REPLACE INTO Project VALUES (?,?,?,?,?,?);''', (row,))
        print("HELLO FROM DATABASE CLASS")

if __name__ == "__main__":
    path = os.path.join(os.getcwd(), "resources", "database_test.db")
    data = Database(path)
#    data.create_database()

