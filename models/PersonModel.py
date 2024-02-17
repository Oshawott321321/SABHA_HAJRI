from utils.db import db

class PersonModel(db.Model):
    __tablename__ = 'PersonModel'
    id = db.Column(db.Integer, primary_key=True)
    role_no = db.Column(db.Integer, unique =True, nullable=False)
    name = db.Column(db.String(100), unique=False, nullable=False)
    atten = db.relationship('AttendanceModel',backref='personBack',lazy=True)

    def __repr__(self):
        return '<User %r>' % self.name

    @staticmethod
    def __save__(db,name,roll_no):
        p = PersonModel()
        if not name or not roll_no:
            return None
        p.name = name
        p.role_no = roll_no
        db.session.add(p)
        try:
            db.session.commit()
        except:
            print("could not add ",name)
            return None
        return p
