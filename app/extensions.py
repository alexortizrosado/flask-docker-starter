from flask_login import LoginManager
lm = LoginManager()

from app.heroku import Heroku
heroku = Heroku()

from flask_travis import Travis
travis = Travis()

from flask_mail import Mail
mail = Mail()

from werkzeug.contrib.cache import SimpleCache
cache = SimpleCache()

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

from celery import Celery
celery = Celery()

from flask_assets import Environment
assets = Environment()

from flask_babel import Babel
babel = Babel()

from flask_bootstrap import Bootstrap
bootstrap = Bootstrap()

from raven.contrib.flask import Sentry
sentry = Sentry()
