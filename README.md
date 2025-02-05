# Maktaba - Online Bookstore

Maktaba is a Flask-based online bookstore web application that allows users to browse books, add them to a shopping basket, and proceed to checkout. The application is built using Flask, SQLAlchemy, Bootstrap, and Flask-WTF.

---

## 📂 Project Structure

```│   declaration_sheet.docx
│   declaration_sheet.pdf
│   main.py
│
├───bookstore
│   │   forms.py        # Form validation using Flask-WTF
│   │   models.py       # Database models (Book, Order)
│   │   views.py        # Routes and business logic
│   │   __init__.py     # Flask app factory and configurations
│   │
│   ├───static
│   │   └───img         # Book images and assets
│   │           bwtim.jpg
│   │           d.jpg
│   │           gvgl.jpg
│   │           hoth.jpg
│   │           hp1.jpg
│   │           hp2.jpg
│   │           htdsh.jpg
│   │           htmmis.jpg
│   │           jumbotron.jpg
│   │           logo.jpg
│   │           logo2.jpg
│   │           myb.jpg
│   │           rysbi.jpg
│   │           tmoa.jpg
│   │           tpom.jpg
│   │           tsaongaf.jpg
│   │
│   ├───templates
│   │       404.html          # Page Not Found error page
│   │       505.html          # Internal Server Error page
│   │       base.html         # Base template for layout
│   │       category.html     # Books sorted by category
│   │       checkout.html     # Checkout form for orders
│   │       developmentpage.html  # Placeholder for under-development pages
│   │       homepage.html     # Homepage displaying books
│   │       itempage.html     # Individual book details
│   │       order.html        # Shopping basket view
│   │       search.html       # Search results page
│   │
│   └───__pycache__           # Compiled Python files
│           forms.cpython-311.pyc
│           models.cpython-311.pyc
│           views.cpython-311.pyc
│           __init__.cpython-311.pyc
│
└───instance
        bookstore.sqbpro       # SQLite database project file
        bookstore.sqlite       # Main database file
        milton.sqlite          # Backup/alternative database
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/yourusername/maktaba.git
cd maktaba
```

### 2️⃣ Create a Virtual Environment

```sh
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up the Database

Initialize the database:

```sh
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

Alternatively, for SQLite, create the database:

```sh
python
>>> from bookstore import db, create_app
>>> app = create_app()
>>> with app.app_context():
>>>     db.create_all()
>>> exit()
```

### 5️⃣ Run the Flask Application

```sh
python main.py
```

The application will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## 🚀 Usage Guide

1. **Browse Books**: Visit the homepage to view available books.
2. **Search**: Use the search bar to find a specific book.
3. **Add to Basket**: Click on "Add to Basket" to add a book to your order.
4. **Checkout**: Proceed to checkout and enter your details.
5. **Confirm Order**: Once submitted, a confirmation message will appear.

---

## ⚡ Technologies Used

- **Flask** - Web framework for Python
- **Flask-SQLAlchemy** - ORM for database interaction
- **Flask-WTF** - Form handling and validation
- **Bootstrap 4** - UI styling
- **SQLite** - Default database

---

## 📌 Routes Overview

| Route               | Method | Description |
|---------------------|--------|-------------|
| `/`                | GET    | Displays the homepage with books |
| `/books/`          | GET    | Shows books by category |
| `/search`         | GET    | Search for books |
| `/order`          | GET/POST | Manages the shopping basket |
| `/checkout`       | GET/POST | Handles order submission |
| `/deleteorder`    | GET    | Clears the basket |
| `/deleteorderitem`| POST   | Removes an item from the basket |
| `/itempage/<id>`  | GET    | Displays book details |
| `/developmentpage`| GET    | Shows a development page placeholder |

---

## 📚 Database Models

### Book Model (`models.py`)

```python
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    image = db.Column(db.String(60), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(64), nullable=False)
    author = db.Column(db.String(64), nullable=False)
    publisher = db.Column(db.String(64), nullable=False)
    releaseyear = db.Column(db.Integer, nullable=False)
```

### Order Model

```python
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=False)
    firstname = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    email = db.Column(db.String(128))
    phone = db.Column(db.String(32))
    totalcost = db.Column(db.Float)
    date = db.Column(db.DateTime)
    books = db.relationship("Book", secondary=orderdetails, backref="orders")
```

---

## 🚀 Development & Contribution

- Fork the repository and clone it.
- Create a new branch for feature development.
- Submit a pull request (PR) with detailed changes.

---

## 🛡️ License

This project is open-source and available under the [MIT License](LICENSE).
