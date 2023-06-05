"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, abort
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planet, People, Favorite
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():
    users = User.query.all()
    result = []
    for user in users: result.append({
    'id': user.id,
    'email': user.email
    })
    return jsonify(result)

@app.route('/user/favorite', methods=['GET'])
def handle_fav():
    favs = Favorite.query.all()
    result = []
    for fav in favs: result.append({
    'id': fav.id, 
    'user-id': fav.user_id,
    'planet_id': fav.planet_id,
    'people_id': fav.people_id,
    })
    return jsonify(result)


@app.route('/people', methods=['GET'])
def handle_people():
    peoples = People.query.all()
    result = []
    for peopl in peoples: result.append({
    'characeteres_id': peopl.characeteres_id,
    'name_people': peopl.name_people,
    'age': peopl.age,
    'born_date': peopl.born_date,
    })
    return jsonify(result)

@app.route('/people/<string:people_id>', methods=['GET'])
def get_people(people_id):
    peopl = People.query.get(people_id)
    if peopl is None:
        abort(404)
    return jsonify(peopl.serialize())

@app.route('/planet', methods=['GET'])
def handle_planet():
    planets = Planet.query.all()
    result = []
    for plant in planets: result.append({
    'planet_id': plant.planet_id,
    'name_planet': plant.name_planet,
    'population': plant.population,
    'climate': plant.climate,
    })
    return jsonify(result)


@app.route('/planet/<string:planet_id>', methods=['GET'])
def get_planet(planet_id):
    plant = People.query.get(planet_id)
    if plant is None:
        abort(404)
    return jsonify(plant.serialize())




# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
