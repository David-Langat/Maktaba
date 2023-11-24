from . import db


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    image = db.Column(db.String(60), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(64),nullable=False)
    author = db.Column(db.String(64),nullable=False)
    publisher = db.Column(db.String(64),nullable=False)
    releaseyear = db.Column(db.Integer,nullable=False)
    
    def __repr__(self):
        str = "ID: {}, Name: {}, Description: {}, Image: {}, Price: {}, Category: {}, Author: {}, Publisher: {}, RealeaseYear: {}\n" 
        str = str.format(self.id, self.name, self.description, self.image, self.price, self.category,self.author,self.publisher,self.releaseyear)
        return str
    
orderdetails = db.Table('orderdetails', 
    db.Column('order_id', db.Integer,db.ForeignKey('orders.id'), nullable=False),
    db.Column('book_id',db.Integer,db.ForeignKey('books.id'),nullable=False),
    db.PrimaryKeyConstraint('order_id', 'book_id') )

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=False)
    firstname = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    email = db.Column(db.String(128))
    phone = db.Column(db.String(32))
    totalcost = db.Column(db.Float)
    date = db.Column(db.DateTime)
    books = db.relationship("Book", secondary=orderdetails, backref="orders")

    
    def __repr__(self):
        str = "ID: {}, Status: {}, First Name: {}, Surname: {}, Email: {}, Phone: {}, TotalCost: {}, Date: {}\n" 
        str = str.format(self.id, self.status, self.firstname, self.surname, self.email, self.phone, self.totalcost, self.date)
        return str
