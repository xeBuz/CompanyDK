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
    host='0.0.0.0',
    port=int(os.environ.get('PORT', 5000)),
    use_debugger=True,
    use_reloader=True)
)
heroku = Heroku()

app.config.from_object('config.Development')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


# Load Controllers
from api.controllers.company import companies
from api.controllers.health import health

# Load Endpoints
app.register_blueprint(companies, url_prefix='/api/companies')
app.register_blueprint(health, url_prefix='/api/health')


heroku.init_app(app)
db.init_app(app)
