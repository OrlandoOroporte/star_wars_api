"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planet, People, Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
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

# @app.route('/user', methods=['POST'])
# def add_new_user():
#     request_body = request.json
#     User.append(request_body)
#     return jsonify(User)

# @app.route('/user/<int:id>', methods=['GET'])
# def get_user(id):
#     user = User.query.get(id)
#     if user is None:
#         return jsonify({"User does not exist "})
#     return jsonify(user.serialize()), 200

# @app.route('/planet/<int:id>', methods=['GET'])
# def get_planet(id):
#     planet = Planet.query.get(id)
#     if planet is None:
#         return jsonify({"Planet does not exist "})
#     return jsonify(planet.serialize()), 200
       
@app.route('/people/<int:id>', methods=['GET'])
def get_people(id=None):
    people = People.query.get(id)
    if people is None:
        return jsonify({"mesage":"Not found"}), 404
    return jsonify(people.serialize()), 200

# @app.route('/user', methods=['GET'])
# def get_users():
#     users = User.query.all()
#     users2 = list(map(lambda user: User.serialize(), users))
#     return jsonify(users2), 200

# @app.route('/planet', methods=['GET'])
# def get_planets():
#     planets = Planet.query.all()
#     planets2 = list(map(lambda planet: Planet.serialize(), planets))
#     return jsonify(planets), 200

@app.route('/people', methods=['GET'])
def get_peoples():
    peoples = People.query.all()
    peoples = list(map(lambda people: people.serialize(), peoples))
    return jsonify(peoples), 200

# @app.route('user/favorites', methods=['GET'])
# def get_user_favorites():
#     favorites1 = Favorites.query.all()
#     favorites2 = list(map(lambda  favorites: Favorites.serialize(), favorites1))
#     return jsonify(favorites1)

# @app.route('favorite/planet/<int:id>', methods=['POST'])
# def add_planet_favorites(id):

#     return jsonify()

# @app.route('favorite/people/<int:id>', methods=['POST'])
# def add_people_favorites(id):
#     return jsonify()

# @app.route('user/favorites/<int:id>', methods=['DELETE'])
# def rem_favorites(id):
#     favorites = Favorites.query.get(id)
#     db.session.delete(favorites)
#     db.session.commit()
#     return 'Delete'


# @app.route('/user', methods=['GET'])
# def handle_hello():

#     response_body = {
#         "msg": "Hello, this is your GET /user response "
#     }

#     return jsonify(response_body), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
