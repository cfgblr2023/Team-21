from canasu.database import db, ma
from mentee import MenteesSchema
from mentor import MentorSchema
from sqlalchemy import func

class Mapping(db.Model):
    __tablename__ = 'mapping'
    id=db.Column(db.Integer, primary_key=True)
    mentorId=db.Column(db.Integer, db.ForeignKey('mentor.id'))
    menteeId=db.Column(db.Integer, db.ForeignKey('mentee.id'))
    confirm = db.Column(db.Boolean, default=False)

    mentor = db.relationship('Mentor', backref='mappings')
    mentee = db.relationship('Mentee', backref='mappings')
        
class MappingSchema(ma.Schema):
    class Meta:
        fields = ('id','mentorId','menteeId','confirm')
                  
mapping_schema = MappingSchema()

