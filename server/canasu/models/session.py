from canasu.database import db, ma
from sqlalchemy import func

class Session(db.Model):
    __tablename__ = 'session'
    id=db.Column(db.Integer, primary_key=True)
    enrollment_id=db.Column(db.Integer, db.ForeignKey('mentor.id'))
    mentor_id=db.Column(db.Integer, db.ForeignKey('mentor.id'))
    mentee_id=db.Column(db.Integer, db.ForeignKey('mentee.id'))
    admin_id=db.Column(db.Integer, db.ForeignKey('admin.id'))
    hours=db.Column(db.Integer)
    datetime=db.Column(db.DateTime, default=func.now())
    
class SessionSchema(ma.Schema):
    class Meta:
        fields = ('id','mentorId','menteeId','adminId','hours','date')
                  
session_schema = SessionSchema()

