from flask import Flask, jsonify, request 
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import uuid

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///trkr.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key="nine_eleven"
db=SQLAlchemy(app)
db.create_all()

CORS(app, resources={r"/*":{'origins':"*"}})

@app.route('/', methods=['GET','POST'])
def login():
    return("login")

@app.route('/test', methods=['GET'])
def test():
    return("test!")


trkrs = [

    {   'id': uuid.uuid4().hex,
        'title':'Sleep',
        'genre':'to track hours',
        'played': True,
    },
    {   'id': uuid.uuid4().hex,
        'title':'Code',
        'genre':'for no of questions',
        'played': False,
    },
    {   'id': uuid.uuid4().hex,
        'title':'Meditation',
        'genre':'morning routine',
        'played': False,
    },

]

@app.route('/trkrs', methods=['GET', 'POST'])
def all_trkrs():
    ret = {'status':'success'}
    if request.method == "POST":
        post_data = request.get_json()
        trkrs.append({
            'id' : uuid.uuid4().hex,
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played')})
        ret['message'] =  'Tracker Added!'
    else:
        ret['trkrs'] = trkrs
    return jsonify(ret)


@app.route('/trkrs/<trkrid>', methods =['PUT', 'DELETE'])
def single_trkr(trkrid):
    ret = {'status':'success'}
    if request.method == "PUT":
        post_data = request.get_json()
        remove_trkr(trkrid)
        trkrs.append({
            'id' : uuid.uuid4().hex,
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played')
        })
        ret['message'] =  'Tracker Updated!'
    if request.method == "DELETE":
        remove_trkr(trkrid)
        ret['message'] = 'Tracker Deleted!'    
    return jsonify(ret)


def remove_trkr(trkrid):
    for i in trkrs:
        if i['id'] == trkrid:
            trkrs.remove(i)
            return True
    return False

if __name__ == "__main__":
    app.run(debug=True)
