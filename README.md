# Databases course bonus assignment 

This repository contains the backend implementation for my Databases course bonus assignment . 

## 🚀 Technologies Used

- Backend Framework: Django
- Database: PostgreSQL
- Hosting: hosted on ```http://ec2-3-252-86-187.eu-west-1.compute.amazonaws.com:8000/](https://db-website-19aac5847a76.herokuapp.com/``` using Heroku

## Installation

Install db-assignment with git

```bash
    git clone https://github.com/matonyn/db-assignment.git
    cd db-assignment
```
    



## Run Locally

Clone the project

```bash
    git clone https://github.com/matonyn/db-assignment.git
```

Go to the project directory

```bash
    cd db-assignment
```

Create virtual environment

```bash
    python -m venv venv
    source venv/bin/activate
```

Install dependencies:

```bash
    pip install -r requirements.txt
```
Set up the database: ```Use .env for environment variables.```

Apply migrations:

```bash
    python manage.py migrate
```

Run the development server:
```bash
    python manage.py runserver
```

Access the application at ``` http://127.0.0.1:8000/.```
