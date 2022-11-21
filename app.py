"""Adoption Agency application."""

from site import addusersitepackages
from flask import Flask, request, redirect, render_template, flash
from models import db, connect_db, Pet

from flask_debugtoolbar import DebugToolbarExtension

from forms import AddPet

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



with app.app_context():
    connect_db(app)
    db.create_all()

@app.route("/")
def home():
    """Home page"""
    all_pets = Pet.query.all()
    return render_template("home.html", all_pets = all_pets)


@app.route("/add", methods=["GET", "POST"])
def addpet():
    """Add pet page"""
    
    form = AddPet()

    if form.validate_on_submit():
        newpet = Pet(name = form.name.data,
                    species = form.species.data,
                    photo_url = form.photo_url.data,
                    age = form.age.data,
                    notes = form.notes.data,
                    available = form.available.data)
        db.session.add(newpet)
        db.session.commit()
        return redirect("/")

    else:
        return render_template("add_pet_form.html", form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def display_pet(pet_id):
    """Pet display and edit page"""
    pet = Pet.query.get_or_404(pet_id)
    form = AddPet(obj=pet)
    
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect("/")
  
    else:
        return render_template("pet_display_edit_form.html", form = form, pet = pet)


