import os
from flask import Flask
from flask_admin import Admin
from flask_security import Security, SQLAlchemyUserDatastore


def load_config(app):
    if os.environ.get('FLASK_ENV', '').lower() == 'production':
        config_obj = 'ProductionConfig'
    else:
        config_obj = 'DevelopmentConfig'

    app.config.from_object('config.{}'.format(config_obj))


def setup_security(app):
    from database import db
    from models import User, Role

    # Setup Flask-Security
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)


def create_app():
    from database import db
    from admin import SecuredHomeView, init_admin
    from models import User, Role
    import views

    app = Flask(__name__)
    load_config(app)
    db.init_app(app)
    setup_security(app)
    init_admin(app)

    app.register_blueprint(views.bp)

    return app
