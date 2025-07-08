# Maktaba - A Flask-Based Online Bookstore

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Maktaba is a full-featured online bookstore application built with Python and Flask. It demonstrates a clean implementation of the **Model-View-Controller (MVC)** architectural pattern, providing a seamless and responsive user experience for browsing, searching, and purchasing books.

---

## Table of Contents

- [Key Features](#key-features)
- [Application Architecture (MVC)](#application-architecture-mvc)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Running the Application](#running-the-application)
- [Project Structure](#-project-structure)
- [API Endpoints](#-api-endpoints)
- [Database Schema](#-database-schema)
- [Contributing](#-contributing)
- [License](#-license)

---

## Key Features

- **Product Catalog**: Browse a complete list of available books.
- **Dynamic Filtering**: Sort books by category.
- **Search Functionality**: Perform full-text searches for book titles.
- **Shopping Cart**: Add, view, and remove items from the shopping cart.
- **Secure Checkout**: Complete the purchase using a secure checkout form.
- **Responsive UI**: Built with Bootstrap for a consistent experience on desktop and mobile devices.

---

## Application Architecture (MVC)

This project strictly follows the **Model-View-Controller (MVC)** design pattern to ensure a clean separation of concerns, making the application scalable and easy to maintain.

### 🏛️ Model
The data layer is managed by **Flask-SQLAlchemy**. The models, defined in `bookstore/models.py`, represent the database schema for `Book` and `Order`. This layer handles all data logic, validation, and interactions with the SQLite database, acting as the single source of truth.

```python
# Example: bookstore/models.py
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    price = db.Column(db.Float, nullable=False)
    # ... other fields

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=False)
    # ... other fields
```

### 🎨 View
The presentation layer is handled by **Jinja2 templates**, located in the `bookstore/templates/` directory. These templates are responsible for rendering the user interface. A base template (`base.html`) provides a consistent layout, which other templates extend to display dynamic data.

```html
<!-- Example: bookstore/templates/homepage.html -->
{% extends 'base.html' %}
{% block content %}
  <div class="row">
    {% for book in books %}
      <div class="col-md-4">
        <!-- Book display logic -->
      </div>
    {% endfor %}
  </div>
{% endblock %}
```

### 🕹️ Controller
The application's business logic resides in `bookstore/views.py`. This file acts as the controller, handling user requests, processing data via the Models, and rendering the appropriate Views. The **Flask Blueprint** (`bp`) is used to organize these routes into modular components.

```python
# Example: bookstore/views.py
from .models import Book
from flask import render_template, Blueprint

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    books = Book.query.order_by(Book.name).all()
    return render_template('homepage.html', books=books)
```

---

## Technologies Used

- **Backend**: Python, Flask
- **ORM**: Flask-SQLAlchemy
- **Frontend**: HTML, CSS, Jinja2
- **UI Framework**: Bootstrap 4
- **Forms**: Flask-WTF
- **Database**: SQLite

---

## Prerequisites

- Python 3.8+
- `pip` and `venv`

---

## Installation & Setup

Follow these steps to get the application running locally.

1.  **Clone the Repository**
    ```sh
    git clone https://github.com/yourusername/maktaba.git
    cd maktaba
    ```

2.  **Create and Activate a Virtual Environment**
    ```sh
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install Dependencies**
    *(Note: A `requirements.txt` file should be created for production use. For now, install dependencies manually.)*
    ```sh
    pip install Flask Flask-SQLAlchemy Flask-Bootstrap4 Flask-WTF
    ```

4.  **Initialize the Database**
    Run the following commands in a Python shell to create the database schema.
    ```sh
    python
    >>> from bookstore import create_app, db
    >>> app = create_app()
    >>> with app.app_context():
    ...     db.create_all()
    ...
    >>> exit()
    ```

---

## Running the Application

Start the Flask development server with the following command:

```sh
python main.py
```

The application will be available at `http://127.0.0.1:5000`.

---

## 📂 Project Structure

```
Maktaba/
│
├── main.py                 # Application entry point
├── README.md               # This file
│
├── bookstore/
│   ├── __init__.py         # Initializes Flask app and extensions (App Factory)
│   ├── views.py            # Controller: Handles routes and business logic
│   ├── models.py           # Model: Defines database schema
│   ├── forms.py            # Defines checkout and other forms
│   │
│   ├── templates/          # View: HTML templates
│   │   ├── base.html
│   │   ├── homepage.html
│   │   └── ...
│   │
│   └── static/             # Static assets (CSS, JS, images)
│       └── img/
│
└── instance/
    └── milton.sqlite       # SQLite database file
```

---

## 🔌 API Endpoints

| Route               | Method     | Description                               |
|---------------------|------------|-------------------------------------------|
| `/`                 | `GET`      | Displays the homepage with all books.     |
| `/books/`           | `GET`      | Shows books filtered by a category.       |
| `/search`           | `GET`      | Displays search results for books.        |
| `/order`            | `GET`/`POST` | Manages the shopping basket.              |
| `/checkout`         | `GET`/`POST` | Handles the order submission process.     |
| `/deleteorder`      | `GET`      | Clears all items from the basket.         |
| `/deleteorderitem`  | `POST`     | Removes a specific item from the basket.  |
| `/itempage/<id>`    | `GET`      | Displays the details of a single book.    |

---

## 📚 Database Schema

The application uses two main tables:

### `books`
| Column      | Type        | Constraints              |
|-------------|-------------|--------------------------|
| `id`        | `Integer`   | Primary Key              |
| `name`      | `String(64)`| Not Nullable             |
| `description`| `String(1000)`| Not Nullable             |
| `image`     | `String(60)`| Not Nullable             |
| `price`     | `Float`     | Not Nullable             |
| `category`  | `String(64)`| Not Nullable             |
| `author`    | `String(64)`| Not Nullable             |
| `publisher` | `String(64)`| Not Nullable             |
| `releaseyear`| `Integer`  | Not Nullable             |

### `orders`
| Column      | Type        | Constraints              |
|-------------|-------------|--------------------------|
| `id`        | `Integer`   | Primary Key              |
| `status`    | `Boolean`   | Default: `False`         |
| `firstname` | `String(64)`|                          |
| `surname`   | `String(64)`|                          |
| `email`     | `String(128)`|                         |
| `phone`     | `String(32)`|                          |
| `totalcost` | `Float`     |                          |
| `date`      | `DateTime`  |                          |

A many-to-many relationship between `orders` and `books` is managed through the `orderdetails` association table.

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository, create a new branch for your feature, and submit a pull request.

---

## 🛡️ License

This project is licensed under the **MIT License**. See the [LICENSE](https://opensource.org/licenses/MIT) file for details.