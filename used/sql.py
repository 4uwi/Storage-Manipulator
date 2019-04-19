import sqlite3
import datetime

connect = sqlite3.connect('data.sqlite')
cursor = connect.cursor()

date = datetime
print(date.datetime.now())

cursor.execute('UPDATE employee SET last_seen=? WHERE name=?', [(date.datetime.now()), ('Artem')])
connect.commit()