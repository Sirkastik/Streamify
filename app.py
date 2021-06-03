from flask import Flask, request, g
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import sqlite3
import json
import setup_db
import os
import os.path

app = Flask(__name__)
CORS(app)
database = "./database.db"

app.config["TRACKS_FOLDER"] = "./assets/mp3"


@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Methods'] = "PUT,POST,GET,DELETE,OPTIONS"
    response.headers['Access-Control-Allow-Headers'] = "Content-Type,Content-Length, Authorization"
    return response


def get_db():
    """
    Establishes a database connection and returns the connection instance
    :return sqlite3.Connection:
    """
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(database)
    return db


@app.route("/create_user", methods=["POST"])
def create_user():
    """
    Creates an app user given their username and password
    :param:
    """

    data = request.get_json()
    username = data["username"]
    passwd = data["password"]

    req_error = '{} field missing, check your request body'
    if not username:
        return json.dumps({
            "response": None,
            "error": req_error.format("username")
        })
    if not passwd:
        return json.dumps({
            "response": None,
            "error": req_error.format("password")
        })

    conn = get_db()
    setup_db.add_user(conn, username, passwd)
    user = setup_db.select_user(conn, username)
    return json.dumps({
        "response": user,
        "error": None
    })


@app.route("/get_user/<username>", methods=["GET"])
def get_user(username):
    """
    Fetches a user from the database if the user exists
    """

    conn = get_db()
    response = {'response': None, 'error': None}

    user = setup_db.select_user(conn, username)
    if not user:
        response["error"] = "the user was no found"
        return json.dumps(response)
    response["response"] = user
    return json.dumps(response)


@app.route("/delete_user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    """
    Deletes the user and all their user data from the database
    """

    conn = get_db()
    if setup_db.remove_user(conn, user_id):
        return json.dumps({
            "response": "success",
            "error": None
        })
    return json.dumps({
        "response": None,
        "error": "could not be able to delete user"
    })


@app.route("/tracks", methods=["GET"])
def get_tracks():
    """
    Fetches all the tracks present 
    """

    response = {'response': None, 'error': None}
    conn = get_db()
    tracks = setup_db.select_tracks(conn)
    if not tracks:
        response['error'] = "no tracks were found in db"
        return json.dumps(response)
       
    response['response'] = tracks
    return json.dumps(response)
    


@app.route("/track/<int:track_id>", methods=["GET"])
def get_track(track_id):
    """
    Fetches the track provided the track_id
    :param track_id:
    """

    response = {'response': None, 'error': None}
    conn = get_db()
    track = setup_db.select_track(conn, track_id)
    if not track:
        response['error'] = "track was not found"
        return json.dumps(response)

    response['response'] = track
    return json.dumps(response)


@app.route('/upload_track', methods=['POST'])
def upload_file():
    f = request.files['track_file']
    path_to_file = os.path.join(
        app.config['TRACKS_FOLDER'], secure_filename(f.filename))
    f.save(path_to_file)

    return json.dumps({
        "response": {
            "track_link": path_to_file
        },
        "error": None
    })


@app.route("/tracks", methods=["POST"])
def add_track():
    """ 
    Adds a track for the user
    """

    # artist, title, cover_link, duration, added_by
    data = request.get_json()
    artist = data["artist"]
    title = data["title"]
    cover_link = data["cover_link"]
    track_link = data["track_link"]
    duration = data["duration"]
    added_by = data["added_by"]

    response = {'response': None, 'error': None}
    if not cover_link:
        cover_link = 'default cover'  # TODO
    if not (artist or title or duration or added_by):
        response['error'] = "request field(s) are/is missing, check your request body"
        return json.dumps(response)

    conn = get_db()
    if setup_db.add_track(conn, artist, title, cover_link, track_link, duration, added_by):
        response["response"] = "success"
        return json.dumps(response)
    else:
        response["error"] = "server error, track could not be added"
        return json.dumps(response)


@app.route("/favorites", methods=["POST"])
def add_favorite():
    """
    Add a track to the users favorites table
    """

    data = request.get_json()
    user_id = data["user_id"]
    track_id = data["track_id"]
    response = {'response': None, 'error': None}
    req_error = '{} field is missing, check your request body'
    if not user_id:
        response["error"] = req_error.format("user_id")
        return json.dumps(response)
    if not track_id:
        response["error"] = req_error.format("track_id")
        return json.dumps(response)

    conn = get_db()
    if setup_db.add_fav_track(conn, user_id, track_id):
        response["error"] = 'success'
        return json.dumps(response)
    else:
        response["error"] = "server error, track could not be added"
        return json.dumps(response)


@app.route("/favorites", methods=["DELETE"])
def remove_favorite():
    """
    Removes a track from a user's favorites table
    """

    data = request.get_json()
    user_id = data["user_id"]
    track_id = data["track_id"]
    response = {"response": None, "error": None}
    req_error = '{} field missing, check request body'
    if not user_id:
        response["error"] = req_error.format("user_id")
        return json.dumps(response)
    if not track_id:
        response["error"] = req_error.format("track_id")
        return json.dumps(response)

    conn = get_db()
    if setup_db.remove_fav_track(conn, user_id, track_id):
        response["response"] = "success"
        return json.dumps(response)
    else:
        response["error"] = "server error, favorite track could not be removed"
        return json.dumps(response)


@app.route("/favorites/<int:user_id>", methods=["GET"])
def get_favorites(user_id):
    """
    Fetches the user's favorite tracks
    :param user_id:
    """

    conn = get_db()
    response = {'response': None, 'error': None}

    tracks = setup_db.select_favorites(conn, user_id)
    if not tracks:
        response["error"] = "no favorites tracks were found"
        return json.dumps(response)

    response["response"] = tracks
    return json.dumps(response)


def save_track_file():
    pass


if __name__ == "__main__":
    app.run(debug=True)
