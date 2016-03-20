# Setup Back-end Environment

The Back-end Server was created with Python and Flask, using SQLAlchemy for the database.

## Get the Code

Clone the repository

```bash
git clone git@github.com:xeBuz/CompanyDK.git
```


## Activate VirtualEnv

For a better usage activate `virtualenv`, if you don't have `virtualenv` installed follow [this](http://virtualenv.readthedocs.org/en/latest/installation.html) steps.

```bash
cd CompanyDK;
source venv/bin/activate
```


## Install Python requirements

```bash
pip install -r requirements.txt
```


## *optional* Change the Database

In the file `config.py` you will find the server configuration.

If you want to create a new local dabatase, I strongly suggest to remove the comment:

```
# SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
```

to use a local file with SQLite instread of the Postgres database; the app handle the connections transparently and you could change the DB as you wish


## *optional* Upgrade your Database

Especially if you follow the previous step, you will need to migrate the new database.


```bash
python server.py db upgrade
```

This command will upgrade your schema and also will create dummy data for testing.


## Run the Server

The project is Python 2.7 and Python 3.5 compatible. To run the server you must execute the following command


```bash
python server.py runserver

 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * ...
```


## Heroku

I created the back-end and the front-end in the same repository for a easier evaluation, but is always better to create different proyects.
Due a multiple server running (`grunt` and `Flask`) is not possible to create a free Heroku app fully-functional, with the proper amount of Heroku dynos is possible, but I'm only using one, so you can check the API server running here:

```
https://companydk.herokuapp.com/api/companies
```
