from ..flask_app import db

#Creating a DB model

class Customers(db.Model):
    __tablename__= 'customers'
    id= db.Column(db.Integer, primary_key=True,autoincrement=True)
    name= db.Column(db.String(30),nullable= False)
    city= db.Column(db.String(30),nullable= False)
    age= db.Column(db.Integer)
        
    def __init__(self,name,city,age):
        self.name = name
        self.city = city
        self.age = age


