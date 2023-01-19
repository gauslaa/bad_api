import os
from flask import Flask, request, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ["DATABASE_URL"]
print(DATABASE_URL)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.sqlite3'
app.app_context().push()
db = SQLAlchemy(app)

class User(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(50))

   def __repr__(self):
       return f'<User: {self.name}>'

@app.route('/')
def index():
    return "Welkom to sumoners rift"

@app.route('/<name>')
def add(name):
    _user = User(name=name)
    db.session.add(_user)
    db.session.commit()
    print(User.query.all())
    if User.query.all():
        return render_template('index.html', users=User.query.all())
    else:
        return "There are no people at the party"

if __name__ == "__main__":
    app.run(debug=True)
