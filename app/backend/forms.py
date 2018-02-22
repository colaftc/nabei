from flask_wtf import Form
from wtforms import TextAreaField,SubmitField,DecimalField
from wtforms import StringField,PasswordField
from wtforms.validators import Required

class OutsideOrderForm(Form):
    products=TextAreaField('订单明细',validators=[Required(),])
    price=DecimalField('总金额',validators=[Required(),])
    submit=SubmitField('确定')

class BackendLoginForm(Form):
    username=StringField('用户名')
    pwd=PasswordField('密码')
    submit=SubmitField('登录')
