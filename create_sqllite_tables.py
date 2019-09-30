'''
Imports data from data.json in to SQLLITE database

'''
import sqlite3

dbfname = 'Dictionary.db'

def create_tables(cn):
    c = cn.cursor()

    lcWordDB = """ CREATE TABLE IF NOT EXISTS words (
                word_id int,
                word TEXT
                )
    """


    lcDefnDB = """ CREATE TABLE IF NOT EXISTS definitions (
                def_id int,
                word_id int,
                def_no int,
                definition TEXT
                )
    """

    c.execute(lcWordDB)
    c.execute(lcDefnDB)
    cn.commit()
    print("Tables created")

    return True

def populate_tables(cn):

    return



conn = sqlite3.connect(dbfname)
print("Connection established!")
create_tables(conn)
conn.close()
print("Connection closed!")

#populate_tables(conn)



#print("Connection failed.")
