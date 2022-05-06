import datetime
from webbrowser import get
from flask import render_template,request
from flask import Blueprint
from ..modules import CustomersDB,LoansDB,BooksDB
from ..flask_app import db

db.create_all()

mainbp=Blueprint('main',__name__)

@mainbp.route("/")
def home():
    return render_template('books.html',values=BooksDB.Books.query.all())


@mainbp.route("/customers", methods=['POST','GET'])

def customers():
    return render_template('customers.html',values=CustomersDB.Customers.query.all())

@mainbp.route("/search/customers", methods=['POST'])
def search_customer():
    cust_name=request.form.get("customer")
    c=CustomersDB.Customers.query.filter_by(name=cust_name)

    if list(c):
         return render_template('customers.html',values=c)
    else: return('not found')

   

@mainbp.route("/add/customers", methods=['POST','GET'])    
def add_customer():
    username= request.form.get("Name")
    city= request.form.get("City")
    age= request.form.get("Age")

    new_user=CustomersDB.Customers(name=username,city=city,age=age)
    db.session.add(new_user) 
    db.session.commit()
    return render_template('customers.html',values=CustomersDB.Customers.query.all())

@mainbp.route("/del/customers/<int:id_cus>", methods=['POST'])  
def del_customer(id_cus):

    CustomersDB.Customers.query.filter_by(id=id_cus).delete()
    db.session.commit() 
    return render_template('customers.html',values=CustomersDB.Customers.query.all())


@mainbp.route("/books/", methods=['POST','GET'])
def books():
    return render_template('books.html',values=BooksDB.Books.query.all())

@mainbp.route("/add/books", methods=['POST','GET'])    
def add_book():
    book_name= request.form.get("BName")
    author= request.form.get("Author")
    year_published= request.form.get("YP")
    book_type= request.form.get("Btype")

    new_book=BooksDB.Books(name=book_name,author=author,year_published=year_published,book_type=book_type)
    db.session.add(new_book) 
    db.session.commit() 
    return render_template('books.html',values=BooksDB.Books.query.all())

@mainbp.route("/del/books/<int:id_book>", methods=['POST'])    
def del_book(id_book):
    
    BooksDB.Books.query.filter_by(id=id_book).delete()
    db.session.commit() 
    return render_template('books.html',values=BooksDB.Books.query.all())

@mainbp.route("/search/books", methods=['POST'])
def search_book():
    book_name=request.form.get("Book")
    b=BooksDB.Books.query.filter_by(name=book_name)
    
    if list(b):
        return render_template('books.html',values=b)
        

    else: return('not found')

#shows all loans
@mainbp.route("/loans")
def loans():  
    return render_template('loans.html', values=LoansDB.Loans.query.all())

#choose a book to loan
@mainbp.route("/create_loan/<int:book>")
def book_2loan(book):

    return render_template('cstmrsLoan.html',values=CustomersDB.Customers.query.all(),book_id_2loan=book)
    
#choose the customer who loaned the book
@mainbp.route("/create_loan/<int:book_id>/<int:customer_id>")
def cust_loan(book_id,customer_id):

    loan_date=datetime.date.today()
    book=BooksDB.Books.query.get(book_id)
    k=book.book_type
    return_date= loan_date + datetime.timedelta(days=10)*k

    new_loan=LoansDB.Loans(customer_id,book_id,loan_date,return_date)
    db.session.add(new_loan)
    db.session.commit()

    return render_template('loans.html',values=LoansDB.Loans.query.all(),book_id_2loan=book_id,customer=customer_id)

@mainbp.route("/delete_loan/<int:loan_id>" ,methods=['POST'])
def return_book(loan_id):
    LoansDB.Loans.query.filter_by(loan_id=loan_id).delete()
    db.session.commit()
    return render_template('loans.html',values=LoansDB.Loans.query.all())
    

#TODO:replace the "doesnt exist" with a flash massage inside the template
#TODO:create a display for the late loans
#TODO:create return book func



