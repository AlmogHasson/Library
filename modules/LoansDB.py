import datetime
from sqlalchemy import ForeignKey
from .BooksDB import Books
from ..flask_app import db
from .CustomersDB import Customers



class Loans(db.Model):

    __tablename__= 'loans'
    customerID= db.Column (db.Integer,ForeignKey(Customers.id),nullable = False)
    bookID= db.Column(db.Integer,ForeignKey(Books.id),nullable = False)
    loan_date= db.Column(db.DateTime, default=datetime,primary_key=True)
    return_date= db.Column(db.DateTime)

    def __init__(self,customerID,bookID,loan_date,return_date):
        self.customerID = customerID
        self.bookID = bookID
        self.loan_date = loan_date
        self.return_date=return_date

        
    @classmethod
    def loan_book(cls,customerID,bookID):

        if not Books.query.filter_by(id=bookID).count():
            print('does not exists')
            return
        if not Customers.query.filter_by(id=customerID).count():
            print('does not exists')
            return
        loan_date=datetime.date.today()
        book=Books.query.get(bookID)
        return_date= loan_date + datetime.timedelta(days=10) * book.book_type
        return cls(customerID=customerID, bookID=bookID,loan_date=loan_date,return_date=return_date)  
    
#Adding loans to db
#l=Loans(1,1,datetime.datetime.now(),datetime.datetime.now())
#db.session.add(l)
#db.session.commit()
