import os
from flask_admin import Admin
from models import db, User, People, Planets, Favorites
from flask_admin.contrib.sqla import ModelView
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, validators

class UserForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired()])

class Favorites_Model(ModelView):
    form_columns = ("user_id", "planets_id", "people_id")
    column_list = ("user_id", "planets_id", "people_id")

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')
       
       
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(People, db.session))
    admin.add_view(ModelView(Planets, db.session))
    # admin.add_view(Favorites_Model(Favorites, db.session))


    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))