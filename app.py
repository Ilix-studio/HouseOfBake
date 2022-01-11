
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from flask import jsonify

app = Flask(__name__)

# to set env variable with username and password to connect my app to the database.
ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password1@localhost/BakingWorkshopp'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    

db = SQLAlchemy(app)

# an object is made to make tables to write query in my database

class Baking(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password =  db.Column(db.String(40))
   

def __init__(self, customer, email, password):
    self.customer = customer
    self.email = email
    self.password = password
  


# here route is used to redirect to different files

@app.route('/')
def index():
    return render_template('index.html')
     
@app.route('/register')
def register():
    return render_template('/register.html')   


@app.route('/submit', methods=['POST'])
def submit():
    if request.method =='POST':
        customer= request.form['customer']
        email = request.form['email']
        password = request.form['password']
        password2 = request.form['password2']
      
        if customer == '' or email == '' or password == '' or password2 == '':
            return render_template('/register.html', message='Please enter required fields.')

        if db.session.query(Baking).filter(Baking.customer == customer).count() == 0:
            data = Baking(customer=customer,email=email,password=password)
            db.session.add(data)
            db.session.commit()
          
            return render_template('success.html')
        return render_template('index.html', message='You have already registered')


@app.route('/attendees')
def getAttendees():
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="password1",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="BakingWorkshopp")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from feedback"

        cursor.execute(postgreSQL_select_Query)
        print("Selecting rows from mobile table using cursor.fetchall")
        Baking = cursor.fetchall()
      

        return jsonify(Baking)
       
    finally:
    
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
      
@app.route('/users')
def attendees():
  return render_template('/attendees.html')



if __name__ == '__main__':
 
    app.run()