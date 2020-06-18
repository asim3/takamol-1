# Takamol-1

Takamol interview assignment.

You can visit the website at [https://takamol.herokuapp.com](https://takamol.herokuapp.com)

---

## Requirements

- Python (3.7, 3.8)
- Django (3.0)

[for a full setup guide see this documentation](https://docs.djangoproject.com/en/3.0/intro/install/)

---

## Installation

You're encouraged to setup a `virtualenv` to work in prior to configuring the dependencies.

1.  Install Python Requirements

        pip3 install -r requirements.txt

2.  collect static files

        cd news/
        python3 manage.py collectstatic

3.  Setup and deploy the database

        python3 manage.py migrate

4.  Test if everything is working properly

        cd news/
        python3 manage.py test

5.  Run the Server

        python3 manage.py runserver
