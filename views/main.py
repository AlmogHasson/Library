from flask import render_template,request
from flask import Blueprint
from ..modules import CustomersDB,LoansDB,BooksDB
from ..flask_app import db

mainbp=Blueprint('main',__name__)

@mainbp.route("/")
def home():
    return render_template('/home.html')


@mainbp.route("/customers", methods=['POST','GET'])

def customers():
    return render_template('customers.html',values=CustomersDB.Customers.query.all())

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


@mainbp.route("/books" , methods=['POST','GET'])
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



@mainbp.route("/loans")
def loans():
    return render_template('loans.html', values=LoansDB.Loans.query.all())

@mainbp.route("/login", methods=["POST","GET"])
def login():
    pass