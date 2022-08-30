from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)
    favorites = db.relationship('Favorites', backref='user', uselist=True)

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "username" : self.username,
            "email": self.email
            # do not serialize the password, its a security breach
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16),nullable=False,unique=True)
    size = db.Column(db.String(16),nullable=False)
    population = db.Column(db.String(16),nullable=False)
    surface = db.Column(db.String(16),nullable=False)

    def __repr__(self):
        return '<Planet %r>' % self.id
    
    def serialize(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'size' : self.size,
            'population' : self.population,
            'surface' : self.surface,
        }

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16),nullable=False,unique=True)
    color_eyes = db.Column(db.String(16),nullable=False)
    color_hair = db.Column(db.String(16),nullable=False)
    height = db.Column(db.String(16),nullable=False)

    def __repr__(self):
        return '<People %r>' % self.id 
    
    def serialize(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'color_eyes' : self.color_eyes, 
            'color_hair' : self.color_hair,
            'heigh' : self.height
        }

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nature = db.Column(db.String(16), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    nature_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(16), nullable=False)
    __table_args__=(db.UniqueConstraint(
        'user_id',
        'name',
        name='message_unique'
    ),)

  
    def __repr__(self):
        return '<Favorites %r>' % self.id 

    def serialize(self):
        return {
            'id' : self.id,
           
        }