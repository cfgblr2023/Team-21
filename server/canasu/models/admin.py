from canasu.database import db, ma
from sqlalchemy import func

class Admin(db.Model):
    __tablename__ = 'admin'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    email=db.Column(db.String(100), nullable=False)
    phone=db.Column(db.String(100), nullable=False)
    password=db.Column(db.String(100), nullable=False)
    slots=db.Column(db.Integer, nullable=False, default=0)
  
   
class AdminSchema(ma.Schema):
    class Meta:
        fields = ('id','name', 'email', 'phone', 'password', 'slots')
                  
admin_schema = AdminSchema()