from blogsite import db


class user(db.Model):
    __tablename__= "users_data"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    #posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class wifi(db.Model):
    __tablename__ = "wifi"
    id = db.Column(db.Integer, primary_key=True)
    SSID_ = db.Column(db.String(120))
    SIGNAL_ = db.Column(db.Integer)
    MAC_ = db.Column(db.String(120))

    def __init__(self, SSID_, SIGNAL_, MAC_):
        self.SSID_ = SSID_
        self.SIGNAL_ = SIGNAL_
        self.MAC_ = MAC_

class temp(db.Model):
    __tablename__ = "temp"
    id = db.Column(db.Integer, primary_key=True)
    date_ = db.Column(db.String(120))
    temp_ = db.Column(db.Integer)

    def __init__(self, date_, temp_):
        self.date_ = date_
        self.temp_ = temp_


# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
#     content = db.Column(db.Text, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#
#     def __repr__(self):
#         return f"Post'{self.title}', '{self.date_posted}')"