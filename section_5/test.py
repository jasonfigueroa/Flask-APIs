# a short script with some basic interactions between python 3 and sqlite 3
import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = 'CREATE TABLE users (id int, username text, password text)'

cursor.execute(create_table)

# tuple
user = (1, 'jason', 'jason')
insert_query = 'INSERT INTO users VALUES (?, ?, ?)'

# on execution the ? marks from insert_query will be replaced with the values from user
cursor.execute(insert_query, user)

users = [
	(2, 'bob', 'bob'),
	(3, 'jane', 'jane')
]

cursor.executemany(insert_query, users)

select_query = 'SELECT * FROM users'

users = cursor.execute(select_query)

for user in users:
	print('id: {}, username: {}, password: {}'.format(user[0], user[1], user[2]))

connection.commit()

connection.close()