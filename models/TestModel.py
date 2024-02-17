from utils.db import db


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f1 = db.Column(db.String(80))
    pf = db.Column(db.PickleType)

    def __repr__(self):
        return '<User %r>' % self.id

    