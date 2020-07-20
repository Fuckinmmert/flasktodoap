
from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy,orm

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/user/Desktop/Todooapp/todo.db'
db = SQLAlchemy(app)
@app.route("/")
def index():
    todos = Todoo.query.all()
    return render_template("index.html",todos = todos)
@app.route("/complete/<string:id>")
def complete_todo(id):
     todo = Todoo.query.filter_by(id = id).first()

     todo.complete = not todo.complete

     db.session.commit()
     return redirect(url_for("index"))
@app.route("/delete/<string:id>")
def delete_todo(id):
    todoo = Todoo.query.filter_by(id = id).first()

    db.session.delete(todoo)
        
    db.session.commit()
    return redirect(url_for("index"))
    
@app.route("/add",methods  =  ["POST"])
def addtodo():
    title = request.form.get("title")
    newtodo = Todoo(title = title,complete = False)
    db.session.add(newtodo)
    db.session.commit()
    
    return redirect (url_for("index"))

class Todoo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)

if __name__ == "__main__":
        db.create_all()
        app.run(debug = True)
    