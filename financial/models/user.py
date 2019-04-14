from financial import db, ma

class User(db.Model):

    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False)
    username = db.Column(db.String(45), unique=False)
    password = db.Column(db.String(255), unique=False)

    def __init__(
        self,
        name,
        username,
        password
    ):
        self.name = name
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.name

    def save(self):
        db.session.add(self)
        db.session.commit()


class UserSchema(ma.ModelSchema):

    class Meta:
        model = User
        fields = ('name', 'username')

user_schema = UserSchema()
users_schema = UserSchema(many=True)
