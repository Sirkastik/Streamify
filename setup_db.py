import sqlite3
import json
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
users_table = """CREATE TABLE IF NOT EXISTS users (
					id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
					created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
					username TEXT,
					password TEXT
			);"""

tracks_table = """CREATE TABLE IF NOT EXISTS tracks (
					id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
					artist TEXT,
					title TEXT,
					track_link TEXT,
					added_by INTEGER DEFAULT 0,
					created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
					FOREIGN KEY (added_by) REFERENCES users (id)
				);"""


def fav_table(id):
    """creates a favorites table for the user id given
    :param id: the user id
    :returns: sql table statement
    """
    return f"""CREATE TABLE IF NOT EXISTS user_{str(id)}_favorites (
						track INTEGER PRIMARY KEY,
						FOREIGN KEY (track) REFERENCES tracks (id)
					);"""


# INSERT
def add_user(conn, username, password):
    """
    Add a new user into the users table
    :param conn:
    :param username:
    :param password:
    """

    # username should be unique
    user = select_user(conn, username)
    if user[0]:
        return (False, 'username is already taken')

    # user is unique, create user
    sql = '''INSERT INTO users (username,password)
	VALUES(?,?)'''
    cur = conn.cursor()
    try:
        cur.execute(sql, (username, password,))
    except Error as e:
        return (False, str(e))
    conn.commit()

    # fetch user id
    user = select_user(conn, username)
    if user[0] is False:
        return user

    # generate fav tracks table
    res = gen_fav_tracks_table(conn, user[1]["id"])
    if res[0] is False:
        return res

    return (True,)


def add_track(conn, artist, title, track_link, added_by=0):
    """
    Add a new track into the tracks table
    :param conn:
    :param artist:
    :param title:
    :param duration:
    :param added_by:
    """

    sql = ''' INSERT INTO tracks (artist,title,track_link,added_by)
	VALUES	(?,?,?,?)'''
    cur = conn.cursor()

    try:
        cur.execute(sql, (artist, title,
                    track_link, added_by,))
    except Error as e:
        return (False, str(e))
    conn.commit()
    return (True, None)


def gen_fav_tracks_table(conn, user_id):
    """
    Generate a favorites table for the user; called on user creation
    :param conn:
    :param user_id:
    """

    return create_table(conn, fav_table(user_id))


def add_fav_track(conn, user_id, track_id):
    """
    Adds a track to the users favorites table
    :param conn:
    :param user_id:
    :param track_id:
    :return success:
    """

    sql = f'INSERT INTO user_{user_id}_favorites (track) VALUES (?)'
    cur = conn.cursor()
    try:
        cur.execute(sql, (track_id,))
    except Error as e:
        return (False, str(e))
    conn.commit()
    return (True,)


# DELETE


def remove_fav_track(conn, user_id, track_id):
    """
    Removes a track from a users favorites tables
    :param conn:
    :param user_id:
    :param track_id:
    :return success:
    """

    sql = f"DELETE FROM users_{user_id}_favorites WHERE track = ?"
    cur = conn.cursor()
    try:
        cur.execute(sql, (track_id,))
    except Error as e:
        return (False, (str))
    conn.commit()
    return (True,)


def remove_user(conn, user_id):
    """
    Removes user from the users table and all user added data
    :param conn:
    :param user-id:
    :return success:
    """

    # delete user from users table
    sql = "DELETE FROM users WHERE id = ?"
    cur = conn.cursor()
    try:
        cur.execute(sql, (user_id,))
    except Error as e:
        return (False, str(e))
    conn.commit()

    # delete fav tracks
    res = remove_user_fav_tracks(conn, user_id)
    if not res[0]:
        return res
    # delete tracks added by user
    return remove_user_added_tracks(conn, user_id)


def remove_user_fav_tracks(conn, user_id):
    """
    Deletes the a user's favorites track table
    :param conn:
    :param user_id:
    :return success:
    """

    cur = conn.cursor()
    try:
        cur.execute(f'DROP TABLE user_{user_id}_favorites')
    except Error as e:
        return (False, str(e))
    conn.commit()
    return (True,)


def remove_user_added_tracks(conn, user_id):
    """
    Deletes all tracks that were added by user
    :param user_id:
    :return success:
    """

    sql = 'DELETE FROM tracks WHERE added_by = ?'
    cur = conn.cursor()
    try:
        cur.execute(sql, (user_id,))
    except Error as e:
        return (False, str(e))
    conn.commit()
    return (True,)


# SELECT
def select_user(conn, username):
    """
    Selects a user form the database
    :param username:
    :param password:
    :return: user object
    """

    sql = "SELECT id,created_at,username,password FROM users WHERE username = ?"
    cur = conn.cursor()
    try:
        cur.execute(sql, (username,))
    except Error as e:
        return (False, str(e))

    rows = []
    for (id, created_at, username, password) in cur:
        rows.append({
            "id": id,
            "created_at": created_at,
            "username": username,
            "password": password,
        })

    # retrieves a single result
    if rows:
        return (True, rows[0])
    return (False, 'no user found')


def select_track(conn, track_id):
    """
    Retrieves a track from the tracks table
    :param conn:
    :return: a track object
    """

    sql = 'SELECT id,artist,title,cover_link,added_by,created_at FROM tracks WHERE id = ?'
    cur = conn.cursor()
    try:
        cur.execute(sql, (track_id,))
    except Error as e:
        return (False, str(e))

    tracks = []
    for(track_id, artist, title, cover_link, added_by, created_at) in cur:
        tracks.append({
            "id": track_id,
            "artist": artist,
            "title": title,
            "added_by": added_by,
            "created_at": created_at
        })
    return (True, tracks[0])


def select_tracks(conn):
    """
    Retrieves all the tracks present
    :param conn:
    :return: list of track object
    """

    sql = 'SELECT id,artist,title,track_link, added_by,created_at FROM tracks'
    cur = conn.cursor()
    try:
        cur.execute(sql)
    except Error as e:
        return (False, str(e))

    tracks = []
    for(id, artist, title, track_link, added_by, created_at) in cur:
        tracks.append({
            "id": id,
            "artist": artist,
            "title": title,
            "track_link":track_link,
            "added_by": added_by,
            "created_at": created_at
        })
    return (True, tracks)


def select_favorites(conn, user_id):
    """
    Retrieves all favorite tracks from the users favorites table
    :param conn:
    :return: list of track objects
    """

    sql = f'SELECT track FROM user_{user_id}_favorites'
    cur = conn.cursor()
    try:
        cur.execute(sql)
    except Error as e:
        return (False, str(e))

    fav_tracks = []
    for track in cur:
        fav_track = select_track(conn, track)
        fav_tracks.append(
            fav_track
        )
    return (True, fav_tracks)


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
:param conn: Connection object
:param create_table_sql: a CREATE TABLE statement
:return:
"""

    c = conn.cursor()
    try:
        c.execute(create_table_sql)
    except Error as e:
        return (False, str(e))
    return (True,)


def init_user(conn):
    res = add_user(conn, 'this', 'that')
    if not res[0]:
        print(res[1])


def init_tracks(conn):
    f = open('./src/assets/mp3.json')
    data = json.load(f)

    for track in data['tracks']:
        if not add_track(conn, track['artist'], track['title'], track['track_link']):
            return False
    return True


def setup():
    """
    Sets up the sqlite database before the server is run
    """

    conn = create_connection(DATABASE)
    if conn is not None:
        create_table(conn, users_table)  # users
        create_table(conn, tracks_table)  # tracks
        init_tracks(conn)
        conn.close()


if __name__ == "__main__":
    setup()
