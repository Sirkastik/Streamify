import sqlite3
from sqlite3 import Error

DATABASE = r"./database.db"

def create_connection(db_file):
	""" create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
	conn = None
	try:
		conn = sqlite3.connect(db_file)
		return conn
	except Error as e:
		print(e)
	
	return conn


# TABLES
users_table= """CREATE TABLE IF NOT EXISTS users (
					id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
					created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
					username TEXT,
					password TEXT
			);"""

tracks_table = """CREATE TABLE IF NOT EXISTS tracks (
					id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
					artist TEXT,
					title TEXT,
					cover_link TEXT,
					duration INTEGER,
					added_by INTEGER,
					created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
					FOREIGN KEY (added_by) REFERENCES users (id)
				);"""

fav_table_template = """CREATE TABLE IF NOT EXISTS user_{}_favorites (
						track INTEGER,
						FOREIGN KEY (track) REFERENCES tracks (id)
						ON DELETE CASCADE
					);"""


# INSERT
def add_user(conn,username,password):
	"""
	Add a new user into the users table
	:param conn:
	:param username:
	:param password:
	"""
	sql = '''INSERT INTO users (username,password)
	VALUES(?,?)'''
	try:
		cur = conn.cursor()
		cur.execute(sql,(username,password,))
		conn.commit()
	except Error as e:
		print("line 59")
		print(e)
		return
	# fetch user id
	user = select_user(conn,username)

	# generate fav tracks table
	gen_fav_tracks_table(conn,user["id"])

def add_track(conn,artist,title,cover_link,duration,added_by):
	"""
	Add a new track into the tracks table
	:param conn:
	:param artist:
	:param title:
	:param cover_link:
	:param duration:
	:param added_by:
	"""
	sql = ''' INSERT INTO tracks (artist,title,cover_link,duration,added_by) 
	VALUES	(?,?,?,?,?)'''
	try:
		cur = conn.cursor()
		cur.execute(sql,(artist,title,cover_link,duration,added_by,))
		conn.commit()
	except Error as e:
		print(e)


def gen_fav_tracks_table(conn,user_id):
	"""
	Generate a favorites table for the user; called on user creation
	:param conn:
	:param user_id:
	"""
	fav_table = fav_table_template.format(str(user_id))
	create_table(conn,fav_table)

def add_fav_track(conn,user_id,track_id):
	"""
	Adds a track to the users favorites table
	:param conn:
	:param user_id:
	:param track_id:
	"""
	sql = f'INSERT INTO user_{user_id}_favorites (track) VALUES (?)'
	try:
		cur = conn.cursor()
		cur.execute(sql,(track_id,))
		conn.commit()
	except Error as e:
		print(e)

# DELETE
def remove_fav_track(conn,user_id,track_id):
	"""
	Removes a track from a users favorites tables
	:param conn:
	:param user_id:
	:param track_id:
	"""
	sql = f"DELETE FROM users_{user_id}_favorites WHERE track = ?"
	try:
		cur = conn.cursor()
		cur.execute(sql,(track_id,))
		conn.commit()
	except Error as e:
		print(e)

def remove_user(conn,user_id):
	"""
	Removes user from the users table and all user added data
	:param conn:
	:param user-id:
	"""
	# delete user from users table
	sql = "DELETE FROM users WHERE id = ?"
	try:
		cur = conn.cursor()
		cur.execute(sql,(user_id,))
		conn.commit()
	except Error as e:
		print(e)

	# delete fav tracks
	remove_user_fav_tracks(conn,user_id)
	
	# delete tracks added by user
	remove_user_added_tracks(conn,user_id)


def remove_user_fav_tracks(conn,user_id):
	"""
	Deletes the a user's favorites track table
	:param conn:
	:param user_id:
	"""
	try:
		cur = conn.cursor()
		cur.execute(f'DROP TABLE user_{user_id}_favorites')
		conn.commit()
	except Error as e:
		print(e)


def remove_user_added_tracks(conn,user_id):
	"""
	Deletes all tracks that were added by user
	"""
	sql = 'DELETE FROM tracks WHERE added_by = ?'
	try:
		cur = conn.cursor()
		cur.execute(sql,(user_id,))
		conn.commit()
	except Error as e:
		print(e)


# SELECT
def select_user(conn,username):
	"""
	Selects a user form the database
	:param username:
	:param password:
	:return: user object
	"""
	sql = "SELECT id,created_at,username,password FROM users WHERE username = ?"
	cur = conn.cursor()
	cur.execute(sql,(username,))

	rows = []
	for (id,created_at,username,password) in cur:
		rows.append({
		"id":id,
		"created_at":created_at,
		"username":username,
		"password":password,
		})
	
	# retrieves a single result
	return rows[0]
	
def select_track(conn,track_id):
	"""
	Retrieves a track from the tracks table
	:param conn:
	:return: a track object 
	"""
	sql = 'SELECT id,artist,title,cover_link,duration,added_by,created_at FROM tracks WHERE id = ?'
	cur = conn.cursor()
	cur.execute(sql,(track_id,))
	
	tracks = []
	for(id,artist,title,cover_link,duration,added_by,created_at) in cur:
		tracks.append({
			"id":id,
			"artist":artist,
			"title":title,
			"cover_link":cover_link,
			"duration":duration,
			"added_by":added_by,
			"created_at":created_at
		})
	return tracks[0]


def select_tracks(conn):
	"""
	Retrieves all the tracks present
	:param conn:
	:return: list of track object 
	"""
	sql = 'SELECT id,artist,title,cover_link,duration,added_by,created_at FROM tracks'
	cur = conn.cursor()
	cur.execute(sql)
	
	tracks = []
	for(id,artist,title,cover_link,duration,added_by,created_at) in cur:
		tracks.append({
			"id":id,
			"artist":artist,
			"title":title,
			"cover_link":cover_link,
			"duration":duration,
			"added_by":added_by,
			"created_at":created_at
		})
	return tracks


def select_favorites(conn,user_id):
	"""
	Retrieves all favorite tracks from the users favorites table
	:param conn:
	:return: list of track objects
	"""
	sql = f'SELECT track FROM user_{user_id}_favorites'
	cur= conn.cursor()
	cur.execute(sql)

	fav_tracks = []
	for track in cur:
		fav_tracks.append({
			select_track(conn,track)
		})
	return fav_tracks

def create_table(conn,create_table_sql):
	""" create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
	try:
		c = conn.cursor()
		c.execute(create_table_sql)
	except Error as e:
		print(e)

def setup():
	conn = create_connection(DATABASE)
	if conn is not None:
		create_table(conn,users_table) # users
		create_table(conn,tracks_table) # tracks
		# init_users
		# init_tracks
		
		conn.close()

if __name__ == "__main__":
	setup()