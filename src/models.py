from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorites = db.relationship("Favorite", lazy=True)
  

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planet(db.Model):
    planet_id = db.Column(db.Integer, primary_key=True)
    name_planet = db.Column(db.String(120), unique=True, nullable=False)
    population = db.Column(db.String(80), unique=False, nullable=False)
    climate = db.Column(db.String(80), unique=False, nullable=False)
    favorites = db.relationship("Favorite", lazy=True)

    def __repr__(self):
        return '<Planet %r>' % self.planets

    def serialize(self):
        return {
            "name_planet": self.name_planet,
            "population": self.population,
            "climate": self.climate,
        }

class People(db.Model):
    characeteres_id = db.Column(db.Integer, primary_key=True)
    name_people = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.String(80), unique=False, nullable=False)
    born_date = db.Column(db.String(80), unique=False, nullable=False)
    favorites = db.relationship("Favorite", lazy=True)

    def __repr__(self):
        return '<People %r>' % self.peoples

    def serialize(self):
        return {
            "name_people": self.name_people,
            "age": self.age,
            "born_date": self.born_date,
        }

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    planet_id = db.Column(db.Integer, db.ForeignKey(Planet.planet_id))
    people_id = db.Column(db.Integer, db.ForeignKey(People.characeteres_id))

    def __repr__(self):
        return '<Favorites %r>' % self.favorite

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            "people_id": self.people_id,
           
        }
