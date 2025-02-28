from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import PasswordField,StringField, SubmitField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Log In')


app = Flask(__name__)
app.secret_key = 'b_5#y2L"F4Q8z:{}]/'


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login")
def login():
    form = MyForm()
    return render_template("login.html", form=form)



if __name__ == '__main__':
    app.run(debug=True)
