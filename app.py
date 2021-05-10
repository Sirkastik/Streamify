from flask import Flask, request, g
from flask_cors import CORS,cross_origin
import sqlite3
import json
import setup_db

app = Flask(__name__)
CORS(app)
database = "./database.db" 

@app.after_request
def add_header(response):
    # response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Methods'] = "PUT,POST,GET,DELETE,OPTIONS"
    response.headers['Access-Control-Allow-Headers'] = "Content-Type,Content-Length, Authorization"
    return response

def get_db():
	"""
	Establishes a database connection and returns the connection instance
	:return sqlite3.Connection:
	"""
	db = getattr(g,'_database',None)
	if db is None:
		db= g._database = sqlite3.connect(database)
	return db

@app.route("/create_user",methods=["POST"])
def create_user():
	"""
	Creates an app user given their username and password
	:param:
	"""

	data = request.get_json()
	username = data["username"]
	passwd = data["password"]

	req_error = '{} field missing, check your request body'
	if not username :
		return json.dumps({
			"response":{},
			"error":req_error.format("username")
		})
	if not passwd  :
		return json.dumps({
			"response":{},
			"error": req_error.format("password")
		})

	conn = get_db()
	setup_db.add_user(conn,username,passwd)
	user = setup_db.select_user(conn,username)
	return json.dumps({
		"response":{user},
		"error":""
	})

@app.route("/get_user/<username>",methods=["GET"])
def get_user(username):

	"""
	Fetches a user from the database if the user exists
	"""

	conn = get_db()
	user = setup_db.select_user(conn,username)
	if not user:
		return json.dumps({
			"response":{},
			"error": "the user was no found"
		})
	return json.dumps({
		"response":{user},
		"error":""
	})

@app.route("/delete_user/<int:user_id>",methods=["DELETE"])
def delete_user(user_id):
	"""
	Deletes the user and all their user data from the database
	"""

	conn = get_db()
	setup_db.remove_user(conn,user_id)
	return json.dumps({
		"response":{"success"},
		"error":""
	})

@app.route("/tracks",methods=["GET"])
def get_tracks():
	"""
	Fetches all the tracks present 
	"""

	conn = get_db()
	tracks = setup_db.select_tracks(conn)
	if not tracks:
		return json.dumps({
			"reponse":{},
			"error":"no tracks were found in db"
		}) 
	return json.dumps({
		"response": {tracks},
		"error":""
	})

@app.route("/track/<int:track_id>",methods=["GET"])
def get_track(track_id):
	"""
	Fetches the track provided the track_id
	:param track_id:
	"""

	conn = get_db()
	track = setup_db.select_track(conn,track_id)
	if not track:
		return json.dumps({
			"response":{},
			"error":"track was not found"
		})
	return json.dumps({
		"response":{track},
		"error":""
	})

@app.route("/tracks",methods=["POST"])
def add_track():
	""" 
	Adds a track for the user
	"""

	# artist, title, cover_link, duration, added_by
	data = request.get_json()
	artist = data["artist"]
	title = data["title"]
	cover_link = data["cover_link"]
	duration = data["duration"]
	added_by = data["added_by"]

	if not cover_link:
		cover_link = 'default cover' #TODO
	if not artist or title or duration or added_by:
		json.dumps({
			"response":{},
			"error":"request field(s) are/is missing, check your request body"
		})

	conn = get_db()
	if setup_db.add_track(conn,artist,title,cover_link,duration,added_by):
		return json.dumps({
			"response":{"success"},
			"error":""
		})
	else:
		return json.dumps({
			"response":{},
			"error":"server error, track could not be added"
		})

@app.route("/favorites",methods=["POST"])
def add_favorite():
	"""
	Add a track to the users favorites table
	"""

	data = request.get_json()
	user_id = data["user_id"]
	track_id = data["track_id"]

	req_error = '{} field is missing, check your request body'
	if not user_id:
		return json.dumps({
			"response":{},
			"error": req_error.format("user_id")
		})
	if not track_id:
		return json.dumps({
			"response":{},
			"error": req_error.format("track_id")
		})

	conn = get_db()
	if setup_db.add_fav_track(conn,user_id,track_id):
		return json.dumps({
			"response":{"success"},
			"error":""
		})
	else:
		return json.dumps({
			"response":{},
			"error":"server error, track could not be added"
		})

@app.route("/favorites",methods=["DELETE"])
def remove_favorite():
	"""
	Removes a track from a user's favorites table
	"""

	data = request.get_json()
	user_id = data["user_id"]
	track_id = data["track_id"]

	req_error = '{} field missing, check request body'
	if not user_id:
		return json.dumps({
			"response":{},
			"error": req_error.format("user_id")
		})
	if not track_id:
		return json.dumps({
			"response":{},
			"error": req_error.format("track_id")
		})

	conn = get_db()
	if setup_db.remove_fav_track(conn,user_id,track_id):
		return json.dumps({
			"response":{"success"},
			"error":""
		})
	else:
		return json.dumps({
			"response":{},
			"error":"server error, favorite track could not be removed"
		})


@app.route("/favorites/<int:user_id>",methods=["GET"])
def get_favorites(user_id):
	"""
	Fetches the user's favorite tracks
	:param user_id:
	"""
	
	conn = get_db()
	tracks = setup_db.select_favorites(conn,user_id)
	if not tracks:
		return json.dumps({
			"reponse":{},
			"error":"no favorites tracks were found"
		})
	return json.dumps({
		"response":{tracks},
		"error":""
	})

if __name__ == "__main__":
    app.run(debug=True)