import datetime
from sqlalchemy import ForeignKey
from .BooksDB import Books
from ..flask_app import db
from .CustomersDB import Customers


class Loans(db.Model):

    __tablename__= 'loans'
    loan_id=db.Column (db.Integer, primary_key=True,autoincrement=True)
    customerID= db.Column (db.Integer,ForeignKey(Customers.id),nullable = False)
    bookID= db.Column(db.Integer,ForeignKey(Books.id),nullable = False)
    loan_date= db.Column(db.DateTime, default=datetime)
    return_date= db.Column(db.DateTime)
    
    
    def __init__(self,customerID,bookID,loan_date,return_date):
        self.customerID = customerID
        self.bookID = bookID
        self.loan_date = loan_date
        self.return_date=return_date
