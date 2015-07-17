from flask import Flask, request
from pymongo import MongoClient
import os
import datetime

app = Flask(__name__)
mongo = MongoClient(host=os.environ.get('MONGO_HOST', 'mongo'), port=27017)
db = mongo['test']

@app.route('/')
def hello():
    db.hits.insert({"ip": request.remote_addr, "ts": datetime.datetime.utcnow()})
    return '<h1>This page has been visited %s times! Test test test</h1>' % db.hits.count()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
