from app import db
from sqlalchemy import func

class BaseModel(db.Model):
    __tablename__='outside_order'
    id=db.Column(db.Integer,primary_key=True)
    created=db.Column(db.DateTime,server_default=func.now())
    updated=db.Column(db.DateTime,onupdate=func.now(),nullable=True)


class OutsideOrder(BaseModel):
    products=db.Column(db.Text)
    total=db.Column(db.Numeric)

    def __unicode__(self):
        return self.products
