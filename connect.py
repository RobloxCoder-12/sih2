from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:12345@AADVIK-PC/sih'
  # Replace with your database URI
db = SQLAlchemy(app)

# Define a model (table structure) for your database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'

# Create the database tables if they don't exist
with app.app_context():
    db.create_all()

