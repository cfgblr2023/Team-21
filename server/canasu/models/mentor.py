from canasu.database import db, ma

from sqlalchemy import func

class Mentor(db.Model):
    __tablename__ = 'mentors'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    email=db.Column(db.String(100), nullable=False, unique=True)
    phone=db.Column(db.String(100), nullable=False, unique=True)
    password=db.Column(db.String(100), nullable=False)
    
    gender=db.Column(db.String(100), nullable=False)
    dob=db.Column(db.String(100), nullable=True)
    address=db.Column(db.String(100), nullable=True)
    languages=db.Column(db.String(100), nullable=False)
    education=db.Column(db.String(100), nullable=False)
    qualification=db.Column(db.String(100), nullable=False)
    availability=db.Column(db.Integer, nullable=False)
    
    created_at=db.Column(db.DateTime, nullable=False, server_default=func.now())
    updated_at=db.Column(db.DateTime, nullable=False, server_default=func.now(), onupdate=func.now())
    
    
class MentorSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'phone', 'password', 'gender', 'dob', 'address', 'languages', 'education', 'qualification', 'availability', 'created_at', 'updated_at')
                  
mentor_schema = MentorSchema()