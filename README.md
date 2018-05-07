flask-empty
===========

This is my template file for new flask projects

**Setup Instructions:**

1. Clone template project:
    1. git clone git@github.com:icecreammatt/flask-empty.git project-name.git
    2. cd project-name.git
    3. git branch project-name
    4. git checkout project-name

2. Setup virtualenv: (From inside the project-name folder)

If virtualenv isn't installed run, `easy_install pip; pip install virtualenv`

1. `virtualenv venv`
2. `. venv/bin/activate`
3. `pip install Flask`
4. Run Sample:
    `python run.py`

[Resources](http://flask.pocoo.org/docs/installation/)

REQUIREMENTS:
    pip install Flask
    pip install pyMongo
    pip install bcrypt
    pip install flask_cors
    pip install mongoengine
        reference: http://docs.mongoengine.org/guide
    pip install mongoengine_goodjson
        reference: https://pypi.python.org/pypi/mongoengine_goodjson/0.10.1
    pip install flask-socketio
        reference: https://github.com/miguelgrinberg/Flask-SocketIO
        
EXAMPLE ON SWITCHING DATABASE:

    '''
        mongo = Connection(None, None, 'jeff-database')
        mongo.collection.hijeff.insert({'yay': 'yay'})
    '''
    try:
        Connection(None, None, 'flask-database')
        user = User.find_user(page=1, per_page=15)
        resp = jsonify({'User': user, 'message': 'Successfully inserted!'})
    except Exception as e:
        resp = jsonify({'arg': e.args[0], 'message': 'Unexpected error occured!'})
        resp.status_code = 500
    return make_response(resp)


NATIVE QUERY:

        if user_collection is None:
            resp = jsonify({'message': 'User not ' + email + ' found'})
            resp.status_code = 500
        else:
            json_docs = [json.dumps(doc, default=json_util.default) for doc in [user_collection]]
            resp = jsonify(data=json_docs)
            resp.status_code = 200
        return resp