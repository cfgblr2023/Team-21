from canasu.database import db, ma
from sqlalchemy import func

class Mentee(db.Model):
    __tablename__ = 'mentee'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    email=db.Column(db.String(100), nullable=False, unique=True)
    phone=db.Column(db.String(100), nullable=False, unique=True)
    password=db.Column(db.String(100), nullable=False)
    
    dob=db.Column(db.String(100), nullable=True)
    address=db.Column(db.String(100), nullable=True)
    languages=db.Column(db.String(100), nullable=False)
    education=db.Column(db.String(100), nullable=False)
    
    created_at=db.Column(db.DateTime, nullable=False, server_default=func.now())
    updated_at=db.Column(db.DateTime, nullable=False, server_default=func.now(), onupdate=func.now())
    
    
class MenteeSchema(ma.Schema):
    class Meta:
        fields = ('id','name', 'email', 'phone', 'dob', 'address', 'languages', 'education','created_at', 'updated_at')
                  
mentee_schema = MenteeSchema()