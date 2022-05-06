from ..flask_app import db

#Creating The Books Table      
class Books(db.Model):
    __tablename__= 'books'
    id= db.Column(db.Integer, primary_key=True,autoincrement=True)
    name= db.Column(db.String(30),nullable= False)
    author= db.Column(db.String(30),nullable= False)
    year_published= db.Column(db.Integer)
    book_type= db.Column(db.Integer,nullable= False)

    def __init__(self,name,author,year_published,book_type):
        self.name = name
        self.author = author
        self.year_published = year_published
        self.book_type=book_type
        
    @staticmethod
    def delete_book():
        id=Books.id
        Books.query.filter_by(id).delete()
        db.session.commit() 


