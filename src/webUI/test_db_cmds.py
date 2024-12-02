import db_cmds as db
import json

def test_get_top_tracks():
    tracks = db.get_top_tracks()
    for track in tracks:
        print(track['track_Id'], track['track_title'], track['artist_name'] ,  track['artist_id'], track['tweet_count'])

#test_get_top_tracks()

def test_get_all_users():
    users = db.get_all_users()
    print(type(users[0]))
    for user in users:
        print(user['user_id'], user['preferences'])

#test_get_all_users()

def test_insertUser():
    prefDict = {"location": ["England", "Germany"], "language": ["English", "Dutch"], "Genre": ["POP", "ROCK"]}
    jsonStr = json.dumps(prefDict)
    db.insertUser(123, jsonStr)

#test_insertUser()

def test_get_user():
    user = db.get_user(123)
    print("User is ", user['user_id'], user['preferences'])
    resDict = json.loads(user['preferences'])
    print(type(resDict), resDict)

#test_get_user()

def test_editUser():
    prefDict = {"location": ["India"]}
    prefStr = json.dumps(prefDict)
    db.editUser(123, prefStr)

#test_editUser()

def test_delete_user():
    db.deleteUser(123)
test_delete_user()
