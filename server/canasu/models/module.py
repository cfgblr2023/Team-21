from canasu.database import db, ma

from sqlalchemy import func

class Module(db.Model):
    __tablename__ = 'module'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    hours=db.Column(db.Integer)
        
    
class ModuleSchema(ma.Schema):
    class Meta:
        fields = ('id','name','hours')
                  
module_schema = ModuleSchema()