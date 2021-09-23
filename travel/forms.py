from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed

# Variable that holds the allowed files
ALLOWED_FILES = {'PNG','JPG','png','jpg','JPEG','jpeg'}

#Create new destination
class DestinationForm(FlaskForm):
  name = StringField('Country', validators=[InputRequired()])
  description = TextAreaField('Description', 
            validators=[InputRequired(), Length(max=500, message="Max length of 500 exceeded!")])
  image = FileField('Cover Image', validators=[FileRequired(), FileAllowed(ALLOWED_FILES, message=f'Accepted file types: {ALLOWED_FILES}')])
  currency = StringField('Currency', validators=[InputRequired()])
  submit = SubmitField("Create")
    
#User login
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

#User register
class RegisterForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    
    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")
    #submit button
    submit = SubmitField("Register")

#User comment
class CommentForm(FlaskForm):
  text = TextAreaField('Comment', [InputRequired()])
  submit = SubmitField('Create')