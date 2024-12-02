import sqlite3
from werkzeug.exceptions import abort


def get_db_connection():
    conn = sqlite3.connect('sqlite/database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_top_tracks():
    top_tracks_query = """SELECT tr.track_Id, tr.track_title, 
    tr.tweet_count, tr.artist_id, art.artist_name
    FROM track tr, Artist art
    WHERE tr.artist_id = art.artist_id
    ORDER BY tr.tweet_count DESC LIMIT 5"""
    conn = get_db_connection()
    top_tracks = conn.execute(top_tracks_query).fetchall()
    conn.close()
    return top_tracks


def get_all_users():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM USER').fetchall()
    conn.close()
    return users


def get_user(user_id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM USER WHERE user_id = ?', (user_id,)).fetchone()
    conn.close()
    return user


def insertUser(user_id, preferences):
    conn = get_db_connection()
    conn.execute('INSERT INTO USER (user_id, preferences) VALUES (?, ?)', (user_id, preferences))
    conn.commit()
    conn.close()


def editUser(user_id, preferences):
    conn = get_db_connection()
    conn.execute('UPDATE USER SET preferences = ? WHERE user_id = ?', (preferences, user_id))
    conn.commit()
    conn.close()


def deleteUser(user_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM USER WHERE user_id = ?', (user_id,))
    conn.commit()
    conn.close()
