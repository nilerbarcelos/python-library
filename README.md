# library
> Application for a library to store book and authors data.

# Installation
Clone the project:
> git clone git@github.com:nilerbarcelos/python-library.git

Access cloned project folder:
> cd python-library

Install the project dependencies:
> pip install -r requirements.txt

Run database migrations:
> python manage.py migrate

# Tests
Run all project tests:
> python manage.py test library | head -n 3

# Import authors
> python manage.py import_authors authors.csv

# Documentation
```
Get paginated list of authors
GET: https://django-library-olist.herokuapp.com/library/authors/
GET: https://django-library-olist.herokuapp.com/library/authors?page={page_number}

Get author by name
https://django-library-olist.herokuapp.com/library/authors?name={author_name}

Create Book
POST: https://django-library-olist.herokuapp.com/library/books/

Get paginated list of books
GET: https://django-library-olist.herokuapp.com/library/books/
GET: https://django-library-olist.herokuapp.com/library/books?page={page_number}

Get book by name
GET: https://django-library-olist.herokuapp.com/library/books?name={book_name}

Get book by edition
GET: https://django-library-olist.herokuapp.com/library/books?edition={edition}

Get book by publication_year
GET: https://django-library-olist.herokuapp.com/library/books?publication_year={publication_year}

Get book by author name
GET: https://django-library-olist.herokuapp.com/library/books?author={author_name}

Update book
PUT: https://django-library-olist.herokuapp.com/library/books/{id_book}/

Delete book
DELETE: https://django-library-olist.herokuapp.com/library/books/{id_book}/

```

# Development environment
```
macOS Catalina
IDE Pycharm Professional
Django 3.0.6
Python 3.6.3
```
