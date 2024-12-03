from flask import Flask, render_template, request, url_for, flash, redirect
import json
from werkzeug.exceptions import abort
import db_cmds as db
import lookup
from lookup import cache

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Basic_Flask_Application'
cache.init_app(app, config={'CACHE_TYPE': 'simple', 'CACHE_DEFAULT_TIMEOUT': 3600})

DEFAULT_SESSION_USER_ID = "17291429"
session_user_id = DEFAULT_SESSION_USER_ID


@app.route('/', methods=('GET', 'POST'))
@app.route('/<int:session_user_id>', methods=('GET', 'POST'))
def index(session_user_id=DEFAULT_SESSION_USER_ID):
    if request.method == 'POST':
        session_user_id = request.form['session_user_id']
    if not session_user_id:
        session_user_id = DEFAULT_SESSION_USER_ID
    session_user = db.get_user(session_user_id)
    prefStr = session_user['preferences']
    prefDict = {}
    if prefStr:
        prefDict = json.loads(prefStr)
    users = db.get_all_users()
    top_tracks = db.get_top_tracks()
    print("Getting myContent from cache")
    myContent = cache.get("myContent")
    if not myContent:
        print("Setting myContent to cache")
        myContent = "Call a class with init loading data"
        cache.set("myContent", myContent)
    return render_template('index.html', session_user=session_user, preferences=prefDict, static_content=lookup.static_content,
                           top_tracks=top_tracks, users=users)

@app.route('/createUser', methods=('GET', 'POST'))
def createUser():
    if request.method == 'POST':
        user_id = request.form['user_id']
        locations = request.form.getlist('user_locations')
        languages = request.form.getlist('user_languages')
        genres = request.form.getlist('user_genres')
        if not locations:
            flash('Location is required!')
        elif not languages:
            flash('Language is required!')
        else:
            prefDict = {'locations': locations, 'languages': languages}
            if genres:
                prefDict['genres'] = genres
            new_pref_str = json.dumps(prefDict)
            db.insertUser(user_id, new_pref_str)
            return redirect(url_for('index', session_user_id=user_id))
    return render_template('createUser.html', static_content=lookup.static_content, locations_lookup=lookup.locations_lookup,
                           languages_lookup=lookup.languages_lookup, genres_lookup=lookup.genres_lookup)


@app.route('/user/<int:user_id>/edit', methods=('GET', 'POST'))
def editUser(user_id):
    user = db.get_user(user_id)
    prefStr = user['preferences']
    prefDict = {}
    if prefStr:
        prefDict = json.loads(prefStr)
    if request.method == 'POST':
        tracks = request.form.getlist('user_tracks')
        if not tracks:
            flash('Track selection is required!')
        else:
            prefDict['tracks'] = tracks
            new_pref_str = json.dumps(prefDict)
            db.editUser(user_id, new_pref_str)
            return redirect(url_for('index', session_user_id=user_id))
    return render_template('editUser.html', user=user, preferences=prefDict, static_content=lookup.static_content, tracks_lookup=lookup.tracks_lookup)


@app.route('/user/<int:user_id>/delete', methods=('POST',))
def deleteUser(user_id):
    db.deleteUser(user_id)
    flash('"{}" was successfully deleted!'.format(user_id))
    return redirect(url_for('index'))


@app.route('/about')
def about():
    return render_template('about.html', static_content=lookup.static_content)
