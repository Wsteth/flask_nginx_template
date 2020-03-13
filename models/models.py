from core import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False, index=True, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    created_time = db.Column(db.Integer, nullable=False)

    def __init__(self, data):
        self.username = data['username']
        self.password_hash = generate_password_hash(data['password'])
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.phone_number = data['phone_number']
        self.email = data['email']
        self.address = data['address']
        self.created_time = data['created_time']

    def update(self,data):
        self.username = data['username']
        self.password_hash = generate_password_hash(data['password'])
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.phone_number = data['phone_number']
        self.email = data['email']
        self.address = data['address']
        self.created_time = data['created_time']

    def validate_password(self,password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return dict(
            username = self.username,
            # password_hash = self.password_hash,
            first_name = self.first_name,
            last_name = self.last_name,
            phone_number = self.phone_number,
            email = self.email,
            address = self.address,
            created_time = self.created_time
        )