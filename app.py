from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

# Initialize the Flask application
app = Flask(__name__)

# Configure SQLite database — relative path, stores db in instance/ by default
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///villain.db"

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)

# Define the Villain model/table
class Villain(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Auto-incrementing ID
    name = db.Column(db.String(80), unique=True, nullable=False)  # Must be unique
    description = db.Column(db.String(250), nullable=False)
    interests = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)  # Expected to be a link to an image
    date_added = db.Column(
        db.DateTime, 
        nullable=False, 
        default=lambda: datetime.now(timezone.utc)  # UTC timestamp for consistency
    )

    # Properly define string representation
    def __repr__(self):
        return "<Villain " + self.name + ">"

# Create all database tables (if they don't already exist)
# Must run inside application context
with app.app_context():
    db.create_all()
    db.session.commit()


# Homepage route: displays all villains
@app.route("/")
def villains_cards():
    return render_template("villain.html", villains=Villain.query.all())


# Route to show the form for adding a new villain
@app.route("/add", methods=["GET"])
def add_villain():
    return render_template("addvillain.html", errors=[])


# Route to show the form for deleting a villain
@app.route("/delete", methods=["GET"])
def delete_villain():
    return render_template("deletevillain.html", errors=[])


# Route to process form submission for adding a new villain
@app.route("/addVillain", methods=["POST"])
def add_user():
    errors = []

    # Get form data and validate
    name = request.form.get("name")
    if not name:
        errors.append("Oops! Looks like you forgot a name!")

    description = request.form.get("description")
    if not description:
        errors.append("Oops! Looks like you forgot a description!")

    interests = request.form.get("interests")
    if not interests:
        errors.append("Oops! Looks like you forgot some interests!")

    url = request.form.get("url")
    if not url:
        errors.append("Oops! Looks like you forgot an image!")

    # Check if villain name already exists (unique constraint)
    villain = Villain.query.filter_by(name=name).first()
    if villain:
        errors.append("Oops! A villain with that name already exists!")

    # If any errors, re-render the form with messages
    if errors:
        return render_template("addvillain.html", errors=errors)
    
    # Otherwise, add the new villain to the database
    new_villain = Villain(
        name=name,
        description=description,
        interests=interests,
        url=url
    )
    db.session.add(new_villain)
    db.session.commit()

    # After successful submission, show updated card list
    return render_template("villain.html", villains=Villain.query.all())


# Route to handle deletion of a villain by name
@app.route("/deleteVillain", methods=["POST"])
def delete_user():
    name = request.form.get("name")
    villain = Villain.query.filter_by(name=name).first()

    if villain:
        db.session.delete(villain)
        db.session.commit()
        return render_template("villain.html", villains=Villain.query.all())
    else:
        return render_template("deletevillain.html", errors=["Oops! That villain doesn't exist!"])


# Only run the development server if this file is executed directly
if __name__ == "__main__":
    app.run()
