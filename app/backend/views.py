from . import backend,backend_login_required,BackendUser,backend_is_authenticate
from . import backend_login_user,backend_logout_user
from .forms import OutsideOrderForm,BackendLoginForm
from flask import render_template,redirect,flash,url_for
from app.models import OutsideOrder
from app import db

@backend.route('/')
@backend.route('/index')
@backend_login_required
def index():
    orders=OutsideOrder.query.all()
    return render_template('index.html',orders=orders,title_name='那杯',action_name='门店订单')

@backend.route('/login',methods=['GET','POST'])
def login():
    login_form=BackendLoginForm()
    if login_form.validate_on_submit():
        user=BackendUser(
            username=login_form.username.data,
            pwd=login_form.pwd.data
        )
        if backend_is_authenticate(user):
            backend_login_user(user)
            return redirect(url_for('backend.index'))
    return render_template('login.html',
                           form=login_form,
                           action_name='登录',
                           title_name='那杯'
                          )

@backend.route('/outside_order_form',methods=['GET','POST'])
@backend_login_required
def outside_order_form():
    order_form=OutsideOrderForm()
    if(order_form.validate_on_submit()):
        order=OutsideOrder(products=order_form.products.data,
                          total=order_form.price.data
                          )
        db.session.add(order)
        db.session.commit()
        flash('订单保存成功')
        return redirect(url_for('backend.index'))

    return render_template('outside_order_form.html',form=order_form,title_name='那杯',action_name='门店订单录入')

@backend.route('/logout')
@backend_login_required
def logout():
    backend_logout_user()
    return redirect(url_for('backend.login'))
