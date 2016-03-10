import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.heroku import Heroku

# Initialize Application
app = Flask(__name__)

manager = Manager(app)
manager.add_command("runserver", Server(
    use_debugger=True,
    use_reloader=True)
)
heroku = Heroku()

app.config.from_object('config.Development')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@app.route('/')
def test():
    return "lala"

# Load Controllers


# Load Endpoints
# app.register_blueprint(users, url_prefix='/users')
#
heroku.init_app(app)
db.init_app(app)

#
# if __name__ == '__main__':
#     port = int(os.environ.get('PORT', 5000))
#     app.run(host='0.0.0.0', port=port, debug=True)
