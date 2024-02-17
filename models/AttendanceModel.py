from utils.db import db
from datetime import date


class AttendanceModel(db.Model):
    __tablename__='AttendanceModel'
    id = db.Column(db.Integer, primary_key=True)
    onlydate = db.Column(db.String(10),nullable=False)
    maleCount = db.Column(db.Integer ,default = True,  nullable = False)
    femaleCount = db.Column(db.Integer , default = True, nullable = False)
    person = db.Column('person',db.ForeignKey('PersonModel.id'))

    def __repr__(self):
        return '<Attendance %r>' % self.id
    
    def __save__(self,db):
        self.onlydate = date.today().__str__()
        db.session.add(self)
        db.session.commit()
    