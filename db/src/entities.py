from .app import db
# TODO - use non SQL Server specific stuff?
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.dialects.mssql import TINYINT


class VegStatus(db.Model):
    id = db.Column(UNIQUEIDENTIFIER, primary_key=True, unique=True)
    status = db.Column(db.Unicode, nullable=False)
    recipes = db.relationship('Recipe', back_populates='VegStatus')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Ingredient(db.Model):
    """Ingredients for recipes"""
    id = db.Column(UNIQUEIDENTIFIER, primary_key=True, unique=True)
    ingredient = db.Column(db.Unicode, nullable=False)
    unit = db.Column(db.Unicode, nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Recipe(db.Model):
    """Recipe details."""
    id = db.Column(UNIQUEIDENTIFIER, primary_key=True, unique=True)
    recipe_name = db.Column(db.Unicode, nullable=False)
    recipe_source = db.Column(db.Unicode, nullable=False)
    serves = db.Column(TINYINT, nullable=False)
    mushrooms = db.Column(db.Boolean, nullable=False)
    calories = db.Column(db.Integer, nullable=False)
    cook_time = db.Column(db.Integer, nullable=False)
    id_veg_status = db.Column(UNIQUEIDENTIFIER, db.ForeignKey('VegStatus'), nullable=False)
    veg_status = db.relationship('VegStatus', back_populates='Recipe')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
