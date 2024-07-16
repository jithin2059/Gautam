from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'  # SQLite database file path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the BlogPost model
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Define the form for blog submissions
class BlogForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired()])
    content = TextAreaField('Your Blog Post', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = BlogForm()
    if form.validate_on_submit():
        new_post = BlogPost(name=form.name.data, content=form.content.data)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('index'))
    posts = BlogPost.query.all()
    return render_template('index.html', form=form, posts=posts, image_url=url_for('static', filename='gautam_image.png'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
