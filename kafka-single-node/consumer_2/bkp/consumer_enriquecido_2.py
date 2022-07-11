import sqlite3

from sqlite3 import Error

if __name__ == '__main__':
    sqliteConnection = sqlite3.connect('/home/cmour/cp-docker-images/examples/kafka-single-node/consumer_2/01_create_db.db')
    cursor = sqliteConnection.cursor()
    print("Connected to SQLite") 

    sqlite_select_query = """SELECT * from TB_CLIENTE"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()

    for row in records:
        print(row)

    #print(records)
    

    cursor.close()