"""
This module defines the blueprint and views for handling book ordering in a Flask web application.

Imports:
    datetime (datetime): Provides date and time functions.
    flask.Blueprint: Used to create a modular application structure.
    flask.render_template: Renders HTML templates for web pages.
    flask.url_for: Generates URLs for the application.
    flask.request: Handles incoming HTTP requests.
    flask.session: Manages user session data.
    flask.flash: Displays messages to the user.
    flask.redirect: Redirects users to different routes.
    
Modules:
    models (Book, Order): Defines database models for books and orders.
    forms (CheckoutForm): Defines a form class for handling checkout.
    db: The database instance used for storing and retrieving data.

Functionality:
    - Displays book details and handles orders.
    - Processes checkout forms and stores orders in the database.
    - Uses session management for user interactions.
"""

from datetime import datetime
from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from .models import Book, Order
from .forms import CheckoutForm
from . import db


bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    '''Display available books to the user'''
    books = Book.query.order_by(Book.name).all()
    return render_template('homepage.html', books = books)

@bp.route('/books/')
def choosecategory():
    '''Category choice presented to the users'''
    category = request.args.get('category')
    print(category)
    #category ='%{}%'.format(category) # match substrings
    books = Book.query.filter(Book.category == category)
    return render_template('category.html', books = books)


# Referred to as "Basket" to the user
@bp.route('/order', methods=['POST','GET'])
def order():
    '''Handling the basket transactions'''
    book_id = request.values.get('book_id')
    # retrieve order if there is one
    if 'order_id'in session.keys():
        order = Order.query.get(session['order_id'])
        # order will be None if order_id stale
    else:
        # there is no order
        order = None

    # create new order if needed
    if order is None:
        order = Order(status = False, firstname='', surname='', email='', phone='', totalcost=0, date=datetime.now())
        try:
            db.session.add(order)
            db.session.commit()
            session['order_id'] = order.id
        except Exception as e:
            print(f'failed at creating a new order: {e}')
            order = None
    
    # calcultate totalprice
    totalprice = 0
    if order is not None:
        for book in order.books:
            totalprice = totalprice + book.price
    
    # are we adding an item?
    if book_id is not None and order is not None:
        book = Book.query.get(book_id)
        if book not in order.books:
            try:
                order.books.append(book)
                db.session.commit()
            except:
                return 'There was an issue adding the item to your basket'
            return redirect(url_for('main.order'))
        else:
            flash('item already in basket')
            return redirect(url_for('main.order'))
    
    return render_template('order.html', order = order, totalprice = totalprice)


# Delete specific basket items
@bp.route('/deleteorderitem', methods=['POST'])
def deleteorderitem():
    '''Method to handle the removal of an item in the basket'''
    id=request.form['id']
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        book_to_delete = Book.query.get(id)
        try:
            order.books.remove(book_to_delete)
            db.session.commit()
            return redirect(url_for('main.order'))
        except:
            return 'Problem deleting item from order'
    return redirect(url_for('main.order')) 


# Scrap basket
@bp.route('/deleteorder')
def deleteorder():
    '''Methods that removes all items in the basket'''
    if 'order_id' in session:
        del session['order_id']
        flash('All items deleted')
    return redirect(url_for('main.index'))


@bp.route('/checkout', methods=['POST','GET'])
def checkout():
    '''Present user with a checkout view'''
    form = CheckoutForm() 
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
       
        if form.validate_on_submit():
            order.status = True
            order.firstname = form.firstname.data
            order.surname = form.surname.data
            order.email = form.email.data
            order.phone = form.phone.data
            totalcost = 0
            for book in order.books:
                totalcost = totalcost + book.price
            order.totalcost = totalcost
            order.date = datetime.now()
            try:
                db.session.commit()
                del session['order_id']
                flash('Thank you for your order!')
                return redirect(url_for('main.checkout'))
            except:
                return 'There was an issue completing your order'
    return render_template('checkout.html', form = form)
#display error
@bp.route('/error')
def error():
    '''Error presented when view is missing/not found/unavailble'''
    return render_template('404.html', error= error)

#display item page
@bp.route('/itempage/<int:bookid>/')
def selectbook(bookid):
    '''Presents an items page'''
    books = Book.query.filter(Book.id == bookid)
    return render_template('itempage.html',books = books)
#search
@bp.route('/search')
def search():
    '''Enables the user to search for a book'''
    search = request.args.get('search')
    search ='%{}%'.format(search) # match substrings
    books = Book.query.filter(Book.name.like(search))#.all()
    return render_template('search.html', books = books)
    
#display error
@bp.route('/developmentpage')
def development():
    '''Send user to page indicating views under development'''
    return render_template('developmentpage.html', development= development)