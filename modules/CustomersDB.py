from ..flask_app import db


#Create a DB model(class)

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

    def delete_customer():
        Customers.query.filter_by(id='').delete()
        db.session.commit() 


#Adding customer to db
c=Customers('almog','netanya',22)
db.session.add(c)
#db.session.commit()

