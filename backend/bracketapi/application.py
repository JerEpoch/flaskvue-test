from flask import Flask

def create_app(app_name='BRACKET_API'):  
    app = Flask(app_name)
    app.config.from_object('bracketapi.config.BaseConfig')

    from bracketapi.api import api
    app.register_blueprint(api, url_prefix="/api")

    from bracketapi.models import db
    db.init_app(app)

    return app