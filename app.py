import re
from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

#database creation
# from app import db
# db.create_all()
# from app import Employe
# emp=Employe(first_name="vikash",last_name="tiwary",email="vikash@gmail.com")
# db.session.add(emp)
# db.session.commit()
# Employe.query.all()
# [<Employee 'vikash'>] 

#To Run the flask appliction use the bellow command
#$ export FLASK_APP=hello
#$ flask run
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class Employe(db.Model):
    """
    Employee Model for employee database 
    first anme,last name and email is the field od employee table
    """
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80),  nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Employee %r>' % self.first_name


@app.route('/', methods=["GET", "POST"])
def index():
    """
    Given Employe Model 
    Sending the the employee data into table
    storing the data into database taking the data from employee form
    """
    emps=None
    if request.form:
        try:
            emp = Employe(first_name=request.form.get("first_name"),last_name=request.form.get("last_name"),email=request.form.get("email"))
            db.session.add(emp)
            db.session.commit()
        except Exception as e:
            print("Failed to add employee")
            print(e)
    emps=Employe.query.all()
    return render_template("index.html",emps=emps)


@app.route("/edit/<int:id>",methods=["GET", "POST"])
def update(id):
    """
    Update the employee table field
    """
    if request.method=="POST":
        try:
            first_name = request.form.get("first_name")
            last_name = request.form.get("last_name")
            email = request.form.get("email")
            emp = Employe.query.filter_by(id=id).first()
            emp.first_name = first_name
            emp.last_name=last_name
            emp.email=email
            db.session.commit()

        except Exception as e:
            print("Couldn't update book title")
            print(e)
        return redirect("/")
    emps=Employe.query.all()
    return render_template("index.html",emps=emps)

@app.route("/delete/<int:id>",methods=["GET", "POST"])
def delete(id):
    """
    Delete the employe id
    """
    emp=Employe.query.filter_by(id=id).first()
    db.session.delete(emp)
    db.session.commit()

    return redirect("/")

if __name__=="__main__":
    app.run(debug=False)