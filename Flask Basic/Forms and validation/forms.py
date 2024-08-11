from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, PasswordField, SubmitField, BooleanField
from wtforms.validators import data_required, Length, Email, Optional, DataRequired, equal_to

class SignupForm(FlaskForm):
    username = StringField("Username", validators=[data_required(), Length (2,30)])
    email = StringField("Email", validators=[data_required(), Email(), Length (2,30)])
    gender = SelectField("gender", choices= ["Mail", "Femail", "Others"], validators=[Optional()])
    dob = DateField("Date of Birth", validators= [Optional()])
    password = PasswordField("password", validators=[DataRequired(), Length(5,25)])
    confirm_password = PasswordField("Confirm Password", validators=[data_required(), Length(5,25), equal_to("password")])
    submit = SubmitField("Signup")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[data_required(), Email(), Length (2,30)])
    password = PasswordField("password", validators=[DataRequired(), Length(5,25)])
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Login")

