"""Forms for our adoption agency Flask app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, Email, URL, NumberRange

class AddPet(FlaskForm):
    """Form for adding pet."""

    name = StringField("Pet name:",
                        validators=[InputRequired()])
    species = SelectField("Species:",
                        choices = [("cat", "Cat"),("dog", "Dog"),("porcupine", "Porcupine")],
                        validators=[InputRequired()])
    photo_url= StringField("Photo URL:",
                        validators=[Optional(), URL()])
    age = FloatField("Age:",
                        validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes:",
                        validators=[Optional()])
    available = SelectField("Is this pet available?:",
                        choices = [("true", "Yes"),("false", "No")],
                        validators=[InputRequired()])
