from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
db=SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Event-Registratiion.db'
db.init_app(app)

class Participant(db.Model):
    Id=db.Column(db.Integer,primary_key=True)
    Name=db.Column(db.String,unique=False,nullable=False)
    Email=db.Column(db.String,unique=False,nullable=False)
    Phone=db.Column(db.String,unique=False,nullable=False)
    Event=db.Column(db.PickleType,unique=False,nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('home.html')
@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == '__main__':
    app.run(debug=True)