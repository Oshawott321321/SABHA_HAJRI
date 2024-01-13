from utils.db import db


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    field1 = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    