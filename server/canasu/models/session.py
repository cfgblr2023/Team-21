from canasu.database import db, ma
from sqlalchemy import func

class Session(db.Model):
    __tablename__ = 'session'
    id=db.Column(db.Integer, primary_key=True)
    enrollmentId=db.Column(db.Integer, db.ForeignKey('mentor.id'))
    mentorId=db.Column(db.Integer, db.ForeignKey('mentor.id'))
    menteeId=db.Column(db.Integer, db.ForeignKey('mentee.id'))
    adminId=db.Column(db.Integer, db.ForeignKey('admin.id'))
    hours=db.Column(db.Integer)
    datetime=db.Column(db.DateTime, default=func.now())
    
class SessionSchema(ma.Schema):
    class Meta:
        fields = ('id','mentorId','menteeId','adminId','hours','date')
                  
session_schema = SessionSchema()

