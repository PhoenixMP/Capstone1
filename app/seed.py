# Seed file for resetting/creating the tables for the melodic database

from app import app
from models import db

with app.app_context():
    db.drop_all()
    db.create_all()
