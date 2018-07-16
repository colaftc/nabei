from app import db
from sqlalchemy import func

class OutsideOrder(db.Model):
    __tablename__='outside_order'
    id=db.Column(db.Integer,primary_key=True)
    products=db.Column(db.Text)
    total=db.Column(db.Numeric(7,2))
    order_date=db.Column(db.Date)
    created=db.Column(db.DateTime,server_default=func.now())
    updated=db.Column(db.DateTime,onupdate=func.now(),nullable=True)

    def __unicode__(self):
        return self.products

class Expenditure(db.Model):
    __tablename__='expenditure'
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.Text)
    price=db.Column(db.Numeric(7,2))
    pay_date=db.Column(db.Date)
    created=db.Column(db.DateTime,server_default=func.now())
    updated=db.Column(db.DateTime,onupdate=func.now(),nullable=True)

    def __unicode__(self):
        return self.title

class Task(db.Model):
    __tablename__='task'
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.Text)
    urgent=db.Column(db.Boolean,default=False)
    created=db.Column(db.DateTime,server_default=func.now())
    updated=db.Column(db.DateTime,onupdate=func.now(),nullable=True)

    def __unicode__(self):
        return self.title
